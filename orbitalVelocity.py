## Orbital velocity 
## Needs numpy imported
# import numpy as np
# import scipy as sp

def circVel_fromAlt(alt, rPlanet = 6378.1e3, muPlanet = 3.986e14):
	"""
	Inputs (altitude, radius of planet-Earth is default, Gravitation parameter of planet-Earth is default)
	alt unit is in meters
	"""
	r = alt + rPlanet
	v = np.sqrt(muPlanet/r)
	return v

def circVel_fromRad(r, muPlanet = 3.986e14):
	"""
	Inputs (orbit radius, Gravitation parameter of planet-Earth is default)
	alt unit is in meters
	"""
	v = np.sqrt(muPlanet/r)
	return v