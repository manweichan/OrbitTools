## Orbital period
# Needs numpy import
# import numpy as np
def orbitalPeriod_fromAlt(alt, rPlanet = 6378.1e3, muPlanet = 3.986e14):
	"""
	Get orbital period from altitude input
	Outputs orbital Period in seconds
	inputs (alt, rPlanet = 6378.1e3, muPlanet = 3.986e14)
	alt: altitude in meters
	rPlanet: radius of planet. Earth is default no input needed unless it's another body
	muPlanet: gravitation parameter of planet. Earth is default no input needed unless it's another body
	"""
	r = rPlanet + alt
	t = 2*np.pi*np.sqrt(r**3/muPlanet)
	return t

def orbitalPeriod_fromRad(r, muPlanet = 3.986e14):
	"""
	Get orbital period from radius of orbit input
	Outputs orbital Period in seconds
	inputs (r, muPlanet = 3.986e14)
	alt: altitude in meters
	muPlanet: gravitation parameter of planet. Earth is default no input needed unless it's another body
	"""
	t = 2*np.pi*np.sqrt(r**3/muPlanet)
	return t