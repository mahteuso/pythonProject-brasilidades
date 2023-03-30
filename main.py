from cpf import Validate

#cpf = '29838352861'
#cnh = '04506588800'
count = 0
var = "phone_number"

while count < 3:
    print('')
    document = input(f"enter with your {var}:  ")
    new_object = Validate.document_create(document)
    print(new_object)
    if var == 'phone_number':
        var = 'CPF'
    else:
        var = 'CNH'
    count += 1

