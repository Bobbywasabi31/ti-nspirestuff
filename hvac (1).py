# HVAC Toolkit for TI-Nspire CX II CAS
# Unit Converter + Formula Reference
# Compatible with TI-Nspire Python

def pause():
    input("Press Enter to continue...")

def main_menu():
    while True:
        print("\n=== HVAC TOOLKIT ===")
        print("1. Unit Converter")
        print("2. Formula Reference")
        print("3. Quit")
        choice = input("Select (1-3): ")
        if choice == "1":
            unit_menu()
        elif choice == "2":
            formula_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

# ================================
# UNIT CONVERTER MENU
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
        choice = input("Select (1-7): ")
        if choice == "1":
            temp_conv()
        elif choice == "2":
            pres_conv()
        elif choice == "3":
            air_conv()
        elif choice == "4":
            power_conv()
        elif choice == "5":
            length_conv()
        elif choice == "6":
            area_conv()
        elif choice == "7":
            break
        else:
            print("Invalid choice.")

# ================================
# TEMPERATURE CONVERTER
# ================================
def temp_conv():
    while True:
        print("\n--- TEMPERATURE ---")
        print("1. F to C")
        print("2. C to F")
        print("3. F to K")
        print("4. C to K")
        print("5. K to F")
        print("6. K to C")
        print("7. Back")
        choice = input("Select (1-7): ")
        if choice == "7":
            break
        try:
            v = float(input("Enter value: "))
            if choice == "1":
                r = (v-32)*5/9
                print("%.4f C" % r)
            elif choice == "2":
                r = v*9/5+32
                print("%.4f F" % r)
            elif choice == "3":
                r = (v-32)*5/9+273.15
                print("%.4f K" % r)
            elif choice == "4":
                r = v+273.15
                print("%.4f K" % r)
            elif choice == "5":
                r = (v-273.15)*9/5+32
                print("%.4f F" % r)
            elif choice == "6":
                r = v-273.15
                print("%.4f C" % r)
            else:
                print("Invalid choice.")
                continue
            pause()
        except:
            print("Invalid input.")

# ================================
# PRESSURE CONVERTER
# ================================
def pres_conv():
    units = ["PSIG","PSIA","kPa-g","kPa-a",
             "inHg","inH2O","bar"]
    to_kpa = [6.89476,6.89476,1.0,1.0,
              3.38639,0.24908,100.0]
    atm_kpa = 101.325
    is_abs = [False,True,False,True,
              False,False,False]
    while True:
        print("\n--- PRESSURE ---")
        for i,u in enumerate(units):
            print("%d. %s" % (i+1, u))
        print("8. Back")
        c1 = input("From: ")
        if c1 == "8":
            break
        c2 = input("To: ")
        if c2 == "8":
            break
        try:
            f = int(c1)-1
            t = int(c2)-1
            v = float(input("Value: "))
            kpa = v * to_kpa[f]
            if is_abs[f]:
                kpa = kpa - atm_kpa
            r = kpa / to_kpa[t]
            if is_abs[t]:
                r = r + (atm_kpa/to_kpa[t])
            print("%.5f %s" % (r, units[t]))
            pause()
        except:
            print("Invalid input.")

# ================================
# AIRFLOW CONVERTER
# ================================
def air_conv():
    units = ["CFM","m3/h","L/s"]
    to_cfm = [1.0, 0.58858, 2.11888]
    while True:
        print("\n--- AIRFLOW ---")
        for i,u in enumerate(units):
            print("%d. %s" % (i+1, u))
        print("4. Back")
        c1 = input("From: ")
        if c1 == "4":
            break
        c2 = input("To: ")
        if c2 == "4":
            break
        try:
            f = int(c1)-1
            t = int(c2)-1
            v = float(input("Value: "))
            cfm = v * to_cfm[f]
            r = cfm / to_cfm[t]
            print("%.4f %s" % (r, units[t]))
            pause()
        except:
            print("Invalid input.")

