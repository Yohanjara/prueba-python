from fun import asignarSueldos, menu, clasificar_empleados, estadisticas, reporte_de_sueldos
op =0
lista_de_empleados = []
while True:
    
    op = menu()
    if op == 1:
        asignarSueldos(lista_de_empleados)  
    elif op == 2:
        clasificar_empleados(lista_de_empleados)  
    elif op == 3:
        estadisticas(lista_de_empleados) 
    elif op == 4:
        reporte_de_sueldos(lista_de_empleados)
    elif op == 5:
        print("Adios")
        print("Finalizando programa")
        print("creado por yohan jara ")
        print("rut 196332286")
        break

