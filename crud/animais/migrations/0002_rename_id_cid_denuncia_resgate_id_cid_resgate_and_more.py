# Generated by Django 4.1.2 on 2022-10-13 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resgate',
            old_name='id_cid_denuncia',
            new_name='id_cid_resgate',
        ),
        migrations.RenameField(
            model_name='resgate',
            old_name='id_est_denuncia',
            new_name='id_est_resgate',
        ),
        migrations.RenameField(
            model_name='resgate',
            old_name='id_sit_denuncia',
            new_name='id_sit_resgate',
        ),
        migrations.RenameField(
            model_name='resgate',
            old_name='id_usu_denuncia',
            new_name='id_usu_resgate',
        ),
    ]