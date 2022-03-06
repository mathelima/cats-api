from django.db import migrations
from ..utils import breeds_list


def create_breeds(apps, schema_editor):
    Breeds = apps.get_model('cats', 'Breeds')
    for breed in breeds_list:
        try:
            images = [breed["image"]["url"]]
        except:
            images = []
        breed_db = Breeds.objects.create(description=breed["description"], id=breed["id"],
                                         images=images, name=breed["name"],
                                         origin=breed["origin"], temperament=breed["temperament"])
        breed_db.save()


class Migration(migrations.Migration):
    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_breeds),
    ]
