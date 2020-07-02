## Eclipse tools

def worstCaseEclipse(alt, rPlanet = 6378.1e3, muPlanet = 3.986e14):
	"""alt unit is in meters"""
	rOrbit = alt + rPlanet #Radius of orbit (m)
	alph = np.arccos(rPlanet/rOrbit) #Outer central angle
	beta = np.pi - 2*alph #Central angle of eclipsed orbit

	fracOrbitEcl = beta/(2*np.pi) #Fraction of orbit in eclipse
	period = 2*np.pi*np.sqrt(rOrbit**3/muPlanet)
	timeInEclipse = period * fracOrbitEcl #If period is input, get time in eclipse


	print("Central Angle of Eclipsed Orbit : ", beta*180/np.pi, "deg")
	print("Fraction of Orbit in Eclipse    : ", fracOrbitEcl)
	print("Period                          :  {:.0f} s, {:.1f} min, {:.1f} hrs".format(period,period/60,period/60/60))
	print("Time in Eclipse                 :  {:.0f} s, {:.1f} min, {:.1f} hrs".format(timeInEclipse,timeInEclipse/60,timeInEclipse/60/60))