def bubblesort(a):
	for i in range(len(a)):
		for j in range(len(a)-i-1):
			if a[j] > a[j+1]:
				a[j],a[j+1] = a[j+1],a[j]
	return a
				

l = [4,2,7,1,3]
print(bubblesort(l))