# Model Rocket Launch Simulation
This project simulates the flight of a model rocket under the influence of jet thrust, gravitational force and the force of air resistance using Python.
The project analyses the rocket's altitude, velocity and mass as functions of time and features all phases of the flight (powered ascent, unpowered ascent after the burn-out of the rocket motor, uncontrolled descent under the influence of gravity and air resistance and controlled descent with parachutes).
## Features
 Physics-based simulation
 Graph visualization using matplotlib.pyplot and FuncAnimation from matplotlib in order to animate the graphs.
 calculations were done using odeint from scipy.integrate for numerical solution of the differential equations and NumPy for other mathematical calculations and the creation of the time array.
 ## General physics and mathematics behind the rocket flight 

 # How to run
 ```bash
 pip install matplotlib numpy scipy
 rocket_launch#2_26_04-2026.py
