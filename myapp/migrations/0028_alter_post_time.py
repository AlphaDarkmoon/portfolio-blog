# Generated by Django 5.1.3 on 2024-12-02 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_remove_comment_content_remove_comment_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.CharField(blank=True, db_index=True, default='02 December 2024', max_length=100),
        ),
    ]
