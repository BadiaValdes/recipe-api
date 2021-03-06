# Generated by Django 3.2.5 on 2021-07-14 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20210714_2112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='measurement_unit',
            new_name='fk_measurement_unit',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='product',
            new_name='fk_product',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='recipe',
            new_name='fk_recipe',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='user',
            new_name='fk_user',
        ),
        migrations.RenameField(
            model_name='userlike',
            old_name='recipe',
            new_name='fk_recipe',
        ),
        migrations.RenameField(
            model_name='userlike',
            old_name='user',
            new_name='fk_user',
        ),
    ]
