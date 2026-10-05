# HVAC Toolkit for TI-Nspire CX II CAS
# All menus and content fit 11-line screen
# Compatible with TI-Nspire Python

def pause():
    input("-- Enter to continue --")

# ================================
# P-T TABLE DATA
# ================================
PT_410A_T = [-40,-30,-20,-10,0,10,20,24,30,40,45,
             50,60,70,80,90,100,110,120,130]
PT_410A_P = [16,22,30,40,52,66,82,95,103,118,130,
             143,173,207,246,291,342,390,417,478]
PT_22_T =   [-40,-30,-20,-10,0,10,20,30,40,45,
             50,60,70,80,90,100,110,120]
PT_22_P =   [0.5,5,11,18,25,34,45,58,68,76,
             84,101,121,143,168,196,226,260]
PT_134A_T = [-40,-20,0,10,20,30,40,50,60,
             70,80,90,100,110,120]
PT_134A_P = [-2,4,14,20,27,37,49,63,79,
             98,120,146,176,210,248]

def pt_interp(t_list, p_list, x, by_temp=True):
    src = t_list if by_temp else p_list
    dst = p_list if by_temp else t_list
    if x <= src[0]: return dst[0]
    if x >= src[-1]: return dst[-1]
    for i in range(len(src)-1):
        if src[i] <= x <= src[i+1]:
            r = (x-src[i])/(src[i+1]-src[i])
            return dst[i]+r*(dst[i+1]-dst[i])
    return None

def get_pt_data(ref):
    if ref==1: return PT_410A_T,PT_410A_P,"R-410A"
    elif ref==2: return PT_22_T,PT_22_P,"R-22"
    elif ref==3: return PT_134A_T,PT_134A_P,"R-134a"
    return None,None,None

# ================================
# MAIN MENU (6 lines)
# ================================
def main_menu():
    while True:
        print("\n=== HVAC TOOLKIT ===")
        print("1. Unit Converter")
        print("2. Formula Reference")
        print("3. Quick Reference")
        print("4. Quit")
        c = input("Select (1-4): ")
        if c=="1": unit_menu()
        elif c=="2": formula_menu()
        elif c=="3": quick_ref_menu()
        elif c=="4":
            print("Goodbye!")
            break
        else: print("Invalid.")

# ================================
# UNIT CONVERTER (9 lines)
# ================================
def unit_menu():
    while True:
        print("\n=== UNIT CONVERTER ===")
        print("1. Temperature")
        print("2. Pressure")
        print("3. Airflow")
        print("4. Power/Cooling")
        print("5. Length")
        print("6. Area")
        print("7. Back")
        c = input("Select (1-7): ")
        if c=="1": temp_conv()
        elif c=="2": pres_conv()
        elif c=="3": air_conv()
        elif c=="4": power_conv()
        elif c=="5": length_conv()
        elif c=="6": area_conv()
        elif c=="7": break
        else: print("Invalid.")

# ================================
# TEMPERATURE CONVERTER (10 lines)
# ================================
def temp_conv():
    while True:
        print("\n--- TEMPERATURE ---")
        print("1.F>C  2.C>F  3.F>K")
        print("4.C>K  5.K>F  6.K>C")
        print("7.F>Rankine")
        print("8. Back")
        c = input("Select (1-8): ")
        if c=="8": break
        try:
            v = float(input("Value: "))
            if c=="1":   print("%.4f C"%((v-32)*5/9))
            elif c=="2": print("%.4f F"%(v*9/5+32))
            elif c=="3": print("%.4f K"%((v-32)*5/9+273.15))
            elif c=="4": print("%.4f K"%(v+273.15))
            elif c=="5": print("%.4f F"%((v-273.15)*9/5+32))
            elif c=="6": print("%.4f C"%(v-273.15))
            elif c=="7": print("%.4f R"%(v+459.67))
            else: print("Invalid."); continue
            pause()
        except: print("Invalid input.")

# ================================
# PRESSURE CONVERTER (10 lines)
# ================================
def pres_conv():
    # Microns (umHg) are absolute vacuum units
    # 1 micron = 0.000133322 kPa absolute
    # Perfect vacuum = 0 microns
    # 1 atm = 760,000 microns
    units=["PSIG","PSIA","kPa-g","kPa-a",
           "inHg","inH2O","bar","Microns"]
    to_kpa=[6.89476,6.89476,1.0,1.0,
            3.38639,0.24908,100.0,0.000133322]
    is_abs=[False,True,False,True,
            False,False,False,True]
    atm=101.325
    while True:
        print("\n--- PRESSURE ---")
        print("1.PSIG  2.PSIA")
        print("3.kPa-g 4.kPa-a")
        print("5.inHg  6.inH2O")
        print("7.bar   8.Microns")
        print("9. Back")
        c1=input("From: ")
        if c1=="9": break
        c2=input("To: ")
        if c2=="9": break
        try:
            f=int(c1)-1; t=int(c2)-1
            v=float(input("Value: "))
            kpa=v*to_kpa[f]
            if is_abs[f]: kpa-=atm
            r=kpa/to_kpa[t]
            if is_abs[t]: r+=(atm/to_kpa[t])
            print("%.5f %s"%(r,units[t]))
            if units[t]=="Microns":
                if r<250:   print("Excellent vacuum")
                elif r<500: print("Acceptable vacuum")
                elif r<1000:print("Marginal vacuum")
                else:       print("Poor vacuum")
            pause()
        except: print("Invalid input.")

