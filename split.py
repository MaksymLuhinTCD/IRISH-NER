import pandas as pd
import random
df = pd.read_csv("db0102(1).csv")
streets = df['street']
gpe = df['gpe']
county = df['county']
eircode = df['eircode']

string = """
-s-
ICU DAILY PROGRESS NOTE — March 11, 2026
Date: 03-Sep-2025  Time: 01:15
Sinead Kowalski, 27M, Romanian. MRN 22175294.
Address: STREET_LABEL, GPE_LABEL, COUNTY_LABEL, EIRCODE_LABEL.
Admitted 2025-07-18 with severe sepsis.
HR 108, MAP 58 mmHg, Temp 37.1°C, SpO2 30% on FiO2 45%.
Given 500 mL crystalloid; 4 units PRBC transfused.
Blood cultures 1 of 2 positive; 40% of isolates sensitive to piperacillin-tazobactam.
Plan: continue current management, PT/OT review, daily ABG PRN.
Reviewed by Dr. R. Gallagher, ICU consultant at Sligo University Hospital on 27/11/2025 at 18:15.
-s-
RESIDENT NOTE — 18-Dec-2025
Date: April 20, 2026  Time: 13:30
Padraig Singh, 57M, Romanian. MRN 34127884.
Address: STREET_LABEL, GPE_LABEL, COUNTY_LABEL, EIRCODE_LABEL.
Admitted 23-Apr-2025 with DKA.
Severe sepsis, day 9 of ICU admission (fourth episode).
Social work to discuss home oxygen funding, est. €1,200.
Noradrenaline 0.2 mcg/kg/min to keep MAP > 60.
ETT in situ, FiO2 100%, PEEP 12, TV 380 mL. ABG pH 7.21.
HR 129, MAP 91 mmHg, Temp 38.4°C, SpO2 90% on FiO2 92%.
Plan: continue current management, PT/OT review, daily ABG PRN.
Reviewed by Dr. R. Brennan, ICU consultant at Connolly Hospital on 2025-08-26 at 0845 hrs.
-s-
FELLOW NOTE — January 3, 2026
Date: August 22, 2026  Time: 21:30
Padraig Singh, 40M, Polish. MRN 76262352.
Address: STREET_LABEL, GPE_LABEL, COUNTY_LABEL, EIRCODE_LABEL.
Admitted 02/04/2026 with community-acquired pneumonia.
Blood cultures 2 of 2 positive; 94% of isolates sensitive to piperacillin-tazobactam.
Social work to discuss home oxygen funding, est. €4,500.
Noradrenaline 0.2 mcg/kg/min to keep MAP > 60.
HR 113, MAP 90 mmHg, Temp 38.4°C, SpO2 96% on FiO2 92%.
WBC 18.6, Cr 178, lactate 2.4 mmol/L, platelets 82.
Plan: continue current management, PT/OT review, daily ABG PRN.
Reviewed by Dr. S. Byrne, ICU consultant at Cork University Hospital on 22-Apr-2025 at 18:15.
-s-
ATTENDING NOTE — 01-Mar-2026
Date: 2026-10-20  Time: 22:00
David Silva, 90M, Latvian. MRN 63428001.
Address: STREET_LABEL, GPE_LABEL, COUNTY_LABEL, EIRCODE_LABEL.
Admitted 13-Jul-2025 with COPD exacerbation.
Noradrenaline 0.1 mcg/kg/min to keep MAP > 65.
HR 78, MAP 62 mmHg, Temp 38.4°C, SpO2 30% on FiO2 40%.
Plan: continue current management, PT/OT review, daily ABG PRN.
Reviewed by Dr. A. Fitzgerald, ICU consultant at St. James's Hospital on February 18, 2026 at 0215 hrs.
-s-
SOAP NOTE
Date: 2026-11-05  19:30
Patient: Aoife Silva (British), MRN 72544046
Address: STREET_LABEL, GPE_LABEL, COUNTY_LABEL, EIRCODE_LABEL
S: Patient drowsy but rousable, VSS.
O: HR 119, MAP 74 mmHg, Temp 36.2°C, SpO2 45% on FiO2 40%. WBC 14.2, Cr 195, lactate 4.6 mmol/L, platelets 122.
A: Dka, first ICU day.
P: Noradrenaline 0.1 mcg/kg/min to keep MAP > 70. Given 500 mL crystalloid; 2 units PRBC transfused.
Reviewed by Dr. P. Healy, registrar at University Hospital Galway on 2026-09-25 at 0230 hrs.
-s-
ICU HANDOVER NOTE — 06-Jun-2025 1630 hrs
S: Grace Dunne, 43M, bed 8.
B: Admitted 27/07/2025 with acute ischaemic stroke. Home address STREET_LABEL, GPE_LABEL, COUNTY_LABEL, EIRCODE_LABEL.
A: HR 103, MAP 56 mmHg, Temp 36.2°C, SpO2 70% on FiO2 100%.
R: Handed over to Dr. M. O'Connor at Connolly Hospital. Call Dr. M. Lynch PRN.
"""



list_of_notes = string.split("-s-")

for i in list_of_notes:
    index = random.randint(0, 100000)
    print("t")
    while(streets[index] == "" or gpe[index] == "" or county[index] or eircode[index] == ""):
        index = random.randint(0, 100000)
    
    i.replace("STEET_LABEL", streets[index])
    i.replace("GPE_LABEL", gpe[index])
    i.replace("COUNTY_LABEL", county[index])
    i.replace("EIRCODE_LABEL", eircode[index])
    print(i + "\n")