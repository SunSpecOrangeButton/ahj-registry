import csv
import os
from django.contrib.gis.utils import LayerMapping
from .models import *

BASE_DIR_SHP = os.path.expanduser('~/Downloads/2020CensusShapefiles/')


state_mapping = {
    'GEOID': 'GEOID',
    'NAME': 'NAME',
    'ALAND': 'ALAND',
    'AWATER': 'AWATER',
    'INTPTLAT': 'INTPTLAT',
    'INTPTLON': 'INTPTLON',
    'mpoly': 'MULTIPOLYGON'
}


county_mapping = {
    'STATEFP': 'STATEFP',
    'GEOID': 'GEOID',
    'NAME': 'NAME',
    'NAMELSAD': 'NAMELSAD',
    'ALAND': 'ALAND',
    'AWATER': 'AWATER',
    'INTPTLAT': 'INTPTLAT',
    'INTPTLON': 'INTPTLON',
    'mpoly': 'MULTIPOLYGON'
}


cousub_mapping = {
    'STATEFP': 'STATEFP',
    'GEOID': 'GEOID',
    'NAME': 'NAME',
    'NAMELSAD': 'NAMELSAD',
    'ALAND': 'ALAND',
    'AWATER': 'AWATER',
    'INTPTLAT': 'INTPTLAT',
    'INTPTLON': 'INTPTLON',
    'mpoly': 'MULTIPOLYGON'
}


city_mapping = {
    'STATEFP': 'STATEFP',
    'GEOID': 'GEOID',
    'NAME': 'NAME',
    'NAMELSAD': 'NAMELSAD',
    'ALAND': 'ALAND',
    'AWATER': 'AWATER',
    'INTPTLAT': 'INTPTLAT',
    'INTPTLON': 'INTPTLON',
    'mpoly': 'MULTIPOLYGON'
}


def upload_all_shapefile_types():
    upload_state_shapefiles()
    upload_county_shapefiles()
    upload_city_shapefiles()
    upload_countysubdivision_shapefiles()


def upload_state_shapefiles():
    for subdir in os.walk(BASE_DIR_SHP + 'States'):
        for file in subdir[2]:
            if file.endswith('.shp'):
                state_shp = os.path.join(subdir[0], file)
                lm = LayerMapping(StateTemp, state_shp, state_mapping, transform=False)
                lm.save(strict=True, verbose=True)


def upload_county_shapefiles():
    for subdir in os.walk(BASE_DIR_SHP + 'Counties'):
        for file in subdir[2]:
            if file.endswith('.shp'):
                county_shp = os.path.join(subdir[0], file)
                lm = LayerMapping(CountyTemp, county_shp, county_mapping, transform=False)
                lm.save(strict=True, verbose=True)


def upload_city_shapefiles():
    for subdir in os.walk(BASE_DIR_SHP + 'Places'):
        for file in subdir[2]:
            if file.endswith('.shp'):
                city_shp = os.path.join(subdir[0], file)
                lm = LayerMapping(CityTemp, city_shp, city_mapping, transform=False)
                lm.save(strict=True, verbose=True)


def upload_countysubdivision_shapefiles():
    for subdir in os.walk(BASE_DIR_SHP + 'CountySubdivisions'):
        for file in subdir[2]:
            if file.endswith('.shp'):
                cousub_shp = os.path.join(subdir[0], file)
                lm = LayerMapping(CousubTemp, cousub_shp, cousub_mapping, transform=False)
                lm.save(strict=True, verbose=True)


def get_polygon_fields(obj):
    return {
        'Name': obj.NAME,
        'GEOID': obj.GEOID,
        'Polygon': obj.mpoly,
        'LandArea': obj.ALAND,
        'WaterArea': obj.AWATER,
        'InternalPLatitude': obj.INTPTLAT,
        'InternalPLongitude': obj.INTPTLON
    }


def get_state_polygon_type_fields(obj, polygon):
    return {
        'PolygonID': polygon,
        'FIPSCode': obj.GEOID
    }


def get_other_polygon_type_fields(obj, polygon):
    return {
        'PolygonID': polygon,
        'StatePolygonID': StatePolygon.objects.get(FIPSCode=obj.GEOID[:2]),
        'LSAreaCodeName': obj.NAMELSAD
    }


