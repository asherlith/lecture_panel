# Generated by Django 5.0.6 on 2024-06-06 17:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_remove_profile_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudyField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('corequisite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='co_courses', to='course.course')),
                ('prerequisite', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pre_courses', to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('times', models.JSONField(default=dict)),
                ('credits_count', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='course.course')),
                ('lecturer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lectures', to='course.lecturer')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='user.profile')),
            ],
        ),
        migrations.CreateModel(
            name='StudentLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lectures', to='course.lecture')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='course.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='lectures',
            field=models.ManyToManyField(blank=True, null=True, through='course.StudentLecture', to='course.lecture'),
        ),
        migrations.AddField(
            model_name='student',
            name='study_field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='course.studyfield'),
        ),
        migrations.AddField(
            model_name='lecturer',
            name='study_field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lecturers', to='course.studyfield'),
        ),
    ]
