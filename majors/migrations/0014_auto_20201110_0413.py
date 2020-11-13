# Generated by Django 2.2.17 on 2020-11-10 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('majors', '0013_auto_20170918_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionproject',
            name='campus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='majors.Campus'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='campus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='majors.Campus'),
        ),
        migrations.AlterField(
            model_name='major',
            name='admission_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='majors.AdmissionProject'),
        ),
        migrations.AlterField(
            model_name='major',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='majors.Faculty'),
        ),
    ]
