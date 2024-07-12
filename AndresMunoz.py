import csv,os, random,msvcrt,time,statistics

menu_principal = '''
1. Asignar sueldos aleatorios
2. Clasificar sueldos
3. Ver estadísticas.
4. Reporte de sueldos
5. Salir del programa
'''

menu_est = '''
1. Sueldo más alto
2. Sueldo más bajo
3. Promedio de sueldos
4. Media geométrica
'''

trabajadores = ['Juan Pérez', 'María García', 'Carlos López', 'Ana Martínez', 'Pedro Rodríguez', 'Laura Hernández', 'Miguel Sánchez', 'Isabel Gómez', 'Francisco Díaz', 'Elena Fernández']
sueldos_trabajadores = {}
sueldos = []

def sueldos_aleatorios():
    for i in range(len(trabajadores)):
        if trabajadores[i] not in sueldos_trabajadores:
            sueldo = random.randint(300000, 2500000)
            sueldos_trabajadores[trabajadores[i]] = sueldo
            sueldos.append(sueldo)
        else:
            pass
    return


sueldo_bajo = []
sueldo_medio = []
sueldo_mayor = []
        
def ver_estadistica():
    
    while True:
        os.system('cls')
        print(menu_est)
        try:
            eleccion = int(input('> '))
        except ValueError:
            print('Por favor ingresa una de las opcione(1-4).')
            time.sleep(2.0)
            continue
        match eleccion:
            case 1:
                os.system('cls')
                sueldo_mayor.sort()
                print('Sueldo mas alto')
                print(sueldo_mayor[-1])
                return
            case 2:
                os.system('cls')
                sueldo_bajo.sort()
                print('Sueldo mas bajo')
                print(sueldo_bajo[0])
                return
            case 3:
                total = 0
                for sueldo in sueldos:
                    total = total + sueldo
                os.system('cls')
                print(f'Promedio de sueldos: ${round(total/len(sueldos))}')
                return
            case 4:
                os.system('cls')
                print(f'Media geometrica de sueldos: ${round(statistics.geometric_mean(sueldos))}')
                return
            case Default:
                print('Por favor ingrese una de las opciones(1-4).')
                time.sleep(2.5)
                pass

def salir_programa():
    print("Adios")
    
def reporte_sueldo():
    pass

def clasificacion_sueldo(): 
    for valor in sueldos_trabajadores:
        if sueldos_trabajadores[valor] < 800000:
            sueldo_bajo.append(f'Nombre: {valor} | Sueldo: ${sueldos_trabajadores[valor]}')
            continue
        if sueldos_trabajadores[valor] >= 800000 and sueldos_trabajadores[valor] < 2000000:
            sueldo_medio.append(f'Nombre: {valor} | Sueldo: ${sueldos_trabajadores[valor]}')
            continue
        if sueldos_trabajadores[valor] >= 200000:
            sueldo_mayor.append(f'Nombre: {valor} | Sueldo: ${sueldos_trabajadores[valor]}')
            continue
    print('Sueldos menores a $800.000')
    print(f'Total: {len(sueldo_bajo)}')
    for i in sueldo_bajo:
        print(i)
    print('\nSueldos entre $800.000 y $2.000.000')
    print(f'Total: {len(sueldo_medio)}')
    for j in sueldo_medio:
        print(j)
    print('\nSueldos mayores a $2.000.000')
    print(f'Total: {len(sueldo_mayor)}')
    for k in sueldo_mayor:
        print(k)

def menu_principal(): 
    while True:
            os.system('cls')
            print(menu_principal)
            try:
                eleccion_menu = int(input("> "))
            except ValueError:
                print("Por favor ingresa una de las opciones.\n")
                print("Pulsa una tecla para continuar")
                msvcrt.getch()
                continue
            match eleccion_menu:
                case 1:
                    sueldos_aleatorios()
                    continue
                case 2:
                    clasificacion_sueldo()
                    continue
                case 3:
                    reporte_sueldo()
                    continue
                case 4:
                    print("Hasta pronto.")
                    break
                case Default:
                        print("debe ingresar una opcion entre(1-5).")
                        time.sleep(2.0)
                        pass
                        