## Delta V changes

#Inlination change
import numpy as np
def delV_circInc(v, i):
	"""
	Calculates deltaV required for a circular orbit inclination change
	Inputs:
	v: Orbital velocity
	i: Inclination change

	Outputs:
	delV: deltaV required to make maneuver with same units as input 'v'
	"""
	delV = 2 * v * np.sin(i/2.)
	return delV
