from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import math


'''def decryptFile(value):
    value = str(value)
    print(value)
    path = 'pkeys/'+value+'.pem'
    f = open(path,'r')
    key = RSA.importKey(f.read())   #public key
    f.close()
    print("N: ",key.n)              #e and n are known
    
    path = 'cipher/'+value+'.enc'
    f = open(path,'rb')
    c = f.read()
    #print("Ciphertext: ", c)
    f.close()

    phi = int((pow(key.n,1/2)-1)*(pow(key.n,1/2)-1))
    d = pow(key.e,-1,phi)

    key = RSA.construct((key.n, key.e, d))
    key = PKCS1_OAEP(key)
    pt = key.decrypt(c)
    print(pt)
    
    #print(key[i+2]) The key is longer than the message
    print(ris)
    if 'ccit{' in ris:
        print(ris)
        return True
    return False'''

'''def decryptFile(value1,value2):
    value1 = str(value1)
    value2 = str(value2)
    path = 'pkeys/'+value1+'.pem'
    f = open(path,'r')
    key1 = RSA.importKey(f.read())
    f.close()
    path = 'pkeys/'+value2+'.pem'
    f = open(path,'r')
    key2 = RSA.importKey(f.read())
    f.close()

    path = 'cipher/'+value1+'.enc'
    f = open(path,'rb')
    c1 = f.read()
    f.close()
    path = 'cipher/'+value2+'.enc'
    f = open(path,'rb')
    c2 = f.read()
    f.close()


    #print(int(c1)-int(c2))
    #print(key2.n-key1.n)

    p = math.gcd(key1.n,key2.n)
    if(p!=1):
        print("FOUND: ", value1, " ", value2)     #FOUND:  551   9126
        return True

trovato=False
for i in range(19999):
    if trovato == True:
        break
    for j in range(19999):
        if i==j:
            print(i)
        elif decryptFile(i,j):
            trovato = True
            break'''

def decryptFile(value1,value2):
    value1 = str(value1)
    value2 = str(value2)
    path = 'pkeys/'+value1+'.pem'
    f = open(path,'r')
    key1 = RSA.importKey(f.read())
    f.close()
    path = 'pkeys/'+value2+'.pem'
    f = open(path,'r')
    key2 = RSA.importKey(f.read())
    f.close()

    path = 'cipher/'+value1+'.enc'
    f = open(path,'rb')
    c1 = f.read()
    f.close()
    path = 'cipher/'+value2+'.enc'
    f = open(path,'rb')
    c2 = f.read()
    f.close()

    p = math.gcd(key1.n,key2.n)
    q1 = int(key1.n//p)
    q2 = int(key2.n//p)
    f1 = (p-1)*(q1-1)
    f2 = (p-1)*(q2-1)
    d1 = pow(key1.e,-1,f1)
    d2 = pow(key2.e,-1,f2)
    k1 = RSA.construct((key1.n,key1.e,d1))
    k2 = RSA.construct((key2.n,key2.e,d2))
    k1 = PKCS1_OAEP.new(k1);
    k2 = PKCS1_OAEP.new(k2);
    m1 = k1.decrypt(c1)
    m2 = k2.decrypt(c2)
    print(m1)
    print(m2)


decryptFile(551,9126)

#FOUND:  551   9126