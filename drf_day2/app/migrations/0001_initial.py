# Generated by Django 2.0.6 on 2020-10-28 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.SmallIntegerField(choices=[(0, '男'), (1, '女')], default=0)),
                ('ke', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=12)),
                ('pic', models.ImageField(default='pic/1.jpg', upload_to='pic/')),
            ],
            options={
                'verbose_name': '教师',
                'verbose_name_plural': '教师',
                'db_table': 'teacher',
            },
        ),
    ]
