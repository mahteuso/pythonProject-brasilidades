from cpf import Validate
# from date_BR import DateBr

#cpf = '29838352861'
#cnh = '04506588800'
count = 0
var = "phone_number"

while count < 4:
    print('')
    document = input(f"enter with your {var}:  ")
    new_object = Validate.document_create(document)
    print(new_object)
    if var == 'phone_number':
        var = 'CPF'
    if var == 'CPF':
        var = 'CODE'
    else:
        var = 'CNH'
    count += 1


'''

user = DateBr()
print(user.register_user)
'''