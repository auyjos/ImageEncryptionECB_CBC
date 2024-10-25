from PIL import Image
import numpy as np
from Crypto.Cipher import AES
import os

# a. Convertir la imagen a bytes


def image_to_bytes(image_path):
    image = Image.open(image_path).convert('RGBA')
    image_data = np.array(image).reshape(-1)
    return image_data.tobytes()

# b. Cifrar los bytes usando AES-128 en modo ECB


def encrypt_ecb(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    # Rellenar datos para que sean múltiplos de 16
    padding_length = 16 - (len(data) % 16)
    data += bytes([padding_length]) * padding_length
    encrypted_data = cipher.encrypt(data)
    return encrypted_data

# c. Guardar los bytes cifrados como una imagen


def bytes_to_image(data, width, height, output_path):
    img = Image.frombytes('RGBA', (width, height), data)
    img.save(output_path)


# Clave AES de 128 bits (16 bytes)
key = os.urandom(16)

# Ruta de la imagen
image_path = 'tux.bmp'
output_ecb = 'encrypted_ecb.png'

# Ejecución
image_bytes = image_to_bytes(image_path)
encrypted_bytes_ecb = encrypt_ecb(image_bytes, key)
bytes_to_image(encrypted_bytes_ecb, 405, 480, output_ecb)
