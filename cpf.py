from validate_docbr import CPF, CNH
import re


class Validate:
    @staticmethod
    def document_create(document):
        document = document.replace(" ", "")
        cnh = CNH()
        if cnh.validate(document):
            return Cnh(document)

        cpf = CPF()
        if cpf.validate(document):
            return Cpf(document)

        phone_template = "[0-9]{2}[0-9]{5}[0-9]{4}"
        verify = re.findall(phone_template, document)
        verify = str(verify).strip("['']")
        if len(verify) == 11:
            return Phone(document)

        email_template = "\w{3,30}@\w{3,10}.\w{2,3}.\w{2}"
        verify = re.findall(email_template, document)
        verify = str(verify).strip("['']")
        if document == verify:
            return Email(document)

        else:
            raise ValueError('Invalid value, enter another number')


class Cpf:
    def __init__(self, document):
        self.cpf = str(document)
        self.cpf_format()

    def cpf_format(self):
        cpf = CPF()
        return cpf.mask(self.cpf)

    def __str__(self):
        return f' Your cpf: >>>({self.cpf_format()})<<< its valid!'


class Cnh:
    def __init__(self, document):
        self.cnh = str(document)
        self.cnh_format()

    def cnh_format(self):
        cnh = CNH()
        return cnh.mask(self.cnh)

    def __str__(self):
        return f' Your cnh: >>>({self.cnh_format()})<<< its valid!'


class Phone:
    def __init__(self, document):
        self.phone = str(document)
        self.phone_mask()

    def phone_mask(self):
        phone_template = "([0-9]{2})([0-9]{5})([0-9]{4})"
        verify = re.search(phone_template, self.phone)
        mask = f">>>({verify.group(1)}){verify.group(2)}-{verify.group(3)}<<<"
        self.phone = mask
        return self.phone

    def __str__(self):
        return f"Your cell phone: {self.phone} its valid!"


class Email:
    def __init__(self, document):
        self.email = str(document)
        self.email_mask()

    def email_mask(self):
        return self.email

    def __str__(self):
        return f'Your e-mail >>>{self.email}<<< its valid!'
