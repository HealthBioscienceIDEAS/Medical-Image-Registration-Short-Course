"""
example solution for the image registration exercises 3 for module MPHY0025 (IPMI)

Author: Jamie McClelland UCL
Contributors: Zakaria Senousy and Miguel Xochicale UCL-ARC
"""
import matplotlib.pyplot as plt
from src.mirc.utils.demonsReg import demonsReg
from src.mirc.utils.utils3 import dispImage, dispDefField, calcJacobian
import numpy as np
import skimage.io
#%matplotlib qt

cine_MR_img_1 = skimage.io.imread('cine_MR_1.png') 
cine_MR_img_2 = skimage.io.imread('cine_MR_2.png')
cine_MR_img_3 = skimage.io.imread('cine_MR_3.png')


cine_MR_img_1 = np.double(cine_MR_img_1)
cine_MR_img_2 = np.double(cine_MR_img_2)
cine_MR_img_3 = np.double(cine_MR_img_3)

cine_MR_img_1 = np.flip(cine_MR_img_1.T, 1)
cine_MR_img_2 = np.flip(cine_MR_img_2.T, 1)
cine_MR_img_3 = np.flip(cine_MR_img_3.T, 1)

plt.figure()
dispImage(cine_MR_img_1)
plt.figure()
dispImage(cine_MR_img_2)
plt.figure()
dispImage(cine_MR_img_3)
plt.figure()
dispImage(cine_MR_img_1 - cine_MR_img_2)
plt.figure()
dispImage(cine_MR_img_1 - cine_MR_img_3)

plt.close('all')


[warped_image_def, def_field_def] = demonsReg(cine_MR_img_1, cine_MR_img_2)
[warped_image, def_field] = demonsReg(cine_MR_img_1, cine_MR_img_2, sigma_elastic=0)
[warped_image, def_field] = demonsReg(cine_MR_img_1, cine_MR_img_2, sigma_fluid=0)

plt.figure()
dispImage(warped_image_def)
plt.figure()
dispDefField(def_field_def, spacing=2)

[warped_image, def_field] = demonsReg(cine_MR_img_1, cine_MR_img_2, num_lev=1)

[warped_image, def_field] = demonsReg(cine_MR_img_1, cine_MR_img_2, num_lev=6)

[warped_image_add, def_field_add] = demonsReg(cine_MR_img_1, cine_MR_img_2, sigma_elastic=0.5)

[J, J_Mat] = calcJacobian(def_field_add)
plt.figure()
dispImage(J)
plt.set_cmap('jet')
plt.colorbar()
plt.figure()
dispImage(J<=0)

[warped_image_comp, def_field_comp] = demonsReg(cine_MR_img_1, cine_MR_img_2, sigma_elastic=0.5, use_composition=True)
[J, J_Mat] = calcJacobian(def_field_comp)
plt.figure()
dispImage(J)
plt.set_cmap('jet')
plt.colorbar()
plt.figure()
dispImage(J<=0)
plt.figure()
dispImage(warped_image_add)


[warped_image, def_field] = demonsReg(cine_MR_img_1, cine_MR_img_2, check_MSD=False, disp_freq=50)

[warped_image, def_field] = demonsReg(cine_MR_img_1, cine_MR_img_2, check_MSD=False, disp_freq=50, max_it=500)

[warped_image, def_field] = demonsReg(cine_MR_img_1, cine_MR_img_2, use_target_grad=True)

plt.figure()
dispImage(warped_image_def)
plt.figure()
dispDefField(def_field_def, spacing=2)

[warped_image, def_field] = demonsReg(cine_MR_img_1, cine_MR_img_3, sigma_elastic=0, sigma_fluid=5, use_composition=True, num_lev=6, disp_freq=0)
[warped_image, def_field] = demonsReg(cine_MR_img_3, cine_MR_img_1, sigma_elastic=0.6, sigma_fluid=0.5, use_composition=True, num_lev=6, disp_freq=0)


