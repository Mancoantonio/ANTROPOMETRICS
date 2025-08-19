+++ INGLÉS

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

+++ ESPAÑOL

Medidas Antropométricas y Salud (Script)
Este es un script escrito en Python que calcula medidas antropométricas básicas y permite un monitoreo simple de la salud utilizando únicamente una huincha métrica (cm) y una balanza (kg).
⚙️ Funciones Actuales
- IMC (Índice de Masa Corporal)
- Convierte automáticamente kilogramos y centímetros.
- Devuelve la clasificación exacta según la OMS (Organización Mundial de la Salud).
- RCC (Relación Cintura-Cadera)
- Requiere el dato de sexo.
- Devuelve el nivel de riesgo según tablas internacionales.
- RCA (Relación Cintura-Altura)
- No requiere el dato de sexo.
- Clasifica automáticamente el riesgo de salud.

🛣️ Próximas Actualizaciones (ROADMAP)
- Índice de Conicidad (CI)
Fórmula: CINTURA / (1.109 × √(PESO / ALTURA))
- Índice V-Taper
Métrica estética y funcional basada en proporciones corporales.
- Interfaz gráfica (posible GUI o versión web)
- Índice CUN/BAE para calcular el porcentaje de grasa corporal
Requiere el dato de edad.

🧰 Requisitos
- Python 3 o superior (para ejecutar el código)
- Windows 10 u 11 (para usar el archivo .exe)
- Huincha métrica
- Balanza

🚀 Uso
- Ejecuta el archivo .exe
o clona el repositorio desde GitHub, accede al directorio del proyecto y ejecuta el archivo calculantropometrics.py:
git clone https://github.com/mancoantonio/antropometrics.git
cd antropometrics
python calculantropometrics.py


- Ingresa los siguientes datos:
- Peso (kg)
- Altura (m)
- Perímetro de cintura (cm)
- Perímetro de cadera (cm)
- Sexo (M/F)

📋 Ejemplo de salida
- Tu IMC es 24.3 → Clasificación: Normal (OMS)
- Tu RCC es 0.82 → Clasificación: Riesgo de sobrepeso según tablas femeninas
- Tu RCA es 0.47 → Clasificación: Saludable

⚠️ IMPORTANTE - DESCARGO DE RESPONSABILIDAD
Este script es únicamente educativo e informativo.
No reemplaza una evaluación médica ni un diagnóstico profesional.

📘 Actualización README 1.1
Esta herramienta refina el alcance y contexto del script antropométrico.
Está diseñada principalmente para poblaciones adultas sedentarias, ya que infantes y atletas suelen tener composiciones corporales únicas que escapan a los rangos estándar.

❓ ¿Por qué el IMC no es suficiente?
Aunque el IMC es ampliamente utilizado, tiene una gran limitación:
No distingue entre masa muscular y masa grasa.
Una persona muy musculosa puede ser clasificada como “obesa” según el IMC, a pesar de tener poca grasa corporal.

🧠 Introducción al Índice CUN BAE
- Desarrollado en 2012 por José María Gómez-Ambrosi et al. (Universidad Clínica de Navarra, España).
- Propósito: Estimar el porcentaje de grasa corporal con mayor precisión que el IMC.
- Limitación: También presenta dificultades con poblaciones atléticas.

🗂️ Generación de archivo CSV
- Guarda: nombre, altura, peso, perímetro de cintura, perímetro de cadera, IMC, RCA y RCC.
- También guarda la fecha y hora de la consulta en formato dd.mm.yyyy.

🎯 Público objetivo
Individuos con hábitos diarios normales, especialmente aquellos en riesgo de sobrepeso u obesidad.
Se considera que factores étnicos y culturales influyen en la composición corporal y el metabolismo, lo cual ni el IMC ni el CUN BAE capturan completamente.

🎯 Propósito y Audiencia
A pesar de sus limitaciones, esta herramienta cumple una función secundaria:
Monitorear el progreso y los cambios en la antropometría a lo largo del tiempo.
Al combinar múltiples índices, el script ofrece una visión más completa de la composición corporal, especialmente útil para personas no atléticas.

👥 Audiencia objetivo
- Usuarios latinoamericanos
- Interfaz en español
📏 Unidades utilizadas
- Altura → metros (m)
- Perímetros → centímetros (cm)
- Peso → kilogramos (kg)

🔮 Próximas funciones
- Versión en inglés
- Soporte para unidades imperiales
- Interfaz visual (GUI o web)
- Generación de archivo .txt para seguimiento de progreso



##  Quick Start
```bash
git clone https://github.com/mancoantonio/antromopetrics.git
cd antropometrics
python calculantropometrics.py




