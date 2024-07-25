# Generated by Django 5.0.7 on 2024-07-23 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='image')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='app.post')),
            ],
        ),
    ]