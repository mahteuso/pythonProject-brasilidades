from validate_docbr import CPF, CNH


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

        else:
            raise ValueError('Invalid value, enter another number')


class Cpf(Validate):
    def __init__(self, document):
        super().__init__()
        self.cpf = str(document)
        self.cpf_format()

    def cpf_format(self):
        cpf = CPF()
        return cpf.mask(self.cpf)

    def __str__(self):
        return f' Your cpf: >>>({self.cpf_format()})<<< its valid!'


class Cnh(Validate):
    def __init__(self, document):
        super().__init__()
        self.cnh = str(document)
        self.cnh_format()

    def cnh_format(self):
        cnh = CNH()
        return cnh.mask(self.cnh)

    def __str__(self):
        return f' Your cnh: >>>({self.cnh_format()})<<< its valid!'
