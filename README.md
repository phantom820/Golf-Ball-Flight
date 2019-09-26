# Physics
## Simulation of the flight of a golf ball 

This is a simulation for the flight traced out by a golf ball from when it is struck to when it reaches the ground. The simulation is implemented in python 3 using the vpython module . There are two important scripts the animation.py script and the numerics.py script . The visuals and 3D objects are implemented in the animation script and the numerical methods used are in the numerics script. Currently the simulation consist of a golf ball and the playing field . The ball can be struck by clicking the shoot button in the top left part of the window it can also be paused by the same button.Differenct launch parameters such as the angle of attack , launch speed , backspin and sidespin can be changed through the interactive sliders in the window.Currently the numerics script solves a system of differential equations using the euler method , the system of differential equations arisesfrom applying Newton's second law to the ball ( incorporates air resistance and drag ).

## Requirements
-python3
-vpython module

To install vpython if not present on linux run the following
pip3 install vpython

After installation just run the animation script and a tab should open in your browser



