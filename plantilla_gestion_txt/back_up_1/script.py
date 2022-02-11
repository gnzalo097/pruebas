def limpiar_linea(linea, etiqueta):
    new_line1 = linea.replace('{# ', '')
    new_line2 = new_line1.replace(' -#}', '')
    new_line3 = new_line2.replace('\n', '')
    new_line4 = new_line3.replace(etiqueta, '')
    return new_line4

def limpiar_saltos(linea):
    new_line1 = linea.replace('\n', '')
    return new_line1


file_output = open(r"C:\Users\Gonzalo\Desktop\prueba_py\probando_py\word_automatico.py", "w")
file = open("template_pruebas.j2", "r")

# lines = file.readlines()
# print(lines)


file_output.write("from docx import Document\n")
file_output.write("from docx.shared import Inches\n")
file_output.write("from docx.shared import Pt\n")
file_output.write("\n")
file_output.write("document = Document()\n")
file_output.write("style = document.styles['Normal']\n")
file_output.write("font = style.font\n")
file_output.write("font.name = 'Arial'\n")
file_output.write("font.size = Pt(9)\n")
file_output.write("\n")


contador_comandos = 0
array_comandos = []

bloque_info = False

contador_apartado = 0
contador_sub_apartado = 0
contador_sub_sub_apartado = 0
contador_sub_sub_sub_apartado = 0
contador_sub_sub_sub_sub_apartado = 0


for line in file:

    if bloque_info == True:
        if "-#}" in line:
            bloque_info = False
            continue
        else:
            new_line = limpiar_saltos(line)
            file_output.write("document.add_paragraph('" + new_line + "')\n")
            continue


    if "[titulo]" in line:
        print("[titulo]")

        new_line = limpiar_linea(line, "[titulo] ")

        file_output.write("\n")
        file_output.write("document.add_heading('" + new_line + "', 0)\n")
        file_output.write("document.add_page_break()")
        file_output.write("\n")

    elif "[apartado]" in line:
        print("[apartado]")

        contador_sub_apartado = 0
        contador_sub_sub_apartado = 0
        contador_sub_sub_sub_apartado = 0
        contador_sub_sub_sub_sub_apartado = 0
        contador_apartado += 1

        new_line = limpiar_linea(line, "[apartado] ")

        file_output.write("\n")
        file_output.write("document.add_heading('" 
                                                    + str(contador_apartado) + 
                                                    ". " 
                                                    + new_line + "', 1)\n")

    elif "[sub-apartado]" in line:
        print("[sub-apartado]")

        contador_sub_sub_apartado = 0
        contador_sub_sub_sub_apartado = 0
        contador_sub_sub_sub_sub_apartado = 0
        contador_sub_apartado += 1

        new_line = limpiar_linea(line, "[sub-apartado] ")

        file_output.write("\n")
        file_output.write("document.add_heading('" 
                                                    + str(contador_apartado) + 
                                                    "." 
                                                    + str(contador_sub_apartado) + 
                                                    ". " 
                                                    + new_line + "', 2)\n")
      
    elif "[sub-sub-apartado]" in line:
        print("[sub-sub-apartado]")

        contador_sub_sub_sub_apartado = 0
        contador_sub_sub_sub_sub_apartado = 0
        contador_sub_sub_apartado += 1

        new_line = limpiar_linea(line, "[sub-sub-apartado] ")

        file_output.write("\n")
        file_output.write("document.add_heading('" 
                                                    + str(contador_apartado) + 
                                                    "." 
                                                    + str(contador_sub_apartado) + 
                                                    "." 
                                                    + str(contador_sub_sub_apartado) + 
                                                    ". " 
                                                    + new_line + "', 3)\n")

    elif "[sub-sub-sub-apartado]" in line:
        print("[sub-sub-sub-apartado]")

        contador_sub_sub_sub_sub_apartado = 0
        contador_sub_sub_sub_apartado += 1

        new_line = limpiar_linea(line, "[sub-sub-sub-apartado] ")

        file_output.write("\n")
        file_output.write("document.add_heading('" 
                                                    + str(contador_apartado) + 
                                                    "." 
                                                    + str(contador_sub_apartado) + 
                                                    "." 
                                                    + str(contador_sub_sub_apartado) +
                                                    "." 
                                                    + str(contador_sub_sub_sub_apartado) + 
                                                    ". " 
                                                    + new_line + "', 4)\n")


    elif "[sub-sub-sub-sub-apartado]" in line:
        print("[sub-sub-sub-sub-apartado]")

        contador_sub_sub_sub_sub_apartado += 1

        new_line = limpiar_linea(line, "[sub-sub-sub-sub-apartado] ")

        file_output.write("\n")
        file_output.write("document.add_heading('" 
                                                    + str(contador_apartado) + 
                                                    "." 
                                                    + str(contador_sub_apartado) + 
                                                    "." 
                                                    + str(contador_sub_sub_apartado) +
                                                    "." 
                                                    + str(contador_sub_sub_sub_apartado) + 
                                                    "."
                                                    + str(contador_sub_sub_sub_sub_apartado) + 
                                                    ". " 
                                                    + new_line + "', 5)\n")


        
    elif "[info]" in line:
        print("[info]")

        new_line = limpiar_linea(line, "[info] ")

        file_output.write("document.add_paragraph('" + new_line + "')\n")

    elif "[bloque-info]" in line:
        print("[bloque-info]")

        bloque_info = True

        continue

    elif line == "\n" or line == " ":
        print("vacio")

    else:
        print("---- COMANDO")

        # contador_comandos += 1

        new_line = limpiar_saltos(line)

        file_output.write("document.add_paragraph('" + new_line + "')\n")

 
file_output.write("\ndocument.save('word_automatico_render.docx')\n")

file.close() 

file_output.close()



    