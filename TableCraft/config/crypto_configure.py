from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from config.config import key


cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend()) # noqa
