from datetime import datetime

now = datetime.today()

def YearsBP():
    years = int(input("Enter years: "))
    print(str(years) + " = " + str(1950 - years) + " BP")
    
def YearsBPtoYearsAD():
    years = int(input("Enter years: "))
    if years <= 1950:
        print(str(years) + " BP = " + str(1950 - years) + " AD")
    else:
        print(str(years) + " BP = " + str(years - 1950) + " BC")
    
def YearsBPtoYearsBeforeNow():
    years = int(input("Enter years: "))
    print(str(years) + " BP = " + str(years + (now.year - 1950)) + " yrs before now")
    
def YearsBeforeNowtoYearsBP():
    years = int(input("Enter years: "))
    print(str(years) + " yrs before now = " + str(years - (now.year - 1950)) + " BP")
    
def SelectConverter():
    method = input("Enter number: 1. AD/BC to BP? 2. BP to AD/BC? 3. BP to Before Now? 4. Before Now to BP? ")
    if method == "1":
        YearsBP()
    if method == "2":
        YearsBPtoYearsAD()
    if method == "3":
        YearsBPtoYearsBeforeNow()
    if method == "4":
        YearsBeforeNowtoYearsBP()
    else:
        print("Please try again.")
        
SelectConverter()