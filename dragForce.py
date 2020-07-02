## Drag Force

def dragForce(cd, rho, a, v):
	"""
	Calculates drag force
	Inputs (cd, rho, a, v)
	cd:  Coefficient of drag
	rho: Density of fluid
	a:   Cross sectional area
	v:   Speed of object relative to fluid
	"""
	dForce = cd * a * rho * v**2/2
	return dForce