def translate_polygons():
    translate_states()
    translate_counties()
    translate_cities()
    translate_countysubdivisions()


def translate_states():
    states = StateTemp.objects.all()
    count = states.count()
    i = 0
    for state in states:
        polygon = Polygon.objects.create(**get_polygon_fields(state))
        StatePolygon.objects.create(**get_state_polygon_type_fields(state, polygon))
        print("pair_polygons_ahjs {1}: {0:.0%}".format(i/count, StateTemp.__name__))
        i += 1


def translate_counties():
    counties = CountyTemp.objects.all()
    count = counties.count()
    i = 0
    for county in counties:
        polygon = Polygon.objects.create(**get_polygon_fields(county))
        CountyPolygon.objects.create(**get_other_polygon_type_fields(county, polygon))
        print("pair_polygons_ahjs {1}: {0:.0%}".format(i/count, CountyTemp.__name__))
        i += 1


def translate_cities():
    cities = CityTemp.objects.all()
    count = cities.count()
    i = 0
    for city in cities:
        polygon = Polygon.objects.create(**get_polygon_fields(city))
        CityPolygon.objects.create(**get_other_polygon_type_fields(city, polygon))
        print("pair_polygons_ahjs {1}: {0:.0%}".format(i/count, CityPolygon.__name__))
        i += 1


def translate_countysubdivisions():
    cousubs = CousubTemp.objects.all()
    count = cousubs.count()
    i = 0
    for cousub in cousubs:
        polygon = Polygon.objects.create(**get_polygon_fields(cousub))
        CountySubdivisionPolygon.objects.create(**get_other_polygon_type_fields(cousub, polygon))
        print("pair_polygons_ahjs {1}: {0:.0%}".format(i/count, CountySubdivisionPolygon.__name__))
        i += 1


def is_zero_depth_field(name):
    if name.find('.') != -1 and name.find('.') == name.rfind('.'):
        return True
    return False


def build_field_val_dict(row):
    result = {}
    last_sub_obj = ''
    for i, (k, v) in enumerate(row.items()):
        field = k[:k.find('.')]
        if v == '' or last_sub_obj == field:
            continue
        elif is_zero_depth_field(k):
            result[field] = v
        elif k != '':
            subrow = {}
            for i, (k, v) in enumerate(row.items()):
                if v == '':
                    continue
                if k.startswith(field):
                    subrow[k[len(field) + 1:]] = v
            last_sub_obj = field
            if field.find('[') >= 0:
                array_field = field[:field.find('[')]
                if array_field not in result:
                    result[array_field] = []
                result[array_field].append(build_field_val_dict(subrow))
            else:
                result[field] = build_field_val_dict(subrow)

    return result


def create_address(address_dict):
    location_dict = address_dict.pop('Location', None)
    if location_dict is not None:
        address_dict['LocationID'] = create_location(location_dict)
    return Address.objects.create(**address_dict)


def create_location(location_dict):
    return Location.objects.create(**location_dict)


def create_contact(contact_dict):
    address_dict = contact_dict.pop('Address', None)
    if address_dict is not None:
        contact_dict['AddressID'] = create_address(address_dict)
    else:
        contact_dict['AddressID'] = Address.objects.create()
    return Contact.objects.create(**contact_dict)


def load_ahj_data_csv():
    with open(BASE_DIR_SHP + 'AHJRegistryData/ahjregistrydata.csv') as file:
        reader = csv.DictReader(file, delimiter=',', quotechar='"')
        i = 1
        for row in reader:
            ahj_dict = build_field_val_dict(row)
            contacts_dict = ahj_dict.pop('Contacts', [])
            contacts = []
            for contact_dict in contacts_dict:
                contacts.append(create_contact(contact_dict))
            address_dict = ahj_dict.pop('Address', None)
            if address_dict is not None:
                ahj_dict['AddressID'] = create_address(address_dict)
            else:
                ahj_dict['AddressID'] = Address.objects.create()
            ahj = AHJ.objects.create(**ahj_dict)
            for contact in contacts:
                AHJContactRepresentative.objects.create(AHJPK=ahj, ContactID=contact, ContactStatus=1)
            print('AHJ {0}: {1}'.format(ahj.AHJID, i))
            i += 1


