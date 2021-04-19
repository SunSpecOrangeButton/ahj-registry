# Generated by Django 3.1.3 on 2021-03-10 23:30

import ahj_app.models
from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('UserID', models.AutoField(db_column='UserID', primary_key=True, serialize=False)),
                ('Username', models.CharField(db_column='Username', max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('Email', models.CharField(db_column='Email', max_length=254, unique=True)),
                ('is_staff', models.BooleanField(db_column='IsStaff', default=False)),
                ('is_active', models.BooleanField(db_column='IsActive', default=False)),
                ('SignUpDate', models.DateField(blank=True, db_column='SignUpDate')),
                ('PersonalBio', models.CharField(blank=True, db_column='PersonalBio', max_length=255)),
                ('URL', models.CharField(blank=True, db_column='URL', max_length=255, null=True)),
                ('CompanyAffiliation', models.CharField(blank=True, db_column='CompanyAffiliation', max_length=255)),
                ('Photo', models.CharField(blank=True, db_column='Photo', max_length=255, null=True)),
                ('IsPeerReviewer', models.IntegerField(db_column='IsPeerReviewer', default=False, null=True)),
                ('NumReviewsDone', models.IntegerField(db_column='NumReviewsDone', default=0)),
                ('AcceptedEdits', models.IntegerField(db_column='NumAcceptedEdits', default=0)),
                ('SubmittedEdits', models.IntegerField(db_column='NumSubmittedEdits', default=0)),
                ('CommunityScore', models.IntegerField(db_column='CommunityScore', default=0)),
                ('SecurityLevel', models.IntegerField(db_column='SecurityLevel', default=3)),
            ],
            options={
                'db_table': 'User',
                'managed': True,
            },
            managers=[
                ('objects', ahj_app.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('AddressID', models.AutoField(db_column='AddressID', primary_key=True, serialize=False)),
                ('AddrLine1', models.CharField(blank=True, db_column='AddrLine1', max_length=100)),
                ('AddrLine2', models.CharField(blank=True, db_column='AddrLine2', max_length=100)),
                ('AddrLine3', models.CharField(blank=True, db_column='AddrLine3', max_length=100)),
                ('City', models.CharField(blank=True, db_column='City', max_length=100)),
                ('Country', models.CharField(blank=True, db_column='Country', max_length=100)),
                ('County', models.CharField(blank=True, db_column='County', max_length=100)),
                ('StateProvince', models.CharField(blank=True, db_column='StateProvince', max_length=100)),
                ('ZipPostalCode', models.CharField(blank=True, db_column='ZipPostalCode', max_length=100)),
                ('Description', models.CharField(blank=True, db_column='Description', max_length=255)),
                ('AddressType', models.CharField(choices=[('', ''), ('Mailing', 'Mailing'), ('Billing', 'Billing'), ('Installation', 'Installation'), ('Shipping', 'Shipping')], db_column='AddressType', max_length=12)),
            ],
            options={
                'db_table': 'Address',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AHJ',
            fields=[
                ('AHJPK', models.AutoField(db_column='AHJPK', primary_key=True, serialize=False)),
                ('AHJID', models.CharField(db_column='AHJID', max_length=36, unique=True)),
                ('AHJCode', models.CharField(blank=True, db_column='AHJCode', max_length=20)),
                ('AHJLevelCode', models.CharField(choices=[('', ''), ('040', 'State'), ('050', 'State County'), ('061', 'State County Minor Civil Division'), ('162', 'State Incorporated Place')], db_column='AHJLevelCode', max_length=3)),
                ('AHJName', models.CharField(db_column='AHJName', max_length=100)),
                ('Description', models.CharField(blank=True, db_column='Description', max_length=255)),
                ('DocumentSubmissionMethodNotes', models.CharField(blank=True, db_column='DocumentSubmissionMethodNotes', max_length=255)),
                ('PermitIssueMethodNotes', models.CharField(blank=True, db_column='PermitIssueMethodNotes', max_length=255)),
                ('EstimatedTurnaroundDays', models.IntegerField(db_column='EstimatedTurnaroundDays', null=True)),
                ('FileFolderURL', models.CharField(blank=True, db_column='FileFolderURL', max_length=255)),
                ('URL', models.CharField(blank=True, db_column='URL', max_length=2048)),
                ('BuildingCode', models.CharField(choices=[('', ''), ('2021IBC', '2021 IBC'), ('2018IBC', '2018 IBC'), ('2015IBC', '2015 IBC'), ('2012IBC', '2012 IBC'), ('2009IBC', '2009 IBC'), ('NoSolarRegulations', 'No Solar Regulations')], db_column='BuildingCode', max_length=18)),
                ('BuildingCodeNotes', models.CharField(blank=True, db_column='BuildingCodeNotes', max_length=255)),
                ('ElectricCode', models.CharField(choices=[('', ''), ('2020NEC', '2020 NEC'), ('2017NEC', '2017 NEC'), ('2014NEC', '2014 NEC'), ('2011NEC', '2011 NEC'), ('NoSolarRegulations', 'No Solar Regulations')], db_column='ElectricCode', max_length=18)),
                ('ElectricCodeNotes', models.CharField(blank=True, db_column='ElectricCodeNotes', max_length=255)),
                ('FireCode', models.CharField(choices=[('', ''), ('2021IFC', '2021 IFC'), ('2018IFC', '2018 IFC'), ('2015IFC', '2015 IFC'), ('2012IFC', '2012 IFC'), ('2009IFC', '2009 IFC'), ('NoSolarRegulations', 'No Solar Regulations')], db_column='FireCode', max_length=18)),
                ('FireCodeNotes', models.CharField(blank=True, db_column='FireCodeNotes', max_length=255)),
                ('ResidentialCode', models.CharField(choices=[('', ''), ('2021IRC', '2021 IRC'), ('2018IRC', '2018 IRC'), ('2015IRC', '2015 IRC'), ('2012IRC', '2012 IRC'), ('2009IRC', '2009 IRC'), ('NoSolarRegulations', 'No Solar Regulations')], db_column='ResidentialCode', max_length=18)),
                ('ResidentialCodeNotes', models.CharField(blank=True, db_column='ResidentialCodeNotes', max_length=255)),
                ('WindCode', models.CharField(choices=[('', ''), ('ASCE716', 'ASCE7-16'), ('ASCE710', 'ASCE7-10'), ('ASCE705', 'ASCE7-05'), ('SpecialWindZone', 'Special Wind Zone')], db_column='WindCode', max_length=15)),
                ('WindCodeNotes', models.CharField(blank=True, db_column='WindCodeNotes', max_length=255)),
                ('AddressID', models.ForeignKey(db_column='AddressID', on_delete=django.db.models.deletion.DO_NOTHING, to='ahj_app.address')),
            ],
            options={
                'db_table': 'AHJ',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AHJInspection',
            fields=[
                ('InspectionID', models.AutoField(db_column='InspectionID', primary_key=True, serialize=False)),
                ('InspectionType', models.CharField(choices=[('', ''), ('RoughIn', 'Rough In'), ('Final', 'Final'), ('Windstorm', 'Windstorm'), ('Electrical', 'Electrical'), ('Structural', 'Structural')], db_column='InspectionType', max_length=10)),
                ('AHJInspectionName', models.CharField(db_column='AHJInspectionName', max_length=255)),
                ('AHJInspectionNotes', models.CharField(blank=True, db_column='AHJInspectionNotes', max_length=255)),
                ('Description', models.CharField(blank=True, db_column='Description', max_length=255)),
                ('FileFolderURL', models.CharField(blank=True, db_column='FileFolderURL', max_length=255)),
                ('TechnicianRequired', models.IntegerField(db_column='TechnicianRequired', null=True)),
                ('InspectionStatus', models.IntegerField(db_column='InspectionStatus')),
                ('AHJPK', models.ForeignKey(db_column='AHJPK', on_delete=django.db.models.deletion.DO_NOTHING, to='ahj_app.ahj')),
            ],
            options={
                'db_table': 'AHJInspection',
                'managed': True,
                'unique_together': {('AHJPK', 'AHJInspectionName')},
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('LocationID', models.AutoField(db_column='LocationID', primary_key=True, serialize=False)),
                ('Altitude', models.DecimalField(db_column='Altitude', decimal_places=6, max_digits=15, null=True)),
                ('Elevation', models.DecimalField(db_column='Elevation', decimal_places=8, max_digits=17, null=True)),
                ('Latitude', models.DecimalField(db_column='Latitude', decimal_places=8, max_digits=10)),
                ('Longitude', models.DecimalField(db_column='Longitude', decimal_places=8, max_digits=11)),
                ('Description', models.CharField(blank=True, db_column='Description', max_length=255)),
                ('LocationDeterminationMethod', models.CharField(choices=[('', ''), ('GPS', 'GPS'), ('Survey', 'Survey'), ('AerialImage', 'Aerial Image'), ('EngineeringReport', 'Engineering Report'), ('AddressGeocoding', 'Address Geocoding'), ('Unknown', 'Unknown')], db_column='LocationDeterminationMethod', max_length=17)),
                ('LocationType', models.CharField(choices=[('', ''), ('DeviceSpecific', 'Device Specific'), ('SiteEntrance', 'Site Entrance'), ('GeneralProximity', 'General Proximity'), ('Warehouse', 'Warehouse')], db_column='LocationType', max_length=16)),
            ],
            options={
                'db_table': 'Location',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Polygon',
            fields=[
                ('PolygonID', models.AutoField(db_column='PolygonID', primary_key=True, serialize=False)),
                ('Name', models.CharField(db_column='Name', max_length=100)),
                ('GEOID', models.CharField(db_column='GEOID', max_length=7)),
                ('Polygon', django.contrib.gis.db.models.fields.MultiPolygonField(db_column='Polygon', srid=4326)),
                ('LandArea', models.BigIntegerField(db_column='LandArea')),
                ('WaterArea', models.BigIntegerField(db_column='WaterArea')),
                ('InternalPLatitude', models.DecimalField(db_column='InternalPLatitude', decimal_places=8, max_digits=10)),
                ('InternalPLongitude', models.DecimalField(db_column='InternalPLongitude', decimal_places=8, max_digits=11)),
            ],
            options={
                'db_table': 'Polygon',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='StatePolygon',
            fields=[
                ('PolygonID', models.OneToOneField(db_column='PolygonID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='ahj_app.polygon')),
                ('FIPSCode', models.CharField(db_column='FIPSCode', max_length=2)),
            ],
            options={
                'db_table': 'StatePolygon',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WebpageToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='webpage_token', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Edit',
            fields=[
                ('EditID', models.AutoField(db_column='EditID', primary_key=True, serialize=False)),
                ('AHJPK', models.IntegerField(db_column='AHJPK')),
                ('SourceTable', models.CharField(db_column='SourceTable', max_length=255)),
                ('SourceColumn', models.CharField(db_column='SourceColumn', max_length=255)),
                ('SourceRow', models.IntegerField(db_column='SourceRow')),
                ('Comments', models.CharField(blank=True, db_column='Comments', max_length=255)),
                ('OldValue', models.CharField(blank=True, db_column='OldValue', max_length=255)),
                ('NewValue', models.CharField(blank=True, db_column='NewValue', max_length=255)),
                ('DateRequested', models.DateField(db_column='DateRequested')),
                ('DateEffective', models.DateField(blank=True, db_column='DateEffective', null=True)),
                ('ReviewStatus', models.CharField(db_column='ReviewStatus', max_length=1)),
                ('ApprovedBy', models.ForeignKey(db_column='ApprovedBy', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='related_secondary_edit', to=settings.AUTH_USER_MODEL)),
                ('ChangedBy', models.ForeignKey(db_column='ChangedBy', on_delete=django.db.models.deletion.DO_NOTHING, related_name='related_primary_edit', to=settings.AUTH_USER_MODEL)),
                ('InspectionID', models.ForeignKey(db_column='InspectionID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ahj_app.ahjinspection')),
            ],
            options={
                'db_table': 'Edit',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('ContactID', models.AutoField(db_column='ContactID', primary_key=True, serialize=False)),
                ('FirstName', models.CharField(blank=True, db_column='FirstName', max_length=255)),
                ('MiddleName', models.CharField(blank=True, db_column='MiddleName', max_length=255)),
                ('LastName', models.CharField(blank=True, db_column='LastName', max_length=255)),
                ('HomePhone', models.CharField(blank=True, db_column='HomePhone', max_length=15)),
                ('MobilePhone', models.CharField(blank=True, db_column='MobilePhone', max_length=15)),
                ('WorkPhone', models.CharField(blank=True, db_column='WorkPhone', max_length=15)),
                ('ContactType', models.CharField(choices=[('', ''), ('Homeowner', 'Homeowner'), ('OffTaker', 'Off Taker'), ('Inspector', 'Inspector'), ('Engineer', 'Engineer'), ('Originator', 'Originator'), ('Installer', 'Installer'), ('Investor', 'Investor'), ('PermittingOfficial', 'Permitting Official'), ('FireMarshal', 'Fire Marshal'), ('ProjectManager', 'Project Manager'), ('Salesperson', 'Salesperson')], db_column='ContactType', max_length=18)),
                ('ContactTimezone', models.CharField(blank=True, db_column='ContactTimezone', max_length=255)),
                ('Description', models.CharField(blank=True, db_column='Description', max_length=255)),
                ('Email', models.CharField(blank=True, db_column='Email', max_length=50)),
                ('Title', models.CharField(blank=True, db_column='Title', max_length=255)),
                ('URL', models.CharField(blank=True, db_column='URL', max_length=255)),
                ('PreferredContactMethod', models.CharField(choices=[('', ''), ('Email', 'Email'), ('WorkPhone', 'Work Phone'), ('CellPhone', 'Cell Phone'), ('HomePhone', 'Home Phone'), ('CellTextMessage', 'Cell Text Message')], db_column='PreferredContactMethod', max_length=15)),
                ('AddressID', models.ForeignKey(blank=True, db_column='AddressID', on_delete=django.db.models.deletion.DO_NOTHING, to='ahj_app.address')),
            ],
            options={
                'db_table': 'Contact',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('CommentID', models.AutoField(db_column='CommentID', primary_key=True, serialize=False)),
                ('CommentText', models.TextField(blank=True, db_column='CommentText', null=True)),
                ('AHJPK', models.IntegerField(db_column='AHJPK')),
                ('Date', models.DateTimeField(db_column='Date', default=django.utils.timezone.now)),
                ('ReplyingTo', models.IntegerField(db_column='ReplyingTo', null=True)),
                ('UserID', models.ForeignKey(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Comment',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='APIToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Key')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='api_token', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ahj',
            name='PolygonID',
            field=models.ForeignKey(db_column='PolygonID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ahj_app.polygon'),
        ),
        migrations.AddField(
            model_name='address',
            name='LocationID',
            field=models.ForeignKey(db_column='LocationID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ahj_app.location'),
        ),
        migrations.AddField(
            model_name='user',
            name='ContactID',
            field=models.ForeignKey(db_column='ContactID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ahj_app.contact'),
        ),
        migrations.CreateModel(
            name='FeeStructure',
            fields=[
                ('FeeStructurePK', models.AutoField(db_column='FeeStructurePK', primary_key=True, serialize=False)),
                ('FeeStructureID', models.CharField(db_column='FeeStructureID', max_length=36)),
                ('FeeStructureName', models.CharField(db_column='FeeStructureName', max_length=255, unique=True)),
                ('FeeStructureType', models.CharField(choices=[('', ''), ('Flat', 'Flat'), ('SystemSize', 'System Size')], db_column='FeeStructureType', max_length=10)),
                ('Description', models.CharField(blank=True, db_column='Description', max_length=255)),
                ('FeeStructureStatus', models.IntegerField(db_column='FeeStructureStatus')),
                ('AHJPK', models.ForeignKey(db_column='AHJPK', on_delete=django.db.models.deletion.DO_NOTHING, to='ahj_app.ahj')),
            ],
            options={
                'db_table': 'FeeStructure',
                'managed': True,
                'unique_together': {('FeeStructureID', 'AHJPK')},
            },
        ),
        migrations.CreateModel(
            name='CountyPolygon',
            fields=[
                ('PolygonID', models.OneToOneField(db_column='PolygonID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='ahj_app.polygon')),
                ('LSAreaCodeName', models.CharField(db_column='LSAreaCodeName', max_length=100)),
                ('StatePolygonID', models.ForeignKey(db_column='StatePolygonID', on_delete=django.db.models.deletion.DO_NOTHING, to='ahj_app.statepolygon')),
            ],
            options={
                'db_table': 'CountyPolygon',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CityPolygon',
            fields=[
                ('PolygonID', models.OneToOneField(db_column='PolygonID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='ahj_app.polygon')),
                ('LSAreaCodeName', models.CharField(db_column='LSAreaCodeName', max_length=100)),
                ('StatePolygonID', models.ForeignKey(db_column='StatePolygonID', on_delete=django.db.models.deletion.DO_NOTHING, to='ahj_app.statepolygon')),
            ],
            options={
                'db_table': 'CityPolygon',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AHJInspectionContact',
            fields=[
                ('RepresentativeID', models.AutoField(db_column='RepresentativeID', primary_key=True, serialize=False)),
                ('ContactStatus', models.IntegerField(db_column='ContactStatus')),
                ('ContactID', models.ForeignKey(db_column='ContactID', on_delete=django.db.models.deletion.DO_NOTHING, to='ahj_app.contact')),
                ('InspectionID', models.ForeignKey(db_column='InspectionID', on_delete=django.db.models.deletion.DO_NOTHING, to='ahj_app.ahjinspection')),
            ],
            options={
                'db_table': 'AHJInspectionContact',
                'managed': True,
                'unique_together': {('InspectionID', 'ContactID')},
            },
        ),
        migrations.CreateModel(
            name='AHJContactRepresentative',
            fields=[
                ('RepresentativeID', models.AutoField(db_column='RepresentativeID', primary_key=True, serialize=False)),
                ('ContactStatus', models.IntegerField(db_column='ContactStatus')),
                ('AHJPK', models.ForeignKey(db_column='AHJPK', on_delete=django.db.models.deletion.DO_NOTHING, to='ahj_app.ahj')),
                ('ContactID', models.ForeignKey(db_column='ContactID', on_delete=django.db.models.deletion.DO_NOTHING, to='ahj_app.contact')),
            ],
            options={
                'db_table': 'AHJContactRepresentative',
                'managed': True,
                'unique_together': {('AHJPK', 'ContactID')},
            },
        ),
    ]
