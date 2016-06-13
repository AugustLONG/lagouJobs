# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobsNewsItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('idnumber', models.IntegerField(null=True, blank=True)),
                ('positionname', models.CharField(max_length=400, null=True, blank=True)),
                ('salary', models.CharField(max_length=400, null=True, blank=True)),
                ('companyname', models.CharField(max_length=400, null=True, blank=True)),
                ('positionid', models.URLField(max_length=400, null=True, blank=True)),
                ('createtime', models.CharField(max_length=400, null=True, blank=True)),
            ],
            options={
                'ordering': ['-createtime'],
            },
        ),
        migrations.CreateModel(
            name='JobsNewsItemSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='jobsnewsitem',
            name='item_set',
            field=models.ForeignKey(to='webapp.JobsNewsItemSet', null=True),
        ),
    ]
