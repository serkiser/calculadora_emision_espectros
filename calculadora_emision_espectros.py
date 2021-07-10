import math
import astropy.constants
from astropy import constants as const
def Presentation():
    """Presentation"""
print("""%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% by :Slod Calculadora de lineas %%%%
%%%%%de emision de hidrogeno v.3.2%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%""")
def Equations():
     """Equations"""
print("""
     1        |  1     1   |
  ------- = R | --- - ---  |
   landa      | i^2   j^2  |
    
          c
   f = -------
        landa

    E = h*f
    """)

def calculos():
    j = int(input("   Enter the value to calculate\n"))
    i = 2
    R = 10967758
    c = (const.c)
    h = (const.h)
    print("""---------------------------""")
    print("""Dates:
i = 2
R = 10967758
c = 299792458
h = 6.62606896*10^-34""")
    print("""---------------------------""")
    print("First we are going to calculate landa")
    print("""---------------------------""")
    print("First step -> ((1/(i**2))-(1/(j**2)))")
    P_1 = ((1/i**2) - (1/j**2))
    print(P_1)
    print("""---------------------------""")
    print("Second step -> R*(((1/(i**2))-(1/(j**2))))")
    p_2 = P_1*R
    print(p_2)
    print("""---------------------------""")
    print("Third step ->1/(R*(((1/(i**2))-(1/(j**2)))))")
    p_3 = 1/p_2
    print(p_3)
    print("""---------------------------""")
    print("Fourth step -> Move the comma")
    p_4 = p_3*1000000000
    print(p_4)
    print("""---------------------------""")
    print("Fifth step -> Truncate the number")
    p_5 = math.trunc(p_4)
    print(p_5,"nm")
    print("""---------------------------""")
    print("To calculate f")
    print("""---------------------------""")
    print("sixth step -> c*landa = f")
    p_6 = c*p_4
    print(p_6)
    print("""---------------------------""")
    print("Calculate energy")
    print("""---------------------------""")
    print("Seventh step -> h*f = E")
    p_7 = h*p_6
    print(p_7)
    print("""---------------------------""")
    print("Landa is =", p_4, "nm")
    print("f is =", p_6, "Hz")
    print("E is = ", p_7, "J")
    print("""---------------------------""")
    opc = int(input("   End\n"))
calculos()