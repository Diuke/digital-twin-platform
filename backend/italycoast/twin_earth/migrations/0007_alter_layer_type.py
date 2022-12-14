# Generated by Django 3.2.5 on 2022-02-10 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twin_earth', '0006_alter_layer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='type',
            field=models.CharField(choices=[('WFS', 'WFS'), ('WMS', 'WMS'), ('WMST', 'WMST'), ('ARCGIS_IS', 'ArcGIS ImageServer'), ('ARCGIS_MS', 'ArcGIS MapServer')], max_length=256),
        ),
    ]
