class Cipher:
    def __init__(self):
        pass

    def caesar(self, str):
        from codecs import encode
        return encode(str, 'rot13')
