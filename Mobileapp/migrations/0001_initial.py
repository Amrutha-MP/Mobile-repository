# Generated by Django 5.0.7 on 2024-07-20 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile_Db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Description', models.CharField(blank=True, max_length=50, null=True)),
                ('Company_Image', models.ImageField(blank=True, null=True, upload_to='company pictures')),
            ],
        ),
    ]
