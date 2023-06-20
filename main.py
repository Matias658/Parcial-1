from funciones import *
import os
flag_cargar_datos = False
flag_leer_json = False
flag_precios_actualizados = False
flag_json_creado = False


while True:
    os.system("cls")
    opcion = menu()
    if opcion == 1:
        flag_cargar_datos = True
        mensaje = 'Datos cargados con exito'
        print(f"{mensaje:^500s}")
    elif flag_cargar_datos or opcion == 12:
        match opcion:
            case 7:
                flag_leer_json = True
                if flag_json_creado:
                    print("Ya se creó el archivo .json anteriormente.")
                    os.system("pause")
                    continue
                flag_json_creado = True

            case 8:
                if flag_leer_json == False:
                    print("PRIMERO LEA EL JSON")
                    os.system("pause")
                    continue
                else:
                    pass
            case 9:
                if flag_precios_actualizados:
                    print("Ya se actualizó la lista anteriormente.")
                    os.system("pause")
                    continue
                flag_precios_actualizados = True

                
                
    else:
        print("PRIMERO CARGUE LOS DATOS POR FAVOR")
        os.system("pause")
        continue


    salir = elegir_opcion(opcion)
    if salir == "s":
        break
    os.system("pause")
