"""
function to peform a registration between two 2D images using the demons algorithm

Author: Jamie McClelland, UCL
Contributors: 
- Clea Dronne, UCL
- Zakaria Senousy, UCL-ARC
- Miguel Xochicale, UCL-ARC
"""

import matplotlib.pyplot as plt
import numpy as np
from skimage.transform import rescale, resize
from scipy.ndimage import gaussian_filter
from utils import dispImage, resampImageWithDefField, calcMSD, dispDefField, calcJacobian

def demonsReg(source, target, sigma_elastic=1, sigma_fluid=1, num_lev=3, use_composition=False,
              use_target_grad=False, max_it=1000, check_MSD=True, disp_freq=5, disp_spacing=2, 
              scale_update_for_display=10, disp_method_df='grid', disp_method_up='arrows'):
    """
    SYNTAX:
        demonsReg(source, target)
        demonsReg(source, target, ..., variable=value, ...)
        warped_image = demonsReg(...)
        warped_image, def_field = demonsReg(...)

    DESCRIPTION:
        Perform a registration between the 2D source image and the 2D target
        image using the demons algorithm. The source image is warped (resampled)
        into the space of the target image.
    
        The final warped image and deformation field can be returned as outputs
        from the function.
    
        There are a number of optional parameters which affect the registration
        or how the results are displayed, which are explained below. These can be
        speficied using variable=value inputs.
        The default values are given after the parameter name
        sigma_elastic = 1
        sigma_fluid = 1
            the amount of elastic and fluid regularistion to apply. these values
            specify the standard deviation of the Gaussian used to smooth the
            update (fluid) or displacement field (elastic). a value of 0 means no
            smoothing is applied.
        num_lev = 3
            the number of levels to use in the multi-resolution scheme
        use_composition = false
            specifies whether the registration is performed using the classical
            demons algorithm, where the updates are added to the current
            transformation, or using the diffeomorphic demons algorithm, where
            the updates are composed with the current transformation. Set
            use_composition to true to compose the updates, or to false to add
            the updates.
        use_target_grad = false
            logical (true/false) value indicating whether the target image
            gradient or warped image gradient is used when calculating the
            demons forces.
        max_it = 1000
            the maximum number of iterations to perform.
        check_MSD = true
            logical value indicating if the Mean Squared Difference (MSD)
            should be checked for improvement at each iteration. If true, the
            MSD will be evaluated at each iteration, and if there is no
            improvement since the previous iteration the registration will move
            to the next resolution level or finish if it is on the final level.
        disp_freq = 3
            the frequency with which to update the displayed images. the images
            will be updated every disp_freq iterations. If disp_freq is set to
            0 the images will not be updated during the registration
        disp_spacing = 2
            the spacing between the grid lines or arrows when displaying the
            deformation field and update.
        scale_update_for_display = 10
            the factor used to scale the update field for displaying
        disp_method_df = 'grid'
            the display method for the deformation field.
            can be 'grid' or 'arrows'
        disp_method_up = 'arrows'
            the display method for the update. can be 'grid' or 'arrows'
    """
  
    # Make copies of full resolution images
    source_full = source
    target_full = target
    
    # Prepare the figure for live update during registration process
    fig, axs = plt.subplots(1, 3, figsize=(12, 6))
    iteration_text = fig.text(0.5, 0.92, '', ha='center', va='top', fontsize=10, color='black')
    fig.suptitle('Live display')
    
    # Loop over resolution levels
    for lev in range(1, num_lev + 1):        
        # if not final level, resample images
        if lev != num_lev:
            resamp_factor = np.power(2, num_lev - lev)
            target = rescale(target_full, 1.0 / resamp_factor, mode='edge', order=3, anti_aliasing=True)
            source = rescale(source_full, 1.0 / resamp_factor, mode='edge', order=3, anti_aliasing=True)
        else: # if final level, we don't need to resample
            target = target_full
            source = source_full
    
        X, Y = np.mgrid[0:target.shape[0], 0:target.shape[1]]

        # if first level, initialise deformation and displacement fields
        if lev == 1:
            def_field = np.zeros((X.shape[0], X.shape[1], 2))
            def_field[:, :, 0], def_field[:, :, 1] = X, Y
            disp_field_x, disp_field_y = np.zeros(target.shape), np.zeros(target.shape)
        # otherwise upsample the displacement field from previous level and recalculate the corresponding deformation field
        else:
            disp_field_x = 2 * resize(disp_field_x, (target.shape[0], target.shape[1]), mode='edge', order=3)
            disp_field_y = 2 * resize(disp_field_y, (target.shape[0], target.shape[1]), mode='edge', order=3)
            def_field = np.zeros((X.shape[0], X.shape[1], 2))  # clear def_field from previous level
            def_field[:, :, 0], def_field[:, :, 1] = X + disp_field_x, Y + disp_field_y

        # initialise updates
        update_x, update_y = np.zeros(target.shape), np.zeros(target.shape)
        warped_image = resampImageWithDefField(source, def_field)
        def_field_prev, prev_MSD = def_field.copy(), calcMSD(target, warped_image)
        
        # calculate the image gradient if required  
        if use_target_grad and target is not None:
            img_grad_x, img_grad_y = np.gradient(target)
        
        # main iterative loop - repeat until max number of iterations reached
        for it in range(max_it):          
            # plot if first iteration
            if it == 0 and lev == 1:
                update_live_display(axs, fig, iteration_text, source, def_field, update_x, update_y, lev, it, prev_MSD, X, Y, disp_spacing, scale_update_for_display, disp_method_df, disp_method_up)

            # if the warped image gradient is used (instead of the target image gradient) this needs to be calculated 
            if not use_target_grad:
                [img_grad_x, img_grad_y] = np.gradient(warped_image)

            # calculate difference image
            diff = target - warped_image
            # calculate denominator of demons forces
            denom = np.power(img_grad_x, 2) + np.power(img_grad_y, 2) + np.power(diff, 2)
            # calculate the x and y components of the update
            update_x, update_y = diff * img_grad_x / denom, diff * img_grad_y / denom
            
            # set nan values to 0
            update_x[np.isnan(update_x)], update_y[np.isnan(update_y)] = 0, 0
                    
            # if fluid like regularisation used smooth the update
            if sigma_fluid > 0:
                update_x = gaussian_filter(update_x, sigma_fluid, mode='nearest')
                update_y = gaussian_filter(update_y, sigma_fluid, mode='nearest')
            
            # update displacement field using addition (original demons) or composition (diffeomorphic demons)
            if use_composition:
                update_def_field = np.dstack((update_x + X, update_y + Y))
                # calculate the update to the deformation field
                def_field = resampImageWithDefField(def_field, update_def_field)
                # calculate the displacement field from the composed deformation field
                disp_field_x, disp_field_y = def_field[:, :, 0] - X, def_field[:, :, 1] - Y
                # replace nans in disp field with 0s
                disp_field_x[np.isnan(disp_field_x)], disp_field_y[np.isnan(disp_field_y)] = 0, 0
            else:
                # add the update to the current displacement field
                disp_field_x = disp_field_x + update_x
                disp_field_y = disp_field_y + update_y
            
            # if elastic like regularisation used smooth the displacement field
            if sigma_elastic > 0:
                disp_field_x = gaussian_filter(disp_field_x, sigma_elastic, mode='nearest')
                disp_field_y = gaussian_filter(disp_field_y, sigma_elastic, mode='nearest')
            
            # update deformation field from disp field
            def_field[:, :, 0], def_field[:, :, 1] = disp_field_x + X, disp_field_y + Y
            # transform the image using the updated deformation field
            warped_image = resampImageWithDefField(source, def_field)

            # calculate MSD between target and warped image and print results
            MSD = calcMSD(target, warped_image)
            print('Level {0:d}, Iteration {1:d}: MSD = {2:f}\n'.format(lev, it, MSD))

            # update images if required for this iteration
            if disp_freq > 0 and it % disp_freq == 0:
                update_live_display(axs, fig, iteration_text, warped_image, def_field, update_x, update_y, lev, it, MSD, X, Y, disp_spacing, scale_update_for_display, disp_method_df, disp_method_up)
            
            # check for improvement in MSD if required
            if check_MSD and MSD >= prev_MSD:
                # restore previous results and finish level
                def_field = def_field_prev
                warped_image = resampImageWithDefField(source, def_field)
                print('No improvement in MSD')
                break
            
            # update previous values of def_field and MSD
            def_field_prev, prev_MSD = def_field.copy(), MSD.copy()
    
    # update the live display with the final results
    update_live_display(axs, fig, iteration_text, warped_image, def_field, update_x, update_y, lev, it, MSD, X, Y, disp_spacing, scale_update_for_display, disp_method_df, disp_method_up)
    # and make the final display appear
    final_display(source_full, target_full, warped_image, def_field, disp_spacing, disp_method_df)
    
    # return the transformed image and the deformation field
    return warped_image, def_field


