# Generated by Django 4.0.4 on 2022-06-16 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0005_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('Emp_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Email', models.CharField(max_length=50)),
                ('Phone', models.IntegerField()),
                ('Name', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('Stream_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.stream')),
            ],
        ),
    ]
