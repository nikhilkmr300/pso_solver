# Refer: https://en.wikipedia.org/wiki/Test_functions_for_optimization

import numpy as np
import matplotlib.pyplot as plt
import pso_solver

pso_solver.setSeed(1)

lower = xlower = ylower = -50
upper = xupper = yupper = 50
particleList = pso_solver.createRandomParticleList(2, numParticles=10, lower=lower, upper=upper)

# Testing on sphere function
f = lambda x, y: x**2 + y**2

pso_solver.psoVisualizeBivariate(particleList, f, xlower, xupper, ylower, yupper, c1=1, c2=1, W=0.5, numIters=30, maxFlag=False, sleepTime=0.1, density=100, accuracy=2, verbose=False)
