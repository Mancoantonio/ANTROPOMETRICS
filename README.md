Health & Anthropometric Measurements (Script)
This is a script written in Python that calculates basic anthropometric measurements and allows a simple monitoring of health using only a MEASURING TAPE(cm) and a SCALE(kg)

Actual Functions

1.- BMI (Body Mass Index) 
  -Converts kg and cm automatically.
  -Returns exact classification according to WHO (World Health Organization).
2.- WHR (Waist Hip Relation)
  -Requires GENDER.
  -Returns level of risk classification according to international tables.
3.- WHtR (Waist Height Relation)
  -Does not require GENDER data.
  -Automatically classifies risk of health.

Future Updates(ROADMAP):
- CI (Conicity Index)
  Formula = WAIST/(1.109 x √(WEIGHT/HEIGHT)
- V-Taper Index.
- Possible graphics interface.
- CUN/BAE Index for calculating FAT PERCENTAGE. Requires AGE data.

Requirements:
-Python 3 or superior(for code)
-Windows 10 or 11 (for .exe)
-Metric Tape
-Scale

Use:
1.- Either run .exe file or
  -Clone repository from GitHub, access proyect directory and execute file imc.py
2.- Input this data:
  -WEIGHT (kg)
  -HEIGHT (m)
  -WAIST PERIMETER (cm)
  -HIP PERIMETER (cm)
  -GENDER(M/F)

  Output example:

  -Your BMI is 24.3 -> Classification is normal (WHO)
  - Your WHR is 0.82 -> Classification is at risk of overweight according to women's tables 
  - Your WHtR is 0.47 -> Classification is Healthy

IMPORTANT - DISCLAIMER

This script is ONLY educational and informative. In no way replaces medical evaluation or further professional diagnosis.
