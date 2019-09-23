from vpython import *
import math
import matplotlib.pyplot as plt

#euler method
def euler(y0,yprime0,x0,xprime0,dt):

	#the coefficient of square veocity term cd=0.25,p=1.225, A = pir^2 , r=42.67/1000and m= 0.045
	alpha=((0.25)*1.225*math.pi*(42.67/1000)**2)/(2*0.045)
	y=[y0]
	x=[x0]
	yprime=[yprime0]
	xprime=[xprime0]
	t=[0]
	i=0;
	time=0

	while y[i]>=0:
		#x position and x velocity update
		x.append(x[i]+dt*xprime[i])
		xprime.append(xprime[i]-dt*alpha*(xprime[i])**2)

		#y position and y velocity update
		y.append(y[i]+dt*yprime[i])
		yprime.append(yprime[i]+dt*(-9.8-alpha*(y[i])**2)) 
		t.append(t[i]+dt)
	
		i=i+1

	plt.plot(x,y)
	plt.show()
	return (y,yprime)

#f1 = gcurve(color=color.cyan)	# a graphics curve
v0=60;
v0x=v0*math.cos(math.radians(30))
v0y=v0*math.sin(math.radians(30))
euler(0,v0y,0,v0x,0.01)
