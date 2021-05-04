# Generated by Django 3.2 on 2021-04-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0009_conversationmessage_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='category',
            field=models.CharField(default='uncategorised', max_length=255),
        ),
    ]