from calculos import obtener_monto_cuenta, obtener_porcentaje, obtener_personas
from calculos import calcular_propina, calcular_total_con_propina, dividir_total, mostrar_resultado

def menu_principal():
    print("""=============================================
  SIMULADOR DE PROPINA
=============================================
1. Calcular propina y total a pagar
2. Calcular total a pagar divido entre varias personas
3. Salir
=============================================""")
    
def menu_opcion1():
    print("=============================================")
    print("  Cálculo de Propina")
    print("=============================================")
    monto_cuenta = obtener_monto_cuenta()
    porcentaje = obtener_porcentaje()
    propina_real = calcular_propina(monto_cuenta, porcentaje)
    pago_con_propina = calcular_total_con_propina(monto_cuenta, propina_real)
    print("=============================================")
    mostrar_resultado(propina_real, pago_con_propina, total_persona = None, num_persona = None)

def menu_opcion2():
    print("=============================================")
    print("    Dividir Cuenta entre Varias Personas")
    print("=============================================")
    monto_cuenta = obtener_monto_cuenta()
    porcentaje = obtener_porcentaje()
    num_personas = obtener_personas()
    propina_real = calcular_propina(monto_cuenta, porcentaje)
    pago_con_propina = calcular_total_con_propina(monto_cuenta, propina_real)
    total_por_persona = dividir_total(pago_con_propina, num_personas)
    print("=============================================")
    mostrar_resultado(propina_real, pago_con_propina, total_por_persona, num_personas)

def menu_opcion3():
    print("=============================================")
    print("¡Gracias por usar el Simulador de Propina!")
    print("=============================================")
        

    
#*CODE MAIN*#

