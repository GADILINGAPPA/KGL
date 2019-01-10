def mat_multiply(a,b):
	f={}
	for i in range(0,m1,1):
		for j in range(0,n2,1):
			f[i,j]=0
	for i in range(0,m1,1):
		for j in range(0,n2,1):
			for k in range(0,n1,1):
				f[i,j]=f[i,j]+(a[i,k]*b[k,j])
	return f
a={}
b={}
print ("Note:The columns of first matrix should match the rows of second matrix")
m1=input("Enter the rows of the matrix A:")
n1=input("Enter the columns of the matrix A:")
print ("Enter the elements of the matrix A:")
for i in range(0,m1,1):
	for j in range(0,n1,1):
		a[i,j]=input("")
m2=input("Enter the rows of the matrix B:")
n2=input("Enter the columns of the matrix B:")
if (n1==m2):
	print ("Enter the elements of the matrix B:")
	for i in range(0,m2,1):
		for j in range(0,n2,1):
			b[i,j]=input("")
	c=mat_multiply(a,b)
	print (c)
else:
	print ("Invalid attempt")

