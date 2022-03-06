'''
Geoffrey Gomlak
Problem #20 Given the radius of a circle, 
print the area of the circle.
2/15/20
'''
import math

def main():
    
    # varriable / input
    radius = input("Enter a radius: ")
    AREA = math.pi * int(radius) ** 2
    
     # processing / output
    print("With the raidus", int(radius), "the area of the circle is", round(AREA, 2))
   
    
if __name__ == '__main__':
    main()