# ================================
# AIRFLOW CONVERTER (7 lines)
# ================================
def air_conv():
    units=["CFM","m3/h","L/s"]
    to_cfm=[1.0,0.58858,2.11888]
    while True:
        print("\n--- AIRFLOW ---")
        print("1.CFM  2.m3/h  3.L/s")
        print("4. Back")
        c1=input("From: ")
        if c1=="4": break
        c2=input("To: ")
        if c2=="4": break
        try:
            f=int(c1)-1; t=int(c2)-1
            v=float(input("Value: "))
            r=v*to_cfm[f]/to_cfm[t]
            print("%.4f %s"%(r,units[t]))
            pause()
        except: print("Invalid input.")

# ================================
# POWER/COOLING CONVERTER (9 lines)
# ================================
def power_conv():
    units=["BTU/hr","Tons","kW","Watts","HP","kWh"]
    to_btu=[1.0,12000.0,3412.14,3.41214,2544.43,3412.14]
    while True:
        print("\n--- POWER/COOLING ---")
        print("1.BTU/hr  2.Tons")
        print("3.kW      4.Watts")
        print("5.HP      6.kWh")
        print("7. Back")
        c1=input("From: ")
        if c1=="7": break
        c2=input("To: ")
        if c2=="7": break
        try:
            f=int(c1)-1; t=int(c2)-1
            v=float(input("Value: "))
            r=v*to_btu[f]/to_btu[t]
            print("%.4f %s"%(r,units[t]))
            pause()
        except: print("Invalid input.")

# ================================
# LENGTH CONVERTER (8 lines)
# ================================
def length_conv():
    units=["Feet","Inches","Meters","cm","mm","Microns(um)"]
    to_ft=[1.0,0.08333,3.28084,0.0328084,
           0.00328084,0.00000328084]
    while True:
        print("\n--- LENGTH ---")
        print("1.Feet   2.Inches")
        print("3.Meters 4.cm")
        print("5.mm     6.Microns(um)")
        print("7. Back")
        c1=input("From: ")
        if c1=="7": break
        c2=input("To: ")
        if c2=="7": break
        try:
            f=int(c1)-1; t=int(c2)-1
            v=float(input("Value: "))
            r=v*to_ft[f]/to_ft[t]
            print("%.6f %s"%(r,units[t]))
            pause()
        except: print("Invalid input.")

# ================================
# AREA CONVERTER (8 lines)
# ================================
def area_conv():
    units=["ft2","in2","m2","cm2"]
    to_ft2=[1.0,0.006944,10.7639,0.00107639]
    while True:
        print("\n--- AREA ---")
        print("1.ft2  2.in2")
        print("3.m2   4.cm2")
        print("5. Back")
        c1=input("From: ")
        if c1=="5": break
        c2=input("To: ")
        if c2=="5": break
        try:
            f=int(c1)-1; t=int(c2)-1
            v=float(input("Value: "))
            r=v*to_ft2[f]/to_ft2[t]
            print("%.6f %s"%(r,units[t]))
            pause()
        except: print("Invalid input.")

# ================================
# FORMULA REFERENCE (5 lines)
# Split into Calculators/Reference
# ================================
def formula_menu():
    while True:
        print("\n=== FORMULA REF ===")
        print("1. Calculators")
        print("2. Reference Guides")
        print("3. Back")
        c=input("Select (1-3): ")
        if c=="1": calc_menu()
        elif c=="2": ref_menu()
        elif c=="3": break
        else: print("Invalid.")

# ================================
# CALCULATORS SUBMENU (8 lines)
# ================================
def calc_menu():
    while True:
        print("\n--- CALCULATORS ---")
        print("1. Heat Load")
        print("2. Efficiency EER/COP")
        print("3. Duct Velocity")
        print("4. Gas Laws")
        print("5. Properties")
        print("6. Back")
        c=input("Select (1-6): ")
        if c=="1": calc_heat()
        elif c=="2": calc_eer()
        elif c=="3": calc_duct()
        elif c=="4": calc_gas_laws()
        elif c=="5": props_menu()
        elif c=="6": break
        else: print("Invalid.")

# ================================
# REFERENCE SUBMENU (7 lines)
# ================================
def ref_menu():
    while True:
        print("\n--- REFERENCE ---")
        print("1. Refrigeration")
        print("2. Psychrometrics")
        print("3. Electrical")
        print("4. Brazing/Tubing")
        print("5. Back")
        c=input("Select (1-5): ")
        if c=="1": refrig_menu()
        elif c=="2": ref_psychro()
        elif c=="3": calc_elec()
        elif c=="4": ref_braze()
        elif c=="5": break
        else: print("Invalid.")

# ================================
# QUICK REFERENCE MENU (10 lines)
# ================================
def quick_ref_menu():
    while True:
        print("\n=== QUICK REFERENCE ===")
        print("1. Key Constants")
        print("2. Heat Transfer")
        print("3. Refrigeration Cycle")
        print("4. Refrigerant Facts")
        print("5. Safety & Tools")
        print("6. Instruments")
        print("7. Pipe & Fittings")
        print("8. Back")
        c=input("Select (1-8): ")
        if c=="8": break
        elif c=="1": qr_constants()
        elif c=="2": qr_heat_transfer()
        elif c=="3": qr_refrig_cycle()
        elif c=="4": qr_refrigerants()
        elif c=="5": qr_safety()
        elif c=="6": qr_instruments()
        elif c=="7": qr_pipe()
        else: print("Invalid.")

