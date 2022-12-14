# Generated by Django 4.1.2 on 2022-11-02 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('animais', '0002_rename_id_cid_denuncia_resgate_id_cid_resgate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='id_usu_denuncia',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='resgate',
            name='id_usu_resgate',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
