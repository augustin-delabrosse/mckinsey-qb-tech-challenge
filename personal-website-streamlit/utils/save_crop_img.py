import io
from PIL import Image
import leafmap.foliumap as leafmap
import os 
import cv2

"""
    plotly_hist(lat, lon): 
        Usecase: saves and crops the image around the searched coordinates
        Input:  m
                    - Leafmap map object
                top_left_coordinates (tuple)
                    - top_left_coordinates tuple
                bottom_right_coordinates (tuple)
                    - bottom_right_coordinates tuple
        Output: Cropped image of location
"""

def save_crop_image(m, top_left_coordinates, bottom_right_coordinates):
    m.fit_bounds([top_left_coordinates, bottom_right_coordinates]) 
    img_data = m._to_png(5)
    img_data = Image.open(io.BytesIO(img_data))
    box = (430, 75, 930, 575)
    img_data = img_data.crop(box)
    img_data.save('images/demonstration.png')
    return img_data