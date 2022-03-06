import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breeds',
            fields=[
                ('description', models.CharField(blank=True, max_length=1023)),
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), size=None)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('origin', models.CharField(blank=True, max_length=255)),
                ('temperament', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), size=None)),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
