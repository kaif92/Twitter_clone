# Generated by Django 3.2.16 on 2023-03-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_app', '0002_auto_20230314_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='img',
            field=models.ImageField(default='user.png', upload_to=''),
            preserve_default=False,
        ),
    ]