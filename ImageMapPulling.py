
import requests

def getImage(date, cord):
    url = 'https://wvs.earthdata.nasa.gov/api/v1/snapshot?REQUEST=GetSnapshot&&CRS=EPSG:4326&WRAP=DAY&LAYERS=MODIS_Terra_CorrectedReflectance_Bands721&FORMAT=image/jpeg&HEIGHT=800&WIDTH=800&BBOX='+ cord + '&TIME=' + date
    page = requests.get(url)
    f_ext = 'Input_map.jpg'
    with open(f_ext, 'wb') as f:
        f.write(page.content)
        
    return 1    