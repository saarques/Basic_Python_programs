#Operations are performed on the original list, check out why it is not performing operations on a local copy.
a=[3,4,6,9,1,0]
def bdha_yr(a):
	for i in range(0,len(a)):
		a[i]=a[i]+1
	print "Bdha hua a: ",a
def ghta_yr(a):
	for i in range(len(a)):
		a[i]=a[i]-1
	print "ghta hua a: ",a
bdha_yr(a)
ghta_yr(a)
print "Achaa to ye original maal h: ",a