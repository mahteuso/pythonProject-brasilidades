from cpf import Validate

#cpf = '29838352861'
#cnh = '04506588800'

document = input("enter with Cpf or Cnh: ")


new_object = Validate.document_create(document)
print(new_object)
