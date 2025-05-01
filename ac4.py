def emp(name):
    return name

def sal(exp):
    if exp>=6:
        return 300000
    elif exp>=3:
        return 100000
    else:
        return 50000
    
print("Emp Name:",emp("Nihitha"))
print("Salary:",sal(8))