# Generated by Django 5.1.4 on 2025-01-15 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_rename_links_project_github_link_project_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
