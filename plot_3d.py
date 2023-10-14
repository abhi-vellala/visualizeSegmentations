# from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import nibabel as nib

mask_load = nib.load('./data/covid_infection_mask.nii')
mask = mask_load.get_fdata()
mask = mask.T
z, x, y = mask.nonzero()

ax = plt.axes(projection='3d')

ax.scatter(x, y, z, c=z, alpha=0.05)
plt.show()
