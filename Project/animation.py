from vpython import *

#make the pause or start menu

#animation starts out pause
running=False

def Run():
	global running
	if(not running):
		running=True
	
	else:
		running=False

#setting the launch speed
def launchSpeed(s):
	wt.text='{:1.2f}'.format(s.value)


	#make the ball bounce up and down with some slider velocity
def bounce(ball,v):
	ball.velocity=vector(0,v,0)
	ball.mass=0.25
	
	ball.p=ball.velocity*ball.mass
	g=vector(0,-9.8,0)
	Fnet=g*ball.mass
	dt=0.001
	t=0
	
	while running:
		rate(300)
		ball.pos=ball.pos + (ball.p/ball.mass)*dt
		ball.p = ball.p +Fnet*dt
		t = t + dt
		if ball.pos.y < (floor.pos.y + ball.radius):
			ball.p = -ball.p

#set the title
scene.title="Projectiles\n"
	
#make the scene dimensions
'''for now default are fine '''

#make the pause button to control animation

button(text="Pause",pos=scene.title_anchor,bind=Run) 

#create ground and ball
ball=sphere(pos=vector(0,0.1, 0), radius=0.1, color=color.white)
floor=box(pos=vector(0,0,0), size=vector(1,0.05,1),
color=color.green)

#create initial velocity and angular launch angle slider

scene.caption="\nVary the launch speed\n\n"

vsl=slider(min=0.3,max=3,value=1.5,length=220,bind=launchSpeed,right=15)
wt=wtext(text='{:1.2f}'.format(vsl.value))

scene.append_to_caption(" metres/s \n")

scene.camera.follow(ball)

while True:
	print(running)
	bounce(ball,4)

