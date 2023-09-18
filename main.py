red = int(input())
green = int(input())
blue = int(input())


if red < green and red < blue:
    new_red = red - red
    new_green = green - red
    new_blue = blue - red
    print(new_red, new_green, new_blue)
elif green < red and green < blue:
    new_green = green - green
    new_red = red - green
    new_blue = blue - green
    print(new_red, new_green, new_blue)
elif blue < green and blue < red:
    new_blue = blue - blue
    new_green = green - blue
    new_red = red - blue
    print(new_red, new_green, new_blue)
else:
    print(0, 0, 0)
