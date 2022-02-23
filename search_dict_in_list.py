list_data = [
  {"name": "Tom", "age": 10},
  {"name": "Mark", "age": 5},
  {"name": "Pam", "age": 7},
  {"name": "Tam", "age":15}
]

print(list_data)

# search dict element in list_data
# need to use generator expression "next"

dict = next(item for item in list_data if item['name'] == 'Tom')
print(dict)

# To manage non existing element, provide default response
dict = next((item for item in list_data if item['name'] == 'Tam'), None)
print(dict)

# Iterating list of dictionary to search if a required element exist. Very useful if desired element not exist in list and want to add to the list
dict = next((item for item in list_data if item['name'] == 'Jam'), None)
new_elem = {}
if dict == None:
    new_elem['name'] = 'Jam'
    new_elem['age'] = 18
    list_data.append(new_elem)
print(list_data)

# Find index of the dict element of a list
dict_index = next((i for i, item in enumerate(list_data) if item['name'] == 'Tam'), None)
print(dict_index)

dict_index = next((i for i, item in enumerate(list_data) if item['name'] == 'Dan'), None)
print(dict_index)