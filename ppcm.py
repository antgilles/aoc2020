
import math

def pgcd(m,n):
    while m%n:
        r=m%n
        m=n
        n=r
    return n

def ppcm(m,n):
    return m*n//pgcd(m,n)

def main():
    print(ppcm(221,19))



    #print(ppcm(1993524,4702))

if __name__ == '__main__':
    main() 