# ================================
# KEY CONSTANTS (paginated)
# ================================
def qr_constants():
    print("\n--- CONSTANTS (1/4) ---")
    print("PRESSURE:")
    print(" 1 atm = 14.696 psia")
    print(" 1 atm = 29.92 inHg")
    print(" 1 atm = 101.325 kPa")
    print(" 1 atm = 33.9 ft H2O")
    print(" psig + 14.696 = psia")
    pause()
    print("\n--- CONSTANTS (2/4) ---")
    print("POWER/COOLING:")
    print(" 1 Ton = 12,000 BTU/hr")
    print(" 1 Ton = 3.517 kW")
    print(" 1 kW  = 3,412 BTU/hr")
    print(" 1 HP  = 746 Watts")
    print(" 1 HP  = 2,544 BTU/hr")
    print(" 1 HP  = 33,000 ft-lb/min")
    print(" 1 kWh = 3,412 BTU")
    pause()
    print("\n--- CONSTANTS (3/4) ---")
    print("TEMPERATURE:")
    print(" Abs zero = -459.67 F")
    print(" Abs zero = -273.15 C")
    print(" Rankine  = F + 459.67")
    print(" Kelvin   = C + 273.15")
    print("ENERGY:")
    print(" 1 BTU = 778 ft-lbf")
    print(" 1 BTU = raise 1lb H2O 1F")
    pause()
    print("\n--- CONSTANTS (4/4) ---")
    print("AIR (70F, standard):")
    print(" Density  = 0.075 lb/ft3")
    print(" Sp.Vol   = 13.33 ft3/lb")
    print(" Sp.Heat  = 0.240 BTU/lb/F")
    print("WATER:")
    print(" Density  = 62.37 lb/ft3")
    print(" Sp.Heat  = 1.000 BTU/lb/F")
    print(" 1 gal    = 8.34 lb")
    pause()

# ================================
# HEAT TRANSFER (paginated)
# ================================
def qr_heat_transfer():
    print("\n--- HEAT TRANSFER (1/3) ---")
    print("CONDUCTION:")
    print(" Heat thru solid material")
    print(" Direct contact required")
    print(" Ex: hand on hot pan")
    print(" Ex: heat thru copper pipe")
    pause()
    print("\n--- HEAT TRANSFER (2/3) ---")
    print("CONVECTION:")
    print(" Heat thru fluid movement")
    print(" FORCED or NATURAL")
    print(" Forced = fan/pump")
    print(" Natural = buoyancy")
    print(" Ex: warm air rising")
    print("RADIATION:")
    print(" No contact needed")
    print(" Ex: sun rays heating car")
    pause()
    print("\n--- HEAT TRANSFER (3/3) ---")
    print("SENSIBLE HEAT:")
    print(" Causes TEMP CHANGE")
    print(" Measurable w/thermometer")
    print("LATENT HEAT:")
    print(" Causes PHASE CHANGE")
    print(" No temp change occurs")
    print(" Ex: ice melting at 32F")
    print("Conservation of Energy:")
    print(" Energy cannot be created")
    pause()

# ================================
# REFRIGERATION CYCLE QR (paginated)
# ================================
def qr_refrig_cycle():
    print("\n--- REFRIG CYCLE (1/3) ---")
    print("Basic cycle type:")
    print(" Repeating vapor-compression")
    print("4 Components:")
    print(" 1.Compressor")
    print(" 2.Condenser")
    print(" 3.Metering Device")
    print(" 4.Evaporator")
    pause()
    print("\n--- REFRIG CYCLE (2/3) ---")
    print("Refrigerant States:")
    print(" CompIN:  100% vapor low P")
    print(" CompOUT: 100% vapor high P")
    print(" CondOUT: 100% liquid high P")
    print(" EvapIN:  75%liq/25%vap low P")
    print(" EvapOUT: 100% vapor low P")
    pause()
    print("\n--- REFRIG CYCLE (3/3) ---")
    print("Compressor:")
    print(" Low P vapor > high P vapor")
    print("Condenser rejects:")
    print(" LATENT + SENSIBLE heat")
    print("Vacuum in system:")
    print(" Air pulled INTO system")
    print("Compressor burnout:")
    print(" Produces ACID")
    pause()

# ================================
# REFRIGERANT FACTS (paginated)
# ================================
def qr_refrigerants():
    print("\n--- REFRIGERANTS (1/3) ---")
    print("CFC (R-11,R-12):")
    print(" HIGHEST ozone depletion!")
    print(" Phased out")
    print("HCFC (R-22):")
    print(" Medium ozone depletion")
    print(" Being phased out")
    print("HFC (R-410A,R-134a):")
    print(" NO ozone depletion")
    pause()
    print("\n--- REFRIGERANTS (2/3) ---")
    print("HFC (cont):")
    print(" HIGH GWP")
    print("HFO (R-32,R-454B):")
    print(" No ODP, LOW GWP")
    print(" Newer replacements")
    print("ODP ranking (high>low):")
    print(" CFC > HCFC > HFC/HFO")
    print("HFCs: NO ODP, HIGH GWP")
    pause()
    print("\n--- REFRIGERANTS (3/3) ---")
    print("REFRIGERANT definition:")
    print(" Changes to vapor by boiling")
    print(" OR liquid by condensing")
    print("N2 tank rule:")
    print(" MUST have press.regulator")
    print("Oil + O2 under pressure:")
    print(" Can cause EXPLOSION!")
    print("Frostbite risk:")
    print(" Liquid line service port")
    pause()

