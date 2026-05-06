# Chapter 5 Problem 2 - Parking Garage

# prompt for the # of hours parked, and return this value
# if the input is not an integer, return the special value None
def getParkingHours():
    instring = input("Enter number of hours parked: ")
    if instring.isdigit():
        return float(instring)
    else:
        return None

# takes as input hours (number), and returns the parking fee
# this is a calculation-only function (it does not use input() or print())
def calcParkingFee(hours):
    fee = 2.50 * hours
    if fee < 6:
        fee = 6
    elif fee > 20:
        fee = 20
    return fee

# get number of hours parked
hours = getParkingHours()
# if invalid input, give message
if hours == None:
    print("Invalid input entered for hours")
# otherwise calculate and display parking fee
else:
    fee = calcParkingFee(hours)
    print("Fee = $", fee)
