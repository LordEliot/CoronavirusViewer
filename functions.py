
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