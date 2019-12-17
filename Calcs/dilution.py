import re
from fractions import Fraction
from decimal import Decimal
# I refers to initial ; F refers to final
initial = ''
final_vol = ''
concentration = ''
startvol = ''
finalconcentration = ''
finalvol = ''
percentweight = ''
density = ''
molecformweight = ''

def default_input():
	S = float(initial)
	return S
def default_final():
	F = float(final_vol)
	return F
def nondefault_input():	
	esearch = initial.find("E")
	negative = initial.find("-")
	if (negative):
		S = float(initial)
		return S
	else:
		default_input()
		
def nondef_final():
	fsearch = final_vol.find("E")
	negative = final_vol.find("-")
	if (negative):
		F = float(final_vol)
		return F
	else:
		default_final()
	
def output(S, F):
	dil = round((F/S), 100)
	rat = round((S/F), 100)
	ratio = Fraction(rat).limit_denominator(1000000)
	print('\n' f"Dilution factor: {dil} \nDilution ratio:  {ratio}")

# M1V1 = M2V2
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

	


#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––


#prompt_start = input("If you wish to use the dilution calculator, press ENTER:  ")

#if prompt_start == '':
#	print("use 'E' to denote x*(10^y)")
#	initial = initial + input("Initial volume (L is default):  ")
#	final_vol = final_vol + input("Final volume (L is default):  ")
#	isearch = re.search("E", initial)
#	fsearch = re.search("E", final_vol)
#	if (isearch) and (fsearch):
#		output(nondefault_input(), nondef_final())
#	elif (isearch) and not (fsearch):
#		output(nondefault_input(), default_final())
#	elif not (isearch) and (fsearch):
#		output(default_input(), nondef_final())
#	else:
#		output(default_input(), default_final())
#




#------------------------------------------------------
prompt_start = input("If you wish to use the dilution calculator, press ENTER:  ")
if prompt_start == '':
    User = input("\n[1] – For calculating dilution factor/ratio\n[2] – For solution dilution of known Molarity tool\n[3] – For calculating concentration (M) from %wt tool\n       Option:  ")
    if User == '1':
        print("\n(use 'E' to raise value *10^n)")
        initial = initial + input("\nInitial volume (L is default):  ")
        final_vol = final_vol + input("Final volume (L is default):  ")
        isearch = re.search("E", initial)
        fsearch = re.search("E", final_vol)
        if (isearch) and (fsearch):
            output(nondefault_input(), nondef_final())
        elif (isearch) and not (fsearch):
            output(nondefault_input(), default_final())
        elif not (isearch) and (fsearch):
            output(default_input(), nondef_final())
        else:
            output(default_input(), default_final())
    if User == '2':
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
    if User == '3':
        percentweight = percentweight + input("% weight (solute weight/total_weight)*100: ")
        density = density + input("Density of sample (g/mL): ")
        molecformweight = molecformweight + input("Molecular or Formula weight (g/mol): ")
        M_out(p_wt(), den(), MW())

