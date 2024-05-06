import base64
import itertools
from Crypto.Cipher import Blowfish

text = base64.b64decode("BahoP2kAnYuRf5LqEW5umIRwZZD7iKrcOzdKXglXMKg=")

print(text)


def bruteforce_key(length=8):
    characters = 'ABCDEF'
    for combo in itertools.product(characters, repeat=length):
        yield ''.join(combo)

for key in bruteforce_key():
    cipher = Blowfish.new(key.encode(), Blowfish.MODE_ECB)
    result = cipher.decrypt(text)
    if(b"ph0wn" in result):
        print("->", key)
        print(result)
        exit(1)
    print(key)