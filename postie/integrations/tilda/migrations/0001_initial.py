# Generated by Django 2.1 on 2020-07-04 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_key', models.CharField(max_length=255, verbose_name='Public key')),
                ('private_key', models.CharField(max_length=255, verbose_name='Private key')),
            ],
            options={
                'verbose_name': 'Preferences',
            },
        ),
    ]