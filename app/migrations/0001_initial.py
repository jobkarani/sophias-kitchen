# Generated by Django 3.2.9 on 2022-05-01 20:14

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(blank=True, max_length=250)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='MpesaPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('type', models.TextField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.TextField()),
            ],
            options={
                'verbose_name': 'Mpesa Payment',
                'verbose_name_plural': 'Mpesa Payments',
            },
        ),
        migrations.CreateModel(
            name='NewsLetterRecipients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('county', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=50)),
                ('order_note', models.CharField(blank=True, max_length=100)),
                ('order_total', models.FloatField()),
                ('status', models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='New', max_length=10)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('is_ordered', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=144, null=True)),
                ('last_name', models.CharField(blank=True, max_length=144, null=True)),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('description', models.TextField(blank=True, max_length=500)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('flavour', models.CharField(choices=[('CHOCOLATE FUDGE', 'CHOCOLATE FUDGE'), ('CHOCOLATE MINT', 'CHOCOLATE MINT'), ('CHOCOLATE CHIP', 'CHOCOLATE CHIP'), ('RED VELVET', 'RED VELVET'), ('BLUE VELVET', 'BLUE VELVET'), ('GREEN VELVET', 'GREEN VELVET'), ('VANILLA', 'VANILLA'), ('COFFEE', 'COFFEE'), ('COCONUT', 'COCONUT'), ('GINGER', 'GINGER'), ('ZEBRA', 'ZEBRA'), ('CINNAMON', 'CINNAMON'), ('SPICE', 'SPICE'), ('MARBLE', 'MARBLE'), ('PINA COLADA', 'PINA COLADA'), ('LEMON', 'LEMON'), ('LIME', 'LIME'), ('BANANA', 'BANANA'), ('ORANGE', 'ORANGE'), ('PASSION JUICE', 'PASSION JUICE'), ('BUBBLEGUM', 'BUBBLEGUM'), ('CARROT', 'CARROT'), ('MINT', 'MINT'), ('OREO', 'OREO'), ('CARAMEL', 'CARAMEL'), ('BLUEBERRY', 'BLUEBERRY'), ('STRAWBERRY', 'STRAWBERRY'), ('BUTTER', 'BUTTER'), ('FRUIT', 'FRUIT'), ('BLACK FOREST', 'BLACK FOREST'), ('WHITE FOREST', 'WHITE FOREST'), ('BLUEBERRY FOREST', 'BLUEBERRY FOREST'), ('PASSION FRUIT FOREST', 'PASSION FRUIT FOREST')], default='VANILLA', max_length=60)),
                ('topping', models.CharField(choices=[('SKITTLES', 'SKITTLES'), ('GUMMIES', 'GUMMIES'), ('FRUITS', 'FRUITS'), ('NUTS', 'NUTS'), ('OREOS', 'OREOS'), ('CHERRIES', 'CHERRIES'), ('CAKE SAIL', 'CAKE SAIL'), ('CAKE TOPPERS', 'CAKE TOPPERS'), ('ASSORTED CHOCOLATES', 'ASSORTED CHOCOLATES')], default='GUMMIES', max_length=60)),
                ('size', models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], default='Medium', max_length=60)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variation_category', models.CharField(choices=[('flavour', 'flavour'), ('topping', 'topping'), ('size', 'size')], max_length=100)),
                ('variation_value', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('email', models.EmailField(max_length=256, null=True)),
                ('phone', models.CharField(max_length=100)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=100)),
                ('payment_method', models.CharField(max_length=100)),
                ('amount_paid', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product_price', models.FloatField()),
                ('ordered', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.order')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.payment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('variations', models.ManyToManyField(blank=True, to='app.Variation')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('variations', models.ManyToManyField(blank=True, to='app.Variation')),
            ],
        ),
    ]
