# Generated by Django 5.1.5 on 2025-02-05 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('credit_hours', models.PositiveIntegerField()),
                ('grade', models.CharField(choices=[('select grade', 'Select Grade'), ('grade 9', 'Grade 9'), ('grade 10', 'Grade 10'), ('grade 11', 'Grade 11'), ('grade 12', 'Grade 12')], default='select grade', max_length=50)),
                ('description', models.TextField()),
                ('prerequisites', models.CharField(choices=[('basic mathematics', 'Basic mathematics'), ('introduction to physics', 'Introduction to physics'), ('basic chemistry', 'Basic chemistry'), ('english language', 'English language')], max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='departments.department')),
            ],
        ),
    ]