state_fips_to_abbr = {
    '01': 'AL',
    '02': 'AK',
    '60': 'AS',
    '04': 'AZ',
    '05': 'AR',
    '81': 'BI',
    '06': 'CA',
    '08': 'CO',
    '09': 'CT',
    '10': 'DE',
    '11': 'DC',
    '12': 'FL',
    '64': 'FM',
    '13': 'GA',
    '66': 'GU',
    '15': 'HI',
    '16': 'ID',
    '17': 'IL',
    '18': 'IN',
    '19': 'IA',
    '86': 'JI',
    '67': 'JA',
    '20': 'KS',
    '21': 'KY',
    '89': 'KR',
    '22': 'LA',
    '23': 'ME',
    '68': 'MH',
    '24': 'MD',
    '25': 'MA',
    '26': 'MI',
    '71': '71',  # Territory abbr collides with state abbr
    '27': 'MN',
    '28': 'MS',
    '29': 'MO',
    '30': 'MT',
    '76': '76',  # Territory abbr collides with state abbr
    '31': 'NE',
    '32': 'NV',
    '33': 'NH',
    '34': 'NJ',
    '35': 'NM',
    '36': 'NY',
    '37': 'NC',
    '38': 'ND',
    '69': 'MP',
    '39': 'OH',
    '40': 'OK',
    '41': 'OR',
    '70': 'PW',
    '95': '95',  # Territory abbr collides with state abbr
    '42': 'PA',
    '72': 'PR',
    '44': 'RI',
    '45': 'SC',
    '46': 'SD',
    '47': 'TN',
    '48': 'TX',
    '74': 'UM',
    '49': 'UT',
    '50': 'VT',
    '51': 'VA',
    '78': 'VI',
    '53': 'WA',
    '54': 'WV',
    '55': 'WI',
    '56': 'WY'
}

abbr_to_state_fips = dict(map(reversed, state_fips_to_abbr.items()))


def pair_all():
    AHJ.objects.all().update(PolygonID=None)
    pair_polygons(CountyPolygon)
    pair_polygons(CityPolygon)
    pair_polygons(CountySubdivisionPolygon)
    pair_state_polygons()


def pair_polygons(model):
    polgyons = model.objects.all()
    ahjs = AHJ.objects.filter(PolygonID=None).order_by('AddressID__StateProvince')
    i = 0
    total = len(ahjs)
    # Pair polygons
    current_state_fips = ''
    temp_polygons = model.objects.none()
    for ahj in ahjs:
        addr = Address.objects.get(AddressID=ahj.AddressID.AddressID)
        temp_state_fips = abbr_to_state_fips[addr.StateProvince]
        if current_state_fips != temp_state_fips:
            current_state_fips = temp_state_fips
            temp_polygons = polgyons.filter(PolygonID__GEOID__startswith=current_state_fips).order_by('LSAreaCodeName')
        polygon_index = binary_search(temp_polygons, ahj.AHJName)
        if polygon_index != -1:
            polygon = temp_polygons[polygon_index]
            ahj.PolygonID = polygon.PolygonID
            ahj.save()
        i += 1
        print("pair_polygons_ahjs {1}: {0:.0%}".format(i/total, model.__name__))


def pair_state_polygons():
    # Pair states
    states = StatePolygon.objects.all()
    i = 0
    total = len(states)
    for state in states:
        ahj = AHJ.objects.get(AHJName=state.PolygonID.Name + ' state')
        ahj.PolygonID = state.PolygonID
        ahj.save()
        i += 1
        print("pair_polygons_ahjs {1}: {0:.0%}".format(i/total, StatePolygon.__name__))


# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    x = x.lower()

    while low <= high:
        mid = (high + low) // 2
        # Check if x is present at mid
        if arr[mid].LSAreaCodeName.lower() < x:
            low = mid + 1

        # If x is greater, ignore left half
        elif arr[mid].LSAreaCodeName.lower() > x:
            high = mid - 1

        # If x is smaller, ignore right half
        else:
            return mid

            # If we reach here, then the element was not present
    return -1
