# Generated by Django 4.2.2 on 2023-07-04 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_main_document_details_main_documents_files'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main_documents_files',
            old_name='civil_defence_document',
            new_name='main_file_document',
        ),
    ]
