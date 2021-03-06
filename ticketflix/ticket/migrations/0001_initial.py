# Generated by Django 2.0.8 on 2018-11-19 22:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('session', '0002_auto_20181119_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(help_text='Tipo', max_length=50, verbose_name='Tipo')),
                ('seat', models.CharField(help_text='Assento', max_length=50, verbose_name='Assento')),
                ('price', models.FloatField(help_text='Preço', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Preço')),
                ('session', models.OneToOneField(help_text='Sessão do Ticket', on_delete=django.db.models.deletion.CASCADE, to='session.Session', verbose_name='Sessão')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
            },
        ),
    ]
