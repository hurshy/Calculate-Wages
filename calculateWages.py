#Tyler Hegewald Calculate Wages
#Ask for name and salary
name = input("Enter your name ")
salary = float(input("Enter your salary in amount per hour "))

#Ask hour many hours worked
hoursWorked = float(input("Enter your hours worked in the past week "))

#Regular Pay
regPay = 40 * salary

#Determine Overtime pay
if hoursWorked > 40:
    overWorked = hoursWorked - 40
    moneyEarned = overWorked * (salary * 1.5)
    grossWage = moneyEarned + regPay
    print(name,"$%.2f"%grossWage)
if hoursWorked <= 40:
    belowOver = hoursWorked * salary
    print(name, "$%.2f"%belowOver)

