import re
from django.core.exceptions import ValidationError

def validar_cpf(value):
    cpf = re.sub(r'\D', '', value)

    if len(cpf) != 11 or not cpf.isdigit():
        raise ValidationError("CPF deve conter 11 dígitos numéricos.")
    
    if cpf == cpf[0] * 11:
        raise ValidationError("CPF inválido.")
    
    def calcular_digito(cpf, peso):
        soma = sum(int(cpf[i]) * (peso - i) for i in range(peso - 1))
        resto = (soma * 10) % 11
        return 0 if resto == 10 else resto

    digito1 = calcular_digito(cpf, 10)
    digito2 = calcular_digito(cpf, 11)

    if int(cpf[9]) != digito1 or int(cpf[10]) != digito2:
        raise ValidationError("CPF inválido.")
    
    return value

def validar_telefone(value):
    pattern = re.compile(r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$')

    if not pattern.match(value):
        raise ValidationError("Número de telefone inválido. Use o formato (XX) XXXXX-XXXX.")
    
    return value
