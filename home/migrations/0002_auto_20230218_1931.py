# Generated by Django 3.2.18 on 2023-02-19 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='test', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='education',
            name='major',
            field=models.CharField(default='test', max_length=50),
        ),
        migrations.AlterField(
            model_name='education',
            name='school',
            field=models.CharField(default='test', max_length=50),
        ),
        migrations.AlterField(
            model_name='education',
            name='time',
            field=models.CharField(default='test', max_length=20),
        ),
        migrations.AlterField(
            model_name='position',
            name='company',
            field=models.CharField(default='test', max_length=50),
        ),
        migrations.AlterField(
            model_name='position',
            name='desc',
            field=models.TextField(default='test'),
        ),
        migrations.AlterField(
            model_name='position',
            name='link',
            field=models.CharField(default='test', max_length=50),
        ),
        migrations.AlterField(
            model_name='position',
            name='location',
            field=models.CharField(default='test', max_length=50),
        ),
        migrations.AlterField(
            model_name='position',
            name='time',
            field=models.CharField(default='test', max_length=50),
        ),
        migrations.AlterField(
            model_name='position',
            name='title',
            field=models.CharField(default='test', max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='desc',
            field=models.TextField(default='test'),
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.CharField(default='test', max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(default='test', max_length=100),
        ),
    ]
