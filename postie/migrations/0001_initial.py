# Generated by Django 2.0.2 on 2018-05-01 06:10

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('attachment', models.FileField(upload_to='', verbose_name='Letter attachment')),
            ],
            options={
                'verbose_name': 'Letter attachment',
                'verbose_name_plural': 'Letter attachments',
            },
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject')),
                ('html', ckeditor.fields.RichTextField(verbose_name='HTML')),
                ('plain', models.TextField(verbose_name='Plain text')),
                ('email_from', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email from')),
                ('recipients', models.TextField(verbose_name='Letter recipients')),
                ('event', models.CharField(blank=True, max_length=255, null=True, verbose_name='Event')),
                ('status', models.CharField(choices=[('draft', 'draft'), ('sent', 'Sent'), ('failed', 'Failed')], default='draft', max_length=255, verbose_name='Status')),
                ('language', models.CharField(blank=True, max_length=127, null=True, verbose_name='Language')),
            ],
            options={
                'verbose_name': 'Mail letter',
                'verbose_name_plural': 'Mail letters',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('message', models.CharField(max_length=255, verbose_name='Log message')),
                ('traceback', models.TextField(blank=True, null=True, verbose_name='Traceback')),
                ('letter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postie.Letter', verbose_name='Letter')),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('event', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=255, verbose_name='Event')),
            ],
            options={
                'verbose_name': 'Mail template',
                'verbose_name_plural': 'Mail templates',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TemplateTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject')),
                ('html', models.TextField(verbose_name='HTML text')),
                ('plain', models.TextField(blank=True, help_text='Alternative version of html text', null=True, verbose_name='Plain text')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='postie.Template')),
            ],
            options={
                'verbose_name': 'Mail template Translation',
                'db_table': 'postie_template_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
            },
        ),
        migrations.AddField(
            model_name='attachment',
            name='letter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='postie.Letter', verbose_name='Letter'),
        ),
        migrations.AlterUniqueTogether(
            name='templatetranslation',
            unique_together={('language_code', 'master')},
        ),
    ]
