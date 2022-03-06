'''
Geoffrey Gomlak
CNG 119
2/15/22
Practice 2.2 # 5
'''
import math

def main():

    x1 = 3
    y1 = 4
    x2 = 4
    y2 = 4
    # Equation
    distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

    # Compute the distance between the two points
    print("Distance:", distance)

if __name__ == '__main__':
    main()
