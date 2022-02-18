#!/usr/bin/env python
# coding: utf-8

import numpy as np
import re

file = open(r"C:\Users\Gonzalo\Documents\GitHub\pruebas\1_plantilla_gestion_demo\template.j2", "r")

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

    elif line == "\n" or line == " \n" or line == "  \n":
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

# RELLENA array_cuadros A PARTIR DEL array_resumen_linea
for linea in array_resumen_linea:

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

        elif cuadro_info == True:

            cuadro_info = False
            contador_cuadro_info += 1
            array_cuadros = np.append(array_cuadros, "nada" )        

        else:

            array_cuadros = np.append(array_cuadros, "nada" )


#print(array_resumen_linea.shape)
#print(array_cuadros.shape)

#print(array_resumen_linea)
#print(array_cuadros)

#print("--------------LINEAS--------------------------")
#print()
#for x in array_resumen_linea:
#   print(x)
print()

#print("---------------CUADROS-------------------")
#print()
#for x in array_cuadros:
#  print(x)
print()



file_2 = open("template.j2", "r")
lines = file_2.readlines()

contador_cuadro = 1
contador_info = 1

cuadro_comandos = False
cuadro_info = False

array_temporal_comandos = np.array([])
array_variables_cuadro = np.array([])

array_temporal_info = np.array([])
array_variables_info = np.array([])

array_resultados = np.array([])

#print(lines[1])
#print(array_cuadros[1])



# EN array_temporal_comandos guarda todas las lineas de comandos de un cuadro
# EN array_variables_cuadro guarda todas las variables que ha encontrado en un cuadro
for index, linea in enumerate(array_cuadros, start=0):

    if linea == "cuadro" + str(contador_cuadro):

        cuadro_comandos = True
        #print(index + 1)
        comando = lines[index]
        array_temporal_comandos = np.append(array_temporal_comandos, comando )

    elif linea == "[info-var]" + str(contador_info):

        if cuadro_comandos == True:

            # print(array_temporal_comandos)

            for item in array_temporal_comandos:

                variables_encontradas = re.findall('\{\{.*?\}\}',item)
                array_variables_cuadro = np.append(array_variables_cuadro, variables_encontradas)

            # print(array_variables_cuadro)

            print("----- cuadro " + str(contador_cuadro))
            cuadro_comandos = False
            contador_cuadro += 1

            array_temporal_comandos = np.array([])


        cuadro_info = True
        #print("-- " + str(index + 1) )
        comando = lines[index]
        array_temporal_info = np.append(array_temporal_info, comando )    

    else:

        if cuadro_comandos == True:

            # print(array_temporal_comandos)

            for item in array_temporal_comandos:

                variables_encontradas = re.findall('\{\{.*?\}\}',item)
                array_variables_cuadro = np.append(array_variables_cuadro, variables_encontradas)

            # print(array_variables_cuadro)

            print("----- cuadro " + str(contador_cuadro))
            print()

            if array_variables_cuadro.size != 0: 
                print("  !! FALTA [info-var]")
                print()
                array_resultados = np.append(array_resultados, False)

            else:

                cuadro_comandos = False
                contador_cuadro += 1
                array_resultados = np.append(array_resultados, True)

                array_temporal_comandos = np.array([])
                array_variables_cuadro = np.array([])


        elif cuadro_info == True:

            # print()
            # print(array_temporal_info)
            # print()

            for item in array_temporal_info:

                variables_encontradas = re.findall('\{\{.*?\}\}',item)
                array_variables_info = np.append(array_variables_info, variables_encontradas)

            # print(array_variables_info)

            # print("----- info " + str(contador_info))
            cuadro_info = False
            contador_info += 1

            # print()
            # print(array_variables_cuadro)
            # print(array_variables_info)
            # print()

            array_variables_cuadro_2 = np.unique(array_variables_cuadro)
            array_variables_info_2 = np.unique(array_variables_info)

            print()
            print(array_variables_cuadro_2)
            print(array_variables_info_2)
            print()

            equal_arrays = np.array_equal(array_variables_cuadro_2, array_variables_info_2)
            array_resultados = np.append(array_resultados, equal_arrays)

            print("--------------- [[ " + str(equal_arrays) + " ]]")
            print()

            array_temporal_info = np.array([])
            array_variables_info = np.array([])

            array_variables_cuadro = np.array([])


        else: 

            continue


# print(array_resultados.shape)

print("--------------- [[[[[ RESULTADOS ]]]]] ")
print()


resultado_final = True
contador_resultados = 1

for index, item in enumerate(array_resultados, start=0):

    if item == False:

        resultado_final = False

        print(str(contador_resultados) + ". Revisar cuadro" + str(index+1))

        contador_resultados += 1

print()
print("--------------- TODOS LOS CUADROS COINCIDEN CON LAS VARIABLES EXPLICADAS ------- [[ " + str(resultado_final) + " ]]")
print()
print()
print()








# file_2.close()

file.close() 

