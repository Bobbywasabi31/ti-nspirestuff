# HVAC PRO TOOLKIT v5
# Optimized for TI-Nspire & 2026 Standards
# Includes: A2L Support, SH/SC Diagnostics, & Advanced Calcs

import math

# --- DATA & UTILITIES ---
REFRIGERANTS = {
    1: {"name":"R-410A",  "T":[-40,0,40,80,120,160], "P":[16,52,118,246,417,660]},
    2: {"name":"R-22",    "T":[-40,0,40,80,120],     "P":[0.5,25,68,143,260]},
    3: {"name":"R-32",    "T":[-40,0,40,80,120],     "P":[18,56,125,258,435]},
    4: {"name":"R-454B",  "T":[-40,0,40,80,120],     "P":[15,50,114,238,410]},
    5: {"name":"R-134a",  "T":[-40,0,40,80,120],     "P":[-2,14,49,120,248]},
    6: {"name":"R-1234yf","T":[-40,0,40,80,120],     "P":[-4,13,50,122,254]}
}

def pt_interp(t_list, p_list, p_in):
    # Linear interpolation for Saturation Temp
    if p_in <= p_list[0]: return t_list[0]
    if p_in >= p_list[-1]: return t_list[-1]
    for i in range(len(p_list)-1):
        if p_list[i] <= p_in <= p_list[i+1]:
            pct = (p_in - p_list[i]) / (p_list[i+1] - p_list[i])
            return t_list[i] + pct * (t_list[i+1] - t_list[i])

def pause():
    input("\nPress Enter to continue...")

# --- CORE FUNCTIONS ---
def calc_charging():
    print("\n-- SELECT REFRIGERANT --")
    for k, v in REFRIGERANTS.items():
        print("%d. %s" % (k, v['name']))
    
    try:
        r_idx = int(input("Select: "))
        ref = REFRIGERANTS[r_idx]
        
        print("\n1. Superheat (Suction)")
        print("2. Subcooling (Liquid)")
        mode = input("Select: ")
        
        p = float(input("Pressure (psig): "))
        line_t = float(input("Line Temp (F): "))
        sat_t = pt_interp(ref["T"], ref["P"], p)
        
        print("\n--- %s RESULTS ---" % ref["name"])
        print("Sat Temp: %.1f F" % sat_t)
        
        if mode == "1":
            sh = line_t - sat_t
            print("Superheat: %.1f F" % sh)
            if sh < 2: print("!! WARNING: FLOODBACK !!")
            elif 8 <= sh <= 12: print("Status: Optimal (TXV)")
        else:
            sc = sat_t - line_t
            print("Subcooling: %.1f F" % sc)
            if sc < 5: print("Status: Low Charge")
            elif 10 <= sc <= 15: print("Status: Normal")
        pause()
    except:
        print("Input Error.")

def calc_advanced():
    print("\n-- ADVANCED DIAGNOSTICS --")
    print("1. Air Delta T (Split)")
    print("2. Compression Ratio")
    print("3. Target Superheat")
    print("4. CFM via Elec. Heat")
    c = input("Select: ")
    
    try:
        if c == "1":
            ret = float(input("Return Air: "))
            sup = float(input("Supply Air: "))
            print("Delta T: %.1f F" % (ret - sup))
        elif c == "2":
            hi = float(input("Head (PSIA): "))
            lo = float(input("Suction (PSIA): "))
            print("Ratio: %.2f:1" % (hi/lo))
        elif c == "3":
            idwb = float(input("Indoor Wet Bulb: "))
            oddb = float(input("Outdoor Dry Bulb: "))
            target = ((idwb * 3) - oddb - 80) / 2
            print("Target SH: %.1f F" % target)
        elif c == "4":
            v, a = float(input("Volts: ")), float(input("Amps: "))
            dt = float(input("Temp Rise: "))
            cfm = (v * a * 3.413) / (1.08 * dt)
            print("Airflow: %.0f CFM" % cfm)
        pause()
    except:
        print("Calc Error.")

# --- MAIN INTERFACE ---
def main():
    while True:
        print("\n=== HVAC(5) TOOLKIT ===")
        print("1. Charging (SH/SC)")
        print("2. Advanced / Delta T")
        print("3. P-T Quick Lookup")
        print("4. Electrical (Ohm/Watts)")
        print("5. Exit")
        
        cmd = input("Select (1-5): ")
        if cmd == "1": calc_charging()
        elif cmd == "2": calc_advanced()
        elif cmd == "3":
            print("P-T Feature coming in v5.1") # Placeholder for lookup
        elif cmd == "4":
            v = float(input("Volts: "))
            a = float(input("Amps: "))
            print("Watts: %.1f" % (v * a))
            pause()
        elif cmd == "5":
            break

if __name__ == "__main__":
    main()