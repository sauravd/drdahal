# Generated by Django 2.1.1 on 2018-12-02 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hariblog', '0005_auto_20181202_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='comments',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]