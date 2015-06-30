
print
print "Enter the Real & Imaginary Part of Divident \n\tSeperated with commas"
(a,b)=input()
print "Enter the Real & Imaginary Part of Divisor \n\tSeperated with commas"
(c,d)=input()
print "Divident Is:\t %d%+di"%(a,b)
print "Divisor Is :\t %d%+di"%(c,d)
if (a,b)==(c,d):
	print "Equal"
else :
	n=(a*c+b*d)
	m=(a*d+b*c)
	p=(c*c+d*d)
	r=float(n)/float(p)
	i=float(m)/float(p)
	print "Quotient is \t ",r,i,"i"
	print "Quotient Is\t %.2f%+.2fi "%(r,i)
print
