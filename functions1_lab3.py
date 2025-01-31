def Solve(heads, legs):
    chicken = -(legs - 4*heads)/2
    rabb = heads - chicken
    return rabb, chicken
print(Solve(35,94))