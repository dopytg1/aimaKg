# Generated by Django 4.1 on 2022-09-14 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=225, unique=True)),
                ('text', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('slug', models.SlugField(max_length=225, unique=True)),
                ('photo', models.ImageField(null=True, upload_to='photos/%y/%m/%d')),
                ('price', models.IntegerField(default=0)),
                ('text', models.TextField(null=True)),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sewingRoom.categories')),
            ],
            options={
                'verbose_name': 'Одежда',
                'verbose_name_plural': 'Одежда',
                'ordering': ['title'],
            },
        ),
    ]
