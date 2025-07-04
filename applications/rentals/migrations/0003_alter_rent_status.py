# Generated by Django 5.2.1 on 2025-05-29 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Очікується'), ('CONFIRMED', 'Підтверджено'), ('CANCELLED', 'Відміненно'), ('DECLINED', 'Відмовлено'), ('COMPLETED', 'Завершено')], default='PENDING', max_length=10),
        ),
    ]
