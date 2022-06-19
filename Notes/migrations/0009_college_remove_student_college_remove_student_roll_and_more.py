# Generated by Django 4.0.4 on 2022-06-19 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0008_rename_year_student_year_of_paasing_student_college'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('College_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('College_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='College',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Roll',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='Emp_id',
        ),
        migrations.AddField(
            model_name='teacher',
            name='id',
            field=models.BigAutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='Email',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='student',
            name='College_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Notes.college'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='College_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Notes.college'),
            preserve_default=False,
        ),
    ]