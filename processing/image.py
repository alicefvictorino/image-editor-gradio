import cv2
import numpy as np


class Image:
    def __init__(self, data):
        self.data = data

    def translate(self, x, y):
        """Translate the image by (x, y) pixels."""
        transformation_matrix = np.float32([[1, 0, x], [0, 1, y]])
        translated_image = cv2.warpAffine(self.data, transformation_matrix, (self.data.shape[1], self.data.shape[0]))
        return Image(translated_image)
    
    def rotate(self, angle, scale):
        """Rotate the image by a given angle and scale."""
        (height, width) = self.data.shape[:2]
        center = (width // 2, height // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
        rotated_image = cv2.warpAffine(self.data, rotation_matrix, (width, height))
        return Image(rotated_image)
    
    def scale(self, new_width, new_height):
        """Resize image to specified dimensions."""
        scaled_image = cv2.resize(self.data, (new_width, new_height))
        return Image(scaled_image)
    
    def change_colorspace(self, option):
        """Convert image to specified color space."""
        color_spaces = {
            'gray': cv2.COLOR_BGR2GRAY,
            'hsv': cv2.COLOR_BGR2HSV,
            'lab': cv2.COLOR_BGR2LAB,
            'rgb': cv2.COLOR_BGR2RGB,
            'ycrcb': cv2.COLOR_BGR2YCrCb,
            'xyz': cv2.COLOR_BGR2XYZ
        }

        converted_image = cv2.cvtColor(self.data, color_spaces[option])
        return Image(converted_image)
    
    def constrast(self, constant):
        """Adjust image contrast"""
        contrast_image = cv2.convertScaleAbs(self.data, alpha=constant, beta=0) # avoid overflow/underflow
        return Image(contrast_image)
    
    def gamma_correction(self, gamma):
        """Apply gamma correction to the image."""
        inv_gamma = 1.0 / gamma
        table = np.array([(i / 255.0) ** inv_gamma * 255 for i in range(256)], dtype="uint8")
        gamma_corrected_image = cv2.LUT(self.data, table)
        return Image(gamma_corrected_image)
