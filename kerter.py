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
	
def nyolcszogKerulet():
	a=float(input("Kérem a 8szög oldalát[cm]:"))	
	r=float(input("Kérem a 8szög sugarát[cm]:"))	
	return float(4*a*r)
	
def haromszogKerulet():
	a=float(input("Kérem adja meg a háromszög egyik oldalát:"))
	b=float(input("Kérem adja meg a háromszög másik oldalát:"))
	c=float(input("Kérem adja meg a háromszög harmadik oldalát:"))
	return float(a+b+c)
def haromszogTerulet():
	a=float(input("Kérem adja meg a háromszög adott oldalát:"))
	ma=float(input("Kérem adja meg a háromszög adott oldalának a magasságát:"))
	return float(a*ma/2)
def korKerulet():
	r=float(input("Kérem adja meg a kör sugarát:"))
	return float(2*3.14*r)
def korTerulet():
	r=float(input("Kérem adja meg a kör sugarát:"))
	return float(3.14*r**2)
	
	
print("1 - Háromszög")
print("2 - Kör")
print("3 - Teglalap")
print("4 - Nyolcszög")
v=input("Milyen alakzattal szeretnél dolgozni?")
if v=="3":
	print(teglalapKerulet())
	print(teglalapTerulet())









