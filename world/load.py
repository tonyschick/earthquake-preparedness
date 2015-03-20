import os
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder
from .models import TsunamiZone

world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'mpoly' : 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for TsunamiZone model
tsunamizone_mapping = {
    'pid' : 'Id',
    'name' : 'Location',
    'location' : 'Location',
    'type' : 'Type',
    'geom' : 'MULTIPOLYGON',
}

world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/TM_WORLD_BORDERS-0.3.shp'))
tsunami_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/DOGAMI_TsunamiEvacuationZones_2013.shp'))

def run(verbose=True):
    lm = LayerMapping(WorldBorder, world_shp, world_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=False)
    lm2 = LayerMapping(TsunamiZone, tsunami_shp, tsunamizone_mapping,
                      transform=True, encoding='iso-8859-1')

    lm2.save(strict=True, verbose=verbose)