# Generated by Django 4.1.3 on 2023-06-14 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chitfund',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('balance', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=40)),
                ('pincode', models.IntegerField()),
                ('chitfund_emp', models.ManyToManyField(related_name='addresses', to='djsignalling.chitfund')),
            ],
        ),
    ]