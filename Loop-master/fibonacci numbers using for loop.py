#Fibonacci numbers-used in the analysis of financial markets.
#the first two fibonacci number are 0 and 1 , and each subsequent number is the sum of the previous two.
#calculate the N first fibonacci numbers.
N = 10
fib1 = 0
fib2 = 1
print(fib1)
print(fib2)
for k in range(N-2):
    fib_nxt=fib2 + fib1
    fib1 = fib2
    fib2=fib_nxt
    print(fib_nxt)

#alternative solution
fib = [0, 1]
for k in range (N-2):
    fib_nxt=fib[k+1]+fib[k]
    fib.append(fib_nxt)