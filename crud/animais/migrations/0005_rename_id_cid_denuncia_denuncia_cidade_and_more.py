# Generated by Django 4.1.2 on 2022-11-02 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0004_alter_resgate_id_usu_resgate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='denuncia',
            old_name='id_cid_denuncia',
            new_name='cidade',
        ),
        migrations.RenameField(
            model_name='denuncia',
            old_name='id_sit_denuncia',
            new_name='situacao',
        ),
        migrations.RenameField(
            model_name='denuncia',
            old_name='id_usu_denuncia',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='resgate',
            old_name='id_cid_resgate',
            new_name='cidade',
        ),
        migrations.RenameField(
            model_name='resgate',
            old_name='id_est_resgate',
            new_name='estado',
        ),
        migrations.RenameField(
            model_name='resgate',
            old_name='id_sit_resgate',
            new_name='situacao',
        ),
        migrations.RenameField(
            model_name='resgate',
            old_name='id_usu_resgate',
            new_name='usuario',
        ),
    ]
