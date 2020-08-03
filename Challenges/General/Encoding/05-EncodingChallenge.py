import telnetlib
import json
from Crypto.Util import number
import codecs
import base64


def readline():
    return tn.read_until(b"\n")


def json_recv():
    line = readline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)


def decoder(json):
    if 'flag' in json:
        print("FOUND THE FLAG ----> ",json['flag'])

    type_rcv = json['type']
    encoded = json['encoded']

    if type_rcv == 'hex':
        hex_string_as_bytes = bytes.fromhex(encoded)
        return hex_string_as_bytes.decode('UTF-8')

    elif type_rcv == 'utf-8':
        flag_decoded = [chr(elm) for elm in encoded]
        return "".join(flag_decoded)

    elif type_rcv == 'base64':
        return base64.b64decode(encoded).decode('UTF-8')

    elif type_rcv == 'rot13':
        return codecs.encode(encoded, 'rot_13')

    elif type_rcv == 'bigint':
        converted_to_int = int(encoded, 0)
        conv = number.long_to_bytes(converted_to_int)
        return conv.decode('UTF-8')

if __name__ == '__main__':

    HOST = "socket.cryptohack.org"
    PORT = 13377

    tn = telnetlib.Telnet(HOST, PORT)

    for i in range(0, 101):
        received = json_recv()
        print(f" i = {i} --- RECEIVED: ---> {received}")

        x = decoder(received)
        to_send = {
            "decoded": x
        }
        print("SENDING: ---> ", to_send)
        json_send(to_send)

