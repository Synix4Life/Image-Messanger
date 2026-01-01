import numpy as np
import cv2

def ascii_to_binary(_text: str) -> np.ndarray:
    binary_string = ''.join([bin(ord(char))[2:].zfill(8) for char in _text])
    num_bits = len(binary_string)

    height = int(np.floor(np.sqrt(num_bits)))
    width = int(np.ceil(num_bits / height))

    padded_binary_string = binary_string.ljust(height * width, '0')

    return np.array(list(padded_binary_string), dtype=int).reshape((height, width))

def array_to_image(_array: np.array, filename: str):
    img = (1 - _array) * 255
    cv2.imwrite(filename, img.astype(np.uint8))

def generate(message: str, filename: str) -> None:
    """
    Method to generate the message
    :param message: The message you want to 'encrypt'
    :param filename: The filename
    """
    binary = ascii_to_binary(message)
    array_to_image(binary, filename)
