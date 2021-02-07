# Generated by Django 3.1.6 on 2021-02-07 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('contents', models.TextField()),
                ('author', models.CharField(max_length=25)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
