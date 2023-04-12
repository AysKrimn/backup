# Generated by Django 4.1.1 on 2023-03-27 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=50, verbose_name='Ürünün adı')),
                ('urunDetayi', models.TextField(max_length=200, verbose_name='Ürün hakkında açıklama')),
                ('eklenmeTarihi', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]