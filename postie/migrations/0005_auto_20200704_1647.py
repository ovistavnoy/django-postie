# Generated by Django 2.1 on 2020-07-04 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postie', '0004_auto_20200323_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='templatetranslation',
            name='tilda_html',
            field=models.TextField(blank=True, editable=False, null=True, verbose_name='Tilda HTML'),
        ),
        migrations.AddField(
            model_name='templatetranslation',
            name='tilda_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Tilda id'),
        ),
    ]
