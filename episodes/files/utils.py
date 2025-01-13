"""
utility functions for use in the image registration exercises

updated Oct 24

Author: Jamie McClelland, UCL
Contributor: Clea Dronne, UCL
"""

import numpy as np 
import matplotlib.pyplot as plt
import scipy.interpolate as scii

def dispImage(img, int_lims=[], title=''):
    """
    Function to display a grey-scale image that is stored in 'standard
    orientation' with y-axis on the 2nd dimension and 0 at the bottom.
    SYNTAX:
        dispImage(img)
        dispImage(img, int_lims)

    INPUTS:
        img - image to be displayed
        int_lims - the intensity limits to use when displaying the image
            int_lims(1) = min intensity to display
            int_lims(2) = max intensity to display
            default = [np.nanmin(img), np.nanmax(img)]
        title - the title to display above the image
    """
    if not int_lims:
        int_lims = [np.nanmin(img), np.nanmax(img)]
        if int_lims[0] == int_lims[1]:
            int_lims[0] -= 1
            int_lims[1] += 1

    img = img.T
    plt.gca().clear()
    plt.imshow(img, cmap='gray', vmin=int_lims[0], vmax=int_lims[1], origin='lower')
    plt.title(title)
    plt.axis('image')
    plt.tight_layout()

def defFieldFromAffineMatrix(aff_mat, num_pix_x, num_pix_y):
    """
    Function to create a 2D deformation field from an affine matrix.

    SYNTAX:
        def_field = defFieldFromAffineMatrix(aff_mat, num_pix_x, num_pix_y)

    INPUTS:
        aff_mat - a 3 x 3 numpy array representing the 2D affine transformation
            in homogeneous coordinates
        num_pix_x - number of pixels in the deformation field along the x
            dimension
        num_pix_y - number of pixels in the deformation field along the y
            dimension

    OUTPUTS:
        def_field - the 2D deformation field as a 3D numpy array

    NOTES:
        the function calculates the pixel coordinates of the deformation field
        as:
            x = 0:num_pix_x - 1
            y = 0:num_pix_y - 1
    """
    [X, Y] = np.mgrid[0:num_pix_x, 0:num_pix_y]
    total_pix = num_pix_x * num_pix_y
    pix_coords = np.array([np.reshape(X, -1), np.reshape(Y, -1), np.ones(total_pix)])
    
    trans_coords = aff_mat @ pix_coords
    
    def_field = np.zeros((num_pix_x, num_pix_y, 2))
    def_field[:, :, 0] = np.reshape(trans_coords[0, :], (num_pix_x, num_pix_y))
    def_field[:, :, 1] = np.reshape(trans_coords[1, :], (num_pix_x, num_pix_y))
    
    return def_field

def resampImageWithDefField(source_img, def_field, interp_method='linear', pad_value=np.nan):
    """
    Function to resample a 2D image with a 2D deformation field.

    SYNTAX:
        resamp_img = resampImageWithDefField(source_img, def_field)
        resamp_img = resampImageWithDefField(source_img, def_field, interp_method)
        resamp_img = resampImageWithDefField(source_img, def_field, interp_method, pad_value)

    INPUTS:
        source_img - the source image to be resampled, as a 2D matrix
        def_field - the deformation field, as a 3D array
        interp_method - interpolation method accepted by interpn function
            default = 'linear'
        pad_value - the value to assign to pixels that are outside the source image
            default = NaN

    OUTPUTS:
        resamp_img - the resampled image
    """
    x_coords = np.arange(source_img.shape[0], dtype='float')
    y_coords = np.arange(source_img.shape[1], dtype='float')
    
    return scii.interpn((x_coords, y_coords), source_img, def_field, bounds_error=False, fill_value=pad_value, method=interp_method)

def resampImageWithDefFieldPushInterp(source_img, def_field, interp_method='linear'):
    """
    Function to resample a 2D image with a 2D deformation field using push interpolation.

    SYNTAX:
        resamp_img = resampImageWithDefFieldPushInterp(source_img, def_field)
        resamp_img = resampImageWithDefFieldPushInterp(source_img, def_field, interp_method)

    INPUTS:
        source_img - the source image to be resampled, as a 2D matrix
        def_field - the deformation field, as a 3D matrix
        interp_method - interpolation method accepted by griddata function ('linear', 'nearest', or 'cubic')
            default = 'linear'

    OUTPUTS:
        resamp_img - the resampled image
    """
    [X, Y] = np.mgrid[0:source_img.shape[0], 0:source_img.shape[1]]
    pix_coords = np.array([np.reshape(X, -1), np.reshape(Y, -1)]).T
    
    def_field_x = def_field[:, :, 0]
    def_field_y = def_field[:, :, 1]
    def_field_reformed = np.array([np.reshape(def_field_x, -1), np.reshape(def_field_y, -1)]).T
    resamp_img = scii.griddata(def_field_reformed, np.reshape(source_img, -1), pix_coords, method=interp_method)
    
    return np.reshape(resamp_img, source_img.shape)