# ================================
# POWER / COOLING CONVERTER
# ================================
def power_conv():
    units = ["BTU/hr","Tons","kW","Watts"]
    to_btu = [1.0, 12000.0, 3412.14, 3.41214]
    while True:
        print("\n--- POWER/COOLING ---")
        for i,u in enumerate(units):
            print("%d. %s" % (i+1, u))
        print("5. Back")
        c1 = input("From: ")
        if c1 == "5":
            break
        c2 = input("To: ")
        if c2 == "5":
            break
        try:
            f = int(c1)-1
            t = int(c2)-1
            v = float(input("Value: "))
            btu = v * to_btu[f]
            r = btu / to_btu[t]
            print("%.4f %s" % (r, units[t]))
            pause()
        except:
            print("Invalid input.")

# ================================
# LENGTH CONVERTER
# ================================
def length_conv():
    units = ["Feet","Inches","Meters","cm"]
    to_ft = [1.0, 0.08333, 3.28084, 0.0328084]
    while True:
        print("\n--- LENGTH ---")
        for i,u in enumerate(units):
            print("%d. %s" % (i+1, u))
        print("5. Back")
        c1 = input("From: ")
        if c1 == "5":
            break
        c2 = input("To: ")
        if c2 == "5":
            break
        try:
            f = int(c1)-1
            t = int(c2)-1
            v = float(input("Value: "))
            ft = v * to_ft[f]
            r = ft / to_ft[t]
            print("%.5f %s" % (r, units[t]))
            pause()
        except:
            print("Invalid input.")

# ================================
# AREA CONVERTER
# ================================
def area_conv():
    units = ["ft2","in2","m2","cm2"]
    to_ft2 = [1.0, 0.006944, 10.7639, 0.00107639]
    while True:
        print("\n--- AREA ---")
        for i,u in enumerate(units):
            print("%d. %s" % (i+1, u))
        print("5. Back")
        c1 = input("From: ")
        if c1 == "5":
            break
        c2 = input("To: ")
        if c2 == "5":
            break
        try:
            f = int(c1)-1
            t = int(c2)-1
            v = float(input("Value: "))
            ft2 = v * to_ft2[f]
            r = ft2 / to_ft2[t]
            print("%.6f %s" % (r, units[t]))
            pause()
        except:
            print("Invalid input.")

# ================================
# FORMULA REFERENCE MENU
# ================================
def formula_menu():
    while True:
        print("\n=== FORMULA REFERENCE ===")
        print("1. Heat Load")
        print("2. Efficiency (EER/COP)")
        print("3. Duct Velocity")
        print("4. Refrigeration Cycle")
        print("5. Psychrometrics")
        print("6. Electrical")
        print("7. Properties Tables")
        print("8. Brazing/Tubing")
        print("9. Specific Weight")
        print("10. Density")
        print("11. Specific Volume")
        print("12. Gas Laws")
        print("13. Back")
        choice = input("Select (1-13): ")
        if choice == "1":
            calc_heat()
        elif choice == "2":
            calc_eer()
        elif choice == "3":
            calc_duct()
        elif choice == "4":
            ref_refrig()
        elif choice == "5":
            ref_psychro()
        elif choice == "6":
            calc_elec()
        elif choice == "7":
            ref_props()
        elif choice == "8":
            ref_braze()
        elif choice == "9":
            calc_sp_weight()
        elif choice == "10":
            calc_density()
        elif choice == "11":
            calc_sp_volume()
        elif choice == "12":
            calc_gas_laws()
        elif choice == "13":
            break
        else:
            print("Invalid choice.")

# ================================
# HEAT LOAD CALCULATOR
# ================================
def calc_heat():
    while True:
        print("\n--- HEAT LOAD ---")
        print("1. Sensible: Q=1.08xCFMxdT")
        print("2. Total:    Q=4.5xCFMxdh")
        print("3. Latent:   Q=0.68xCFMxdW")
        print("4. BTU to Tons")
        print("5. Back")
        choice = input("Select (1-5): ")
        if choice == "5":
            break
        try:
            if choice == "1":
                cfm = float(input("CFM: "))
                dt = float(input("dT (F): "))
                q = 1.08 * cfm * dt
                print("Q = %.1f BTU/hr" % q)
                print("  = %.4f Tons" % (q/12000))
                print("  = %.3f kW" % (q/3412.14))
            elif choice == "2":
                cfm = float(input("CFM: "))
                dh = float(input("dh (BTU/lb): "))
                q = 4.5 * cfm * dh
                print("Q = %.1f BTU/hr" % q)
                print("  = %.4f Tons" % (q/12000))
                print("  = %.3f kW" % (q/3412.14))
            elif choice == "3":
                cfm = float(input("CFM: "))
                dw = float(input("dW (gr/lb): "))
                q = 0.68 * cfm * dw
                print("Q = %.1f BTU/hr" % q)
                print("  = %.4f Tons" % (q/12000))
            elif choice == "4":
                btu = float(input("BTU/hr: "))
                print("%.4f Tons" % (btu/12000))
                print("%.3f kW" % (btu/3412.14))
            else:
                print("Invalid choice.")
                continue
            pause()
        except:
            print("Invalid input.")

