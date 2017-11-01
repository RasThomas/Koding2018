myConstPi = 3.14
radius= 0

#Here we want to take an input form the user

print("Please enter the radis of the circle:")

radius = float(input())

if(radius < 0):
    print("You have typed a negative value")
    exit()
else:

    print("You have entered a radius of ", radius)

    print("The radius of the circle is ", radius)

    print("The areal of the circle is ", myConstPi *radius*radius)

    print("The conference of the circle is ", 2 *myConstPi *radius)
#Casting
    print("The conference of the circle as an interger is ", int(2 *myConstPi *radius))

