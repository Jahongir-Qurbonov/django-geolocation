# import geoip2.database
from django.contrib.gis.geoip2 import GeoIP2


# Helper function to get the IP address of the client

def get_geo(ip):
    g = GeoIP2()
    country = g.country(ip)
    city = g.city(ip)
    lat, lon = g.lat_lon(ip)
    return country, city, lat, lon



# def get_country(ip):
#     reader = geoip2.database.Reader('GeoLite2-Country.mmdb')
#     response = reader.country(ip)
#     return response.country.name

# def get_city(ip):
#     reader = geoip2.database.Reader('GeoLite2-City.mmdb')
#     response = reader.city(ip)
#     return response.city.name

# def get_coordinates(ip):
#     reader = geoip2.database.Reader('GeoLite2-City.mmdb')
#     response = reader.city(ip)
#     return response.location.latitude, response.location.longitude

# def get_timezone(ip):
#     reader = geoip2.database.Reader('GeoLite2-City.mmdb')
#     response = reader.city(ip)
#     return response.location.time_zone

# def get_postal(ip):
#     reader = geoip2.database.Reader('GeoLite2-City.mmdb')
#     response = reader.city(ip)
#     return response.postal.code

# def get_asn(ip):
#     reader = geoip2.database.Reader('GeoLite2-ASN.mmdb')
#     response = reader.asn(ip)
#     return response.autonomous_system_organization

# def get_isp(ip):
#     reader = geoip2.database.Reader('GeoLite2-ASN.mmdb')
#     response = reader.asn(ip)
#     return response.autonomous_system_organization

# def get_all(ip):
#     reader = geoip2.database.Reader('GeoLite2-City.mmdb')
#     response = reader.city(ip)
#     return response

# if __name__ == '__main__':
#     ip = ''   # Enter your IP address here
#     print(get_country(ip)) # United States
#     print(get_city(ip)) # New York
#     print(get_coordinates(ip)) # (40.7142, -74.0064)
#     print(get_timezone(ip)) # America/New_York
#     print(get_postal(ip)) # 10007
#     print(get_asn(ip)) # AS15169 Google LLC
#     print(get_isp(ip)) # Google LLC
#     print(get_all(ip)) # <geoip2.models.City object at 0x7f8b8c0b4e80>
