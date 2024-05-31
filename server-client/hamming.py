import math


def encode(word):
    if len(word) % 2 == 1:
        word = word + ' '
    bin_result = ''.join(format(x, '08b') for x in bytearray(word, 'utf-8'))
    message = ""
    bin = bin_result
    blocks = len(bin_result) / 16
    for i in range(math.ceil(blocks)):
            chuck = bin[:16]
            bin = bin[16:]
            chuck = '00' + chuck[0] + '0' + chuck[1:4] + '0' + chuck[4:11] + '0' + chuck[11:]
            bits = [1, 2, 4, 8, 16]
            for k in bits:
                contrl = 0
                for a in range(k-1, len(chuck), k+k):
                    for y in range(a, a+k, 1):
                        if chuck[y] == '1':
                            contrl += 1
                        if y+1 == len(chuck):
                            break
                if contrl % 2 == 0:
                    chuck = chuck[:k-1] + '0' + chuck[k:]
                else:
                    chuck = chuck[:k-1] + '1' + chuck[k:]
            message += chuck
    return message


def decode(message):
    result = ''
    blocks = len(message) / 21
    for i in range(int(blocks)):
        chuck = message[:21]
        eq = message[:21]
        message = message[21:]
        chuck = '00' + chuck[2] + '0' + chuck[4:7] + '0' + chuck[8:15] + '0' + chuck[16:]
        bits = [1, 2, 4, 8, 16]
        error = 0
        for k in bits:
            contrl = 0
            for a in range(k - 1, len(chuck), k + k):
                for y in range(a, a + k, 1):
                    if chuck[y] == '1':
                        contrl += 1
                    if y + 1 == len(chuck):
                        break
            if contrl % 2 == 0:
                chuck = chuck[:k - 1] + '0' + chuck[k:]
            else:
                chuck = chuck[:k - 1] + '1' + chuck[k:]
        for j in range(len(chuck)):
            if chuck[j] != eq[j]:
                error += j+1
        if error != 0:
            if chuck[error-1] == '0':
                chuck = chuck[:error-1] + '1' + chuck[error:]
            else:
                chuck = chuck[:error-1] + '0' + chuck[error:]
        chuck = chuck[2] + chuck[4:7] + chuck[8:15] + chuck[16:]
        result += chuck
    normal_string = ''.join(chr(int(result[i:i + 8], 2)) for i in range(0, len(result), 8))
    return normal_string


def do_error(message):
    if message[10] == '0':
        message = message[:10] + '1' + message[11:]
    else:
        message = message[:10] + '0' + message[11:]
    return message