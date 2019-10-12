
#Replace all ______ with rjust, ljust or center.

thickness = 5 #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print(' ' * 2 + (c*thickness).ljust(thickness*3)+(c*thickness).ljust(thickness*5))

#Middle Belt
for i in range((thickness+1)// 2):
    print(' ' * 2 +(c*thickness*5).ljust(thickness*5))

#Bottom Pillars
for i in range(thickness+1):
    print(' ' * 2 + (c * thickness).ljust(thickness * 3)+(c * thickness).ljust(thickness * 6))

#Bottom Cone
for i in range(thickness):
    print(' ' * 2 +((c*(thickness-i-1)).rjust(thickness *2)+c+(c*(thickness-i-1)).ljust(thickness)).center(
        thickness*6))





# Print the position of the decimal point.
# Find and print the number of digits after the decimal points.
# Now you have identified those digits cut away the rest, except for the first two numbers of the string.





























