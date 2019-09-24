from vpython import *
import math
import matplotlib.pyplot as plt
import numpy as np

#euler method without magnus force
def euler1(y0,yprime0,x0,xprime0,dt):

	#the coefficient of square veocity term cd=0.25,p=1.225, A = pir^2 , r=42.67/1000and m= 0.045
	alpha=((0.25)*1.225*math.pi*(42.67/1000)**2)/(2*0.045)
	#lists for values
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

		#y position and y' velocity update
		y.append(y[i]+dt*yprime[i])
		yprime.append(yprime[i]+dt*(-9.8-alpha*(yprime[i])**2)) 
		t.append(t[i]+dt)
	
		i=i+1
	print("Without magnus")
	print("max height ",max(y))
	print("distance ",max(x))
	plt.plot(x,y)
	#plt.plot(t,x)
	#plt.plot(t,y)
	#plt.show()
	#returns a matrix that has first row as x ,second row x'.third y , fourth y'
	matrix=[x,xprime,y,yprime]

	return matrix

#euler method with magnus force
def euler2(y0,yprime0,x0,xprime0,z0,zprime0,dt):
	#the coefficient of square veocity term cd=0.25,p=1.225, A = pir^2 , r=42.67/1000and m= 0.045
	alpha=((0.25)*1.225*math.pi*(42.67/1000)**2)/(2*0.045)
	#the  coefficient of magnus terms S=s/m where s=.000005
	S=s=0.00005/0.045
	#spin values 
	omega_i=0
	omega_j=0
	omega_k=150

	y=[y0]
	yprime=[yprime0]
	x=[x0]
	xprime=[xprime0]

	z=[z0]
	zprime=[zprime0]

	t=[0]
	i=0;
	time=0

	while y[i]>=0:
		#y and y' update
		y.append(y[i]+dt*yprime[i]) 
		yprime.append(yprime[i]+dt*(-9.8-alpha*(yprime[i])**2+S*(omega_k*xprime[i]-omega_i*zprime[i])))

		#x and x' update
		x.append(x[i]+dt*xprime[i])
		xprime.append(xprime[i]+dt*(-alpha*(xprime[i])**2+S*(omega_j*zprime[i]-omega_k*yprime[i])))

		zprime.append(0)

		t.append(t[i]+dt)
		i=i+1

	print("With magnus")
	print("max height ",max(y))
	print("distance ",max(x))
	
	plt.plot(x,y)
	#plt.plot(t,x)
	#plt.plot(t,y)
	#plt.show()
	matrix=[x,xprime,y,yprime]

	return matrix
#f1 = gcurve(color=color.cyan)	# a graphics curve
v0=70;
v0x=v0*math.cos(math.radians(30))
v0y=v0*math.sin(math.radians(30))
euler2(0,v0y,0,v0x,0,0,0.01)
euler1(0,v0y,0,v0x,0.01)

plt.xlabel('distance (m)')
plt.ylabel('height (m)')
plt.show()