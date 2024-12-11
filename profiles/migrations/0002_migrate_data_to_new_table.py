from django.db import migrations

def migrate_profiles(apps, schema_editor):
    OldModel = apps.get_model('oc_lettings_site', 'Profile')  # Access the old model
    NewModel = apps.get_model('profiles', 'Profile')  # Access the new model
    UserModel = apps.get_model('auth', 'User')

    for obj in OldModel.objects.all():
        NewModel.objects.create(user=UserModel.objects.get(id=obj.user.id), favorite_city=obj.favorite_city)

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),  # Replace with the actual initial migration name
        ('oc_lettings_site', '0003_auto_20241211_1152'),  # Replace with the last migration for app1
    ]

    operations = [
        migrations.RunPython(migrate_profiles),
    ]
