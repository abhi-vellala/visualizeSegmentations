
import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import clear_border
from skimage import measure
from skimage.measure import label,regionprops
from scipy import ndimage as ndi
from scipy.ndimage import measurements, center_of_mass, binary_dilation, zoom
import plotly.graph_objects as go



def plotmask(mask, zoom_ratio, enlarge_by, save_path, img_type='html', show_img = False,
             renderer='browser'):
    im = zoom(1 * (mask), (zoom_ratio))
    z, y, x = [np.arange(i) for i in im.shape]
    z *= enlarge_by
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

    fig = go.Figure(data=go.Volume(
        x=X.flatten(),
        y=Y.flatten(),
        z=Z.flatten(),
        value=np.transpose(im, (1, 2, 0)).flatten(),
        isomin=0.1,
        opacity=0.1,  # needs to be small to see through all surfaces
        surface_count=17,  # needs to be a large number for good volume rendering
    ))
    if img_type == 'html':
        fig.write_html(save_path)
    if img_type == 'png' or img_type == 'jpeg':
        fig.write_image(save_path)

    if show_img:
        fig.show(renderer=renderer)


