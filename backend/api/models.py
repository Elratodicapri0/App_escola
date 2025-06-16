from django.db import models
from .validators import validar_cpf, validar_telefone


class Responsavel(models.Model):
    name = models.CharField(max_length=50, verbose_name="Digite o nome do responsavel")
    phone_number = models.CharField(max_length=15, verbose_name="Digite o numero do celular(xx)xxxxx-xxxx", validators=[validar_telefone])
    email = models.EmailField(max_length=100, verbose_name="Digite o email do responsavel")
    adress = models.CharField(max_length=100, verbose_name="Digite o endereço do responsavel") 
    cpf = models.CharField(max_length=11, unique=True, verbose_name="Digite o cpf do responsavel", validators=[validar_cpf])
    birthday = models.DateField()

    def __str__(self):
        return self.name
    
class Professor(models.Model):

    name_professor = models.CharField(max_length=50, verbose_name="Digite o nome do professor", blank=False)
    phone_number_professor = models.CharField(max_length= 11, verbose_name="Digite o numero do celular (xx)xxxxx-xxxx")
    email_professor = models.EmailField(max_length=100, verbose_name="Digite o email do professor")
    cpf_professor = models.CharField(max_length=11, unique=True, verbose_name="Digite o cpf do professor")
    birthday_professor = models.DateField()
    matricula_professor = models.CharField(max_length=11,unique=True,verbose_name="Digite sua matricula: ")

    def __str__(self):
        return self.name_professor

class Bimestre(models.Model):
    numero = models.IntegerField()
    def __str__(self):
        return f"Bimestre {self.numero}"


class Aluno(models.Model):

    TURMA_CHOICES = (
    ("1A", "1 ANO A"),
    ("1B", "1 ANO B"),
    ("1C", "1 ANO C"),
    ("2A", "2 ANO A"),
    ("2B", "2 ANO B"),
    ("2C", "2 ANO C"),
    ("3A", "3 ANO A"),
    ("3B", "3 ANO B"),
    ("3C", "3 ANO C"),
    )

    name_aluno = models.CharField(max_length=50, verbose_name="Digite o nome do Aluno", blank=True, null=False)
    phone_number_aluno = models.CharField(max_length= 11, verbose_name="Digite o numero do celular (xx)xxxxx-xxxx")
    email_aluno = models.EmailField(max_length=100, verbose_name="Digite o email do aluno")
    cpf_aluno = models.CharField(max_length=11, unique=True, verbose_name="Digite o cpf do aluno")
    birthday_aluno = models.DateField()
    class_choice = models.CharField(max_length=2, choices=TURMA_CHOICES, blank=True, null=False)
    faltas_aluno = models.CharField(max_length=2, blank=True, null=False)

    Responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name_aluno if self.name_aluno else "Aluno sem nome"

class Nota(models.Model):
    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE)
    bimestre = models.ForeignKey('Bimestre', on_delete=models.CASCADE)
    valor = models.FloatField()
    disciplina = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.aluno} - {self.disciplina} - Bimestre {self.bimestre.numero}: {self.valor}"

class AtividadePendente(models.Model):
    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE)
    bimestre = models.ForeignKey('Bimestre', on_delete=models.CASCADE)
    disciplina = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.aluno} - {self.disciplina} - Bimestre {self.bimestre.numero}"

class EventoExtracurricular(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data = models.DateField()
    professor_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titulo} ({self.data})"

class PagamentoPendente(models.Model):
    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data_vencimento = models.DateField()
    descricao = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.aluno} - R$ {self.valor} - Vencimento: {self.data_vencimento}"
