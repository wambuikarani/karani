# calculating average marks
def average_marks(a,b,c,d,e):
    average=(a+b+c+d+e)/5
    print("The average marks is:",average)
average_marks(25,30,70,15,45)
average_marks(50,60,70,90,80)

print("===============")

# calculating area of a rectangle
def rectangle_area(length,width):
    area=length*width
    print("The area of a rectangle is:",area)
rectangle_area(12,4)
rectangle_area(20,5)

print("===============")

# calculating speed
def calculate_speed(distance,time):
    speed=distance/time
    print("the speed is:",speed)
calculate_speed(400,5)
calculate_speed(60,30)

print("===============")

# calculating total price with tax
def total_with_tax(price,taxrate):
    Total_price=price+(price*taxrate)
    print("The total with tax is:",Total_price)
total_with_tax(4000,20)
total_with_tax(2300,54)

print("===============")










































































# calculating simple interest
def calculate_interest(principal,rate):
    interest=principal*rate
    print("The interest is:",interest)
calculate_interest(4500,10)
calculate_interest(100,15)
