# Generated by Django 3.2.9 on 2021-12-27 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='user_name',
        ),
        migrations.AddField(
            model_name='comment',
            name='user_email',
            field=models.EmailField(default='Test', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=400),
        ),
    ]
