# Generated by Django 3.2.3 on 2021-07-07 02:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('PRopre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Op_retrait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_R', models.FloatField(null=True)),
                ('date_retrait', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PRopre.propre')),
            ],
        ),
    ]
