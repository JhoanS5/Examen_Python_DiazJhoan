def obtener_monto_cuenta():
    while True:
        try:
            monto = float(input("Ingrese el monto total de la cuenta: $ "))
            if monto > 0:
                return monto
            elif monto == 0:
                print("El monto no puede ser 0")
            else:
                print(f"El monto no recibe valores negativos. ")
        except ValueError:
            print(f"Error: El valor del monto no esta permitido...")

def obtener_porcentaje():
    while True:
        try:
            porcentaje = float(input("Ingrese el porcentaje de propina (por ejemplo: 15): "))
            if 0 < porcentaje <= 100:
                return porcentaje
            else:
                print(f"El porcentaje que ingresaste esta fuera del rango permitido(1 a 100)")
        except ValueError:
            print(f"Error: El valor del porcentaje no esta permitido...")

def obtener_personas():
    while True:
        try:
            personas = int(input("Ingrese el numero de personas: "))
            if personas > 0:
                return personas
            elif personas == 0:
                print("El numero de personas no puede ser 0")
            else:
                print(f"El numero de personas no puede ser negativo")
        except ValueError:
            print(f"Error: El valor de personas no esta permitido")

def calcular_propina(monto_total, porcentaje):
    porcentaje_decimal = porcentaje / 100
    propina_real = monto_total * porcentaje_decimal
    return propina_real

def calcular_total_con_propina(monto_total, propina_real):
    pago_con_propina = monto_total + propina_real
    return pago_con_propina

def dividir_total(pago_con_propina, num_personas):
    if num_personas:
        total_por_persona = pago_con_propina / num_personas
        return total_por_persona
    return None

def mostrar_resultado(propina, total, total_persona, num_persona):
    print(f"La propina calculada es: ${propina}")
    print(f"El total a pagar es: ${total}")
    if num_persona:
        print(f"Monto por persona: ${total_persona}")


#*CODE MAIN*#
