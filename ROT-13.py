def encode(message):
    l1 = []
    r=''
    plain=list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    cypher=list('NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
    for i in message:
        for k1,v1 in enumerate(plain):
            if i == v1:
                l1.append(k1)
    for x in l1:
        v2 = cypher[int(x)]
        r = r+v2
    return r

def decode(message):
    l1 = []
    r=''
    plain=list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    cypher=list('NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
    for i in message:
        for k1,v1 in enumerate(cypher):
            if i == v1:
                l1.append(k1)
    for x in l1:
        v2 = plain[int(x)]
        r = r+v2
    return r

var=input('Would you like to encode or decode?: ')
string=input('Please enter text: ')

if var == 'encode':
    print(encode(string))
if var == 'decode':
    print(decode(string))