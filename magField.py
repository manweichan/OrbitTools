##Earth's magnetic field. (19-7) SME SMAD

def magField(r, m=7.98e15):
    #m: magnetic moment of the earth times magnetic constant (tesla * m^3)
    #r: Radius of earth center (dipole center) to spacecaraft (m)
    B = 2*m/r**3 #Magnetic field
    return B