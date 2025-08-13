import msvcrt

def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc


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
        if rcc < 0.90:
            return "RCC saludable para hombres"
        else:
            return "RCC elevada para hombres, riesgos de salud asociados"
    elif sexo == "f":
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
    
def main():
    
    print("Necesitas una BALANZA o PESA y una HUINCHA PARA MEDIR CENTÍMETROS, en este programa vamos a calcular medidas antropométricas básicas: ")
    peso = float(input("Ingresa tu peso en kilogramos (con un decimal): "))
    altura = float(input("Ingresa tu altura en metros: "))
    altura_cm = altura * 100

    imc = calcular_imc(peso, altura)
    print(f"Tu IMC es: {imc:.2f}")


    print(f"CLasificación OMS: {clasificacion_oms(imc)}")

    print("Bien ahora a calcular tu relación cintura/cadera.")
    sexo = input("Antes de eso, ingresa tu sexo, escribe M para masculino o F para femenino: ").lower()
    cadera_cm = float(input("Ingresa tu perímetro de cadera en cm: "))
    cintura_cm = float(input("Ingresa tu perímetro de cintura en cm: "))
    rcc = cintura_cm/cadera_cm
    rca = cintura_cm/altura_cm

    print(f"Tu relación cintura altura o RCA es: {rca:.2f}")
    print(f"Tu relación cintura cadera o RCC es: {rcc:.2f}")



    print(f"Clasificación de Relación Cintura Cadera: {clasificacion_rcc(rcc, sexo)}")
    print(f"Clasificación de Relación Cintura Altura: {clasificacion_rca(rca, cintura_cm, altura_cm)}")


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