def affineMatrixForRotationAboutPoint(theta, p_coords):
    """
    Function to calculate the affine matrix corresponding to an anticlockwise rotation about a point.

    SYNTAX:
      aff_mat = affineMatrixForRotationAboutPoint(theta, p_coords)
    
    INPUTS:
      theta - the angle of the rotation, specified in degrees
      p_coords - the 2D coordinates of the point that is the center of rotation.
          p_coords[0] is the x coordinate,
          p_coords[1] is the y coordinate
    
    OUTPUTS:
      aff_mat - a numpy array representing the 3 x 3 affine matrix
    """ 
    theta = np.pi * theta / 180

    T1 = np.array([[1, 0, -p_coords[0]], [0, 1, -p_coords[1]], [0, 0, 1]])
    T2 = np.array([[1, 0, p_coords[0]], [0, 1, p_coords[1]], [0, 0, 1]])
    R = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])

    aff_mat = T2 @ R @ T1
    return aff_mat

def calcSSD(A, B):
    """
    Function to calculate the sum of squared differences between two images.

    SYNTAX:
        SSD = calcSSD(A, B)

    INPUTS:
        A - an image stored as a 2D array
        B - an image stored as a 2D array. B must the same size as A

    OUTPUTS:
        SSD - the value of the sum of squared differences
    """
    return np.nansum((A - B) ** 2)

def calcMSD(A, B):
    """
    Function to calculate the mean of squared differences between two images.

    SYNTAX:
        MSD = calcMSD(A, B)

    INPUTS:
        A - an image stored as a 2D array
        B - an image stored as a 2D array. B must be the same size as A

    OUTPUTS:
        MSD - the value of the mean of squared differences
    """
    return np.nanmean((A - B) ** 2)

def calcEntropies(A, B, num_bins=[32, 32]):
    """
    Function to calculate the joint and marginal entropies for two images.

    SYNTAX:
        [H_AB, H_A, H_B] = calcEntropies(A, B)
        [H_AB, H_A, H_B] = calcEntropies(A, B, num_bins)

    INPUTS:
        A - an image stored as a 2D array
        B - an image stored as a 2D array. B must be the same size as A
        num_bins - a 2 element vector specifying the number of bins to use in the joint histogram for each image
            default = [32, 32]

    OUTPUTS:
        H_AB - the joint entropy between A and B
        H_A - the marginal entropy in A
        H_B - the marginal entropy in B
    """
    nan_inds = np.logical_or(np.isnan(A), np.isnan(B))
    A = A[np.logical_not(nan_inds)]
    B = B[np.logical_not(nan_inds)]
    
    joint_hist, _, _ = np.histogram2d(A, B, bins=num_bins)
    probs_AB = joint_hist / np.sum(joint_hist)
    
    probs_A = np.sum(probs_AB, axis=1)
    probs_B = np.sum(probs_AB, axis=0)
    
    eps = np.finfo(float).eps
    H_AB = -np.nansum(probs_AB * np.log(probs_AB + eps))
    H_A = -np.nansum(probs_A * np.log(probs_A + eps))
    H_B = -np.nansum(probs_B * np.log(probs_B + eps))
    
    return H_AB, H_A, H_B