# ================================
# EER / COP CALCULATOR
# ================================
def calc_eer():
    while True:
        print("\n--- EFFICIENCY ---")
        print("1. EER (BTU/hr / Watts)")
        print("2. COP (Qout / Win)")
        print("3. Back")
        choice = input("Select (1-3): ")
        if choice == "3":
            break
        try:
            if choice == "1":
                btu = float(input("BTU/hr: "))
                w = float(input("Watts: "))
                eer = btu / w
                print("EER  = %.2f" % eer)
                print("SEER~= %.2f (est)" % (eer*1.1))
                print("COP  = %.2f" % (eer/3.412))
            elif choice == "2":
                qout = float(input("Output (kW): "))
                win = float(input("Input (kW): "))
                cop = qout / win
                print("COP  = %.3f" % cop)
                print("EER~ = %.2f" % (cop*3.412))
            else:
                print("Invalid choice.")
                continue
            pause()
        except:
            print("Invalid input.")

# ================================
# DUCT VELOCITY CALCULATOR
# ================================
def calc_duct():
    import math
    while True:
        print("\n--- DUCT VELOCITY ---")
        print("Supply:  600-900 FPM")
        print("Return:  600-700 FPM")
        print("Mains: 1000-1800 FPM")
        print("1. Round duct")
        print("2. Rectangular duct")
        print("3. Back")
        choice = input("Select (1-3): ")
        if choice == "3":
            break
        try:
            cfm = float(input("CFM: "))
            if choice == "1":
                d = float(input("Diameter (in): "))
                area = math.pi * (d/24)**2
            elif choice == "2":
                w = float(input("Width (in): "))
                h = float(input("Height (in): "))
                area = w * h / 144
            else:
                print("Invalid choice.")
                continue
            vel = cfm / area
            print("Area = %.4f ft2" % area)
            print("Vel  = %.1f FPM" % vel)
            if vel < 400:
                print("WARNING: Very low!")
            elif vel < 600:
                print("Low - check design")
            elif vel < 900:
                print("OK for supply/return")
            elif vel < 1800:
                print("OK for main duct")
            else:
                print("HIGH - upsize duct!")
            pause()
        except:
            print("Invalid input.")

# ================================
# REFRIGERATION REFERENCE
# ================================
def ref_refrig():
    print("\n--- REFRIGERATION CYCLE ---")
    print("4 Components:")
    print(" 1.Compressor")
    print(" 2.Condenser")
    print(" 3.Metering Device")
    print(" 4.Evaporator")
    print("")
    print("States:")
    print(" CompIN:  low P vapor")
    print(" CompOUT: high P vapor")
    print(" CondOUT: high P liquid")
    print(" EvapIN:  low P liquid")
    print(" EvapOUT: low P vapor")
    print("")
    print("Superheat=ActTemp-SatTemp")
    print("Subcool=SatTemp-ActTemp")
    pause()

# ================================
# PSYCHROMETRICS REFERENCE
# ================================
def ref_psychro():
    print("\n--- PSYCHROMETRICS ---")
    print("DB = dry bulb temp")
    print("WB = wet bulb temp")
    print("DP = dew point temp")
    print("DB > WB > DP always")
    print("")
    print("RH=(actual/max)x100")
    print("")
    print("Enthalpy (h):")
    print("h=0.240xDB+")
    print(" W(1061+0.444xDB)")
    print("W=humidity ratio(lb/lb)")
    print("")
    print("1. Calculate Enthalpy")
    print("2. Back")
    choice = input("Select: ")
    if choice == "1":
        try:
            db = float(input("Dry Bulb Temp (F): "))
            w = float(input("Humidity Ratio (lb/lb): "))
            h = 0.240*db + w*(1061+0.444*db)
            print("h = %.3f BTU/lb" % h)
            pause()
        except:
            print("Invalid input.")

