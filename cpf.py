from validate_docbr import CPF, CNH


class Cpf:
    def __init__(self, cpf, cnh):
        self.cpf = str(cpf)
        self.cnh = str(cnh)
        if self.cpf_validates() and self.cnh_validate():
            self.cpf_format()
            self.cnh_format()
        else:
            raise ValueError('Invalid value, enter another number!')

    def __str__(self):
        return f' Your cpf: {self.cpf_format()} and your cnh: {self.cnh_format()}'

    def cpf_validates(self):
        new_cpf = CPF()
        return new_cpf.validate(self.cpf)

    def cpf_format(self):
        cpf = CPF()
        return cpf.mask(self.cpf)

    def cnh_validate(self):
        cnh = CNH()
        return cnh.validate(self.cnh)
    def cnh_format(self):
        cnh = CNH()
        return cnh.mask(self.cnh)