# ================================
# SAFETY & TOOLS (paginated)
# ================================
def qr_safety():
    print("\n--- SAFETY (1/3) ---")
    print("PPE (3 items):")
    print(" Safety glasses")
    print(" Gloves")
    print(" Work boots")
    print("PASS (fire extinguisher):")
    print(" Pull the pin")
    print(" Aim at base of fire")
    print(" Squeeze handle")
    pause()
    print("\n--- SAFETY (2/3) ---")
    print("PASS (cont):")
    print(" Sweep side to side")
    print("Ladder rule:")
    print(" 1ft out per 4ft height")
    print(" 30ft roof = 2.5ft base")
    print("Fume prevention:")
    print(" Ensure ADEQUATE VENTILATION")
    pause()
    print("\n--- SAFETY (3/3) ---")
    print("TUBING TOOLS:")
    print(" Tubing benders:")
    print("  Soft copper & aluminum")
    print(" Tubing cutters:")
    print("  Lever and spring types")
    print(" Reamer: removes burrs")
    print(" Swage: joins two Cu pipes")
    print("Duct pressure in:")
    print(" Inches water column (IWC)")
    pause()

# ================================
# INSTRUMENTS (paginated)
# ================================
def qr_instruments():
    print("\n--- INSTRUMENTS (1/2) ---")
    print("Bourdon tube:")
    print(" Used in ANALOG gauges")
    print(" Curved tube straightens")
    print(" under pressure")
    print("Anemometer:")
    print(" Measures AIR VELOCITY")
    print(" NOT pressure!")
    print("Manometer:")
    print(" Measures low pressures")
    pause()
    print("\n--- INSTRUMENTS (2/2) ---")
    print("Pressure defined as:")
    print(" Force per unit AREA")
    print("Thermometer measures:")
    print(" SENSIBLE HEAT (temp change)")
    print("Work defined as:")
    print(" Force moving object in")
    print(" direction of force")
    print("Low-side test press for:")
    print(" LEAK TESTING")
    pause()

# ================================
# PIPE & FITTINGS (paginated)
# ================================
def qr_pipe():
    print("\n--- PIPE (1/3) ---")
    print("PLASTIC TYPES:")
    print(" PVC: standard ~140F")
    print(" CPVC: up to 180F/100psig")
    print("  Used in HVAC/R apps")
    print(" ABS: drain/waste/vent")
    print(" PE: underground/gas")
    pause()
    print("\n--- PIPE (2/3) ---")
    print("JOINING METHODS:")
    print(" Soldering: water/hydronic")
    print(" Brazing: refrigerant lines")
    print(" Press-fit (Propress):")
    print("  Mfr-specific fittings")
    print(" Welding: steel pipe")
    print(" Threading: NPT")
    print(" Flaring: flare fittings")
    pause()
    print("\n--- PIPE (3/3) ---")
    print("Swage fitting:")
    print(" Joins two copper pipes")
    print(" for brazing/soldering")
    print("Flux main function:")
    print(" Prevents OXIDATION")
    print("TORCH temps (hot>cool):")
    print(" Oxyacetylene > Air-acet")
    print(" > MAPP > Propane")
    pause()

# ================================
# HEAT LOAD CALCULATOR
# ================================
def calc_heat():
    while True:
        print("\n--- HEAT LOAD ---")
        print("1. Sensible Q=1.08xCFMxdT")
        print("2. Total    Q=4.5xCFMxdh")
        print("3. Latent   Q=0.68xCFMxdW")
        print("4. BTU/hr to Tons")
        print("5. Back")
        c=input("Select (1-5): ")
        if c=="5": break
        try:
            if c=="1":
                cfm=float(input("CFM: "))
                dt=float(input("dT (F): "))
                q=1.08*cfm*dt
            elif c=="2":
                cfm=float(input("CFM: "))
                dh=float(input("dh (BTU/lb): "))
                q=4.5*cfm*dh
            elif c=="3":
                cfm=float(input("CFM: "))
                dw=float(input("dW (gr/lb): "))
                q=0.68*cfm*dw
                print("Q=%.1f BTU/hr"%q)
                print(" =%.4f Tons"%(q/12000))
                pause(); continue
            elif c=="4":
                btu=float(input("BTU/hr: "))
                print("%.4f Tons"%(btu/12000))
                print("%.3f kW"%(btu/3412.14))
                pause(); continue
            else: print("Invalid."); continue
            print("Q=%.1f BTU/hr"%q)
            print(" =%.4f Tons"%(q/12000))
            print(" =%.3f kW"%(q/3412.14))
            pause()
        except: print("Invalid input.")

# ================================
# EER / COP CALCULATOR
# ================================
def calc_eer():
    while True:
        print("\n--- EFFICIENCY ---")
        print("1. EER = BTU/hr / Watts")
        print("2. COP = Qout / Win")
        print("3. Back")
        c=input("Select (1-3): ")
        if c=="3": break
        try:
            if c=="1":
                btu=float(input("BTU/hr: "))
                w=float(input("Watts: "))
                eer=btu/w
                print("EER  = %.2f"%eer)
                print("SEER~= %.2f"%(eer*1.1))
                print("COP  = %.2f"%(eer/3.412))
            elif c=="2":
                qout=float(input("Output (kW): "))
                win=float(input("Input (kW): "))
                cop=qout/win
                print("COP  = %.3f"%cop)
                print("EER~ = %.2f"%(cop*3.412))
            else: print("Invalid."); continue
            pause()
        except: print("Invalid input.")

# ================================
# DUCT VELOCITY CALCULATOR
# ================================
def calc_duct():
    import math
    while True:
        print("\n--- DUCT VELOCITY ---")
        print("Supply: 600-900 FPM")
        print("Return: 600-700 FPM")
        print("Mains: 1000-1800 FPM")
        print("1.Round  2.Rect  3.Back")
        c=input("Select (1-3): ")
        if c=="3": break
        try:
            cfm=float(input("CFM: "))
            if c=="1":
                d=float(input("Diameter (in): "))
                area=math.pi*(d/24)**2
            elif c=="2":
                w=float(input("Width (in): "))
                h=float(input("Height (in): "))
                area=w*h/144
            else: print("Invalid."); continue
            vel=cfm/area
            print("Area=%.4f ft2"%area)
            print("Vel =%.1f FPM"%vel)
            if vel<400:   print("WARNING: Too low!")
            elif vel<600: print("Low - check design")
            elif vel<900: print("OK supply/return")
            elif vel<1800:print("OK main duct")
            else:         print("HIGH - upsize!")
            pause()
        except: print("Invalid input.")

