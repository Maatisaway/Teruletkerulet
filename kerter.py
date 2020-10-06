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
	a=float(input("Kérem a 8szög oldalát[cm]:"))	
	return float(8*a)
