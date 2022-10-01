# Generated by Django 4.1.1 on 2022-10-01 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cook", "0006_useringredient"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipe",
            name="user",
        ),
        migrations.AddField(
            model_name="recipe",
            name="user_ingrs",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="cook.useringredient",
            ),
        ),
    ]
