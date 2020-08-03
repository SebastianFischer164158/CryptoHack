string = "label"
res = [ord(x)^13 for x in string]
res_string = [chr(x) for x in res]
result = "".join(res_string)
print(result)
