
def filter_id(a):
    l1 = [{'id': 1, 'name': 'Kannur'}, {'id': 2, 'name': 'Malappuram'}, {'id': 3, 'name': 'Kollam'},
          {'id': 4, 'name': 'Alappuzha'}, {'id': 5, 'name': 'Kottayam'}]
    filtered = list(filter(lambda x: x['id'] == int(a), l1))
    return filtered
    

x = input("Enter the ID to be searched: ")
name = filter_id(x)
if name:
    print("Corresponding Name:", name)
else:
    print("ID not found.")