# ================================
# ELECTRICAL CALCULATOR
# ================================
def calc_elec():
    while True:
        print("\n--- ELECTRICAL ---")
        print("1. Ohms Law (V,I,R)")
        print("2. Power (W,V,I)")
        print("3. 3-Phase Current")
        print("4. Single Phase Current")
        print("5. Back")
        choice = input("Select (1-5): ")
        if choice == "5":
            break
        try:
            if choice == "1":
                print("Enter 2 known values")
                print("(leave unknown as 0)")
                v = float(input("V (volts): "))
                i = float(input("I (amps): "))
                r = float(input("R (ohms): "))
                if v == 0:
                    print("V = %.4f V" % (i*r))
                elif i == 0:
                    print("I = %.4f A" % (v/r))
                elif r == 0:
                    print("R = %.4f ohm" % (v/i))
            elif choice == "2":
                print("Enter 2 known values")
                print("(leave unknown as 0)")
                w = float(input("W (watts): "))
                v = float(input("V (volts): "))
                i = float(input("I (amps): "))
                if w == 0:
                    print("W = %.4f W" % (v*i))
                elif v == 0 and i != 0:
                    print("V = %.4f V" % (w/i))
                elif i == 0 and v != 0:
                    print("I = %.4f A" % (w/v))
            elif choice == "3":
                w = float(input("Watts: "))
                v = float(input("Volts: "))
                pf = float(input("PF (0.85 typical): "))
                i = w / (v * 1.732 * pf)
                print("I = %.4f A" % i)
                print("1.732 = sqrt(3)")
            elif choice == "4":
                w = float(input("Watts: "))
                v = float(input("Volts: "))
                i = w / v
                print("I = %.4f A" % i)
            else:
                print("Invalid choice.")
                continue
            pause()
        except:
            print("Invalid input.")

# ================================
# PROPERTIES REFERENCE
# ================================
def ref_props():
    while True:
        print("\n--- PROPERTIES ---")
        print("1. Specific Weight")
        print("2. Specific Volume")
        print("3. Specific Gravity")
        print("4. Specific Heat")
        print("5. Back")
        choice = input("Select (1-5): ")
        if choice == "5":
            break
        elif choice == "1":
            print("\n-- Sp.Weight (lb/ft3) --")
            print("Air(70F):    0.075")
            print("Air(32F):    0.081")
            print("Water(60F): 62.37")
            print("Ice(32F):   57.5")
            print("Steam(212F): 0.0372")
            print("R-410A liq: 71.4")
            print("R-22 liq:   74.8")
            print("R-134a liq: 73.6")
            print("Glycol50/50:66.0")
            pause()
        elif choice == "2":
            print("\n-- Sp.Volume (ft3/lb) --")
            print("Air(70F):   13.33")
            print("Air(32F):   12.39")
            print("Water(60F): 0.01604")
            print("Steam(212F):26.8")
            print("R-410A vap: 0.65")
            print("R-22 vap:   0.59")
            pause()
        elif choice == "3":
            print("\n-- Sp.Gravity (water=1) --")
            print("Water:      1.000")
            print("Ice:        0.917")
            print("Glycol50/50:1.059")
            print("R-22 liq:   1.197")
            print("R-410A liq: 1.144")
            print("R-134a liq: 1.178")
            print("Copper:     8.96")
            print("Steel:      7.85")
            print("Aluminum:   2.70")
            pause()
        elif choice == "4":
            print("\n-- Sp.Heat (BTU/lb/F) --")
            print("Air(dry):   0.240")
            print("Water:      1.000")
            print("Ice:        0.500")
            print("Steam:      0.480")
            print("Glycol50/50:0.850")
            print("Copper:     0.092")
            print("Steel:      0.120")
            print("Aluminum:   0.215")
            print("R-22 liq:   0.300")
            print("R-410A liq: 0.370")
            pause()
        else:
            print("Invalid choice.")

