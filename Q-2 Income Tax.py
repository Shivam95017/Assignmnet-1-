a=float(input('Gross Income=$'))
b=int(input('Number of Dependents='))
print('Taxable Income=$', str(a-10000.0-(float(3000*b))))
print('Tax=$', str(a-10000.0-(float(3000*b)*0.2)))
