from django.db import migrations

def migrate_address(apps, schema_editor):
    OldModel = apps.get_model('oc_lettings_site', 'Address')  # Access the old model
    NewModel = apps.get_model('lettings', 'Address')  # Access the new model

    for obj in OldModel.objects.all():
        NewModel.objects.create(number=obj.number, street=obj.street, city=obj.city, state=obj.state, zip_code=obj.zip_code, country_iso_code=obj.country_iso_code)

def migrate_letting(apps, schema_editor):
    OldModel = apps.get_model('oc_lettings_site', 'Letting')  # Access the old model
    NewModel = apps.get_model('lettings', 'Letting')  # Access the new model
    AddressObj = apps.get_model('lettings', 'Address')

    for obj in OldModel.objects.all():
        NewModel.objects.create(title=obj.title, address=AddressObj.objects.get(id=obj.address.id))

class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),  # Replace with the actual initial migration name
        ('oc_lettings_site', '0001_initial'),  # Replace with the last migration for app1
    ]

    operations = [
        migrations.RunPython(migrate_address),
        migrations.RunPython(migrate_letting),
    ]

