import math
from fractions import Fraction
def Trigman():
    # Welcome!
    print("TRIGMAN calcilator.\n")

# sin,cos or tan verification
    Stat_= input('enter S for SIN\n      C for COS\n      T for TAN\n').lower()

    # input angle val -degrees
    ang_deg = int(input("angle value in degrees.\n"))

    # sin val in fraction form

    if (Stat_=='s'):
        sin_degrees = math.sin(math.radians(ang_deg))
        print('sin of '+ str(ang_deg) + ' digrees ratio is', Fraction(sin_degrees).limit_denominator())
        print(sin_degrees, 'rounded', round(sin_degrees, 5), 'as decimal\n')

    # cos val in fraction form
    elif (Stat_=='c'):
        cosin_degrees = math.cos(math.radians(ang_deg))
        print('cos of ' + str(ang_deg) + ' digrees ratio is', Fraction(cosin_degrees).limit_denominator())
        print(cosin_degrees, 'rounded', round(cosin_degrees, 5), 'as decimal\n')

    # tan val in fraction form
    elif (Stat_=='t'):
        tan_degrees = math.tan(math.radians(ang_deg))
        print('tan of ' + str(ang_deg) + ' digrees ratio is', Fraction(tan_degrees).limit_denominator())
        print(tan_degrees, 'rounded', round(tan_degrees, 5), 'as decimal\n')

    # Repeat option.
    rep = input('Do you want to repeat for another trig value?\n Y for yes\n N for no\t').upper()
    if rep == 'Y':
        Trigman()

    else:
        exit()
Trigman()