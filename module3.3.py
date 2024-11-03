def print_params ( a=1 , b = 'строка' , c = True):
    print(a , b , c)
print_params(1 , "строка" , True)
print_params(1 , 4)
print_params(1 )
print_params( b= 25)
print_params(c=[1,2,3])

values_list = [77, " apple" , True]
values_dict = { 'a': 55 , 'b' : "яблока" , 'c' : True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [55.32, 'Строка']
print_params(*values_list_2, 42)