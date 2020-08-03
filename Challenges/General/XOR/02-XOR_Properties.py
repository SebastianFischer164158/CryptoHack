import binascii

from pwn import xor

"""
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

Commutative: A ⊕ B = B ⊕ A
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity: A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0

"""
# key2 ^ key1 = a
# key1 ^(key2 ^ key1) = a ^ key1
# (key1^key1) ^ key2 = a ^ key1
# key2 = a ^ key1

key1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
a = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
key2 = hex(int(a, 16) ^ int(key1, 16))

print(key2)
# key2 ^key3 = b
# key2^(key2^key3) = b ^ key2
# (key2^key2) ^ key3 = b ^ key2
# key3 = b ^ key2
b = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
key3 = hex(int(b, 16) ^ int(key2, 16))
print(key3)

# flag ^ key1 ^ key3 ^ key2 = c
# flag ^ res1 = c
# res1^(flag ^ res1) = c ^ res 1
# (res1 ^ res1) ^ flag = c ^ res1
# flag = c ^ res1
# flag = c ^ key1 ^key3 ^ key2
c = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
flag = hex(int(c, 16) ^ int(key1, 16) ^ int(key3,16) ^ int(key2,16))
print(flag, flag[2:])
print("flag---> ", binascii.unhexlify(flag[2:]))