def update_live_display(axs, fig, iteration_text, warped_image, def_field, update_x, update_y, lev, it, MSD, X, Y, disp_spacing, scale_update_for_display, disp_method_df, disp_method_up):
    """
    Updates the live display of the registration process during each iteration.

    SYNTAX:
        update_live_display(axs, fig, iteration_text, warped_image, def_field, 
                            update_x, update_y, lev, it, prev_MSD, X, Y, 
                            disp_spacing, scale_update_for_display, 
                            disp_method_df, disp_method_up)

    DESCRIPTION:
        This function updates the display of three visualizations:
        1. The current warped image.
        2. The deformation field.
        3. The update field for the current iteration.

        The function also updates the iteration text that shows the current 
        multi-resolution level and iteration, along with the Mean Squared 
        Difference (MSD) between the source and target images.

        axs: list of Matplotlib axes
            A list of Matplotlib axes objects to display the warped image, 
            deformation field, and update field.
        fig: Matplotlib figure object
            The figure object used to update the canvas.
        iteration_text: Matplotlib Text object
            The text object to display the current iteration and MSD.
        warped_image: 2D array
            The current warped image being displayed.
        def_field: 3D array
            The current deformation field (displacement vectors) being displayed.
        update_x, update_y: 2D arrays
            The update field's x and y components used for the current iteration.
        lev: int
            The current level of the multi-resolution registration scheme.
        it: int
            The current iteration number.
        MSD: float
            The current Mean Squared Difference (MSD) value.
        X, Y: 2D arrays
            The grid coordinates of the original image.
        disp_spacing: int
            The spacing between grid lines or arrows in the deformation and update fields.
        scale_update_for_display: float
            Scaling factor applied to the update field for visualization purposes.
        disp_method_df: str
            Method used to display the deformation field. Options are 'grid' or 'arrows'.
        disp_method_up: str
            Method used to display the update field. Options are 'grid' or 'arrows'.
    OUTPUT:
        Updates the plots and text on the figure in real-time to reflect the current state 
        of the registration process. The function does not return any value.
    """
    
    for ax in axs:
        ax.clear()

    plt.sca(axs[0])
    dispImage(warped_image, title='Warped Image')
    x_lims, y_lims = plt.xlim(), plt.ylim()

    plt.sca(axs[1])
    dispDefField(def_field, spacing=disp_spacing, plot_type=disp_method_df)
    axs[1].set_xlim(x_lims)
    axs[1].set_ylim(y_lims)
    axs[1].set_title('Deformation Field')

    plt.sca(axs[2])
    up_field_to_display = scale_update_for_display * np.dstack((update_x, update_y))
    up_field_to_display += np.dstack((X, Y))
    dispDefField(up_field_to_display, spacing=disp_spacing, plot_type=disp_method_up)
    axs[2].set_xlim(x_lims)
    axs[2].set_ylim(y_lims)
    axs[2].set_title('Update Field')

    iteration_text.set_text(f'Level {lev}, Iteration {it}: MSD = {MSD:.6f}')
    plt.tight_layout()
    fig.canvas.draw()
    fig.canvas.flush_events()


