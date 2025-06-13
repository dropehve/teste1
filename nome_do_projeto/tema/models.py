from django.db import models

# Create your models here.


class Esporte(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Lesao(models.Model):
    nome = models.CharField(max_length=100)
    parte_afetada = models.CharField(max_length=100, blank=True, null=True)
    intensidade = models.CharField(
        max_length=50,
        choices=[("Baixa", "Baixa"), ("Média", "Média"), ("Alta", "Alta")],
        blank=True,
        null=True
    )
    tempo_medio_recuperacao = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome


class PrevencaoTratamento(models.Model):
    TIPO_CHOICES = [
        ("Prevenção", "Prevenção"),
        ("Tratamento", "Tratamento")
    ]

    lesao = models.ForeignKey(Lesao, on_delete=models.CASCADE, related_name="cuidados")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.tipo} - {self.lesao.nome}"


class LesaoEsporte(models.Model):
    esporte = models.ForeignKey(Esporte, on_delete=models.CASCADE)
    lesao = models.ForeignKey(Lesao, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lesao.nome} em {self.esporte.nome}"


class Causa(models.Model):
    esporte = models.ForeignKey(Esporte, on_delete=models.CASCADE)
    nivel = models.CharField(
        max_length=20,
        choices=[("Amador", "Amador"), ("Profissional", "Profissional")]
    )
    causa = models.TextField()

    def __str__(self):
        return f"Causa ({self.nivel}) - {self.esporte.nome}"
