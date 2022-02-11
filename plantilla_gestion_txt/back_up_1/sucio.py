"""
import numpy as np

array_temporal = np.array([8, 23, 45, 12, 78])

for index, item in enumerate(array_temporal, start=1):   # Python indexes start at zero
    print(index, item)

"""

import re

txt = "hola me gustan {{abc}} mucho estas cosas {{porque}} si y ya esta {{je je}} buenas noches {{ juju }} "

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall('\{\{.*?\}\}',txt)

print(x)


"""
arr2 = np.array([["hola", "hola", "hola"], [4, 5, 6], [4, 5, 6], [4, 5, 6]])

arr2[0][0] = "adios"

#print(arr) 

for x in arr2:
  print(x)

if "adios" in arr2:
    print("jeje")



arr = np.array([11, 2, 6, 7, 2])
# Add / Append an element at the end of a numpy array
arr = np.append(arr, 10)

print('Original Array: ', arr)




{% if modelo_equipo not in modelos_soportados_y_version  | map(attribute='equipo') %}
{{ ' -- EL EQUIPO NO ESTA DENTRO DE LOS EQUIPOS SOPORTADOS -- ' | center }}
{% endif %}


{% if servicio not in servicios_soportados %}
{{ ' -- EL SERVICIO NO ESTA DENTRO DE LOS SERVICIOS SOPORTADOS -- ' | center }}
{% endif %}


"""