def final_display(source, target, warped_image, def_field, disp_spacing, disp_method_df):
    """
    Displays the final results of image registration, allowing interactive navigation 
    between the source, target, and warped images, as well as between the deformation 
    field and the Jacobian.

    SYNTAX:
        final_display(source, target, warped_image, def_field, 
                      disp_spacing, disp_method_df)

    DESCRIPTION:
        This function creates an interactive display with three subplots:
        1. A viewer for the source, target, and warped images.
        2. A visualization of either the deformation field or the Jacobian, depending on user input.
        3. A difference image, showing the difference between the currently selected image 
           (source, target, or warped) and the target image.

        The display allows the user to:
        - Use the left and right arrow keys to switch between the source, target, and warped images.
        - Use the up and down arrow keys to toggle between displaying the deformation field 
          and the Jacobian in the second subplot.

        The deformation field is visualized using the provided spacing and display method.

    PARAMETERS:
        source: 2D array
            The source image used in the registration.
        target: 2D array
            The target image used in the registration.
        warped_image: 2D array
            The final warped image after the registration process.
        def_field: 3D array
            The deformation field (displacement vectors) resulting from the registration process.
        disp_spacing: int
            The spacing between grid lines or arrows when displaying the deformation field.
        disp_method_df: str
            The display method for the deformation field. Options are 'grid' or 'arrows'.

    OUTPUT:
        Displays the source, target, and warped images, deformation field or Jacobian, 
        and a difference image in an interactive figure. No values are returned.
    
    INTERACTIVITY:
        - Left/Right Arrow Keys: Switch between source, target, and warped images.
        - Up/Down Arrow Keys: Switch between the deformation field and the Jacobian.
    """

    # Initialise global variables for current index tracking
    current_image_index = [2]
    current_mode_index = [0]
    
    # Define the images and titles
    images = [source, target, warped_image]
    image_titles = ['Source Image', 'Target Image', 'Warped Image']
    modes = ['Deformation Field', 'Jacobian']

    def on_key(event):
        if event.key == 'right':
            current_image_index[0] = (current_image_index[0] + 1) % len(images)
        elif event.key == 'left':
            current_image_index[0] = (current_image_index[0] - 1) % len(images)
        elif event.key == 'up' or event.key == 'down':
            current_mode_index[0] = (current_mode_index[0] + 1) % len(modes)
        update_display()

    def update_display():
        axs_combined[0].clear()
        plt.sca(axs_combined[0])
        dispImage(images[current_image_index[0]], title=image_titles[current_image_index[0]])
        x_lims, y_lims = plt.xlim(), plt.ylim()

        axs_combined[1].clear()
        plt.sca(axs_combined[1])
        if modes[current_mode_index[0]] == 'Deformation Field': 
            dispDefField(def_field, spacing=disp_spacing, plot_type=disp_method_df)
            axs_combined[1].set_xlim(x_lims)
            axs_combined[1].set_ylim(y_lims)
            axs_combined[1].set_title('Deformation Field')

        else:
            [jacobian, _] = calcJacobian(def_field)
            dispImage(jacobian, title='Jacobian')
            plt.set_cmap('jet')

        axs_combined[2].clear()
        plt.sca(axs_combined[2])
        diff_image = images[current_image_index[0]] - target
        dispImage(diff_image, title='Difference Image')

        fig_combined.canvas.draw()

    # Create a single figure with 3 subplots
    fig_combined, axs_combined = plt.subplots(1, 3, figsize=(12, 6))
    fig_combined.suptitle('Final display')

    # Display initial images
    plt.sca(axs_combined[0])
    dispImage(images[current_image_index[0]], title=image_titles[current_image_index[0]])
    x_lims, y_lims = plt.xlim(), plt.ylim()

    plt.sca(axs_combined[1])
    dispDefField(def_field, spacing=disp_spacing, plot_type=disp_method_df)
    axs_combined[1].set_title('Deformation Field')
    axs_combined[1].set_xlim(x_lims)
    axs_combined[1].set_ylim(y_lims)
    axs_combined[1].set_title('Deformation Field')

    plt.sca(axs_combined[2])
    diff_image = images[current_image_index[0]] - target
    dispImage(diff_image, title='Difference Image')

    # Add instructions for navigating images
    fig_combined.text(0.5, 0.1, 'Press <- or -> to navigate between source, target and warped images, Press Up or Down to switch between deformation field and Jacobian', ha='center', va='top', fontsize=12, color='black')

    # Connect the key event handler to the figure
    fig_combined.canvas.mpl_connect('key_press_event', on_key)

    plt.tight_layout()