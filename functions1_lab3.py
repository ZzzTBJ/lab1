import math
def Volume(rad = int(input())):
    vol = (4/3)*math.pi*pow(rad,3)
    print(f"The volume is {vol:.2f}")
Volume()
