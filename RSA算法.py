import random
from Crypto.Util import number
import gmpy2
from Crypto.Util.number import *
def GenKey(biten):
    p=number.getPrime(biten)
    q=number.getPrime(biten)
    n=p*q
    phi_n=(q-1)*(p-1)
    e=random.randint(0,phi_n-1)
    while(gcd(e,phi_n)!=1):
        e=random.randint(0,phi_n-1)
    [d,k,r]=Exgcd(e,phi_n)
    d=d%phi_n
    return n,e,d
def gcd(a,b):
    if a%b == 0:
        return b
    else :
        return gcd(b,a%b)
def Exgcd(r0,r1):
    s0,s1=1,0
    t0,t1=0,1
    q,r=r0//r1,r0%r1
    while(r):
        s,t=s0-q*s1,t0-q*t1
        s0,s1,t0,t1=s1,s,t1,t
        r0,r1=r1,r
        q,r=r0//r1,r0%r1
    return s1,t1,r1
def Enc(m,e,n):
    return pow(m,e,n)
def Dec(c,d,n):
    return pow(c,d,n)
if __name__=='__main__':
    [n,e,d]=GenKey(512)
    print("\nn=%d\ne=%d\nd=%d\n" % (n,e,d))
    m=input("Input m(digis): ")
    print("\n   m=%s\n" %m)
    c=Enc(bytes_to_long(m.encode("utf-8")),e,n)
    print("c=%d\n" %c)
    m_dec=Dec(c,d,n)
    print("m_dec=%d\n" %m_dec)
    print(bytes_to_long(m.encode("utf-8"))==m_dec)
