# Generated by Django 2.1.5 on 2019-10-19 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20191019_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='spells_json',
            field=models.TextField(null=True),
        ),
    ]