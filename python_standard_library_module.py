import math as m
from math import radians, sin, cos
import datetime

if __name__ == '__main__': 
    print(m.sqrt(36))  # Output: 6.0

    angle_degrees = 40
    angle_radians = radians(angle_degrees)

    sine_value = sin(angle_radians)
    cos_value = cos(angle_radians)

    print(sine_value) # 0.6427876096865393
    print(cos_value)  # 0.766044443118978

    print(m.pi)  # Output: 3.141592653589793

    birthday = datetime.date(1959, 7, 15)
    print(birthday.day)    # 15
    print(birthday.month)  # 7
    print(birthday.year)   # 1959
