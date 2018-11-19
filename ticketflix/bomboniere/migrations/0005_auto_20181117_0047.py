# Generated by Django 2.0.8 on 2018-11-17 00:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bomboniere', '0004_auto_20181116_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combo',
            name='description',
            field=models.TextField(blank=True, help_text='Descrição do Produto', max_length=200, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='combo',
            name='quantity',
            field=models.IntegerField(blank=True, help_text='Quantidade de Itens em Estoque', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, help_text='Descrição do Produto', max_length=200, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(blank=True, help_text='Quantidade de Itens em Estoque', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantidade'),
        ),
    ]