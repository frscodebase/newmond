# Generated by Django 4.2.2 on 2023-06-08 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Industries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='JbImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_images', models.URLField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='JobFunctions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobFunction', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=5000)),
                ('link', models.URLField(max_length=5000)),
                ('date_posted', models.CharField(max_length=100)),
                ('job_payment', models.CharField(max_length=1000)),
                ('industries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_industries', to='monday.industries')),
                ('jb_images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='monday.jbimage')),
                ('job_function', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_functions', to='monday.jobfunctions')),
                ('job_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_types', to='monday.type')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_locations', to='monday.location')),
            ],
        ),
        migrations.CreateModel(
            name='JobDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(max_length=20000)),
                ('bold', models.BooleanField(default=False)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_details', to='monday.jobs')),
            ],
        ),
    ]
