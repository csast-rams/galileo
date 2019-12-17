# M1 x V1 = M2 x V2
#import re
#from fractions import fraction

concentration = ''
startvol = ''
finalconcentration = ''
finalvol = ''

def m1():
    C = float(concentration)
    return C
def v1():
    V1 = float(startvol)
    return V1
def m2():
    fC = float(finalconcentration)
    return fC
def v2():
    V = float(finalvol)
    return V

def out_put(x, y, z):
    O = (x * y)/z
    print(O)
    
#[(% x d) / MW] x 10 = Molarity
percentweight = ''
density = ''
molecformweight = ''

def p_wt():
    wt = float(percentweight)
    return wt
def den():
    D = float(density)
    return D
def MW():
    FW = float(molecformweight)
    return FW

def M_out(p, d, m):
    FM = ((p * d)/m) * 10
    print(FM)
#------------------------------------------------------
User = input("If you would like to use the solution dilution of known Molarity tool, enter [1], if you would like to calculate concentration (M) from %wt, enter [2]")
if User == '1':
    concentration = concentration + input("Initial concentration M1 (mol/L): ")
    startvol = startvol + input("Initial volume V1 (L): ")
    finalconcentration = finalconcentration + input("Final concentration M2 (mol/L): ")
    finalvol = finalvol + input("Final volume V2 (L): ")
    if concentration == '':
        print("\nInitial concentration: ")
        out_put(m2(), v2(), v1())
    elif startvol == '':
        print("\nInitial volume: ")
        out_put(m2(), v2(), m1())
    elif finalconcentration == '':
        print("\nFinal concentration: ")
        out_put(m1(), v1(), v2())
    elif finalvol == '':
        print("\nFinal vol: ")
        out_put(m1(), v1(), m2())
if User == '2':
    percentweight = percentweight + input("% weight (solute weight/total_weight)*100: ")
    density = density + input("Density of sample (g/mL): ")
    molecformweight = molecformweight + input("Molecular or Formula weight (g/mol): ")
    M_out(p_wt(), den(), MW())
    
