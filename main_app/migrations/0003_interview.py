# Generated by Django 4.0.5 on 2022-06-06 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_linkedin_client_linkedin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('company', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('feedback', models.CharField(max_length=300)),
                ('result', models.CharField(max_length=150)),
                ('notes', models.TextField(max_length=500)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='main_app.client')),
            ],
        ),
    ]
