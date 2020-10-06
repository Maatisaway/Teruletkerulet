# file létrehozva
def teglalapKerulet():
	a=float(input("Kérem a téglalap egyik oldalát[cm]:"))	
	b=float(input("Kérem a téglalap másik oldalát[cm]:"))
	return float(2*(a+b))

def teglalapTerulet():
	a=float(input("Kérem a téglalap egyik oldalát[cm]:"))	
	b=float(input("Kérem a téglalap másik oldalát[cm]:"))
	return float(a*b)

def nyolcszogKerulet():
	a = input("Kérem adja meg a nyolcszög egyik oldalát[cm]")
	b = input("Kérem adja meg a nyolcszög második oldalát[cm]")
	c = input("Kérem adja meg a nyolcszög harmadik oldalát[cm]")
	d = input("Kérem adja meg a nyolcszög negyedik oldalát[cm]")
	
	return float(2*(a+b+c+d)