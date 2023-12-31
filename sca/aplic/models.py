from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    endereço = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    data_pedido = models.DateField()
    data_entregar = models.DateField()
    status_pedido = models.CharField(max_length=50)
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Pedido {self.id}'

class ItemPedido(models.Model):
    quantidade = models.PositiveIntegerField()
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    memoria = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.quantidade}x {self.marca} {self.modelo}'

class Manutencao(models.Model):
    data = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return f'Manutenção em {self.data}'

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Celular(models.Model):
    modelo = models.CharField(max_length=100)
    preço = models.DecimalField(max_digits=10, decimal_places=2)
    fabricante = models.CharField(max_length=100)
    sistema_operacional = models.CharField(max_length=100)
    memoria_ram = models.PositiveIntegerField()
    armazenamento_interno = models.PositiveIntegerField()
    registrar_celular = models.DateField(auto_now_add=True)
    registrar_manutencao = models.ManyToManyField(Manutencao, blank=True)
    lista_de_manutencoes_pendentes = models.ManyToManyField(Manutencao, blank=True, related_name='manutencoes_pendentes')
    pedidos = models.ManyToManyField(Pedido, blank=True)
    imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.modelo

class LojaDeCelular(models.Model):
    nome = models.CharField(max_length=100)
    endereço = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    matricula = models.CharField(max_length=20)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

