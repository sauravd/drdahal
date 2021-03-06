# Generated by Django 2.1.1 on 2018-12-02 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hariblog', '0004_auto_20181202_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='comment_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='comment_ornot',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='dislikes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='likes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='shared',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='shared_freq',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
