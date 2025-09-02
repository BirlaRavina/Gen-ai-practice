# Task: Debug the Following Python Script
# There are some errors in the script below. Your task is to find and fix them.
# def calculate_area(radius):
#     pi = 3.1416
#     area = pi * (radius^2)
#     return area
# def calculate_rectangle_perimeter(length, width):
#     perimeter = length + width * 2
#     return perimeter
# def main():
#     # Test case 1: Circle with radius 5
#     radius = 5
#     circle_area = calculate_area(radius)
#     print("Area of Circle:", circle_area)
#     # Test case 2: Rectangle with length 6 and width 4
#     length = 6
#     width = 4
#     rectangle_perimeter = calculate_rectangle_perimeter(length, width)
#     print("Perimeter of Rectangle:", rectangle_perimeter)
#     # Question 3: What happens when negative values are given for length or width?
#     if length < 0 or width < 0:
#         print("Length or Width cannot be negative!")
#     else:
#         print("Dimensions are valid.")
#     string_input = "radius"
#     print("Circle Area:", calculate_area(string_input))
# if __name__ == "__main__":
#     main()

def calculate_area(radius):
    pi = 3.1416
    area = pi * (radius*radius)
    return area

def calculate_rectangle_perimeter(length, width):
    perimeter = (length + width) * 2
    return perimeter

def main():
    # Test case 1: Circle with radius 5
    radius = 5
    circle_area = calculate_area(radius)
    print("Area of Circle:", circle_area)
    # Test case 2: Rectangle with length 6 and width 4
    length = 6
    width = 4
    rectangle_perimeter = calculate_rectangle_perimeter(length, width)
    print("Perimeter of Rectangle:", rectangle_perimeter)
    # Question 3: What happens when negative values are given for length or width?
    if length < 0 or width < 0:
        print("Length or Width cannot be negative!")
    else:
        print("Dimensions are valid.")
    string_input = "radius"
    print("Circle Area:", calculate_area(string_input))
if __name__ == "__main__":
    main()
