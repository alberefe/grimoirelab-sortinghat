# Generated by Django 2.1 on 2020-02-14 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='authored_by',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='operation',
            name='trx',
            field=models.ForeignKey(db_column='tuid', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='operations', to='core.Transaction'),
            preserve_default=False,
        ),
    ]