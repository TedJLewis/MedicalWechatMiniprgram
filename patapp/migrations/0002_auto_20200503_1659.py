# Generated by Django 3.0.5 on 2020-05-03 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagereal',
            name='img',
            field=models.ImageField(default='', max_length=512, upload_to='D:\\workspace\\PythonProject\\miniprogram\\static\\dbimg\\'),
        ),
    ]
