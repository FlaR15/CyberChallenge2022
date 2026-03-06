from hashlib import md5
from Crypto.Cipher import AES

ciphertext = "1d63f681426d76547f276f029294c95291c303fb952dd80321bf1e977a8a5959e66b47519af349001c6453d7f493233254d3299c1427bd193d86120959f6ed77"
ciphertext = ciphertext.upper()
A = []
b = []

for i in range(20):
    f = open("./dumps/dump_%d"%i, "r")
    f.readline()

    #chall = eval(f.readline().strip().replace(" " , ","))
    chall = f.readline().strip()[1:]
    chall = chall.replace(" " , ",").split(",")
    for i in range(len(chall)):
        print(chall[i])
        if ']' in chall[i]:
            continue
        chall[i] = int(chall[i])
    chall = chall[:-1]
    print("CHALL: ", chall)
    res = int(f.readline())

    A.append(chall)
    b.append(res)

A = matrix(ZZ,A)
b = vector(ZZ,b)

x=A.solve_right(b)
key = ""
for k in x:
    key += str(k)

key = md5(key.encode()).digest()

cipher = bytes.fromhex(ciphertext)
alg = AES.new(key, AES.MODE_CBC, b"whoooo_caresssss")
print(alg.decrypt(cipher).strip())
