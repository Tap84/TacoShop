# Generated by Django 2.2.5 on 2019-10-01 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tacocreate', '0002_auto_20190930_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taco',
            name='base_layer_choice',
            field=models.CharField(choices=[('Asian Style Tofu or Pork Marinade', 'Asian Style Tofu or Pork Marinade'), ('Baked Tilapia', 'Baked Tilapia'), ('Baja Beer Battered Fish', 'Baja Beer Battered Fish'), ('Basic Shredded Chicken', 'Basic Shredded Chicken'), ('Carnitas', 'Carnitas'), ('Chopped Steak', 'Chopped Steak'), ('Chorizo', 'Chorizo'), ('Crock Pot Pulled Pork', 'Crock Pot Pulled Pork'), ('Delengua (Beef Tongue)', 'Delengua (Beef Tongue)'), ('Garlic Black Beans', 'Garlic Black Beans'), ('Insane Garlic Ground Turkey', 'Insane Garlic Ground Turkey'), ('Lightly Seasoned Beef', 'Lightly Seasoned Beef'), ('Marinated Portobello Mushroom', 'Marinated Portobello Mushroom'), ('Moroccan Lamb', 'Moroccan Lamb'), ('North Carolina Battered Catfish', 'North Carolina Battered Catfish'), ('Overly Seasoned Ground Beef', 'Overly Seasoned Ground Beef'), ('Red Cabbage Filling', 'Red Cabbage Filling'), ('Soyrizo', 'Soyrizo'), ('Slow-Cooked Salsa Verde Chicken', 'Slow-Cooked Salsa Verde Chicken'), ('Swiss Chard', 'Swiss Chard'), ('Zucchini and Corn Filling', 'Zucchini and Corn Filling'), ('Better Than Powder Groundbeef', 'Better Than Powder Groundbeef'), ('Ground Beef (Traditional; US)', 'Ground Beef (Traditional; US)'), ('Moroccan Lamb', 'Moroccan Lamb'), ('Taco de rajas poblanas', 'Taco de rajas poblanas'), ('Boiled Ground Beef', 'Boiled Ground Beef'), ('Bulgar Black Bean Filling', 'Bulgar Black Bean Filling'), ("@deezthugs' Smokey Turkey Tacos", "@deezthugs' Smokey Turkey Tacos")], max_length=100),
        ),
        migrations.AlterField(
            model_name='taco',
            name='condiment_choice',
            field=models.CharField(choices=[('Pickled Vegetables', 'Pickled Vegetables'), ('Baja White Sauce', 'Baja White Sauce'), ('Beet Salsa', 'Beet Salsa'), ('Chipotlé Sauce', 'Chipotlé Sauce'), ('Guacamole', 'Guacamole'), ('Mango Avocado Salsa', 'Mango Avocado Salsa'), ('Phoning it in Pico de Gallo', 'Phoning it in Pico de Gallo'), ('Pickled Red Onions', 'Pickled Red Onions'), ('Salsa Sauce', 'Salsa Sauce'), ('Simple Salsa Verde', 'Simple Salsa Verde'), ('Roasted Tomatillo and Mushroom Sauce', 'Roasted Tomatillo and Mushroom Sauce'), ('Black Olives', 'Black Olives'), ('Salsa de chile de árbol', 'Salsa de chile de árbol'), ('Cashew Cheeze', 'Cashew Cheeze'), ('Guacamole (Simple)', 'Guacamole (Simple)'), ('Sour Cream', 'Sour Cream'), ('Cranberry Salsa', 'Cranberry Salsa'), ('Garlic Lime Sauce', 'Garlic Lime Sauce'), ('Mango Lime Salsa', 'Mango Lime Salsa'), ('Salsa de Aguacate', 'Salsa de Aguacate')], max_length=100),
        ),
        migrations.AlterField(
            model_name='taco',
            name='mixin_choice',
            field=models.CharField(choices=[('Corn Salad', 'Corn Salad'), ('Drunken Green Beans', 'Drunken Green Beans'), ('Sweet Potato and Apple Hash', 'Sweet Potato and Apple Hash'), ('Veggies for Fish Tacos', 'Veggies for Fish Tacos'), ('Potato Hash', 'Potato Hash'), ('Cheese (Traditional; US)', 'Cheese (Traditional; US)'), ('Lettuce (Traditional; US)', 'Lettuce (Traditional; US)'), ('Tomatoes (Traditional; US)', 'Tomatoes (Traditional; US)'), ('Traditional Taco Mixins', 'Traditional Taco Mixins'), ('Green Chile Cabbage Salad', 'Green Chile Cabbage Salad')], max_length=100),
        ),
        migrations.AlterField(
            model_name='taco',
            name='seasoning_choice',
            field=models.CharField(choices=[('Mahi Mahi Rub', 'Mahi Mahi Rub'), ('Packaged Seasonings', 'Packaged Seasonings'), ('Quick and Dirty Spice Mix', 'Quick and Dirty Spice Mix'), ('Sriracha Salt', 'Sriracha Salt'), ('Universal Taco Seasoning', 'Universal Taco Seasoning'), ('Zaatar', 'Zaatar')], max_length=100),
        ),
        migrations.AlterField(
            model_name='taco',
            name='shell_choice',
            field=models.CharField(choices=[('Fresh Corn Tortillas', 'Fresh Corn Tortillas'), ('Hard Corn Shells (Traditional; US)', 'Hard Corn Shells (Traditional; US)')], max_length=100),
        ),
    ]
