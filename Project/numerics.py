from vpython import *
import math
import matplotlib.pyplot as plt
import numpy as np

#euler method without magnus force
def euler(launchData):
	#retrieve data
	y0=launchData[0]
	yprime0=launchData[1]
	x0=launchData[2]
	xprime0=launchData[3]
	dt=launchData[4]
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
def eulerMagnus(launchData):
	#retrieve data form list [y0,v0y,x0,v0x,z0,v0z,dt,omega_i,omega_j,omega_k]
	y0=launchData[0]
	yprime0=launchData[1]
	x0=launchData[2]
	xprime0=launchData[3]
	z0=launchData[4]
	zprime0=launchData[5]
	dt=launchData[6]
	#spin values 
	omega_i=launchData[7]
	omega_j=launchData[8]
	omega_k=launchData[9]
	
	#the coefficient of square veocity term cd=0.25,p=1.225, A = pir^2 , r=42.67/1000and m= 0.045
	alpha=((0.25)*1.225*math.pi*(42.67/1000)**2)/(2*0.045)
	#the  coefficient of magnus terms S=s/m where s=.000005
	S=s=0.00005/0.045
	
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

		#z and z' updates
		z.append(z[i]+dt*zprime[i])
		zprime.append(zprime[i]+dt*(-alpha*(zprime[i])**2+S*(omega_i*yprime[i]-omega_j*xprime[i])))

		t.append(t[i]+dt)
		i=i+1

	print("With magnus")
	print("max height ",max(y))
	print("distance ",max(x))
	
	plt.plot(z,x)
	#plt.plot(t,x)
	#plt.plot(t,y)
	#plt.show()
	matrix=[x,xprime,y,yprime,z,zprime]

	return matrix
#f1 = gcurve(color=color.cyan)	# a graphics curve
#v0=70;
#v0x=v0*math.cos(math.radians(30))
#v0y=v0*math.sin(math.radians(30))
#eulerMagnus(0,v0y,0,v0x,0,0,0.01)
#euler1(0,v0y,0,v0x,0.01)

#plt.xlabel('z (m)')
#plt.ylabel('x (m)')
#plt.show()