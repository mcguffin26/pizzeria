from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='topic',
            new_name='item',
        ),
    ]
