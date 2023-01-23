from datetime import datetime

now = datetime.today()

def YearsBP(years):
    print(str(years) + " = " + str(1950 - years) + " BP")
    
def YearsBPtoYearsAD(years):
    if years <= 1950:
        print(str(years) + " BP = " + str(1950 - years) + " AD")
    else:
        print(str(years) + " BP = " + str(years - 1950) + " BC")
    
def YearsBPtoYearsBeforeNow(years):
    print(str(years) + " BP = " + str(years + (now.year - 1950)) + " yrs before now")
    
def SelectConverter():
    method = input("1. AD/BC to BP? 2. BP to AD/BC?")
    print(method)

YearsBP(1650)
YearsBP(-50)
YearsBPtoYearsAD(500)
YearsBPtoYearsAD(1950)
YearsBPtoYearsAD(1951)
YearsBPtoYearsBeforeNow(1000)
SelectConverter()
