from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_auto_20221209_0311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='pizza',
            name='date_added',
        ),
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=models.TextField(max_length=100),
        ),
    ]
