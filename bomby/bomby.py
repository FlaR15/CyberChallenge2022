from pwn import *

def fun():
    chars = "maduiersnfotvbyl"
    final = "flyers"
    s = ""
    for c in final:
        n = chars.index(c)
        n = n+0x60
        s += chr(n)
    print(s)
    return s


'''for a in range(1,7):
    for b in range(1,7):
        if a==b:
            continue     
        for c in range(1,7):
            if a==c or b == c:
                continue
            for d in range(1,7):
                if d==a or d==b or d ==c:
                    continue
                for e in range(1,7):
                    if e==a or e==b or e==c or e==d:
                        continue
                    for f in range(1,7):
                        if f==a or f==b or f==c or f==d or f==e:
                            continue
                        stringa = str(a)+" "+str(b)+" "+str(c)+" "+str(d)+" "+str(e)+" "+str(f)
                        print(stringa)
                        if stringa=="4 3 2 1 6 5":
                            continue
                        r = process("./bomb")
                        r.waitfor("a nice day!")
                        r.sendline("Border relations with Canada have never been better.")
                        r.sendline("1 2 4 8 16 32")
                        r.sendline("0 207")
                        r.sendline("7 0")
                        r.sendline("ionefg")
                        r.sendline(stringa)
                        for i in range(8):
                            r.recvline()
                        if not(b'BOOM' in r.recvline()):
                            r.interactive()
                        r.close()'''


r = process("./bomb")
r.waitfor("a nice day!")
r.sendline("Border relations with Canada have never been better.")
r.sendline("1 2 4 8 16 32")
r.sendline("0 207")
r.sendline("7 0")
r.sendline("ionefg")
r.sendline("4 3 2 1 6 5")
r.interactive()