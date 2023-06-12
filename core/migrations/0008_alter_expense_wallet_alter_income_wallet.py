# Generated by Django 4.1 on 2022-09-05 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_total_update_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.wallet'),
        ),
        migrations.AlterField(
            model_name='income',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.wallet'),
        ),
    ]