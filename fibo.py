print "Please enter n:"
nterms = int(raw_input())

def Fibo(n):
    if n<=1 :
        return n
    return Fibo(n-1) + Fibo (n-2)

if nterms <= 1:
    print n
else:
    for i in range(nterms):
        print Fibo(i)
