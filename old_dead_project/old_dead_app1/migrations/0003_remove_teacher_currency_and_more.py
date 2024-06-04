# Generated by Django 5.0.6 on 2024-06-04 20:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('old_dead_app1', '0002_currency_sciencedegree_teachingdegree_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='currency',
        ),
        migrations.AddField(
            model_name='teacher',
            name='currency_abbreviation',
            field=models.ForeignKey(default='USD', on_delete=django.db.models.deletion.PROTECT, to='old_dead_app1.currency', to_field='abbreviation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='currency',
            name='abbreviation',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]
