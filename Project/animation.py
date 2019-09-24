from vpython import *
import math
import random
import numerics

#make the pause or start menu
#animation starts out paused and declare global variables
running=False
stop=False
ball=None
#the trail component
trail=None

#contols pausing
def run():
	global running
	global stop
	if(not running):
		running=True
		stop=False
	else:
		running=False
		
#reset animation to default after changing speed or any reset event
def reset(ball):
	global running
	global stop
	running=False
	stop=True
	ball.pos=vector(0,0.2,0)
	#reset camera pos

	
#setting the launch speed resets things to default
def launchSpeed(s):
	wtv.text='{:1.2f}'.format(s.value)
	global ball
	reset(ball)

#set the launch angle if changed reset to default
def launchAngle(s):
	wta.text='{:1.2f}'.format(s.value)
	global ball
	reset(ball)

#vary the backspin:
def backSpin(s):
	wtb.text='{:1.2f}'.format(s.value)
	global ball
	reset(ball)
#vary the sidespin
def sideSpin(s):
	wts.text='{:1.2f}'.format(s.value)
	global ball
	reset(ball)
#make the ball bounce up and down with some slider velocity
def bounce(ball,v):
	global stop
	ball.velocity=vector(0,v,0)
	ball.mass=0.25
	ball.p=ball.velocity*ball.mass
	g=vector(0,-9.8,0)
	Fnet=g*ball.mass
	dt=0.001
	t=0
	
	while True:
		if running:
			rate(100)
			ball.pos=ball.pos + (ball.p/ball.mass)*dt
			ball.p = ball.p +Fnet*dt
			t = t + dt
			if ball.pos.y < (floor.pos.y + ball.radius):
				ball.p = -ball.p
	
		elif stop:
			break
			
#simulate projectile motion without air resistance basic one
def simpleProjectile(ball,v):
	global running
	global trail
	#say the angle is 30 degrees
	vx=v*math.cos(math.radians(45))
	vy=v*math.sin(math.radians(45))
	ball.mass=0.25

	g=vector(0,-9.8,0)
	ball.v=vector(vx,vy,0)
	dt=0.001
	t=0	
	Fnet=g*ball.mass

	while ball.pos.y>=0.1:
		if running:
			rate(350)
			ball.v=ball.v+(Fnet/ball.mass)*dt
			ball.pos=ball.pos+ball.v*dt/ball.mass
			t=t+dt
		
		elif stop:
			trail.clear()	
			break

	print(ball.pos)
	
#only drag incorporated
def simpleNumericalProjectile(ball):
	global running
	global trail
	#launch parameters from sliders
	v=vsl.value;
	angle=asl.value
	backspin=bsl.value;
	#say the angle is 45 degrees
	v0x=v*math.cos(math.radians(angle))
	v0y=v*math.sin(math.radians(angle))

	#use euler method for x,x',y,y' and z,z'
	#pass all data to euler method as a list [y0,v0y,x0,v0x,z0,v0z,dt,omega_i,omega_j,omega_k]
	launchData=[0.2,v0y,0,v0x,0.01]
	matrix=numerics.euler(launchData)
	x=matrix[0]
	xprime=matrix[1]
	y=matrix[2]
	yprime=matrix[3]

	t=0
	dt=0.01
	i=0
	while y[i]>=0.2:
		if(running):
			rate(60)
			ball.v=vector(xprime[i],yprime[i],0)
			ball.pos=vector(x[i],y[i],0)
			i=i+1
			t=t+dt
			
		elif stop:	
			break
	print(ball.pos)	

