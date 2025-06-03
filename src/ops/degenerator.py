import numpy as np
import cv2

def binary_to_ascii(_binary_array: np.ndarray) -> str:
    binary_string = ''.join(map(str, _binary_array.flatten()))

    length = len(binary_string)
    trimmed_length = length - (length % 8)
    binary_string = binary_string[:trimmed_length]

    ascii_chars = [chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8)]

    return ''.join(ascii_chars)

def image_to_array(filename: str) -> np.array:
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    if img is None:
        raise FileNotFoundError(f"Error: Could not read the image at '{filename}'")
    
    binary_img = (img < 128).astype(int)
    
    return binary_img

def degenerate(filename: str) -> str:
    """
    Method to 'decrypt' the image
    :param filename: The filename
    :raises FileNotFoundError: If the message- image doesn't exist
    """
    result = image_to_array(filename)
    return binary_to_ascii(result)
