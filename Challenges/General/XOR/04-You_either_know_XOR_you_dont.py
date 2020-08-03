
from pwn import xor


encrypted = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
plaintext = b'crypto{1'
key = ''.join(chr(c ^ m) for c, m in zip(encrypted, plaintext))
print(key)

print(xor(encrypted,b'myXORkey'))
