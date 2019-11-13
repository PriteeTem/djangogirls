# Generated by Django 2.2.7 on 2019-11-13 21:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.CharField(help_text='Request ID', max_length=20)),
                ('link_session_id', models.CharField(help_text='Session ID', max_length=20)),
                ('plaid_access_token', models.CharField(help_text='Access Token', max_length=20)),
                ('item_id', models.CharField(help_text='Item ID', max_length=20)),
                ('institution_id', models.CharField(help_text='Insitution ID', max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
