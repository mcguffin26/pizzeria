from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0005_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
    ]
