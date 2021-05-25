inicial=1000
x=0.05

interest_rate=1+(x/100)#Interest rate formula

amount=inicial#Down payment
for i in range(12):
 amount*=interest_rate

print(amount)