from vpython import *
import math
import random

#numerical methods

#the euler method t
def euler(y0,yprime0,dt):
	y=[y0]
	yprime=[yprime0]
	t=[0]
	i=0;
	while y[i]>=0:
		y.append(y[i]+dt*yprime[i])
		yprime.append(yprime[i]-9.8*dt) 
		t.append(t[i]+dt)
		i=i+1

	return (y,yprime)
	
#make the pause or start menu
#animation starts out pause and declare global variables
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
	ball.pos=vector(-60,0.1,0)
	
#setting the launch speed resets things to default
def launchSpeed(s):
	wt.text='{:1.2f}'.format(s.value)
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
	vx=v*math.cos(math.radians(30))
	vy=v*math.cos(math.radians(30))
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
	
def simpleNumericalProjectile(ball,v):
	global running
	global trail
	#say the angle is 30 degrees
	vx=v*math.cos(math.radians(30))
	vy=v*math.cos(math.radians(30))
	ball.mass=0.25
	
	#use euler method for y position
	data=euler(0.1,vy,0.001)
	y=data[0]
	yprime=data[1]
	i=0
	t=0
	dt=0.001
	while ball.pos.y>=0.1:
		if(running):
			rate(350)
			ball.v=vector(vx,yprime[i],0)
			ball.pos=vector(vx*dt+ball.pos.x,y[i],0)
			i=i+1
			t=t+dt
			
		elif stop:
			#trail.clear()	
			break
	print(ball.pos)		
#set the title
scene.title="Projectiles\n"
	
#make the scene dimensions and properties of the cameraa
scene.width=1200
scene.height=800
scene.autoscale=False
scene.camera.pos=vector(0,3,50)
scene.camera.rotate(-math.pi/2.02,vector(0,1.3,0),vector(0,0,0))
scene.background=color.white


#make the pause button to control animation

button(text="Pause",pos=scene.title_anchor,bind=run) 

#create ground and ball
ball=sphere(pos=vector(-60,0.1,0 ), radius=0.1, color=color.white)
floor=box(pos=vector(5,0,0), size=vector(160,0.05,5),
color=color.green)


#create initial velocity and angular launch angle slider

scene.caption="\nVary the launch speed\n\n"

vsl=slider(min=10.0,max=60,value=15,length=220,bind=launchSpeed,right=15)
wt=wtext(text='{:1.2f}'.format(vsl.value))

scene.append_to_caption(" metres/s \n")


#set the trail that follows
trail=attach_trail(ball)
trail.interval=20
trail.color=color.cyan

#main animation loop
while True:
	
	if running:
		simpleNumericalProjectile(ball,vsl.value/1.4)	
		reset(ball)	
		trail.clear()


