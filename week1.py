import math

#GCD naive 1

def gcd1(m,n):

    fm=[]
    for i in range(1,m+1):
        if m%i==0:
            fm.append(i)

    fn=[]
    for i in range(1,n+1):
        if n%i==0:
            fn.append(i) 

    c=[]
    for i in fm:
        if i in fn:
            c.append(i)   

    print(c[-1])     



def gcd2(m,n):

    cf=[]
    for i in range(1,min(m,n)+1):
        if(m%i==0 and n%i==0)      :
            cf.append(i)  

    print(cf[-1])


def gcd3(m,n):

    for i in range(min(m,n)+1,0,-1):

        if( m%i==0 and n%i==0):
            print(i)
            return
        
def gcd4(m,n):

    i=min(m,n)
    while i>0:
        if(m%i==0 and n%i==0):
            print(i)
            return
        else:
            i-=1        
    

#gcd naive-2

def gcd5(m,n):
    #assume m>=n

    if(n>m):
        m,n=n,m

    if(m%n==0):
        print(n)
        return 

    diff=m-n
    gcd5(m,diff)


def gcd6(m,n):
    if(n>m) :
        m,n=n,m

    while(m%n!=0):

        diff=m-n
        m,n=max(diff,n),min(diff,n)

    print(n)
    return

    
#euclid

def gcd7(m,n)    :

    if(n>m):
        n,m=m,n

    if(m%n==0)    :
        print(n)
        return 
    
    gcd7(n,m%n)


def gcd8(m,n):
    if(n>m) :
        m,n=n,m

    while(m%n!=0):
        m,n=n,m%n

    print(n)
    return   



gcd=math.gcd(18,24)
lcm=abs(18 * 24)//gcd

print(lcm)



gcd1(18,24)
gcd2(18,24)
gcd3(12,25)
gcd4(18,24)
gcd5(18,24)
gcd6(18,24)
gcd7(18,24)
gcd8(18,24)



