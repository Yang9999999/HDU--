count=1
def exgcd(a, b):     
    if b == 0:         
        return 1, 0, a     
    else:         
        x, y, q = exgcd(b, a % b)        
        x, y = y, (x - (a // b) * y)         
        return x, y, q
if __name__ == '__main__':
    print(exgcd(2020,1976))