# ================================
# REFRIGERATION MENU (8 lines)
# ================================
def refrig_menu():
    while True:
        print("\n--- REFRIGERATION ---")
        print("1. P-T Chart Lookup")
        print("2. Superheat Calc")
        print("3. Subcooling Calc")
        print("4. Cycle Reference")
        print("5. Classifications")
        print("6. Back")
        c=input("Select (1-6): ")
        if c=="6": break
        elif c=="1": calc_pt()
        elif c=="2": calc_superheat()
        elif c=="3": calc_subcool()
        elif c=="4": ref_refrig()
        elif c=="5": ref_refrig_class()
        else: print("Invalid.")

# ================================
# P-T CHART LOOKUP (8 lines)
# ================================
def calc_pt():
    while True:
        print("\n--- P-T CHART ---")
        print("1.R-410A 2.R-22")
        print("3.R-134a 4.Back")
        rc=input("Refrigerant: ")
        if rc=="4": break
        try:
            tl,pl,name=get_pt_data(int(rc))
            if tl is None: print("Invalid."); continue
            print("1.Press>Temp 2.Temp>Press")
            dc=input("Direction: ")
            if dc=="1":
                p=float(input("Pressure (psig): "))
                t=pt_interp(tl,pl,p,by_temp=False)
                print("%s %.1f psig"%(name,p))
                print("Sat Temp = %.1f F"%t)
            elif dc=="2":
                t=float(input("Sat Temp (F): "))
                p=pt_interp(tl,pl,t,by_temp=True)
                print("%s %.1f F"%( name,t))
                print("Pressure = %.1f psig"%p)
            else: print("Invalid."); continue
            pause()
        except: print("Invalid input.")

# ================================
# SUPERHEAT CALCULATOR (8 lines)
# ================================
def calc_superheat():
    while True:
        print("\n--- SUPERHEAT ---")
        print("SH = Actual - Sat Temp")
        print("1.R-410A 2.R-22")
        print("3.R-134a 4.Manual")
        print("5. Back")
        rc=input("Select (1-5): ")
        if rc=="5": break
        try:
            if rc=="4":
                sat=float(input("Sat Temp (F): "))
                act=float(input("Actual Temp (F): "))
                sh=act-sat
            else:
                tl,pl,name=get_pt_data(int(rc))
                if tl is None: print("Invalid."); continue
                p=float(input("Suction Press (psig): "))
                act=float(input("Outlet Temp (F): "))
                sat=pt_interp(tl,pl,p,by_temp=False)
                sh=act-sat
                print("Sat Temp  = %.1f F"%sat)
            print("Actual    = %.1f F"%act)
            print("Superheat = %.1f F"%sh)
            if sh<5:    print("WARNING: Very low!")
            elif sh<10: print("Low superheat")
            elif sh<=20:print("Normal superheat")
            else:       print("High superheat")
            pause()
        except: print("Invalid input.")

# ================================
# SUBCOOLING CALCULATOR (8 lines)
# ================================
def calc_subcool():
    while True:
        print("\n--- SUBCOOLING ---")
        print("SC = Sat Temp - Actual")
        print("1.R-410A 2.R-22")
        print("3.R-134a 4.Manual")
        print("5. Back")
        rc=input("Select (1-5): ")
        if rc=="5": break
        try:
            if rc=="4":
                sat=float(input("Sat Temp (F): "))
                act=float(input("Actual Temp (F): "))
                sc=sat-act
            else:
                tl,pl,name=get_pt_data(int(rc))
                if tl is None: print("Invalid."); continue
                p=float(input("Liquid Press (psig): "))
                act=float(input("Outlet Temp (F): "))
                sat=pt_interp(tl,pl,p,by_temp=False)
                sc=sat-act
                print("Sat Temp   = %.1f F"%sat)
            print("Actual     = %.1f F"%act)
            print("Subcooling = %.1f F"%sc)
            if sc<5:    print("Low subcooling")
            elif sc<=15:print("Normal subcooling")
            else:       print("High subcooling")
            pause()
        except: print("Invalid input.")

# ================================
# REFRIGERATION CYCLE REF (paginated)
# ================================
def ref_refrig():
    print("\n--- CYCLE REF (1/2) ---")
    print("4 Components:")
    print(" 1.Compressor")
    print(" 2.Condenser")
    print(" 3.Metering Device")
    print(" 4.Evaporator")
    print("Superheat=Actual-SatTemp")
    print("Subcool=SatTemp-Actual")
    pause()
    print("\n--- CYCLE REF (2/2) ---")
    print("States:")
    print(" CompIN:  100% vap low P")
    print(" CompOUT: 100% vap high P")
    print(" CondOUT: 100% liq high P")
    print(" EvapIN:  75liq/25vap low P")
    print(" EvapOUT: 100% vap low P")
    print("Cycle: repeating vap-comp")
    pause()

# ================================
# SYSTEM CLASSIFICATIONS (paginated)
# ================================
def ref_refrig_class():
    print("\n--- CLASSIFICATIONS ---")
    print("HIGH TEMP: above 32 F")
    print(" AC/comfort cooling")
    print(" 35-40F storage = HIGH!")
    print("MEDIUM TEMP: 0-32 F")
    print(" Food/dairy/walk-ins")
    print("LOW TEMP: below 0 F")
    print(" Ice/deep freeze")
    pause()

