# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-07 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpaste', '0003_snippet_highlighted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='lexer',
            field=models.CharField(default='python', max_length=30, verbose_name='Lexer'),
        ),
    ]
