swap= lambda x,y: (y,x)

var_one=input("Enter variable one:")
var_two=input("Enter variable two:")
print("Before swapping : variable_one=",var_one,"variable_two:",var_two)
var_one, var_two=swap(var_one,var_two)
print("After swapping : variable_one=",var_one,"variable_two:",var_two)

