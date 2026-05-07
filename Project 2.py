print("Welcome to tip calculator")
bill= float(input("What was the total bill? $"))
tip= int(input("How much tip would you like to give? 10, 12, or 15? "))
people= int(input("How many people to split the bill? "))   
tip_as_percent= (tip / 100)*bill
total_bill= bill + tip_as_percent
bill_per_person= total_bill / people
print(f"Each person should pay: ${bill_per_person:.2f}")    
