
def sum(N):
	if N == 1:
		return 1
	else:
		return N+sum(N-1)

print sum(input("Enter value of N:"))
