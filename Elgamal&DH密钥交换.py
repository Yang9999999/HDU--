import random
import libnum
import string
import gmpy2
from Crypto.Util import number

def fastPowMod(b,n,m):
    b = b % m
    a = 1
    while n!=0:
        if n&1:
            a = (a*b)%m
        n>>=1
        b = (b*b)%m
    return a

def GenPara(bitlen):
    q = number.getPrime(bitlen-1)
    while(not number.isPrime(2*q+1)):
        q = number.getPrime(bitlen-1)
    p = 2*q+1
    g = random.randint(0,p-1)
    while(fastPowMod(g,2,p) == 1 or fastPowMod(g,q,p) == 1):
        g = random.randint(0,p-1)
    return p,q,g

def GenKey(p,g):
    x = random.randint(0,p-1)
    y = fastPowMod(g,x,p)
    return x,y

def Enc(m,p,g,y):
    k = random.randint(1,p-2)
    while (not libnum.gcd(k,p-1) == 1):
        k = random.randint(0,p-1)
    u = fastPowMod(g,k,p)
    v = pow(m*fastPowMod(y,k,p),1,p) 
    c = str(u)+","+str(v)
    return c

def Dec(c,p,x):
    i = c.rfind(',',0,len(c))
    u = int(c[:i])
    v = int(c[i+1:])
    m = fastPowMod(v*fastPowMod(u,p-1-x,p),1,p)
    return m

def Round1(x1,p,g):
    y1 = fastPowMod(g,x1,p)
    return y1

def Round2(x2,p,g):
    y2 = fastPowMod(g,x2,p)
    return y2

def FinalRound(x1,y1,x2,y2,p):
    z1 = fastPowMod(y2,x1,p)
    z2 = fastPowMod(y1,x2,p)
    return z1,z2

if __name__ == '__main__':
    [p,q,g] = GenPara(512)
    print("p = %d\ng = %d"%(p,g))
    print("\nElgamal: ")
    [x,y] = GenKey(p,g)
    print("\nx = %d\ny = %d"%(x,y))
    m = random.randint(0,p-1)
    print("\nm =%d"%m)
    c = Enc(m,p,g,y)
    print("\nc = %s"%c)
    m_dec = Dec(c,p,x)
    print("\nm_dec = %d"%m_dec)
    print(m == m_dec)

    print("\nDH key exchange: ")
    x1 = random.randint(0,p-1)
    print("\nAlice chooses x1 = %d"%x1)
    y1 = Round1(x1,p,g)
    print("\nAlice sends %d to Bob"%y1)
    x2 = random.randint(0,p-1)
    print("\nBob chooses x2 = %d"%x2)
    y2 = Round2(x2,p,g)
    print("\nBob sends %d to Alice"%y2)
    print("\nAlice and Bob agree with the same key: ")
    [z1,z2] = FinalRound(x1,y1,x2,y2,p)
    print("%d\n%d"%(z1,z2))
    print(z1 == z2)