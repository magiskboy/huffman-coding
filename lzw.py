from bitarray import bitarray
import utils

CODE_LENGTH = 9

def create_bits(x):
    return bitarray(bin(x)[2:].zfill(CODE_LENGTH))

def initial_dict():
    return {chr(i): i for i in range(256)}

def encode(data):
    output = []

    d = initial_dict()
    c = len(d.values())

    buf = data[0]
    # create dictionary
    for ch in data[1:]:
        buf += ch 
        if buf in d:
            continue
        
        d[buf] = c
        c += 1
        buf = buf[1:]

    # encoding
    ret = bitarray()
    buf = ''
    for ch in data:
        buf += ch
        if buf not in d:
            continue

        encoded = create_bits(d[buf])
        ret += encoded
        buf = ''

    return ret.tobytes()

def decode(data):
    bs = bitarray()
    bs.frombytes(data)

    d = initial_dict()
    c = len(d.values())
    output = ''
    
    w = data[0]

    for i in range(len(bs) / CODE_LENGTH):
        seg = bs[i*CODE_LENGTH:(i+1)*CODE_LENGTH]

    for item in bs.__iand__:
        entry = d[chr(item)]
        output += chr(entry)
        d[w + entry] = c
        c += 1
        w = entry

    return output


if __name__ == '__main__':
    data = utils.load_example()

    encoded = encode(data)

    print(data.encode().__len__())