# ================================
# BRAZING / TUBING REFERENCE
# ================================
def ref_braze():
    while True:
        print("\n--- BRAZING/TUBING ---")
        print("1. Solder/Braze Rods")
        print("2. Copper Tubing Types")
        print("3. ACR Tubing Sizes")
        print("4. Flux Rules")
        print("5. Back")
        choice = input("Select (1-5): ")
        if choice == "5":
            break
        elif choice == "1":
            print("\n-- Rods --")
            print("95/5 SnAntimony:")
            print(" Melt:452F Flow:464F")
            print(" Water lines only")
            print("BCuP-2 (0% Ag):")
            print(" Melt:1310F Flow:1460F")
            print(" Cu-Cu only, no flux")
            print("BCuP-3 (5% Ag):")
            print(" Melt:1190F Flow:1480F")
            print(" Cu-Cu only, no flux")
            print("Stay-Silv15 (15%Ag):")
            print(" Melt:1190F Flow:1480F")
            print(" Cu-Cu only, no flux")
            print("BAg-1a (45% Ag):")
            print(" Sol:1125F Liq:1145F")
            print(" Cu-brass/steel, FLUX")
            print("BAg-7 (56% Ag):")
            print(" Sol:1145F Liq:1205F")
            print(" Cu-brass/steel, FLUX")
            pause()
        elif choice == "2":
            print("\n-- Copper Tubing --")
            print("Type K: GREEN")
            print(" Thickest wall")
            print(" Underground/medical")
            print("Type L: BLUE")
            print(" Medium wall")
            print(" HVAC/plumbing")
            print("Type M: RED")
            print(" Thin wall")
            print(" Light plumbing only")
            print("ACR: BLUE cap")
            print(" Cleaned for refrig.")
            print(" Sized by OD not ID")
            pause()
        elif choice == "3":
            print("\n-- ACR Sizes (OD) --")
            print("1/4  = capillary")
            print("3/8  = small systems")
            print("1/2  = suction/liquid")
            print("5/8  = med suction")
            print("3/4  = larger suction")
            print("7/8  = comm. suction")
            print("1-1/8= large comm.")
            pause()
        elif choice == "4":
            print("\n-- Flux Rules --")
            print("BCuP rods:")
            print(" No flux on copper")
            print(" Need flux on brass")
            print("BAg rods:")
            print(" ALWAYS need flux")
            print("")
            print("NITROGEN PURGE:")
            print("ALWAYS flow N2 when")
            print("brazing refrig lines!")
            print("Rate: 1-3 CFH (low)")
            pause()
        else:
            print("Invalid choice.")

# ================================
# SPECIFIC WEIGHT CALCULATOR
# ================================
def calc_sp_weight():
    while True:
        print("\n--- SPECIFIC WEIGHT ---")
        print("spW = weight / volume")
        print("spW = density x 32.174")
        print("Unit: lb/ft3")
        print("1. From weight and volume")
        print("2. From density")
        print("3. Back")
        choice = input("Select (1-3): ")
        if choice == "3":
            break
        try:
            if choice == "1":
                w = float(input("Weight (lb): "))
                v = float(input("Volume (ft3): "))
                sw = w / v
                print("Sp.Weight = %.4f lb/ft3" % sw)
                print("Density   = %.6f lb-s2/ft4" % (sw/32.174))
                print("Sp.Volume = %.5f ft3/lb" % (1/sw))
            elif choice == "2":
                d = float(input("Density (lb-s2/ft4): "))
                sw = d * 32.174
                print("Sp.Weight = %.4f lb/ft3" % sw)
                print("Sp.Volume = %.5f ft3/lb" % (1/sw))
            else:
                print("Invalid choice.")
                continue
            pause()
        except:
            print("Invalid input.")

