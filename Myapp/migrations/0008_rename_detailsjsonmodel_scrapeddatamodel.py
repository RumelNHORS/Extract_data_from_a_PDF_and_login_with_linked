# Generated by Django 4.2.1 on 2023-05-30 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0007_alter_detailsjsonmodel_json_detail'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DetailsJsonModel',
            new_name='ScrapedDataModel',
        ),
    ]
