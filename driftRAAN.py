##Rate of ascending node precession change
##Needs numpy imported
# import numpy as np

def precRate_RAAN(a, e, w, i, J2 = 1.08262668e-3, rPlanet = 6378.1e3):
	"""
	https://en.wikipedia.org/wiki/Nodal_precession
	Calculates right ascension nodal precession rate of a satellite around a body
	inputs(a, e, w, i, J2 = 1.08262668e-3, rPlanet = 6378.1e3)
	a: semi major axis (meters)
	e: eccentricity
	w: Mean motion/angular velocity of satellite motion (2 pi / T) where T is satellite period. 
	i: inclination (radians)
	J2: second dynamic form factor of body
	rPlanet: body's equitorial radius

	Ouputs:
	wp: precession rate 
	Note For a satellite in a prograde orbit, precession is westward, i.e. node and satellite
	move in opposite directions

	"""
	wp = ( (-3/2) * rPlanet**2 * J2 * w * np.cos(i) ) / (a * (1 - e**2))**2
	return wp

def delPrecRate_RAAN(a, e, w, i, J2 = 1.08262668e-3, rPlanet = 6378.1e3):
	"""
	Calculates differential right ascension nodal precession rate of a satellite around a body
	with respect to a change in inclination
	inputs(a, e, w, i, J2 = 1.08262668e-3, rPlanet = 6378.1e3)
	a: semi major axis (meters)
	e: eccentricity
	w: Mean motion/angular velocity of satellite motion (2 pi / T) where T is satellite period. 
	J2: second dynamic form factor of body
	rPlanet: body's equitorial radius

	Ouputs:
	wp: precession rate 
	Note For a satellite in a prograde orbit, precession is westward, i.e. node and satellite
	move in opposite directions

	"""
	delWP = ( (-3/2) * rPlanet**2 * J2 * w * np.sin(i) ) / (a * (1 - e**2))**2
	return delWP

def delPrecRateDelA_Raan(a, e, w, i, J2 = 1.08262668e-3, rPlanet = 6378.1e3):
	"""
	Calculates differential right ascension nodal precession rate of a satellite around a body
	with respect to a change in semi major axis
	inputs(a, e, w, i, J2 = 1.08262668e-3, rPlanet = 6378.1e3)
	a: semi major axis (meters)
	e: eccentricity
	w: Mean motion/angular velocity of satellite motion (2 pi / T) where T is satellite period. 
	J2: second dynamic form factor of body
	rPlanet: body's equitorial radius

	Ouputs:
	wp: precession rate
	"""
	delWP_a = (3 * rPlanet ** 2 * J2 * w * np.cos(i)) / (a**3 * (1-e**2)**2)
	return delWP_a