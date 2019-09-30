# This program is to calculate the areas of
# two Rectangles and find out which has the greater area.

# Dimensions of Rectangle1.
length1 = int(input('Length of Rectangle1: '))
width1 = int(input('Width of Rectangle1: '))

# Calculate area of Rectangle1.
area1 = length1 * width1

# Dimensions of Rectangle2.
length2 = int(input('Length of Rectangle2: '))
width2 = int(input('Width of Rectangle2: '))

# Calculate area of Rectangle2.
area2 = length2 * width2

# Determine which Rectangle has greater area.
if area1 > area2:
    print('Rectangle1 has greater area.')
elif area2 >area1:
    print('Rectangle2 has greater area.')
else:
    print('Both Rectangles have the same area.')