#back spin incorporated
def simpleNumericalProjectile2(ball):
	global running
	global trail
	#launch parameters from sliders
	v=vsl.value;
	angle=asl.value
	backspin=bsl.value;
	sidespin=ssl.value
	#velocities from launch angle
	v0x=v*math.cos(math.radians(angle))
	v0y=v*math.sin(math.radians(angle))

	#use euler method for x,x',y,y' and z,z'
	#pass all data to euler method as a list [y0,v0y,x0,v0x,z0,v0z,dt,omega_i,omega_j,omega_k]
	launchData=[0.2,v0y,0,v0x,0,0,0.01,sidespin,0,backspin]
	matrix=numerics.eulerMagnus(launchData)
	x=matrix[0]
	xprime=matrix[1]
	y=matrix[2]
	yprime=matrix[3]

	z=matrix[4]
	zprime=matrix[5]

	t=0
	dt=0.01
	i=0
	while y[i]>=0.2:
		if(running):
			rate(60)
			#update the distance as flight progresses
			distanceData.text="Distance covered : "+str(round(ball.pos.x,3))+" m"
			#update the y value for the height till max height
			if(y[i]>ball.pos.y):
				maxheightData.text="Maximum Height : "+str(round(ball.pos.y,3))+" m"
			#height update
			heightData.text="Current Height : "+str(round(ball.pos.y,3))+" m"

			#time 
			timeData.text="Time of Flight : "+str(round(t,3))+" s"

			#velocity data
			velocityData.text="Speed : "+str(round(math.sqrt(xprime[i]**2+yprime[i]**2+zprime[i]**2),3))+" ms<sup>-1</sup>"

			ball.v=vector(xprime[i],yprime[i],0)
			ball.pos=vector(x[i],y[i],z[i])
			i=i+1
			t=t+dt
			
		elif stop:
			#trail.clear()	
			break
	print(ball.pos)	

#scene.append_to_caption('\n\n')	
#set the title
scene.title="<b>Flight of a golf ball simulation\n</b>\n"

#make the scene dimensions and properties of the camera
scene.center=vector(5,0,0)
scene.width=1200
scene.height=600
scene.autoscale=False
scene.camera.pos=vector(5,7,-2)
scene.camera.rotate(-math.pi/1.8,vector(0,1.3,0),vector(0,0,0))
scene.background=color.black

#lighting conditions
distant_light(direction=vector(60,-4,0), color=color.gray(0.3))


#make the pause button to control animation
button(text="<b>Shoot / Pause </b>",pos=scene.title_anchor,bind=run) 

#create ground and ball
ball=sphere(pos=vector(0,0.2,0 ), radius=0.2, color=color.white,emissive=False)
floor=box(pos=vector(105,0,0), size=vector(240,0.05,40),
color=color.green,emissive=False)

#side ground 
floor2=box(pos=vector(105,0,40), size=vector(240,0.05,40),
color=vector( 82.7/100, 78/100, 63.5/100),emissive=False)
floor3=box(pos=vector(105,0,-40), size=vector(240,0.05,40),
color=vector( 82.7/100, 78/100, 63.5/100),emissive=False)
#create initial velocity and angular launch angle slider
scene.caption="\n\t Launch speed"

vsl=slider(min=50.0,max=70,value=60,length=200,bind=launchSpeed,right=15)
wtv=wtext(text='{:1.2f}'.format(vsl.value))
#velocity slider text
scene.append_to_caption(" metres/s \n")

scene.append_to_caption("\n\n\t Angle of attack")
asl=slider(min=15.0,max=45,value=30,length=200,bind=launchAngle,right=15)
wta=wtext(text='{:1.2f}'.format(asl.value))
#angle slider text
scene.append_to_caption(" degrees \n")

scene.append_to_caption("\n\n\t Backspin ωk")
#the backspin slider
bsl=slider(min=0.0,max=200,value=0,length=220,bind=backSpin,right=15)
wtb=wtext(text='{:1.2f}'.format(bsl.value))
#backspin slider text

scene.append_to_caption(" radians/s ")

#sidespin slider
scene.append_to_caption("\n\n\t Sidespin ωi")
ssl=slider(min=-70.0,max=70,value=0,length=150,bind=sideSpin,right=15)
wts=wtext(text='{:1.2f}'.format(ssl.value))

#sidespin text
scene.append_to_caption(" radians/s ")

#set the trail that follows
trail=attach_trail(ball,emissive=True)
trail.interval=20
trail.color=color.cyan

#data as the ball flies
flightData =label( pos=vec(0,12,-5), text='<b>Flight data</b>',height=20,box=False) 
distanceData =label( pos=vec(0,11,-5), text='Distance covered :',color=color.cyan,box=False)
velocityData =label( pos=vec(0,10,-5), text='Velocity :',color=color.cyan,box=False)
heightData =label( pos=vec(0,9,-5), text='Current Height :',color=color.cyan,box=False)
maxheightData =label( pos=vec(0,8,-5), text='Maximum Height :',color=color.cyan,box=False)
timeData =label( pos=vec(0,7,-5), text='Time of Flight :',color=color.cyan,box=False)
#main animation loop
while True:
	if running:
		simpleNumericalProjectile2(ball)
		sleep(1)
		reset(ball)	
		trail.clear()
		


