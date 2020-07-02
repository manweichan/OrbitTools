## Hohmann transfer equations
#Need numpy imported
#import numpy as np
def circ2elip_Hohmann(r1, r2, muPlanet = 3.986e14):
	"""
	Delta V required to go from circular orbit to elliptical
	circ2elip_Hohmann(r1, r2, muPlanet = 3.986e14)
	r1: semi major axis of circular orbit (m)
	r2: semi major axis of larger ellipse (m)
	muPlanet: Gravitation parameter (Earth default)
	"""
	v1 = np.sqrt(muPlanet/r1) * (np.sqrt(2*r2/(r1 + r2)) - 1)
	return v1

def elip2circ_Hohmann(r1, r2, muPlanet = 3.986e14):
	"""
	Delta V required to go from elliptical orbit to circular orbit
	elip2circ_Hohmann(r1, r2, muPlanet = 3.986e14)
	r1: semi major axis of circular orbit (m)
	r2: semi major axis of larger ellipse (m)
	muPlanet: Gravitation parameter (Earth default)
	"""
	v2 = np.sqrt(muPlanet/r2) * (1 - np.sqrt(2*r1/(r1 + r2)))
	return v2

def delV_Hohmann(r1, r2, muPlanet = 3.986e14):
	"""
	Delta V required to conduct a Hohmann Transfer
	delV_Hohmann(r1, r2, muPlanet = 3.986e14)
	r1: semi major axis of circular orbit (m)
	r2: semi major axis of larger ellipse (m)
	muPlanet: Gravitation parameter (Earth default)
	"""
	v1 = circ2elip_Hohmann(r1, r2)
	v2 = elip2circ_Hohmann(r1, r2)
	delV = v1 + v2
	return delV

def t_Hohmann(r1, r2, muPlanet = 3.986e14):
	"""
	Time required to conduct a Hohmann Transfer
	t_Hohmann(r1, r2, muPlanet = 3.986e14)
	r1: semi major axis of circular orbit (m)
	r2: semi major axis of larger ellipse (m)
	muPlanet: Gravitation parameter (Earth default)
	"""
	t = np.pi * np.sqrt((r1 + r2)**3 / (8 * muPlanet))
	return t