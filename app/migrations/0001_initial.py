# Generated by Django 3.1 on 2020-11-08 15:23

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
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=20)),
                ('country', models.CharField(choices=[('Europe', (('PT', 'Portugal'), ('ES', 'Spain'), ('FR', 'France'), ('NL', 'The Netherlands'), ('EN', 'England'))), ('America', (('CA', 'Canada'), ('US', 'United States of America'), ('BR', 'Brazil'))), ('Africa', (('AL', 'Algeria'), ('AN', 'Angola'))), ('Asia', (('CH', 'China'), ('CM', 'Cambodia'), ('IN', 'India'), ('JA', 'Japan'))), ('Oceania', (('AU', 'Australia'), ('NZ', 'New Zealand'), ('PO', 'Polynesia')))], max_length=100)),
                ('door', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument_name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('wind', 'wind'), ('strings', 'strings'), ('percussion', 'percussion')], max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('instrument_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.instrument')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(choices=[('Europe', (('PT', 'Portugal'), ('ES', 'Spain'), ('FR', 'France'), ('NL', 'The Netherlands'), ('EN', 'England'))), ('America', (('CA', 'Canada'), ('US', 'United States of America'), ('BR', 'Brazil'))), ('Africa', (('AL', 'Algeria'), ('AN', 'Angola'))), ('Asia', (('CH', 'China'), ('CM', 'Cambodia'), ('IN', 'India'), ('JA', 'Japan'))), ('Oceania', (('AU', 'Australia'), ('NZ', 'New Zealand'), ('PO', 'Polynesia')))], max_length=100)),
                ('logo', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_ts', models.TimeField()),
                ('payment_time', models.DateTimeField()),
                ('order_status', models.CharField(choices=[('PROC', 'Processing order'), ('DELIV', 'Sent to delivery'), ('SENT', 'On its way'), ('REC', 'Delivered at the address')], max_length=100)),
                ('delivery_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.address')),
            ],
        ),
        migrations.CreateModel(
            name='ProdList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.order')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nib', models.PositiveBigIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other / Rather not say')], max_length=100)),
                ('contact', models.PositiveBigIntegerField()),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=20)),
                ('country', models.CharField(choices=[('Europe', (('PT', 'Portugal'), ('ES', 'Spain'), ('FR', 'France'), ('NL', 'The Netherlands'), ('EN', 'England'))), ('America', (('CA', 'Canada'), ('US', 'United States of America'), ('BR', 'Brazil'))), ('Africa', (('AL', 'Algeria'), ('AN', 'Angola'))), ('Asia', (('CH', 'China'), ('CM', 'Cambodia'), ('IN', 'India'), ('JA', 'Japan'))), ('Oceania', (('AU', 'Australia'), ('NZ', 'New Zealand'), ('PO', 'Polynesia')))], max_length=100)),
                ('door', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.person'),
        ),
        migrations.AddField(
            model_name='instrument',
            name='manufacturer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.manufacturer'),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('A', 'Admin'), ('S', 'Staff')], max_length=10)),
                ('employee_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.person')),
            ],
        ),
    ]
