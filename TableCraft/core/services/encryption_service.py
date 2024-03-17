from cryptography.hazmat.primitives import padding
from config.crypto_configure import cipher


class EncryptData():

    def encrypt(self, data_to_encrypt):

        data = data_to_encrypt

        encryptor = cipher.encryptor()
        url_bytes = data.encode('utf-8')

        padder = padding.PKCS7(128).padder()
        padded_url_bytes = padder.update(url_bytes) + padder.finalize()

        encrypted_url = encryptor.update(padded_url_bytes) + encryptor.finalize() # noqa

        return encrypted_url.strip()


class DecryptData():

    def decrypt(self, data_to_decrypt):

        data = data_to_decrypt
        decryptor = cipher.decryptor()

        decrypted_url = decryptor.update(data) + decryptor.finalize()
        original_url = decrypted_url.decode('utf-8')

        return original_url.strip()
