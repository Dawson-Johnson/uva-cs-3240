# Generated by Django 4.2.18 on 2025-03-26 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_userprofile_profile_pic_alter_userprofile_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_pic",
            field=models.ImageField(default="images/default.jpg", upload_to="images/"),
        ),
    ]
