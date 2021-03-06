# Generated by Django 3.1.4 on 2021-01-02 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0002_comment_num_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ocena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('ocena', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Telefon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('memorija', models.CharField(max_length=20)),
                ('boja', models.CharField(max_length=20)),
                ('cena', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='ocena',
            name='idTelefona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baza.telefon'),
        ),
    ]
