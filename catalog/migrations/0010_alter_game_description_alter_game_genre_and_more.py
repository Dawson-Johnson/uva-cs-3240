# Generated by Django 4.2.18 on 2025-04-18 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0009_alter_game_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game", name="description", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="game", name="genre", field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="game",
            name="location",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="game", name="platform", field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="game", name="release_date", field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="loan", name="borrow_date", field=models.DateTimeField(),
        ),
    ]
