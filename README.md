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



**README Update 1.1**

This tool refines the scope and context of our anthropometric script.  
It is designed primarily for **adult sedentary populations**, since infants and athletes often have unique body compositions that fall outside standard ranges.

---

##  Why BMI Alone Isn’t Enough
While Body Mass Index (BMI) is widely used, it has a major limitation:  

- BMI does **not distinguish** between fat mass and muscle mass.  
- A highly muscular individual may be classified as “obese” by BMI standards, despite having low body fat.  

---

##  Introducing the CUN BAE Index
- **Developed:** 2012, José María Gómez-Ambrosi et al. (Navarra Clinical University, Spain).  
- **Purpose:** Estimates body fat percentage more accurately than BMI.  
- **Limitation:** Still struggles with athletic populations.  

## CSV file generation with relevant information
-**This stores name, height, weight, waist perimeter, hip perimeter, BMI, WHtR and WHR)
-**Stores also TIMESTAMP of consultation, format of date dd.mm.yyy

 **Intended for:** individuals with normal daily habits, especially those at risk of overweight or obesity.  

> Note: Ethnic and cultural factors influence body composition and metabolism, which both BMI and CUN BAE do not fully capture.

---

## Purpose & Audience
Even with its limitations, this tool serves a **secondary purpose**:  
tracking progress and changes in anthropometry over time.  

By combining multiple indices, the script offers a more **holistic view of body composition**—especially useful for **non-athletic users**.

**Target Audience:**  
- Latin American users  
- Spanish-speaking interface  

**Units used:**  
- Height → meters (m)  
- Perimeters → centimeters (cm)  
- Weight → kilograms (kg)  

---

## Upcoming Features
-  English version  
-  Imperial unit support  
-  Visual Interface (GUI or web-based)  
-  TXT file generation for progress tracking 

---

##  Quick Start
```bash
git clone https://github.com/mancoantonio/antromopetrics.git
cd antropometrics
python calculantropometrics.py

