# Generated by Django 4.2.2 on 2023-06-30 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_property_id_company_property_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owners_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_type', models.CharField(max_length=240, null=True)),
                ('owner_name', models.CharField(max_length=240, null=True)),
                ('owner_phone', models.CharField(max_length=240, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Owners_Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_document_name', models.CharField(max_length=240, null=True)),
                ('owner_document', models.FileField(blank=True, null=True, upload_to='owner_documents/')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.owners_details')),
            ],
        ),
    ]