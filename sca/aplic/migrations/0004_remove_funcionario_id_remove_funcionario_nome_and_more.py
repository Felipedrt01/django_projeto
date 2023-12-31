# Generated by Django 4.2.6 on 2023-10-19 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0003_pessoa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='id',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='telefone',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='pessoa_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplic.pessoa'),
            preserve_default=False,
        ),
    ]
