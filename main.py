import nibabel as nib
from mask_visualize import plotmask


mask_load = nib.load('./data/covid_infection_mask.nii')
mask = mask_load.get_fdata()
mask = mask.T

zoom_ratio = (0.2,0.2,0.2)
enlarge_by = 4
save_path = 'plot_covid_infections.html'

plotmask(mask, zoom_ratio, enlarge_by,  save_path, img_type='html', show_img = False,
             renderer='browser')

