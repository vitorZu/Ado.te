# Generated by Django 4.1.5 on 2023-01-12 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divulgar', '0004_pet_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='sexo',
            field=models.CharField(choices=[('M', 'Macho'), ('F', 'Fémea')], default='F', max_length=1),
        ),
    ]
