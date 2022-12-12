from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0007_image_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
