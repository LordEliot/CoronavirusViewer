#listaNumeros = [1, 6, 8]
#print(listaNumeros[2])
#for elemento in listaNumeros:
#ultimo = [1, 1, 6, 8]
    #for elementod in ultimo:
        #print(elemento+elementod)
        #break
#for elemento in listaNumeros:
    #print(elemento + ultimoElemento)
    #ultimoElemento = elemento
#ejemploUno = [3, 5, 6, 2]
#for impresionUno in ejemploUno:
 #   print(impresionUno)

#ejemploDos =[(4, 6), (1, 4)]
#for impresionDos in ejemploDos:
 #   print(impresionDos[1] + 1)

#array2d = [[4, 6], [1, 4]]
#for elementoUno in array2d:
 #   elementoUno[1] = elementoUno[1] + 1
  #  print(array2d)
#casoTres = [[3, 5, 12, 56, 23], [65, 23, 45, 67, 1]]
#for tresImpreso in casoTres:
 #   tresImpreso[4] = tresImpreso[4] + 2
  #  print(tresImpreso)

#array = input()
#if array[0] % 2 == 0:
 #   print("La primer posicion es par")
#else:
 #   print("La primer posicion es impar")

#for par in range(23,2789,4):
 #   print(par)

#array1 = input()
#array2 = input()
#for i in array1:
 #   for i2 in array2:
  #      if i == i2:
   #         print(i)

#array = input()
#counter = 0  
#for element in array:
  #   counter = counter + 1
#print(counter)

#array = input()
#counter = 0
#for element in array:
 #   counter = counter + 1
#first_value = array[0]
#array[0] = array[counter - 1]
#array[counter - 1] = first_value
#print(array)

#a = [1, 2, 3, 4]
#a.insert(4, 5)
#a.insert(6, 10)

#array = input()
#array.append("buldarico")
#array.remove("diego")
#print(array)

#array = input()
#array.clear()
#array = [1, 2, 3]
#print(array)

#array = ["andres", "sofia", "luz", "felipe", "diego", "robert", "juan", "maria", "tania", "rosenbert", "jean", "patricia," "ana", "zeus", "daniel", "jorge"]
#name = input()
#for element in array:
#if name == element:
#print("eureka")
#else:
#print("lo siento")

#array = ["andres", "sofia", "andres", "felipe", "diego", "robert", "juan", "maria", "tania", "rosenbert", "jean", "patricia," "ana", "zeus", "daniel", "jorge"]
#name = input()
##called = array.count(name)
#if called >= 1:
 # print("eureka") 
#else:
 # print("lo siento")

#def revert_list(my_list):
 # return list(reversed(my_list))

#names = ["diego", "juan", "marta"]
#last_names = ["rubio", "vidales", "castano"]

#names_reverted = revert_list(names)
#other_var = revert_list(last_names)

#print(names_reverted)
#print(other_var)

#FUNCIONES

#def evaluate(number):
 # if number > 10:
  #  print("es mayor a diez")
  #else:
   # print("es menor a 10")

#user_input = input()

#evaluate(user_input)

#def compare_strings(s1, s2):
 # if s1 == s2:
  #  return True
  #else:
   # return False

#data = input()
#data2 = input()
#result = compare_strings(data, data2)

#if result is True:
 # print("son iguales")
#else:
 # print("no son iguales")

#DICCIONARIOS
#people = [
 # ["maria", "ross", "felipe", "camila"], 
 # ["martha", "camilo", "fabian", "tomy"],
 # ["viviana", "alejandro", "juan", "cesar"]
 # "jon",
 # "tyrion"
#]
#people.pop(1)
#print(people)
#people[0].remove("felipe")

#people[2].pop(2)
#people.clear()
#people.pop(2)
#people[2].clear()

#people[1].append("diego")
#people.append(["Jon", "Tyrion"])

#me = {"name": "Diego", "age": "24", "ocuppation": "lawyer" }

#print(me.items())

#for key, value in me.items():
 # print(key + value)

""" abecedary = ["a", "b", "c", "d"]

for item in abecedary:
  print(item)

print(abecedary[1])
print(abecedary.count("c"))
abecedary.pop(3)
abecedary.append("e")
print(abecedary) """
  
"""integers = (1, 2, 3, 4, 5)

print(integers[2])
print(len(integers))"""

"""naranja = {"size": "m", "color": "blue" }
naranja.get("color")
naranja["size"] = "s"
naranja.update({"size": "l"})

for k, v in naranja.items():
  print("The {} of the orange is {}".format(
    k,
    v
  ))

phrase = "{} y {} son {} e {}".format(
  "Diego",
  "Martha",
  "madre",
  "hijo"
)
print(phrase)"""


def get_item_count(lookup, list_to_look):
  count = list_to_look.count(lookup)
  
  if count == 1:
    single = "vez"
  else:
    single = "veces"
  
  print("{} aparece {} {} en la lista".format(
      lookup.capitalize(),
      count,
      single
    )
  )
  
input_string = input()
input_list = input()

if type(input_string) is not str:
  print("{} no es un string. Ingrese un string".format(
    input_string
  ))
  quit()

if type(input_list) is not list:
  print("{} no es una lista. Ingrese una lista".format(
    input_list
  ))
  quit()

get_item_count(input_string, input_list)
print("hola")


print("esta vez no la vamos a cagar")


Esto es algo que está en la nueva realidad y quiero que esté ahora en la realidad original.
  



    


      

    

 