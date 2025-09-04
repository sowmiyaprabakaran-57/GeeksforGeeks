#User function Template for python3
#Back-end complete function Template for Python 3
n = int(input())

if n==0:
    print(0)
elif n==1:
    print(1)
else:
    a,b=0,1
    for i in range(2, n+1):
        a,b=b,a+b
    print(b)
