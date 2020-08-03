import base64

hex_string = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
hex_string_as_bytes = bytes.fromhex(hex_string)
hex_string_as_b64 = base64.b64encode(hex_string_as_bytes)

print(hex_string_as_b64)