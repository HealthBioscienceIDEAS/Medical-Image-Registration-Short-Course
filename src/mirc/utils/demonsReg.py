"""
function to peform a registration between two 2D images using the demons  algorithm
 
provided for use in image registration exercises 3 for module MPHY0025 (IPMI)

Authors: Jamie McClelland, UCL
Contributors: Zakaria Senousy and Miguel Xochicale, UCL-ARC
"""
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np
from skimage.transform import rescale, resize
from scipy.ndimage import gaussian_filter
from src.mirc.utils.utils3 import dispImage, resampImageWithDefField, calcMSD, dispDefField, calcJacobian


def demonsReg(source, target, sigma_elastic=1, sigma_fluid=1, num_lev=3, use_composition=False,
              use_target_grad=False, max_it=1000, check_MSD=True, disp_freq=3, disp_spacing=2, 
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
  
  # make copies of full resolution images
  source_full = source;
  target_full = target;
  
  #Preparing figure for live update during registration process
  fig, axs = plt.subplots(1, 3, figsize=(12, 6))
  iteration_text = fig.text(0.5, 0.92, '', ha='center', va='top', fontsize=10, color='black')
  
  # loop over resolution levels
  for lev in range(1, num_lev + 1):
    
    # resample images if not final level
    if lev != num_lev:
      resamp_factor = np.power(2, num_lev - lev)
      target = rescale(target_full, 1.0 / resamp_factor, mode='edge', order=3, anti_aliasing=True)
      source = rescale(source_full, 1.0 / resamp_factor, mode='edge', order=3, anti_aliasing=True)
    else:
      target = target_full
      source = source_full
      
    # if first level initialise def_field and disp_field
    if lev == 1:
      [X, Y] = np.mgrid[0:target.shape[0], 0:target.shape[1]]
      def_field = np.zeros((X.shape[0], X.shape[1], 2))
      def_field[:, :, 0] = X
      def_field[:, :, 1] = Y
      disp_field_x = np.zeros(target.shape)
      disp_field_y = np.zeros(target.shape)
    else:
      # otherwise upsample disp_field from previous level
      disp_field_x = 2 * resize(disp_field_x, (target.shape[0], target.shape[1]), mode='edge', order=3)
      disp_field_y = 2 * resize(disp_field_y, (target.shape[0], target.shape[1]), mode='edge', order=3)
      # recalculate def_field for this level from disp_field
      X, Y = np.mgrid[0:target.shape[0], 0:target.shape[1]]
      def_field = np.zeros((X.shape[0], X.shape[1], 2))  # clear def_field from previous level
      def_field[:, :, 0] = X + disp_field_x
      def_field[:, :, 1] = Y + disp_field_y
    
    #initialise updates
    update_x = np.zeros(target.shape)
    update_y = np.zeros(target.shape)
    update_def_field = np.zeros(def_field.shape)
    
    # calculate the transformed image at the start of this level
    warped_image = resampImageWithDefField(source, def_field)
    
    # store the current def_field and MSD value to check for improvements at 
    # end of iteration 
    def_field_prev = def_field.copy()
    prev_MSD = calcMSD(target, warped_image)
        
    # if target image gradient is being used this can be calculated now as it will
    # not change during the registration
    if use_target_grad:
      [img_grad_x, img_grad_y] = np.gradient(target)


    
    # Function to update the display
    def live_update():
        # Clear the axes
        for ax in axs:
            ax.clear()

        # Plotting the warped image in the first subplot
        plt.sca(axs[0])
        dispImage(warped_image, title='Warped Image')
        x_lims = plt.xlim()
        y_lims = plt.ylim()
        # Plotting the deformation field in the second subplot
        plt.sca(axs[1])
        dispDefField(def_field, spacing=disp_spacing, plot_type=disp_method_df)
        axs[1].set_xlim(x_lims)
        axs[1].set_ylim(y_lims)
        axs[1].set_title('Deformation Field')

        # Plotting the updated deformation field in the third subplot
        plt.sca(axs[2])
        up_field_to_display = scale_update_for_display * np.dstack((update_x, update_y))
        up_field_to_display += np.dstack((X, Y))
        dispDefField(up_field_to_display, spacing=disp_spacing, plot_type=disp_method_up)
        axs[2].set_xlim(x_lims)
        axs[2].set_ylim(y_lims)
        axs[2].set_title('Update Field')

        # Update the iteration text
        iteration_text.set_text('Level {0:d}, Iteration {1:d}: MSD = {2:.6f}'.format(lev, it, prev_MSD))
        
        # Adjust layout for better spacing
        plt.tight_layout()

        # Redraw the figure
        fig.canvas.draw()
        fig.canvas.flush_events()  # Ensure the figure updates immediately

        plt.pause(0.5)
    
    
    # main iterative loop - repeat until max number of iterations reached
    for it in range(max_it):
      
      # calculate update from demons forces
      #
      # if the warped image gradient is used (instead of the target image gradient)
      # this needs to be calculated 
      if not use_target_grad:
        [img_grad_x, img_grad_y] = np.gradient(warped_image)
        
      # calculate difference image
      diff = target - warped_image
      # calculate denominator of demons forces
      denom = np.power(img_grad_x, 2) + np.power(img_grad_y, 2) + np.power(diff, 2)
      # calculate x and y components of numerator of demons forces
      numer_x = diff * img_grad_x
      numer_y = diff * img_grad_y
      # calculate the x and y components of the update
      #denom[denom < 0.01] = np.nan
      update_x = numer_x / denom
      update_y = numer_y / denom
      
      # set nan values to 0
      update_x[np.isnan(update_x)] = 0
      update_y[np.isnan(update_y)] = 0
            
      # if fluid like regularisation used smooth the update
      if sigma_fluid > 0:
        update_x = gaussian_filter(update_x, sigma_fluid, mode='nearest')
        update_y = gaussian_filter(update_y, sigma_fluid, mode='nearest')
      
      # update displacement field using addition (original demons) or
      # composition (diffeomorphic demons)
      if use_composition:
        # compose update with current transformation - this is done by
        # transforming (resampling) the current transformation using the
        # update. we can use the same function as used for resampling
        # images, and treat each component of the current deformation
        # field as an image
        # the update is a displacement field, but to resample an image
        # we need a deformation field, so need to calculate deformation
        # field corresponding to update.
        update_def_field[:, :, 0] = update_x + X
        update_def_field[:, :, 1] = update_y + Y
        # use this to resample the current deformation field, storing
        # the result in the same variable, i.e. we overwrite/update the
        # current deformation field with the composed transformation
        def_field = resampImageWithDefField(def_field, update_def_field)
        # calculate the displacement field from the composed deformation field
        disp_field_x = def_field[:, :, 0] - X
        disp_field_y = def_field[:, :, 1] - Y
        # replace nans in disp field with 0s
        disp_field_x[np.isnan(disp_field_x)] = 0
        disp_field_y[np.isnan(disp_field_y)] = 0
      else:
        # add the update to the current displacement field
        disp_field_x = disp_field_x + update_x
        disp_field_y = disp_field_y + update_y
      
      
      # if elastic like regularisation used smooth the displacement field
      if sigma_elastic > 0:
        disp_field_x = gaussian_filter(disp_field_x, sigma_elastic, mode='nearest')
        disp_field_y = gaussian_filter(disp_field_y, sigma_elastic, mode='nearest')
      
      # update deformation field from disp field
      def_field[:, :, 0] = disp_field_x + X
      def_field[:, :, 1] = disp_field_y + Y
            
      # transform the image using the updated deformation field
      warped_image = resampImageWithDefField(source, def_field)

      # update images if required for this iteration
      if disp_freq > 0 and it % disp_freq == 0:
        # Create a single figure with 3 subplots in one row and three columns
        live_update()
      
      # calculate MSD between target and warped image
      MSD = calcMSD(target, warped_image)

      # display numerical results
      print('Level {0:d}, Iteration {1:d}: MSD = {2:f}\n'.format(lev, it, MSD))
      
      # check for improvement in MSD if required
      if check_MSD and MSD >= prev_MSD:
        # restore previous results and finish level
        def_field = def_field_prev
        warped_image = resampImageWithDefField(source, def_field)
        print('No improvement in MSD')
        break
      
      # update previous values of def_field and MSD
      def_field_prev = def_field.copy()
      prev_MSD = MSD.copy()
    
    #plt.show()

    if lev == num_lev:
      # Initialise global variables for current index tracking
      current_image_index = [0]
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

          axs_combined[1].clear()
          plt.sca(axs_combined[1])
          if modes[current_mode_index[0]] == 'Deformation Field': 
              dispDefField(def_field, spacing=disp_spacing, plot_type=disp_method_df)
              axs_combined[1].set_title('Deformation Field')

          else:
              [jacobian, _] = calcJacobian(def_field)
              dispImage(jacobian, title='Jacobian')
              plt.set_cmap('jet')
              #plt.colorbar()

          axs_combined[2].clear()
          plt.sca(axs_combined[2])
          diff_image = images[current_image_index[0]] - target
          dispImage(diff_image, title='Difference Image')

          fig_combined.canvas.draw()


      # Create a single figure with 3 subplots
      fig_combined, axs_combined = plt.subplots(1, 3, figsize=(12, 6))

      # Display initial images
      plt.sca(axs_combined[0])
      dispImage(images[current_image_index[0]], title=image_titles[current_image_index[0]])

      plt.sca(axs_combined[1])
      dispDefField(def_field, spacing=disp_spacing, plot_type=disp_method_df)
      axs_combined[1].set_title('Deformation Field')

      plt.sca(axs_combined[2])
      diff_image = images[current_image_index[0]] - target
      dispImage(diff_image, title='Difference Image')

      # Add instructions for navigating images
      fig_combined.text(0.5, 0.02, 'Press <- or -> to navigate between source, target and warped images, Press Up or Down to switch between deformation field and Jacobian', ha='center', va='top', fontsize=12, color='black')

      # Connect the key event handler to the figure
      fig_combined.canvas.mpl_connect('key_press_event', on_key)

      plt.tight_layout()
      plt.show()

  # return the transformed image and the deformation field
  return warped_image, def_field
