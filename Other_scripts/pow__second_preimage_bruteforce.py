#":|\';]}[{>.,<>/?=+-_0)((*&^%$#))
#Task 2: Send me a 4 character uppercase string <str> such that\n'
#b'  md5("mhaluwedxi_"+<str>) is ccb276f1427a910f4b4163f26a2bb417\n'

from pwn import *;
from hashlib import md5;

r = remote('blabla.it',5000);
r.recvuntil(': ');
r.recvuntil(': ');
data = r.recvuntil('\n');
r.send(data);

print(r.recvuntil('("'));
addendo = str(r.recvuntil('_'));
#print(addendo);
addendo = addendo[2:-1];
print('ADDENDO = ' + addendo);
print(type(addendo));
print(r.recvuntil('is '));
somma = str(r.recvline());
#print(somma);
somma = somma[2:-3];
print('SOMMA = ' + somma);
found = 0;
alfabeto = "ABCDEFGHILMNOPQRSTUVZJKXYW"
for a in alfabeto:
    if found==1:
        break
    for b in alfabeto:
        if found==1:
            break
        for c in alfabeto:
            if found==1:
                break
            for d in alfabeto:
                temp = a+b+c+d;
                stringa = addendo+temp;
                #print(temp);
                valore = hashlib.md5(stringa.encode());
                valore = valore.hexdigest();
                #ERRORE;
                if valore == somma:
                    temp = str(temp);
                    #temp = bytes(temp,'utf-8');
                    temp = temp.encode();
                    print(temp);
                    print(type(temp));
                    r.send(temp);
                    print("TROVATO");
                    #print(r.recvall(timeout=1));
                    r.interactive();
                    found = 1;
                    break;
print("FINITO: "+str(found));