# ================================
# PSYCHROMETRICS (paginated)
# ================================
def ref_psychro():
    print("\n--- PSYCHRO (1/2) ---")
    print("DB = dry bulb temp")
    print("WB = wet bulb temp")
    print("DP = dew point temp")
    print("DB > WB > DP always")
    print("RH=(actual/max)x100")
    pause()
    print("\n--- PSYCHRO (2/2) ---")
    print("Enthalpy (h):")
    print("h=0.240xDB+")
    print(" W(1061+0.444xDB)")
    print("W=humidity ratio lb/lb")
    print("1.Calc Enthalpy  2.Back")
    c=input("Select: ")
    if c=="1":
        try:
            db=float(input("Dry Bulb (F): "))
            w=float(input("Hum.Ratio (lb/lb): "))
            h=0.240*db+w*(1061+0.444*db)
            print("h = %.3f BTU/lb"%h)
            pause()
        except: print("Invalid input.")

# ================================
# ELECTRICAL CALCULATOR (7 lines)
# ================================
def calc_elec():
    while True:
        print("\n--- ELECTRICAL ---")
        print("1. Ohms Law V/I/R")
        print("2. Power W/V/I")
        print("3. 3-Phase Current")
        print("4. Single Phase I")
        print("5. Back")
        c=input("Select (1-5): ")
        if c=="5": break
        try:
            if c=="1":
                print("Enter 2 known (0=unknown)")
                v=float(input("V: "))
                i=float(input("I: "))
                r=float(input("R: "))
                if v==0:   print("V=%.4f V"%(i*r))
                elif i==0: print("I=%.4f A"%(v/r))
                elif r==0: print("R=%.4f ohm"%(v/i))
            elif c=="2":
                print("Enter 2 known (0=unknown)")
                w=float(input("W: "))
                v=float(input("V: "))
                i=float(input("I: "))
                if w==0: print("W=%.4f W"%(v*i))
                elif v==0 and i!=0: print("V=%.4f V"%(w/i))
                elif i==0 and v!=0: print("I=%.4f A"%(w/v))
            elif c=="3":
                w=float(input("Watts: "))
                v=float(input("Volts: "))
                pf=float(input("PF (0.85): "))
                print("I=%.4f A"%(w/(v*1.732*pf)))
            elif c=="4":
                w=float(input("Watts: "))
                v=float(input("Volts: "))
                print("I=%.4f A"%(w/v))
            else: print("Invalid."); continue
            pause()
        except: print("Invalid input.")

# ================================
# PROPERTIES MENU (8 lines)
# ================================
def props_menu():
    while True:
        print("\n--- PROPERTIES ---")
        print("1. Tables (lookup)")
        print("2. Sp.Weight Calc")
        print("3. Density Calc")
        print("4. Sp.Volume Calc")
        print("5. Sp.Gravity Calc")
        print("6. Back")
        c=input("Select (1-6): ")
        if c=="6": break
        elif c=="1": ref_props()
        elif c=="2": calc_sp_weight()
        elif c=="3": calc_density()
        elif c=="4": calc_sp_volume()
        elif c=="5": calc_sp_gravity()
        else: print("Invalid.")

# ================================
# PROPERTIES TABLES (paginated)
# ================================
def ref_props():
    while True:
        print("\n--- PROP TABLES ---")
        print("1.Sp.Weight 2.Sp.Volume")
        print("3.Sp.Gravity 4.Sp.Heat")
        print("5. Back")
        c=input("Select (1-5): ")
        if c=="5": break
        elif c=="1":
            print("\n-- Sp.Weight lb/ft3 --")
            print("Air(70F):   0.075")
            print("Air(32F):   0.081")
            print("Water(60F):62.37")
            print("Ice(32F):  57.5")
            print("Steam(212F):0.0372")
            pause()
            print("\n-- Sp.Weight (cont) --")
            print("R-410A liq:71.4")
            print("R-22 liq:  74.8")
            print("R-134a liq:73.6")
            print("Glycol50/50:66.0")
            pause()
        elif c=="2":
            print("\n-- Sp.Volume ft3/lb --")
            print("Air(70F):  13.33")
            print("Air(32F):  12.39")
            print("Water(60F):0.01604")
            print("Steam(212F):26.8")
            print("R-410A vap:0.65")
            print("R-22 vap:  0.59")
            pause()
        elif c=="3":
            print("\n-- Sp.Gravity water=1 --")
            print("Water:     1.000")
            print("Ice:       0.917")
            print("Glycol50/50:1.059")
            print("R-22 liq:  1.197")
            pause()
            print("\n-- Sp.Gravity (cont) --")
            print("R-410A liq:1.144")
            print("R-134a liq:1.178")
            print("Copper:    8.96")
            print("Steel:     7.85")
            print("Aluminum:  2.70")
            pause()
        elif c=="4":
            print("\n-- Sp.Heat BTU/lb/F --")
            print("Air(dry):  0.240")
            print("Water:     1.000")
            print("Ice:       0.500")
            print("Steam:     0.480")
            print("Glycol50/50:0.850")
            pause()
            print("\n-- Sp.Heat (cont) --")
            print("Copper:    0.092")
            print("Steel:     0.120")
            print("Aluminum:  0.215")
            print("R-22 liq:  0.300")
            print("R-410A liq:0.370")
            pause()
        else: print("Invalid.")

