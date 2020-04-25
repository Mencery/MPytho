# Generated by Django 3.0.5 on 2020-04-21 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20200421_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='polls.Question')),
                ('answered_time', models.IntegerField()),
                ('right_answered_time', models.IntegerField()),
            ],
        ),
    ]