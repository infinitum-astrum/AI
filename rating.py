import random as rd

n=100
previous_rating=[rd.randrange(1000,2000) for i in range(n)]
authentification=[rd.randint(0,1) for i in range(n)]
hours=[rd.uniform(0,8) for i in range(n)]
usage_of_social_media=[rd.uniform(0,1) for i in range(n)]
code_quantity=[rd.randint(100,2000) for i in range(n)]
if_test=True
test_results=[rd.randint(0,100) for i in range(n)]
coefficients=[1,-5,4,20]

if if_test:
	ift=0

scores=[(authentification[i]*
		(coefficients[0]*hours[i]-
		coefficients[1]*usage_of_social_media[i]+
		coefficients[2]*code_quantity[i]+
		coefficients[3]*ift*test_results[i]))
			for i in range(n)]

sorted_scores=[[scores[i],i] for i in range(n)]
sorted_scores.sort()

expected=[float(0.0) for i in range(n)]

for i in range(1,n):
	for j in range(i):
		expected[j]+=(1.0/(1+10**((previous_rating[i]-previous_rating[j])/400)))/(n*(n-1)/2)
		expected[i]+=(1.0/(1+10**((previous_rating[j]-previous_rating[i])/400)))/(n*(n-1)/2)

S=[float(0.0) for i in range(n)]

for i in range(n):
	S[sorted_scores[i][1]]=2*(n-(i+1))/(n*(n-1))

new_rating=[(previous_rating[i]+32*(n-1)*(S[i]-expected[i])) for i in range(n)]

print(previous_rating)

print(new_rating)