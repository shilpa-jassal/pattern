n=3
for i in range(1,n+1):
	for j in range(1,5):
		if(j>=n-i+1 and j<=i+2):
			print("*" , end = "")
		else:
			print(" " , end = "")
	print()
