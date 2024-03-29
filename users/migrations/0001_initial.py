# Generated by Django 4.2.5 on 2023-10-06 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('display_name', models.CharField(blank=True, max_length=150, null=True)),
                ('full_name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
            ],
            options={
                'indexes': [models.Index(fields=['username'], name='users_user_usernam_65d164_idx')],
            },
        ),
    ]
