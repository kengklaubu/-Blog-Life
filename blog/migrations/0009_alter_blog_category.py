# Generated by Django 5.0.6 on 2024-09-30 03:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0008_alter_blog_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="category",
            field=models.CharField(default="Uncategorized", max_length=100),
            preserve_default=False,
        ),
    ]
