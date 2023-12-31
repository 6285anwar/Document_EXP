# Generated by Django 4.2.2 on 2023-07-04 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_encodede_company_credentials_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Civil_Defence_Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civil_defence_document_name', models.CharField(max_length=240, null=True)),
                ('civil_defence_document', models.FileField(blank=True, null=True, upload_to='Civil_Defence_documents/')),
                ('civil_defence', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.company_credentials')),
            ],
        ),
    ]
