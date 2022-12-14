# Generated by Django 4.1 on 2022-09-23 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_students_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='votes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentid', models.CharField(max_length=5)),
                ('upvoted', models.CharField(max_length=3)),
            ],
        ),
        migrations.AlterModelOptions(
            name='students',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterField(
            model_name='students',
            name='student_email',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='student_sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=(('Male', 'Male'), ('Female', 'Female')), max_length=6),
        ),
    ]
