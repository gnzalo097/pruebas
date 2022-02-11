import numpy as np
import re

file = open("template_pruebas.j2", "r")

# lines = file.readlines()
# print(lines)

array_resumen_linea = np.array([])

bloque_info = False

# RELLENA array_resumen_linea
for line in file:

    if bloque_info == True:

        #print("[bloque-info]")
        
        if "-#}" in line:
            bloque_info = False
            array_resumen_linea = np.append(array_resumen_linea, "[bloque-info]")
            continue
        else:

            array_resumen_linea = np.append(array_resumen_linea, "[bloque-info]")
            continue


    if "[titulo]" in line:
        #print("[titulo]")
        array_resumen_linea = np.append(array_resumen_linea, "[titulo]")

    elif "[apartado]" in line:
        #print("[apartado]")
        array_resumen_linea = np.append(array_resumen_linea, "[apartado]")

    elif "[sub-apartado]" in line:
        #print("[sub-apartado]")
        array_resumen_linea = np.append(array_resumen_linea, "[sub-apartado]")
      
    elif "[sub-sub-apartado]" in line:
        #print("[sub-sub-apartado]")
        array_resumen_linea = np.append(array_resumen_linea, "[sub-sub-apartado]")

    elif "[sub-sub-sub-apartado]" in line:
        #print("[sub-sub-sub-apartado]")
        array_resumen_linea = np.append(array_resumen_linea, "[sub-sub-sub-apartado]")

    elif "[sub-sub-sub-sub-apartado]" in line:
        #print("[sub-sub-sub-sub-apartado]")
        array_resumen_linea = np.append(array_resumen_linea, "[sub-sub-sub-sub-apartado]")

    elif "[info]" in line:
        #print("[info]")
        array_resumen_linea = np.append(array_resumen_linea, "[info]")

    elif "[info-var]" in line:
        #print("[info]")
        array_resumen_linea = np.append(array_resumen_linea, "[info-var]")    

    elif "[bloque-info]" in line:
        #print("[bloque-info]")
        array_resumen_linea = np.append(array_resumen_linea, "[bloque-info]")
        bloque_info = True

    elif line == "\n" or line == " ":
        #print("vacio")
        array_resumen_linea = np.append(array_resumen_linea, "vacio")

    else:
        #print("---- COMANDO")
        array_resumen_linea = np.append(array_resumen_linea, "---- COMANDO")

print()
print()

array_cuadros = np.array([])

contador_cuadro = 1
contador_cuadro_info = 1

cuadro_comandos = False
cuadro_info = False

bloque_info = False

# RELLENA array_cuadros
for linea in array_resumen_linea:
#for index, linea in enumerate(array_resumen_linea, start=0):

    if linea == "---- COMANDO":

        cuadro_comandos = True
        array_cuadros = np.append(array_cuadros, "cuadro" + str(contador_cuadro) )

    elif linea == "vacio" and cuadro_comandos == True:

        array_cuadros = np.append(array_cuadros, "cuadro" + str(contador_cuadro) )


    elif linea == "[info-var]":

        if cuadro_comandos == True:
            cuadro_comandos = False
            contador_cuadro += 1

        cuadro_info = True
        array_cuadros = np.append(array_cuadros, "[info-var]" + str(contador_cuadro_info) )

    elif linea == "vacio" and cuadro_info == True:

        array_cuadros = np.append(array_cuadros, "[info-var]" + str(contador_cuadro_info) )       
    

    else:

        if cuadro_comandos == True:
            cuadro_comandos = False
            contador_cuadro += 1
            array_cuadros = np.append(array_cuadros, "nada" )

        if cuadro_info == True:
            cuadro_info = False
            contador_cuadro_info += 1
            array_cuadros = np.append(array_cuadros, "nada" )        

        else:

            array_cuadros = np.append(array_cuadros, "nada" )


print(array_resumen_linea.shape)
print(array_cuadros.shape)

#print(array_resumen_linea)
#print(array_cuadros)

print("--------------LINEAS--------------------------")
print()
for x in array_resumen_linea:
  print(x)
print()

print("---------------CUADROS-------------------")
print()
for x in array_cuadros:
  print(x)
print()



file_2 = open("template_pruebas.j2", "r")
lines = file_2.readlines()

contador_cuadro = 1
cuadro = False

array_temporal = np.array([])
array_variables_cuadro = np.array([])

#print(lines[1])
#print(array_cuadros[1])



# EN array_temporal guarda todas las lineas de comandos de un cuadro
# EN array_variables_cuadro guarda todas las variables que ha encontrado en un cuadro
for index, linea in enumerate(array_cuadros, start=0):

    if linea == "cuadro" + str(contador_cuadro):

        cuadro = True

        print(index + 1)

        comando = lines[index]

        array_temporal = np.append(array_temporal, comando )

    else:

        if cuadro == True:

            print(array_temporal)

            for item in array_temporal:

                variables_encontradas = re.findall('\{\{.*?\}\}',item)

                array_variables_cuadro = np.append(array_variables_cuadro, variables_encontradas)

            print(array_variables_cuadro)



            cuadro = False
            contador_cuadro += 1

            array_temporal = np.array([])
            array_variables_cuadro = np.array([])

        else: 

            continue





file.close() 

