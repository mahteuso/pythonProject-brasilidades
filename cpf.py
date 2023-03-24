class Cpf:
    def __init__(self, cpf):
        self.cpf = str(cpf)
        if self.cpf_validates():
            self.cpf_format()
        else:
            raise ValueError('Invalid value, enter another number!')

    def __str__(self):
        return self.cpf_format()

    def cpf_validates(self):
        if len(self.cpf) == 11:
            return True
        else:
            return False

    def cpf_format(self):
        cpf_part_one = self.cpf[:3]
        cpf_part_two = self.cpf[3:6]
        cpf_part_three = self.cpf[6:9]
        cpf_part_four = self.cpf[9:]
        return print(f'{cpf_part_one}.{cpf_part_two}.{cpf_part_three}-{cpf_part_four}')