# ================================
# SPECIFIC WEIGHT CALC
# ================================
def calc_sp_weight():
    while True:
        print("\n--- SP.WEIGHT ---")
        print("spW=weight/vol")
        print("spW=density x 32.174")
        print("1.From wt+vol 2.From dens")
        print("3. Back")
        c=input("Select (1-3): ")
        if c=="3": break
        try:
            if c=="1":
                w=float(input("Weight (lb): "))
                v=float(input("Volume (ft3): "))
                sw=w/v
            elif c=="2":
                d=float(input("Density lb-s2/ft4: "))
                sw=d*32.174
            else: print("Invalid."); continue
            print("Sp.Weight=%.4f lb/ft3"%sw)
            print("Density  =%.6f"%(sw/32.174))
            print("Sp.Vol   =%.5f ft3/lb"%(1/sw))
            print("Sp.Grav  =%.4f"%(sw/62.37))
            pause()
        except: print("Invalid input.")

# ================================
# DENSITY CALC
# ================================
def calc_density():
    while True:
        print("\n--- DENSITY ---")
        print("d=mass/vol  d=1/Sp.Vol")
        print("1.Mass+vol  2.Sp.Volume")
        print("3.Sp.Weight 4.Back")
        c=input("Select (1-4): ")
        if c=="4": break
        try:
            if c=="1":
                m=float(input("Mass (lb): "))
                v=float(input("Volume (ft3): "))
                d=m/v
            elif c=="2":
                sv=float(input("Sp.Vol (ft3/lb): "))
                d=1/sv
            elif c=="3":
                sw=float(input("Sp.Wt (lb/ft3): "))
                d=sw/32.174
                print("Density=%.6f lb-s2/ft4"%d)
                print("Sp.Vol =%.5f ft3/lb"%(1/sw))
                print("Sp.Grav=%.4f"%(sw/62.37))
                pause(); continue
            else: print("Invalid."); continue
            print("Density=%.5f lb/ft3"%d)
            print("Sp.Vol =%.5f ft3/lb"%(1/d))
            print("Sp.Grav=%.4f"%(d/62.37))
            pause()
        except: print("Invalid input.")

# ================================
# SPECIFIC VOLUME CALC
# ================================
def calc_sp_volume():
    while True:
        print("\n--- SP.VOLUME ---")
        print("spV=vol/mass  spV=1/dens")
        print("1.Vol+mass  2.Density")
        print("3.Sp.Weight 4.Back")
        c=input("Select (1-4): ")
        if c=="4": break
        try:
            if c=="1":
                v=float(input("Volume (ft3): "))
                m=float(input("Mass (lb): "))
                sv=v/m
            elif c=="2":
                d=float(input("Density (lb/ft3): "))
                sv=1/d
            elif c=="3":
                sw=float(input("Sp.Wt (lb/ft3): "))
                sv=1/sw
                print("Sp.Vol =%.5f ft3/lb"%sv)
                print("Density=%.6f"%(sw/32.174))
                print("Sp.Grav=%.4f"%(sw/62.37))
                pause(); continue
            else: print("Invalid."); continue
            print("Sp.Vol =%.5f ft3/lb"%sv)
            print("Density=%.5f lb/ft3"%(1/sv))
            print("Sp.Grav=%.4f"%(1/sv/62.37))
            pause()
        except: print("Invalid input.")

# ================================
# SPECIFIC GRAVITY CALC
# ================================
def calc_sp_gravity():
    while True:
        print("\n--- SP.GRAVITY ---")
        print("SG=density/62.37")
        print("1.Density  2.Sp.Weight")
        print("3.Mass+vol 4.Back")
        c=input("Select (1-4): ")
        if c=="4": break
        try:
            if c=="1":
                d=float(input("Density (lb/ft3): "))
                sg=d/62.37
                print("Sp.Grav=%.4f"%sg)
                print("Sp.Vol =%.5f ft3/lb"%(1/d))
            elif c=="2":
                sw=float(input("Sp.Wt (lb/ft3): "))
                print("Sp.Grav=%.4f"%(sw/62.37))
            elif c=="3":
                m=float(input("Mass (lb): "))
                v=float(input("Volume (ft3): "))
                d=m/v
                print("Density=%.4f lb/ft3"%d)
                print("Sp.Grav=%.4f"%(d/62.37))
            else: print("Invalid."); continue
            pause()
        except: print("Invalid input.")

# ================================
# BRAZING / TUBING REF (paginated)
# ================================
def ref_braze():
    while True:
        print("\n--- BRAZING/TUBING ---")
        print("1.Solder/Braze Rods")
        print("2.Copper Tubing Types")
        print("3.ACR Tubing Sizes")
        print("4.Flux Rules")
        print("5. Back")
        c=input("Select (1-5): ")
        if c=="5": break
        elif c=="1":
            print("\n-- Rods (1/2) --")
            print("95/5 SnAntimony:")
            print(" Melt:452F Flow:464F")
            print(" Water lines ONLY")
            print("BCuP-2 (0%Ag):")
            print(" 1310F/1460F Cu-Cu")
            print("BCuP-3 (5%Ag):")
            print(" 1190F/1480F Cu-Cu")
            pause()
            print("\n-- Rods (2/2) --")
            print("Stay-Silv15 (15%Ag):")
            print(" 1190F/1480F Cu-Cu")
            print("BAg-1a (45%Ag):")
            print(" 1125F/1145F FLUX REQ")
            print("BAg-7 (56%Ag):")
            print(" 1145F/1205F FLUX REQ")
            print("Common filler=15-45%Ag")
            pause()
        elif c=="2":
            print("\n-- Copper Tubing --")
            print("Type K: GREEN")
            print(" Thickest/underground")
            print("Type L: BLUE")
            print(" Medium/HVAC/plumbing")
            print("Type M: RED")
            print(" Thin/light plumbing")
            print("ACR: BLUE cap")
            print(" Sized by OD not ID!")
            pause()
        elif c=="3":
            print("\n-- ACR Sizes (OD) --")
            print("1/4  = capillary")
            print("3/8  = small systems")
            print("1/2  = suction/liquid")
            print("5/8  = med suction")
            print("3/4  = larger suction")
            print("7/8  = comm. suction")
            print("1-1/8= large comm.")
            pause()
        elif c=="4":
            print("\n-- Flux Rules --")
            print("BCuP: no flux on Cu")
            print("BAg:  ALWAYS need flux")
            print("Flux = prevents oxidation")
            print("N2 PURGE:")
            print(" ALWAYS when brazing")
            print(" refrig lines!")
            print(" Rate: 1-3 CFH")
            pause()
        else: print("Invalid.")

