##Atmospheric Density

# http://www.sws.bom.gov.au/Category/Educational/Space%20Weather/Space%20Weather%20Effects/SatelliteOrbitalDecayCalculations.pdf
import numpy as np

def atmDensity_below500km(f10, Ap, alt_meters):
	"""
	Calculates atmospheric density
	Useful for satellites below 500 km
	From http://www.sws.bom.gov.au/Category/Educational/Space%20Weather/Space%20Weather%20Effects/SatelliteOrbitalDecayCalculations.pdf
	Inputs (f10, Ap, alt_meters)
	f10: Solar radio flux index (https://www.swpc.noaa.gov/phenomena/f107-cm-radio-emissions)
	Ap: Geomagnetic A index (https://www.spaceweatherlive.com/en/help/the-ap-index. 0-400 according to Aussie paper sws.bom.gov)
	alt_meters: altitude in meters
	"""
	alt = alt_meters * 1e-3 #Convert to km
	SH = (900 + 2.5 * (f10 - 70) + 1.5 * Ap) / (27 - .012 * (alt - 200))
	density = 6e-10 * np.exp(-(alt - 175)/SH)
	return density