# Generated by Django 3.0 on 2021-01-30 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GermanLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('year_of_experience', models.CharField(max_length=3, null=True)),
                ('age', models.SmallIntegerField(null=True)),
                ('nursing_qualification', models.CharField(max_length=100, null=True)),
                ('document_url', models.FileField(max_length=255, null=True, upload_to='')),
                ('german_language_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_register.GermanLanguage')),
            ],
        ),
    ]
