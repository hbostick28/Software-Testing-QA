def BMI():
    x = int(input("Enter Weight(in pounds): "))
    y = int(input("Enter Height(in inches): "))

    weight = x * 0.45
    height = y * 0.025
    height2 = height * height
    overall = weight/height2

    print("BMI: ", round(overall,1))

    if overall <= 18.5:
        print("BMI Category: Underweight")
    elif overall > 18.6 and overall <= 24.9:
        print("BMI Category: Normal weight")
    elif overall > 25 and overall <= 29.9:
        print("BMI Category: Overweight")
    else:
        print("BMI Category: Obese")

    return

def ERA():
    age = int(input("Enter Current Age: "))
    salary = int(input("Enter Annual Salary: "))
    goal = int(input("Enter Desired Money Goal: "))
    percent = int(input("Enter Percentage Saved: "))

    percentSaved = (percent * 0.01) + 0.35
    moneySaved = salary * percentSaved
    money = 0
    yearCount = 0
    while money <= goal:
        yearCount += 1
        money += moneySaved

    overallAge = age + yearCount
    if overallAge >= 100:
        print("Unable to meet Savings Goal")
    else:
        print("Savings goal met by age: ", overallAge)
    
    return

def main():
    print("Menu:")
    print("1) BMI")
    print("2) ERA")
    print("3) EXIT")
    x = int(input("Please enter the number of the menu item you choose: "))

    if x == 1:
        BMI()
    elif x == 2:
        ERA()
    elif x == 3:
        print("Thank you for your time!")
    else:
        main()

main()
