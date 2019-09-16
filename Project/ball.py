from vpython import *

#create the ball and ground

ball=sphere(pos=vector(0,0.1, 0), radius=0.1, color=color.red)
floor=box(pos=vector(0,0,0), size=vector(1,0.05,1),
color=color.green)

#set up initial conditions
ball.velocity=vector(0,5,0)
ball.mass=0.25
ball.p=ball.velocity*ball.mass
g=vector(0,-9.8,0)
Fnet=g*ball.mass
dt = 0.001
t = 0

while t<4:
	rate(300)
	ball.pos=ball.pos + (ball.p/ball.mass)*dt
	ball.p = ball.p +Fnet*dt
	t = t + dt
	
	if ball.pos.y < (floor.pos.y + ball.radius):
		ball.p = -ball.p
