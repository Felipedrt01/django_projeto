from django.contrib import admin
from .models import Celular,LojaDeCelular,Funcionario,Cliente,Pessoa,Pedido,ItemPedido,DetalhesCelular,Manutencao,Fornecedor

admin.site.register(Celular)
admin.site.register(LojaDeCelular)
admin.site.register(Funcionario)
admin.site.register(Cliente)
admin.site.register(Pessoa)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(DetalhesCelular)
admin.site.register(Manutencao)
admin.site.register(Fornecedor)



class CelularAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'preço', 'detalhes_celular', 'registrar_celular', 'registrar_manutenção', 'lista_de_manutenções_pendentes', 'pedidos')
    list_filter = ('modelo', 'preço')  
    search_fields = ('modelo', 'detalhes_celular', 'pedidos')  


class LojaDeCelularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereço', 'cnpj', 'telefone')
    list_filter = ('nome', 'cnpj')  
    search_fields = ('nome', 'cnpj')  

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'cargo', 'telefone')
    list_filter = ('cargo',)  
    search_fields = ('matricula', 'nome', 'cargo')  

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'endereço', 'cpf')
    list_filter = ('nome', 'email') 
    search_fields = ('nome', 'cpf') 

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

class DetalhesCelularAdmin(admin.ModelAdmin):
    list_display = ('fabricante', 'sistema_operacional', 'memoria_ram', 'armazenamento_interno')
    list_filter = ('fabricante', 'sistema_operacional') 
    search_fields = ('fabricante', 'sistema_operacional')

class ManutencaoAdmin(admin.ModelAdmin):
    list_display = ('data', 'descricao')
    list_filter = ('data',)  
    search_fields = ('descricao',)

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contato')
    list_filter = ('nome',)  
    search_fields = ('nome', 'contato')

