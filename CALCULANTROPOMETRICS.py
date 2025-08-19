import msvcrt
import math
import csv
from datetime import datetime


def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc

def calcular_cun_bae(cintura_m, sexo, sexo_num, edad, imc):
    cun_bae = - 44.988 + (0.503 * edad) + (10.689 * sexo_num) + (3.172 * imc) - (0.026 * imc**2) + (.181 * imc * sexo_num) - (0.02 * imc * edad) - (0.005 * imc**2 * sexo_num) + (0.00021 * imc**2 * edad)
    return cun_bae

def clasificacion_oms(imc):
    if imc < 18.5:
        return "Bajo Peso"
    if imc < 25:
        return "Normal"
    if imc < 30:
        return "Sobrepeso"
    if imc < 35:
        return "Obesidad grado I (RIESO GARDIOVASCULAR LIGERO)"
    if imc < 40:
        return "Obesidad grado II (RIESGO CARDIOVASCULAR MODERADO)"
    else:
        return "Obesidad grado III (mórbida) (RIESGOS CARDIOVASCULARES SEVEROS)"
    
def clasificacion_rcc(rcc, sexo):
    if sexo == "m":
        sexo_num = 1
        if rcc < 0.90:
            return "RCC saludable para hombres"
        else:
            return "RCC elevada para hombres, riesgos de salud asociados"
    elif sexo == "f":
        sexo_num = 0
        if rcc < 0.85:
            return "RCC saludable para mujeres"
        else:
            return "RCC elevada para mujeres, riesgos de salud asociados"
    else:
        return "Sexo no reconocido. No se puede clasificar RCC."
    
def clasificacion_rca(rca, cintura_cm, altura_cm):
    if rca < 0.40:
        return "RCA muy bajo, posible desnutrición o bajo peso extremo"
    elif rca < 0.50:
        return "RCA Saludable"
    elif rca <= 0.60:
        return "RCA riesgo moderado de sobrepeso"
    elif rca >= 0.61:
        return "RCA de ALTO RIESGO, posible obesidad abdominal"
    
def ind_conicity(ind_con, cintura_m, peso, altura):
    if ind_con < 1:
        return "Delgado o saludable según índice de conicidad"
    elif ind_con < 1.26:
        return "Riesgo de sobrepeso según índice de conicidad"
    else:
        return "Riesgo de obesidad según índice de conicidad"
    
def class_grasa(sexo, resultado_cun_bae):
    if sexo == "m":
            if resultado_cun_bae < 6:
                return "Grasa Esencial"
            elif resultado_cun_bae < 14:
                return "Atleta"
            elif resultado_cun_bae < 18:
                return "Fitness"
            elif resultado_cun_bae < 25:
                return "Promedio Saludable"
            elif resultado_cun_bae < 30:
                return "Obesidad grado 1"
            elif resultado_cun_bae < 35:
                return "Obesidad grado 2"
            else:
                return "OMGbesidad GRADO 3!!"
    elif sexo == "f":
            if resultado_cun_bae < 14:
                return "Grasa Esencial"
            elif resultado_cun_bae < 21:
                return "Atleta"
            elif resultado_cun_bae < 25:
                return "Fitness"
            elif resultado_cun_bae < 32:
                return "Promedio Saludable"
            elif resultado_cun_bae < 38:
                return "Obesidad grado 1"
            elif resultado_cun_bae < 43:
                return "Obesidad grado 2"
            else:
                return "OMGbesidad GRADO 3!!"



    
def main():
    
    print("Necesitas una BALANZA o PESA y una HUINCHA PARA MEDIR CENTÍMETROS, en este programa \n vamos a calcular medidas antropométricas básicas: ")
    nombre = str(input("Primero que todo: ¿Cómo te llamas ?: "))
    peso = float(input(f"{nombre} ingresa tu peso en kilogramos (con un decimal): "))
    altura = float(input(f"{nombre} ingresa tu altura en metros: "))
    altura_cm = altura * 100

    imc = calcular_imc(peso, altura)
    print(f"{nombre}, tu IMC es: {imc:.2f}")


    print(f"CLasificación OMS: {clasificacion_oms(imc)}")

    print(f"Bien, {nombre} ahora a calcular tu relación cintura/cadera.")
    sexo = input(f"Antes de eso, ingresa tu sexo, escribe M para masculino o F para femenino\n Son sólo dos sexos, {nombre}, tienes que decidirte : ").lower()
    cadera_cm = float(input("Ingresa tu perímetro de cadera en cm: "))
    cintura_cm = float(input("Ingresa tu perímetro de cintura en cm: "))
    cintura_m = cintura_cm / 100
    rcc = cintura_cm/cadera_cm
    rca = cintura_cm/altura_cm
    ind_con = cintura_m / (0.109 * math.sqrt(peso / altura))
    sexo_num = 1 if sexo == "m" else 0
    

    print(f"Tu relación cintura altura o RCA es: {rca:.2f}")
    print(f"Tu relación cintura cadera o RCC es: {rcc:.2f}")
    print(f"Tu índice de conicidad es de: {ind_con:.2f}")

    print(f"\n{nombre}, tus CLASIFICACIONES son las siguientes:\n")

    print(f"Clasificación de Relación Cintura Cadera: {clasificacion_rcc(rcc, sexo)}")
    print(f"Clasificación de Relación Cintura Altura: {clasificacion_rca(rca, cintura_cm, altura_cm)}")
    print(f"clasificación según Índice de Conicidad: {ind_conicity(ind_con, cintura_m, peso, altura)}")

    edad = int(input("Por último, vamos a calcular tu PORCENTAJE DE GRASA corporal. Para esto debes ingresar tu edad : "))
    resultado_cun_bae = calcular_cun_bae(cintura_m, sexo, sexo_num, edad, imc)
    print(f"{nombre}, TU PORCENTAJE DE GRASA CORPORAL ES: {resultado_cun_bae:.2f}%")
    print(f"Entonces según esto, {nombre}, tu clasificación de porcentaje de grasa es: {class_grasa(sexo, resultado_cun_bae)}")
    timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    with open("registro_antropometrico.csv", mode="a", newline="") as archivado:
        writer = csv.writer(archivado)
        writer.writerow({timestamp, nombre, peso, altura, altura_cm, cintura_cm, cintura_m, cadera_cm, imc, rcc, rca})

    print("\nPulsa [Enter] para volver a ingresar datos")
    print("Pulsa [Esc] para salir")

    while True:
        tecla = msvcrt.getch()
        if tecla == b'\r':
            print("\nReiniciando... \n")
            main()
            return
    
        elif tecla == b'\x1b':
            print("\nSaliendo, recuerda tomar agua y ejercitarte a diario")
            exit()

main()

