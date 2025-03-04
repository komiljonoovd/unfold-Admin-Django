# Generated by Django 5.1.6 on 2025-02-15 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=128)),
                ('isdeleted', models.BooleanField(default=False)),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('modifiedon', models.DateTimeField(auto_now=True)),
                ('createdby', models.CharField(blank=True, max_length=128, null=True)),
                ('modifiedby', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'Report Admin',
                'verbose_name_plural': 'Report Admin',
                'db_table': 'Report Admin',
            },
        ),
    ]
