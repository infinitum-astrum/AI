import random as rd

n=100
money_pool=100000
s=0

overall_rating=[rd.randrange(1000,2000) for i in range(n)]

for i in range(n):
	s+=1/overall_rating[i]

need_to_pay=[money_pool*(1/(s*overall_rating[i])) for i in range(n)]

print(need_to_pay)
