# Generated by Django 5.0.4 on 2024-05-25 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0010_ingredient_safety'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='safety',
            field=models.CharField(blank=True, choices=[('S', 'Safe'), ('N', 'Neutral'), ('R', 'Risky')], default='N', max_length=1, null=True),
        ),
    ]
