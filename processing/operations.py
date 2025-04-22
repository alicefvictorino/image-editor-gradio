def apply_geometric_operations(img, trans_x, trans_y, rotation_angle, scale_factor_x, scale_factor_y):
    """Apply geometric transformations to the image."""
    if trans_x != 0 or trans_y != 0:
        img = img.translate(trans_x, trans_y)

    if rotation_angle != 0:
        img = img.rotate(rotation_angle, 1.0)

    if scale_factor_x != 1.0 or scale_factor_y != 1.0:
        height, width = img.data.shape[:2]
        new_width = int(width * scale_factor_x)
        new_height = int(height * scale_factor_y)
        img = img.scale(new_width, new_height)

    return img

def apply_color_operations(img, color_space, contrast_factor):
    """Apply color space transformations and contrast adjustment."""
    
    color_map = {
        "RGB": "rgb",
        "Grayscale": "gray",
        "HSV": "hsv",
        "LAB": "lab"
    }

    if color_space != "RGB":
        img = img.change_colorspace(color_map.get(color_space.lower(), "rgb"))

    if contrast_factor != 1.0:
        img = img.constrast(contrast_factor)  # Note: there's a typo here "constrast" instead of "contrast"

    return img

def apply_gamma_correction(img, gamma_value):
    """Apply gamma correction to the image.
    
    Args:
        img: Image object
        gamma_value: Gamma correction value
        
    Returns:
        Gamma-corrected image object
    """
    if gamma_value != 1.0:
        img = img.gamma_correction(gamma_value)
    return img