def dispImageFlip(image1, image2, int_lims=[]):
    """
    Function to display two grey-scale images that are stored in 'standard
    orientation' with y-axis on the 2nd dimension and 0 at the bottom. It is 
    possible to flip between the two images using the left and right arrow keys.
    SYNTAX:
        dispImage(image1, image2)
        dispImage(image1, image2, int_lims)

    INPUTS:
        image1 - first image to be displayed
        image2 - second image to be displayed
        int_lims - the intensity limits to use when displaying the image
            int_lims(1) = min intensity to display
            int_lims(2) = max intensity to display
            default = [min(np.nanmin(image1), np.nanmin(image2)), max(np.nanmax(image1), np.nanmax(image2))]
    """

    # Calculate the intensity limits if not provided
    if not int_lims:
        int_lims = [min(np.nanmin(image1), np.nanmin(image2)), max(np.nanmax(image1), np.nanmax(image2))]
        if int_lims[0] == int_lims[1]:
            int_lims[0] -= 1
            int_lims[1] += 1

    # Initialize a figure and axis
    fig, ax = plt.subplots()

    # Set up a list of images
    images = [image1.T, image2.T]
    current_image_index = [0]  # Use a list to hold the index, which is mutable

    # Display the first image
    img_display = ax.imshow(images[current_image_index[0]], cmap='gray', vmin=int_lims[0], vmax=int_lims[1], origin='lower')
    img_display.set_array(images[current_image_index[0]])
    ax.set_aspect('equal')
    ax.set_title(f"Image {current_image_index[0] + 1}")

    # Key press event handler
    def on_key(event):
        if event.key == 'right':
            current_image_index[0] = (current_image_index[0] + 1) % len(images)
        elif event.key == 'left':
            current_image_index[0] = (current_image_index[0] - 1) % len(images)
        
        # Update the displayed image
        img_display.set_array(images[current_image_index[0]])
        ax.set_title(f"Image {current_image_index[0] + 1}")
        plt.draw()

    # Connect the event handler to the figure
    fig.canvas.mpl_connect('key_press_event', on_key)
    fig.text(0.5, 0.02, 'Press <- or -> to navigate between the two images.', ha='center', va='top', fontsize=8, color='black')

    # Display the figure
    plt.tight_layout()
    plt.show()

def calcJacobian(def_field):
    """
    A function to calculate the Jacobian from a deformation field.

    SYNTAX:
        [J, J_Mat] = calcJacobian(def_field)

    INPUTS:
        def_field - the deformation field as a 3D array

    OUTPUTS:
        J - the Jacobian determinant for each pixel in the deformation field
        J_Mat - the full Jacobian matrix for each pixel in the deformation
            field as a 4D array (last 2 dimensions contain 2 x 2 matrix for
            each pixel)
    """
    # Calculate gradient of x component of deformation field
    [grad_x_x, grad_x_y] = np.gradient(def_field[:, :, 0])
    # Calculate gradient of y component of deformation field
    [grad_y_x, grad_y_y] = np.gradient(def_field[:, :, 1])

    # Initialize outputs as zeros
    J = np.zeros_like(grad_x_x)
    if grad_x_x.ndim == 2:
        J_Mat = np.zeros((grad_x_x.shape[0], grad_x_x.shape[1], 2, 2))
    elif grad_x_x.ndim == 3:
        J_Mat = np.zeros((grad_x_x.shape[0], grad_x_x.shape[1], grad_x_x.shape[2], 2, 2))

    # Loop over pixels in the deformation field
    for x in range(grad_x_x.shape[0]):
        for y in range(grad_x_x.shape[1]):
            # Form the Jacobian matrix for this pixel
            J_Mat_this_pix = np.array([[grad_x_x[x, y], grad_x_y[x, y]], [grad_y_x[x, y], grad_y_y[x, y]]])
            # Calculate and store the determinant
            J[x, y] = np.linalg.det(J_Mat_this_pix)
            # Store the full matrix
            J_Mat[x, y, :, :] = J_Mat_this_pix
            # More efficient to calculate determinant from matrix in temporary variable
    return J, J_Mat

def dispDefField(def_field, spacing=5, plot_type='grid'):
    """
    Function to display a deformation field.

    SYNTAX:
        dispDefField(def_field)
        dispDefField(def_field, spacing)
        dispDefField(def_field, spacing, plot_type)

    INPUTS:
        def_field - the deformation field as a 3D array
        spacing - the spacing of the grids/arrows in pixels
           default = 5
        plot_type - the type of plot to use, 'grid' or 'arrows'
            default = 'grid'
    """
    # Calculate coordinates for plotting grid-lines/arrows
    x_inds = np.arange(0, def_field.shape[0], spacing)
    y_inds = np.arange(0, def_field.shape[1], spacing)

    # Check if plotting grids
    if plot_type == 'grid':
        # Plot vertical lines
        plt.plot(def_field[x_inds, :, 0].T, def_field[x_inds, :, 1].T, 'k', linewidth=0.5)
        # Plot horizontal lines
        plt.plot(def_field[:, y_inds, 0], def_field[:, y_inds, 1], 'k', linewidth=0.5)

    elif plot_type == 'arrows':
        # Calculate grids of coordinates for plotting
        [Xs, Ys] = np.meshgrid(x_inds, y_inds, indexing='ij')
        # Calculate displacement field for plotting
        disp_field_x = def_field[Xs, Ys, 0] - Xs
        disp_field_y = def_field[Xs, Ys, 1] - Ys

        # Plot displacements using quiver function
        plt.quiver(Xs, Ys, disp_field_x, disp_field_y, angles='xy', scale_units='xy', scale=1)

    else:
        print('Display type must be grid or arrows')

    plt.axis('image')
