# Generated by Django 4.2.2 on 2023-07-04 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_civil_defence_documents'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main_Document_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=240, null=True)),
                ('document_expiry', models.DateField(max_length=240, null=True)),
                ('document_type', models.CharField(max_length=240, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Main_Documents_files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civil_defence_document', models.FileField(blank=True, null=True, upload_to='Main_Documents/')),
                ('document_exp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.main_document_details')),
            ],
        ),
    ]
