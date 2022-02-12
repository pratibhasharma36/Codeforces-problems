t=int(input())
for i in range(t):
	a,b,p,q=list(map(int,input().split()))
	sum=a+b
	count=p+q
	if a==b==p==q:
		print(0)
	elif sum%2==0 and count%2==0 or sum%2!=0 and count%2!=0:
		print("2")
	else:
		print(1)