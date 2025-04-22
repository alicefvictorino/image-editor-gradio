import numpy as np

from processing.image import Image
from processing.operations import (apply_color_operations,
                                   apply_gamma_correction,
                                   apply_geometric_operations)


def process_image(image, image_state, operation, *args):
    """Process the image based on the selected operation and its arguments."""

    # Return early if no valid input is provided
    if image is None and image_state is None:
        return None, None
    
    # Determine the source of the image data
    if image_state is not None:
        image_array = image_state
    elif image is not None:
        image_array = np.array(image)

    img = Image(image_array)

    if operation == "Geometric Transformations":
        trans_x, trans_y, rotation_angle, scale_factor_x, scale_factor_y = args[:5]
        img = apply_geometric_operations(img, trans_x, trans_y, rotation_angle, scale_factor_x, scale_factor_y)

    elif operation == "Color Space Operations":
        color_space, contrast_factor = args[5:7]
        img = apply_color_operations(img, color_space, contrast_factor)

    elif operation == "Gamma Correction":
        gamma_value = args[7]
        img = apply_gamma_correction(img, gamma_value)

    return img.data, img.data