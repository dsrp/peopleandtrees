# Generated by Django 2.0.4 on 2018-04-11 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('culture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Garden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GardenCosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(db_index=True)),
                ('amount', models.FloatField()),
            ],
            options={
                'verbose_name': 'cost',
                'verbose_name_plural': 'costs',
            },
        ),
        migrations.CreateModel(
            name='GardenCostsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'cost category',
                'verbose_name_plural': 'cost categories',
            },
        ),
        migrations.CreateModel(
            name='GardenCulture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.FloatField(help_text='square meter')),
                ('culture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture.Culture')),
                ('garden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden.Garden')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GardenLabour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(db_index=True)),
                ('amount', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GardenLabourCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GardenProduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(db_index=True)),
                ('amount', models.FloatField()),
                ('garden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden.Garden')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='gardenlabour',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='garden.GardenLabourCategory'),
        ),
        migrations.AddField(
            model_name='gardenlabour',
            name='garden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden.Garden'),
        ),
        migrations.AddField(
            model_name='gardencosts',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='garden.GardenCostsCategory'),
        ),
        migrations.AddField(
            model_name='gardencosts',
            name='garden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden.Garden'),
        ),
        migrations.AddField(
            model_name='garden',
            name='cultures',
            field=models.ManyToManyField(through='garden.GardenCulture', to='culture.Culture'),
        ),
    ]