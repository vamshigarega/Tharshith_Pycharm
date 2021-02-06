def fib(n):
  if(n==0):
    return 0
  if(n==1 or n==2):
    return 1
  retrun fib(n-1)+fib(n-2)


a=int(input())
for i in range(a):
  print(fib(i))
