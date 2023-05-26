# Generated by Django 4.0.4 on 2023-02-20 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100)),
                ('price', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
        migrations.DeleteModel(
            name='Mytodo',
        ),
    ]