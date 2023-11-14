from django.contrib import admin
from .models import Celular,LojaDeCelular,Funcionario,Cliente,Pedido,ItemPedido,Manutencao,Fornecedor

admin.site.register(Celular)
admin.site.register(LojaDeCelular)
admin.site.register(Funcionario)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(Manutencao)
admin.site.register(Fornecedor)


class CelularAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'preço', 'fabricante', 'sistema_operacional', 'memoria_ram', 'armazenamento_interno', 'registrar_celular', 'imagens')
    search_fields = ('modelo', 'fabricante', 'sistema_operacional')
    list_filter = ('fabricante', 'sistema_operacional')
    date_hierarchy = 'registrar_celular'
    filter_horizontal = ('registrar_manutencao', 'lista_de_manutencoes_pendentes', 'pedidos')

class LojaDeCelularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereço', 'cnpj', 'telefone')
    list_filter = ('nome', 'cnpj')  
    search_fields = ('nome', 'cnpj')  

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'cargo', 'telefone')
    list_filter = ('cargo',)  
    search_fields = ('matricula', 'nome', 'cargo')  

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'endereço', 'cpf')
    list_filter = ('nome', 'email') 
    search_fields = ('nome', 'cpf')  

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('data_pedido', 'data_entregar', 'status_pedido', 'total_pedido')
    list_filter = ('status_pedido',)  
    search_fields = ('data_pedido', 'status_pedido') 

class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('quantidade', 'modelo', 'marca',)
    list_filter = ('marca',)  
    search_fields = ('modelo',) 

class ManutencaoAdmin(admin.ModelAdmin):
    list_display = ('data', 'descricao')
    list_filter = ('data',)  
    search_fields = ('descricao',)

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contato')
    list_filter = ('nome',)  
    search_fields = ('nome', 'contato')

