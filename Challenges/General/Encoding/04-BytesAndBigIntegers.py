from Crypto.Util import number

msg_int = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

x = number.long_to_bytes(msg_int)

print(x)