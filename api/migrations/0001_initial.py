# Generated by Django 4.0.4 on 2022-04-28 22:07

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('price', models.IntegerField(verbose_name='Price')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
