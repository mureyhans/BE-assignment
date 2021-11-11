# Generated by Django 3.2.9 on 2021-11-04 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_num', models.CharField(max_length=15)),
                ('name', models.CharField(blank=True, default=models.CharField(max_length=15), max_length=60)),
                ('email_address', models.EmailField(blank=True, default='', max_length=320)),
            ],
        ),
        migrations.CreateModel(
            name='ContactList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ContactListDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.contact')),
                ('contact_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.contactlist')),
            ],
        ),
        migrations.AddField(
            model_name='contactlist',
            name='contacts',
            field=models.ManyToManyField(through='contacts.ContactListDetail', to='contacts.Contact'),
        ),
    ]