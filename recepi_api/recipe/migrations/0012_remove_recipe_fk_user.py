# Generated by Django 3.2.5 on 2021-08-04 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0011_remove_recipeimage_fk_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='fk_user',
        ),
    ]