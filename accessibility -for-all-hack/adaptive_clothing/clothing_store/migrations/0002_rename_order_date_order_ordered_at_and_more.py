# Generated by Django 5.1.1 on 2024-09-24 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing_store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_date',
            new_name='ordered_at',
        ),
        migrations.RemoveField(
            model_name='clothingitem',
            name='fabric_type',
        ),
        migrations.RemoveField(
            model_name='clothingitem',
            name='is_customizable',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery_address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='clothingitem',
            name='category',
            field=models.CharField(choices=[('Topwear', 'Topwear'), ('Bottomwear', 'Bottomwear'), ('Footwear', 'Footwear'), ('Accessories', 'Accessories')], default='general', max_length=50),
        ),
        migrations.AddField(
            model_name='clothingitem',
            name='fastening_type',
            field=models.CharField(choices=[('Zipper', 'Zipper'), ('Velcro', 'Velcro'), ('Buttons', 'Buttons'), ('Magnetic', 'Magnetic')], default='button', max_length=50),
        ),
        migrations.AddField(
            model_name='clothingitem',
            name='material',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='clothingitem',
            name='physical_condition',
            field=models.CharField(choices=[('Mobility', 'Mobility impairment'), ('Sensory', 'Sensory sensitivity'), ('Prosthetics', 'Use of prosthetics'), ('Other', 'Other needs')], default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='clothingitem',
            name='size',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(default='default123'),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='default', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='1234567890', max_length=15),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default='1'),
        ),
        migrations.AlterField(
            model_name='clothingitem',
            name='image',
            field=models.ImageField(blank=True, upload_to='clothing_items/'),
        ),
        migrations.AlterField(
            model_name='clothingitem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
    ]