# ================================
# DENSITY CALCULATOR
# ================================
def calc_density():
    while True:
        print("\n--- DENSITY ---")
        print("d = mass / volume")
        print("d = 1 / Sp.Volume")
        print("Unit: lb/ft3")
        print("1. From mass and volume")
        print("2. From specific volume")
        print("3. From specific weight")
        print("4. Back")
        choice = input("Select (1-4): ")
        if choice == "4":
            break
        try:
            if choice == "1":
                m = float(input("Mass (lb): "))
                v = float(input("Volume (ft3): "))
                d = m / v
                print("Density = %.5f lb/ft3" % d)
                print("Sp.Vol  = %.5f ft3/lb" % (1/d))
                print("Sp.Wt   = %.4f lb/ft3" % d)
            elif choice == "2":
                sv = float(input("Sp.Volume (ft3/lb): "))
                d = 1 / sv
                print("Density = %.5f lb/ft3" % d)
                print("Sp.Wt   = %.4f lb/ft3" % d)
            elif choice == "3":
                sw = float(input("Sp.Weight (lb/ft3): "))
                d = sw / 32.174
                print("Density = %.6f lb-s2/ft4" % d)
                print("Sp.Vol  = %.5f ft3/lb" % (1/sw))
            else:
                print("Invalid choice.")
                continue
            pause()
        except:
            print("Invalid input.")

# ================================
# SPECIFIC VOLUME CALCULATOR
# ================================
def calc_sp_volume():
    while True:
        print("\n--- SPECIFIC VOLUME ---")
        print("spV = volume / mass")
        print("spV = 1 / density")
        print("Unit: ft3/lb")
        print("1. From volume and mass")
        print("2. From density")
        print("3. From specific weight")
        print("4. Back")
        choice = input("Select (1-4): ")
        if choice == "4":
            break
        try:
            if choice == "1":
                v = float(input("Volume (ft3): "))
                m = float(input("Mass (lb): "))
                sv = v / m
                print("Sp.Vol  = %.5f ft3/lb" % sv)
                print("Density = %.5f lb/ft3" % (1/sv))
                print("Sp.Wt   = %.4f lb/ft3" % (1/sv))
            elif choice == "2":
                d = float(input("Density (lb/ft3): "))
                sv = 1 / d
                print("Sp.Vol  = %.5f ft3/lb" % sv)
                print("Sp.Wt   = %.4f lb/ft3" % d)
            elif choice == "3":
                sw = float(input("Sp.Weight (lb/ft3): "))
                sv = 1 / sw
                print("Sp.Vol  = %.5f ft3/lb" % sv)
                print("Density = %.6f lb-s2/ft4" % (sw/32.174))
            else:
                print("Invalid choice.")
                continue
            pause()
        except:
            print("Invalid input.")

