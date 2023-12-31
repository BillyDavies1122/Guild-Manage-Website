# Generated by Django 4.1.7 on 2023-09-30 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='guild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guildName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characterName', models.CharField(max_length=30)),
                ('characterClass', models.CharField(choices=[('Mage', 'Mage'), ('Warrior', 'Warrior'), ('Warlock', 'Warlock'), ('Rogue', 'Rogue'), ('DeathKnight', 'Death Knight'), ('Priest', 'Priest'), ('Hunter', 'Hunter'), ('Shaman', 'Shaman'), ('Paladin', 'Paladin'), ('Druid', 'Druid')], max_length=50)),
                ('characterGuild', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guild.guild')),
            ],
        ),
    ]
