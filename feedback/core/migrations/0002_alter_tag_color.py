# Generated by Django 3.2.16 on 2022-10-26 16:51

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="color",
            field=colorfield.fields.ColorField(
                default="#FF0000", image_field=None, max_length=18, samples=None
            ),
        ),
    ]