# ================================
# GAS LAWS CALCULATOR
# ================================
def calc_gas_laws():
    while True:
        print("\n--- GAS LAWS ---")
        print("1. Boyles Law")
        print("2. Charles Law")
        print("3. Gay-Lussacs Law")
        print("4. Combined/General Law")
        print("5. Ideal Gas Law")
        print("6. Daltons Law")
        print("7. Back")
        choice = input("Select (1-7): ")
        if choice == "7":
            break
        try:
            if choice == "1":
                print("\nBoyles Law")
                print("P1V1 = P2V2")
                print("Temp stays constant")
                print("Enter 0 for unknown")
                p1 = float(input("P1 (psia): "))
                v1 = float(input("V1 (ft3): "))
                p2 = float(input("P2 (psia): "))
                v2 = float(input("V2 (ft3): "))
                if v2 == 0:
                    print("V2 = %.5f ft3" % (p1*v1/p2))
                elif p2 == 0:
                    print("P2 = %.5f psia" % (p1*v1/v2))
                elif v1 == 0:
                    print("V1 = %.5f ft3" % (p2*v2/p1))
                elif p1 == 0:
                    print("P1 = %.5f psia" % (p2*v2/v1))
            elif choice == "2":
                print("\nCharles Law")
                print("V1/T1 = V2/T2")
                print("Pressure stays constant")
                print("Temp in Rankine=F+459.67")
                print("Enter 0 for unknown")
                v1 = float(input("V1 (ft3): "))
                t1 = float(input("T1 (Rankine): "))
                v2 = float(input("V2 (ft3): "))
                t2 = float(input("T2 (Rankine): "))
                if v2 == 0:
                    print("V2 = %.5f ft3" % (v1*t2/t1))
                elif t2 == 0:
                    r = v2*t1/v1
                    print("T2 = %.4f R" % r)
                    print("   = %.4f F" % (r-459.67))
                elif v1 == 0:
                    print("V1 = %.5f ft3" % (v2*t1/t2))
                elif t1 == 0:
                    r = v1*t2/v2
                    print("T1 = %.4f R" % r)
                    print("   = %.4f F" % (r-459.67))
            elif choice == "3":
                print("\nGay-Lussacs Law")
                print("P1/T1 = P2/T2")
                print("Volume stays constant")
                print("Temp in Rankine=F+459.67")
                print("Enter 0 for unknown")
                p1 = float(input("P1 (psia): "))
                t1 = float(input("T1 (Rankine): "))
                p2 = float(input("P2 (psia): "))
                t2 = float(input("T2 (Rankine): "))
                if p2 == 0:
                    print("P2 = %.5f psia" % (p1*t2/t1))
                elif t2 == 0:
                    r = p2*t1/p1
                    print("T2 = %.4f R" % r)
                    print("   = %.4f F" % (r-459.67))
                elif p1 == 0:
                    print("P1 = %.5f psia" % (p2*t1/t2))
                elif t1 == 0:
                    r = p1*t2/p2
                    print("T1 = %.4f R" % r)
                    print("   = %.4f F" % (r-459.67))
            elif choice == "4":
                print("\nCombined/General Gas Law")
                print("P1V1/T1 = P2V2/T2")
                print("Temp in Rankine=F+459.67")
                print("Enter 0 for unknown")
                p1 = float(input("P1 (psia): "))
                v1 = float(input("V1 (ft3): "))
                t1 = float(input("T1 (Rankine): "))
                p2 = float(input("P2 (psia): "))
                v2 = float(input("V2 (ft3): "))
                t2 = float(input("T2 (Rankine): "))
                if t2 == 0:
                    r = p2*v2*t1/(p1*v1)
                    print("T2 = %.4f R" % r)
                    print("   = %.4f F" % (r-459.67))
                elif v2 == 0:
                    print("V2 = %.5f ft3" % (p1*v1*t2/(t1*p2)))
                elif p2 == 0:
                    print("P2 = %.5f psia" % (p1*v1*t2/(t1*v2)))
                elif t1 == 0:
                    r = p1*v1*t2/(p2*v2)
                    print("T1 = %.4f R" % r)
                    print("   = %.4f F" % (r-459.67))
                elif v1 == 0:
                    print("V1 = %.5f ft3" % (p2*v2*t1/(t2*p1)))
                elif p1 == 0:
                    print("P1 = %.5f psia" % (p2*v2*t1/(t2*v1)))
            elif choice == "5":
                print("\nIdeal Gas Law")
                print("PV = nRT")
                print("R = 10.7316 psia-ft3/lbmol-R")
                print("T in Rankine = F+459.67")
                print("Enter 0 for unknown")
                R = 10.7316
                p = float(input("P (psia): "))
                v = float(input("V (ft3): "))
                n = float(input("n (lbmol): "))
                t = float(input("T (Rankine): "))
                if p == 0:
                    print("P = %.5f psia" % (n*R*t/v))
                elif v == 0:
                    print("V = %.5f ft3" % (n*R*t/p))
                elif n == 0:
                    print("n = %.6f lbmol" % (p*v/(R*t)))
                elif t == 0:
                    r = p*v/(n*R)
                    print("T = %.4f R" % r)
                    print("  = %.4f F" % (r-459.67))
            elif choice == "6":
                print("\nDaltons Law")
                print("Ptotal=Pa+Pb+Pc...")
                print("Total P = sum of")
                print("partial pressures")
                ng = int(input("Number of gases (2-4): "))
                pt = 0
                for i in range(ng):
                    p = float(input("P%d (psia): " % (i+1)))
                    pt += p
                print("P_total = %.5f psia" % pt)
                print("        = %.5f psig" % (pt-14.696))
                print("        = %.4f kPa-a" % (pt*6.89476))
            else:
                print("Invalid choice.")
                continue
            pause()
        except:
            print("Invalid input.")

# Run the app
main_menu()
