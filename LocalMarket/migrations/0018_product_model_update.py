from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('LocalMarket', '0017_product_product_image'), # Adjust this to the last successful migration
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(max_length=14, choices=[('Kg', 'Kg'), ('Lb', 'Lb'), ('Ltr', 'Ltr'), ('Each', 'Each')], null=True),
        ),
        migrations.RunSQL(
            "UPDATE LocalMarket_product SET unit = 'Kg' WHERE unit IS NULL",
            reverse_sql="UPDATE LocalMarket_product SET unit = NULL"
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(max_length=14, choices=[('Kg', 'Kg'), ('Lb', 'Lb'), ('Ltr', 'Ltr'), ('Each', 'Each')], null=False),
        ),
    ]
