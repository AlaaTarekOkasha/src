# Generated by Django 4.0.7 on 2022-09-05 11:10

import core.models
import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testemonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=1000000)),
                ('image', models.ImageField(null=True, upload_to=core.models.testemonialsImageUpload)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('description', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=1000000, null=True), help_text='Please use ( , ) to add a new bullet point. Example: Educaction is important, Health is wealth', size=None)),
                ('image', models.ImageField(null=True, upload_to=core.models.trainersImageUpload)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('title', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField(max_length=1000000)),
                ('image', models.ImageField(null=True, upload_to=core.models.courseImageUpload)),
                ('price', models.IntegerField()),
                ('hours', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('content', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=1000000), help_text='Please use ( , ) to add a new bullet point. Example: Educaction is important, Health is wealth', size=None)),
                ('course_benefits', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=1000000), help_text='Please use ( , ) to add a new bullet point. Example: Educaction is important, Health is wealth', size=None)),
                ('user_criteria', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=1000000), help_text='Please use ( , ) to add a new bullet point. Example: Educaction is important, Health is wealth', size=None)),
                ('testemonials', models.ManyToManyField(related_name='testemonials', to='core.testemonial')),
                ('trainers', models.ManyToManyField(related_name='trainers', to='core.trainer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
