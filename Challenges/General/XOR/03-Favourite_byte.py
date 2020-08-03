from pwn import xor


hidden = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

for i in range(0,257):
    res = xor(hidden,i)
    if 'crypto' in res.decode():
        print(res)
