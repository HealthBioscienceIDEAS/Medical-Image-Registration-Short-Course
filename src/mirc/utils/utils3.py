"""
utility functions for use in the image registration exercises 3 for module MPHY0025 (IPMI)

Jamie McClelland
UCL
"""

import numpy as np 
import matplotlib.pyplot as plt
plt.style.use('default')
import scipy.interpolate as scii

def dispImage(img, int_lims = [], title = ''):
  """
 function to display a grey-scale image that is stored in 'standard
 orientation' with y-axis on the 2nd dimension and 0 at the bottom

 SYNTAX:
   dispImage(img)
   dispImage(img, int_lims)

 INPUTS:
   img - image to be displayed
   int_lims - the intensity limits to use when displaying the image
       int_lims(1) = min intensity to display
       int_lims(2) = max intensity to display
       default = [np.nanmin(img), np.nanmax(img)]
  """

  #check if intensity limits have been provided, and if not set to min and
  #max of image
  if not int_lims:
    int_lims = [np.nanmin(img), np.nanmax(img)]
    #check if min and max are same (i.e. all values in img are equal)
    if int_lims[0] == int_lims[1]:
      #add one to int_lims(2) and subtract one from int_lims(1), so that
      #int_lims(2) is larger than int_lims(1) as required by imagesc
      #function
      int_lims[0] -= 1
      int_lims[1] += 1
  
  # take transpose of image to switch x and y dimensions and display with
  # first pixel having coordinates 0,0
  img = img.T
  plt.gca().clear()
  plt.imshow(img, cmap = 'gray', vmin = int_lims[0], vmax = int_lims[1], origin='lower')
  
  # Set title for the subplot
  plt.title(title)

  #set axis to be scaled equally (assumes isotropic pixel dimensions), tight
  #around the image
  plt.axis('image')
  plt.tight_layout()

def resampImageWithDefField(source_img, def_field, interp_method = 'linear', pad_value=np.NaN):
  """
 function to resample a 2D image with a 2D deformation field

 SYNTAX:
   resamp_img = resampImageWithDefField(source_img, def_field)
   resamp_img = resampImageWithDefField(source_img, def_field, interp_method)
   resamp_img = resampImageWithDefField(source_img, def_field, interp_method, pad_value)

 INPUTS:
   source_img - the source image to be resampled, as a 2D array
   def_field - the deformation field, as a 3D array
   inter_method - any of the interpolation methods accepted by interpn
       function ('linear', 'nearest' and 'splinef2d')
       default = 'linear'
   pad_value - the value to assign to pixels that are outside the source
       image
       default = NaN

 OUTPUTS:
   resamp_img - the resampled image

 NOTES:
   the deformation field should be a 3D array, where the size of the
   first two dimensions is the size of the resampled image, and the size
   of the 3rd dimension is 2. def_field(:,:,1) contains the x coordinates
   of the transformed pixels, def_field(:,:,2) contains the y coordinates
   of the transformed pixels.
   the origin of the source image is assumed to be the bottom left pixel
  """
  x_coords = np.arange(source_img.shape[0], dtype = 'float')
  y_coords = np.arange(source_img.shape[1], dtype = 'float')
  
  # resample image using interpn function
  return scii.interpn((x_coords, y_coords), source_img, def_field, bounds_error=False, fill_value=pad_value, method=interp_method)

def calcMSD(A,B):
  """
 function to calculate the mean of squared differences between two images

 SYNTAX:
   MSD = calcMSD(A, B)

 INPUTS:
   A - an image stored as a 2D array
   B - an image stored as a 2D array. B must the the same size as A

 OUTPUTS:
   MSD - the value of the mean of squared differences

 NOTE:
   if either of the images contain NaN values these pixels should be 
   ignored when calculating the SSD.
  """
  # use nansum function to find sum of squared differences ignoring NaNs
  return np.nanmean((A-B)*(A-B))

def calcJacobian(def_field):
  """
 a function to calculate the Jacobian from a deformation field

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
  # calculate gradient of x component of deformation field
  [grad_x_x, grad_x_y] = np.gradient(def_field[:, :, 0])
  # calculate gradient of y component of deformation field
  [grad_y_x, grad_y_y] = np.gradient(def_field[:, :, 1])

  # initlaise outputs as 0s
  J = np.zeros_like(grad_x_x)
  if grad_x_x.ndim == 2:
    J_Mat = np.zeros((grad_x_x.shape[0], grad_x_x.shape[1], 2, 2))
  elif grad_x_x.ndim == 3:
    J_Mat = np.zeros((grad_x_x.shape[0], grad_x_x.shape[1], grad_x_x.shape[2], 2, 2))

  # loop over pixels in the deformation field
  for x in range(grad_x_x.shape[0]):
    for y in range(grad_x_x.shape[1]):
      # form the Jacobian matrix for this pixel
      J_Mat_this_pix = np.array([[grad_x_x[x, y], grad_x_y[x, y]], [grad_y_x[x, y], grad_y_y[x, y]]])
      # calculate and store the determinant
      J[x, y] = np.linalg.det(J_Mat_this_pix)
      # and store the full matrix
      J_Mat[x, y, :, :] = J_Mat_this_pix
      # note - more efficient to calculate determinant from matrix in
      # temporary variable rather than directly from values in J_Mat as
      # the matrix values for a pixel are not stored contiguously in
      # memory in J_Mat
  return J, J_Mat

def dispDefField(def_field, spacing=5, plot_type='grid'):
  """
 function to display a deformation field

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
  # calculate coordinates for plotting grid-lines/arrows
  x_inds = np.arange(0, def_field.shape[0], spacing)
  y_inds = np.arange(0, def_field.shape[1], spacing)
  
  # check if plotting grids
  if plot_type == 'grid':
    
    # plot vertical lines
    plt.plot(def_field[x_inds, :, 0].T, def_field[x_inds, :, 1].T, 'k', linewidth=0.5)
    #plot horizontal lines
    plt.plot(def_field[:, y_inds, 0], def_field[:, y_inds, 1], 'k', linewidth=0.5)
    
  else:
    
    if plot_type == 'arrows':
      
      # calculate grids of coords for plotting
      [Xs, Ys] = np.meshgrid(x_inds, y_inds, indexing='ij')
      # calculate displacement field for plotting
      disp_field_x = def_field[Xs, Ys, 0] - Xs
      disp_field_y = def_field[Xs, Ys, 1] - Ys
      
      #plot displacements using quiver function
      plt.quiver(Xs, Ys, disp_field_x, disp_field_y, angles='xy', scale_units='xy', scale=1)
      
    else:
      print('Display type must be grid or arrows')
    
  plt.axis('image')
  
  