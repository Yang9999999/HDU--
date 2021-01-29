import random
count=1
def Euclidean(A,B):
	if A % B ==0:
		return B
	global count 
	count += 1
	r = A % B
	return Euclidean(B,r)

times=0
flag=0
for i in range(10):
	A = random.randint(0,2**1024-1)
	print("A = %d" %A)
	B = random.randint(0,2**1024-1)
	print("B = %d" %B)
	print("gcd(A,B) = %d" %Euclidean(A,B))
	print("count = %d" %count)
	if Euclidean(A,B) == 1:
		flag+=1
	times+=1
	print(times)
print("概率是:"+str(float(flag)/float(times)))
	

	