# ================================
# GAS LAWS CALCULATOR
# ================================
def calc_gas_laws():
    while True:
        print("\n--- GAS LAWS ---")
        print("1.Boyles   2.Charles")
        print("3.Gay-Lussac")
        print("4.Combined/General")
        print("5.Ideal    6.Daltons")
        print("7. Back")
        c=input("Select (1-7): ")
        if c=="7": break
        try:
            if c=="1":
                print("P1V1=P2V2 (T constant)")
                print("PSIA, Enter 0=unknown")
                p1=float(input("P1: "))
                v1=float(input("V1: "))
                p2=float(input("P2: "))
                v2=float(input("V2: "))
                if v2==0:   print("V2=%.5f"%(p1*v1/p2))
                elif p2==0: print("P2=%.5f psia"%(p1*v1/v2))
                elif v1==0: print("V1=%.5f"%(p2*v2/p1))
                elif p1==0: print("P1=%.5f psia"%(p2*v2/v1))
            elif c=="2":
                print("V1/T1=V2/T2 (P constant)")
                print("Rankine=F+459.67")
                print("Expands w/heat!")
                print("Enter 0=unknown")
                v1=float(input("V1: "))
                t1=float(input("T1 (R): "))
                v2=float(input("V2: "))
                t2=float(input("T2 (R): "))
                if v2==0:   print("V2=%.5f"%(v1*t2/t1))
                elif t2==0:
                    r=v2*t1/v1
                    print("T2=%.2fR/%.2fF"%(r,r-459.67))
                elif v1==0: print("V1=%.5f"%(v2*t1/t2))
                elif t1==0:
                    r=v1*t2/v2
                    print("T1=%.2fR/%.2fF"%(r,r-459.67))
            elif c=="3":
                print("P1/T1=P2/T2 (V constant)")
                print("Rankine=F+459.67")
                print("Enter 0=unknown")
                p1=float(input("P1 (psia): "))
                t1=float(input("T1 (R): "))
                p2=float(input("P2 (psia): "))
                t2=float(input("T2 (R): "))
                if p2==0:   print("P2=%.5f psia"%(p1*t2/t1))
                elif t2==0:
                    r=p2*t1/p1
                    print("T2=%.2fR/%.2fF"%(r,r-459.67))
                elif p1==0: print("P1=%.5f psia"%(p2*t1/t2))
                elif t1==0:
                    r=p1*t2/p2
                    print("T1=%.2fR/%.2fF"%(r,r-459.67))
            elif c=="4":
                print("P1V1/T1=P2V2/T2")
                print("Rankine=F+459.67")
                print("PSIA=psig+14.696")
                print("Enter 0=unknown")
                p1=float(input("P1 (psia): "))
                v1=float(input("V1: "))
                t1=float(input("T1 (R): "))
                p2=float(input("P2 (psia): "))
                v2=float(input("V2: "))
                t2=float(input("T2 (R): "))
                if t2==0:
                    r=p2*v2*t1/(p1*v1)
                    print("T2=%.2fR/%.2fF"%(r,r-459.67))
                elif v2==0: print("V2=%.5f"%(p1*v1*t2/(t1*p2)))
                elif p2==0:
                    r=p1*v1*t2/(t1*v2)
                    print("P2=%.4fpsia/%.4fpsig"%(r,r-14.696))
                elif t1==0:
                    r=p1*v1*t2/(p2*v2)
                    print("T1=%.2fR/%.2fF"%(r,r-459.67))
                elif v1==0: print("V1=%.5f"%(p2*v2*t1/(t2*p1)))
                elif p1==0:
                    r=p2*v2*t1/(t2*v1)
                    print("P1=%.4fpsia/%.4fpsig"%(r,r-14.696))
            elif c=="5":
                print("PV=nRT")
                print("R=10.7316 psia-ft3/lbmolR")
                print("Rankine=F+459.67")
                print("Enter 0=unknown")
                R=10.7316
                p=float(input("P (psia): "))
                v=float(input("V (ft3): "))
                n=float(input("n (lbmol): "))
                t=float(input("T (R): "))
                if p==0:   print("P=%.5f psia"%(n*R*t/v))
                elif v==0: print("V=%.5f ft3"%(n*R*t/p))
                elif n==0: print("n=%.6f lbmol"%(p*v/(R*t)))
                elif t==0:
                    r=p*v/(n*R)
                    print("T=%.2fR/%.2fF"%(r,r-459.67))
            elif c=="6":
                print("Ptotal=Pa+Pb+Pc...")
                ng=int(input("Number of gases (2-4): "))
                pt=0
                for i in range(ng):
                    pt+=float(input("P%d (psia): "%(i+1)))
                print("Total=%.4f psia"%pt)
                print("     =%.4f psig"%(pt-14.696))
                print("     =%.3f kPa"%(pt*6.89476))
            else: print("Invalid."); continue
            pause()
        except: print("Invalid input.")

# Run the app
main_menu()
