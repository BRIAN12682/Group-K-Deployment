# Generated by Django 4.0.6 on 2022-07-20 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('std_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('book_title', models.CharField(max_length=70)),
                ('publication_date', models.DateField(verbose_name='publication date')),
                ('subject_area', models.CharField(max_length=70)),
                ('author', models.CharField(max_length=40)),
                ('availability', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Borrowedbooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField(auto_now_add=True)),
                ('bks_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bookid', to='Homeapp.books')),
                ('std_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stdNumber', to='std_app.std_model')),
            ],
        ),
    ]
