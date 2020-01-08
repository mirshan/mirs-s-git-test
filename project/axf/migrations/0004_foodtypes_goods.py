# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-12-27 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0003_mustbuy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foodtypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.IntegerField()),
                ('typename', models.CharField(max_length=50)),
                ('childtypenames', models.CharField(max_length=50)),
                ('typesort', models.IntegerField()),
                ('idDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField()),
                ('productimg', models.CharField(max_length=100)),
                ('productname', models.CharField(max_length=100)),
                ('productlongname', models.CharField(max_length=200)),
                ('isxf', models.BooleanField(default=0)),
                ('pmdesc', models.IntegerField()),
                ('specifics', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('marketprice', models.IntegerField()),
                ('categoryid', models.IntegerField()),
                ('childcid', models.IntegerField()),
                ('childcidname', models.CharField(max_length=50)),
                ('dealerid', models.IntegerField()),
                ('storenums', models.IntegerField()),
                ('productnum', models.IntegerField()),
            ],
        ),
    ]