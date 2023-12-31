# Generated by Django 4.2.4 on 2023-08-18 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wanted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('age', models.IntegerField()),
                ('state', models.CharField(max_length=60)),
                ('reward', models.DecimalField(decimal_places=2, max_digits=15)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Captured',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capture_time', models.DateTimeField()),
                ('inJail', models.BooleanField(default=False)),
                ('fugitive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wantedlist.wanted')),
            ],
        ),
    ]
