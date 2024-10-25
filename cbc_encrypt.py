from PIL import Image
import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

# a. Image to bytes


def image_to_bytes(image_path):
    image = Image.open(image_path).convert('RGBA')
    image_data = np.array(image).reshape(-1)
    return image_data.tobytes()

# b. Cypher bytes using AES-128 CBC


def encrypt_cbc(data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data, 16)  # Rellenar datos para que sean múltiplos de 16
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

# c. Bytes as image


def bytes_to_image(data, width, height, output_path):
    img = Image.frombytes('RGBA', (width, height), data)
    img.save(output_path)


# AES key 128 bits (16 bytes)
key = os.urandom(16)

# Vector (IV) for  CBC
iv = os.urandom(16)  # 16 bytes

image_path = 'tux.bmp'
output_cbc = 'encrypted_cbc.png'


image_bytes = image_to_bytes(image_path)
encrypted_bytes_cbc = encrypt_cbc(image_bytes, key, iv)
bytes_to_image(encrypted_bytes_cbc, 405, 480, output_cbc)

print("Cypher complete. Image saved as:", output_cbc)
