from datetime import datetime

now = datetime.today()

def YearsBP():
    years = int(input("Enter years. "))
    print(str(years) + " = " + str(1950 - years) + " BP")
    
def YearsBPtoYearsAD():
    years = int(input("Enter years. "))
    if years <= 1950:
        print(str(years) + " BP = " + str(1950 - years) + " AD")
    else:
        print(str(years) + " BP = " + str(years - 1950) + " BC")
    
def YearsBPtoYearsBeforeNow():
    years = int(input("Enter years. "))
    print(str(years) + " BP = " + str(years + (now.year - 1950)) + " yrs before now")
    
def SelectConverter():
    method = input("1. AD/BC to BP? 2. BP to AD/BC? ")
    if method == "1":
        YearsBP()
    if method == "2":
        YearsBPtoYearsAD()
        
SelectConverter()