# Generated by Django 4.2.6 on 2023-10-16 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('preço', models.DecimalField(decimal_places=2, max_digits=10)),
                ('registrar_celular', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('endereço', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='DetalhesCelular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabricante', models.CharField(max_length=100)),
                ('sistema_operacional', models.CharField(max_length=100)),
                ('memoria_ram', models.PositiveIntegerField()),
                ('armazenamento_interno', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('contato', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=20)),
                ('nome', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('modelo', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('memoria', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LojaDeCelular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereço', models.CharField(max_length=200)),
                ('cnpj', models.CharField(max_length=18)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Manutencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateField()),
                ('data_entregar', models.DateField()),
                ('status_pedido', models.CharField(max_length=50)),
                ('total_pedido', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
        migrations.AddField(
            model_name='celular',
            name='detalhes_celular',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.detalhescelular'),
        ),
        migrations.AddField(
            model_name='celular',
            name='lista_de_manutencoes_pendentes',
            field=models.ManyToManyField(blank=True, related_name='manutencoes_pendentes', to='aplic.manutencao'),
        ),
        migrations.AddField(
            model_name='celular',
            name='pedidos',
            field=models.ManyToManyField(blank=True, to='aplic.pedido'),
        ),
        migrations.AddField(
            model_name='celular',
            name='registrar_manutencao',
            field=models.ManyToManyField(blank=True, to='aplic.manutencao'),
        ),
    ]