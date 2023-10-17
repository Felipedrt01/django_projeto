# Generated by Django 4.2.6 on 2023-10-17 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0002_celular_cliente_detalhescelular_fornecedor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('endereço', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=14)),
            ],
        ),
    ]
