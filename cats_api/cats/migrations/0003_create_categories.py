from django.db import migrations
from ..utils import categories_list


def create_categories(apps, schema_editor):
    Categories = apps.get_model('cats', 'Categories')
    for category in categories_list:
        category_db = Categories.objects.create(id=category["id"], images=category["images"], name=category["name"])
        category_db.save()


class Migration(migrations.Migration):
    dependencies = [
        ('cats', '0002_create_breeds'),
    ]

    operations = [
        migrations.RunPython(create_categories),
    ]
