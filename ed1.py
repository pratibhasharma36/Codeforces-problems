t=int(input())
for i in range(t):
	n=int(input())
	ans=0
	if n%7==0:
		print(n)
	elif n<7:
		print(7)
	else:
		for j in range(n-7,n+7):
			if j%7==0:
				ans=j
				break
		print(ans)