# Generated by Django 2.1.7 on 2019-02-28 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=50)),
                ('IdentityNumber', models.IntegerField()),
                ('Image', models.ImageField(upload_to='static/teammembers/')),
                ('Bio', models.TextField()),
            ],
        ),
    ]
