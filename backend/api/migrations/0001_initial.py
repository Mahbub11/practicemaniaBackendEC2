# Generated by Django 4.0.10 on 2023-11-18 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articals',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('type', models.IntegerField(default=1)),
                ('content', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listening',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('level', models.IntegerField(default=1)),
                ('total_tested', models.BigIntegerField(default=0)),
                ('type', models.IntegerField(default=5)),
                ('inner_type', models.IntegerField()),
                ('time', models.DecimalField(decimal_places=1, default=2, max_digits=19)),
                ('qa', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('explain', models.CharField(blank=True, max_length=600, null=True)),
                ('level', models.IntegerField(default=1)),
                ('total_tested', models.BigIntegerField(default=0)),
                ('type', models.IntegerField(default=3)),
                ('inner_type', models.IntegerField()),
                ('time', models.DecimalField(decimal_places=1, default=2, max_digits=19)),
                ('qa', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Speaking',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=1)),
                ('total_tested', models.BigIntegerField(default=0)),
                ('type', models.IntegerField(default=4)),
                ('inner_type', models.IntegerField()),
                ('time', models.FloatField(default=2)),
                ('qa', models.JSONField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatisticDUOLINGO',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('qn', models.BigIntegerField(blank=True, default=0, null=True)),
                ('level', models.IntegerField(default=1)),
                ('type', models.IntegerField(default=5)),
                ('inner_type', models.IntegerField()),
                ('time', models.DecimalField(decimal_places=1, max_digits=19)),
                ('result', models.DecimalField(decimal_places=2, max_digits=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=1)),
                ('total_tested', models.BigIntegerField(default=0)),
                ('type', models.IntegerField(default=1)),
                ('inner_type', models.IntegerField(default=11)),
                ('time', models.DecimalField(decimal_places=1, default=2, max_digits=19)),
                ('qa', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Writing',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('level', models.IntegerField(default=1)),
                ('total_tested', models.BigIntegerField(default=0)),
                ('type', models.IntegerField(default=2)),
                ('inner_type', models.IntegerField()),
                ('time', models.DecimalField(decimal_places=1, default=2, max_digits=19)),
                ('qa', models.JSONField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
