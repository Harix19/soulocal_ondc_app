# Generated by Django 3.1.7 on 2022-07-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_search', '0005_auto_20220726_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apicontextprovider',
            old_name='PROVIDER_RANGEDAYS',
            new_name='PROVIDER_RANGEENDAYS',
        ),
        migrations.AddField(
            model_name='apicontextprovider',
            name='PROVIDER_RANGESTDAYS',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
    ]
