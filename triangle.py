"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple python program to classify triangles
@author: jrr
@author: rk
@author: Michayla Ben-Ezra
Updated on September 9 2018
"""


def classify_triangle(side_a, side_b, side_c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'
      BEWARE: there may be a bug or two in this code
    """

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(side_a, int) and isinstance(side_b, int) and isinstance(side_c, int)):
        print('Invalid Input')
        # require that the input values be >= 0 and <= 200
    if side_a > 200 or side_b > 200 or side_c > 200:
        print('Invalid Input')
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        print('Invalid Input')

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (side_a > (side_b + side_c)) or (side_b > (side_a + side_c)) or (side_c > (side_a + side_b)):
        print('This is not a triangle.')
    # now we know that we have a valid triangle

    if side_a == side_b == side_c:
        print('This is an equilateral triangle.')
    elif ((side_a ** 2) + (side_b ** 2)) == (side_c ** 2) or \
            ((side_a ** 2) + (side_c ** 2)) == (side_b ** 2) or \
            ((side_b ** 2) + (side_c ** 2)) == (side_a ** 2):
        print('This is a right triangle')
    elif side_a != side_b != side_c:
        print('This is a scalene triangle.')
    else:
        print('This is an isosceles triangle.')


def main():
    """
    Main function is to get input and output for the program
    """
    choice = input('Would you like to classify a triangle, y/n? ')
    while choice == 'y':

        print('Please enter three integers to make a triangle.')
        side_a = input('a: ')
        side_b = input('b: ')
        side_c = input('c: ')

        side_a = int(side_a)
        side_b = int(side_b)
        side_c = int(side_c)
        print(classify_triangle(side_a, side_b, side_c))
        choice = input('Would you like to classify a triangle, y/n? ')


if __name__ == '__main__':
    main()
