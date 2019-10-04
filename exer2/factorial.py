def fact(n):
	if n==0:
		return 1
	mul = 1
	for i in range(1,n+1):
		mul *= i
	return mul

n = int(input())
if n<0:
	print("Enter non-negative value")
else:
	print(fact(n))
