# Generated by Django 2.0.2 on 2018-05-04 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postie', '0002_auto_20180501_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='templatetranslation',
            name='html',
            field=models.TextField(null=True, verbose_name='HTML text'),
        ),
        migrations.AlterField(
            model_name='templatetranslation',
            name='subject',
            field=models.CharField(max_length=255, null=True, verbose_name='Subject'),
        ),
    ]