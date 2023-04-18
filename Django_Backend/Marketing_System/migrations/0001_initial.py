# Generated by Django 4.2 on 2023-04-18 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marketer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.PositiveIntegerField()),
                ('withdrawal_threshold', models.PositiveIntegerField()),
                ('commission', models.DecimalField(decimal_places=2, max_digits=3)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('reference_link', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('title', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
