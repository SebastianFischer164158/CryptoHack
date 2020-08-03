
flag_encoded = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

flag_decoded = [chr(x) for x in flag_encoded]
flag = "".join(flag_decoded)
print(flag)