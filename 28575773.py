pi=3.414
def area(r):
   return (pi*r*r)
def circumference(r):
   return (pi*2*r)
#radius=0.0
radius=float(input("Enter radius: "))
print("area",area(radius))
print("circumference",circumference(radius))
