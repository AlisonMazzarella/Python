from datetime import datetime

#Days of Week = M0 T1 W2 Th3 F4 Sa5 Su6

promotion = 0.10
sales_tax = 0.06

thisdate = datetime.now() 
dayofweek = thisdate.weekday()

subtotal = float(input("Please enter the subtotal: "))

if subtotal >=50 and (dayofweek == 1 or dayofweek == 2): 
    #what does the 2 stand for? Does it correlate to the weekdays? 
    promotional = round(subtotal * promotion, 2) 
    print(f"The discount amount is: {promotional:.2f}. ")
    #-= means variable on right being subrtracted by value on right
    subtotal -= promotional 

calculation = round(subtotal * sales_tax, 2)
#why are we using round built-in function but then still manually entering round total by 2 places?
print(f"The sales tax amount is: {calculation :.2f}")

final_total = subtotal + calculation 

print(f"Your total is: {final_total:.2f}. ")
