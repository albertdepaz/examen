# Generated by Django 3.0.4 on 2020-03-06 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0006_curso_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on wich the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now_add=True, help_text='Date time on wich the object was last modified.', verbose_name='modified at')),
                ('nota', models.IntegerField(blank=True)),
                ('alumno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='colegio.Curso')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]