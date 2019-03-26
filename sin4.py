#simple quant shit
import random
import time

#shareprice
x = 50

#placeholders
p = 0
s = 0
o = 0

#balance
y = 450

#currently holding share?
w = 0

for a in range(20):

	z = random.randint(-15,16)
	o = x
	x = x + z

	#buy paramater
	if (x - o) > (.1*o):
		u = 1
	else: u = 0

	#sell parameter
	if x > (1.1*p):
		v = 1
	else: v = 0

	#BUY
	if w == 0 and u == 1:
		y = y - x
		w = 1
		#hold buy price
		p = x
		print ('---------------')
		print (y)
		print ('---------------')
	
	#SELL
	elif w == 1 and v == 1:
		y = y + x
		w = 0
		#hold sell price
		s = x
		print ('///////////////')
		print (y)
		print ('///////////////')

	print (x)
	time.sleep(1)
