import math

def distance_between(origin, destination):
    """Calculate the Haversine distance.
    
    Arguments:
    origin -- tuple of float (lat, long)
    destination -- tuple of float (lat, long)
    
    Return Value:
    distance_in_km -- float
    """

    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km

    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)
    a = (math.sin(delta_lat / 2) * math.sin(delta_lat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(delta_lon / 2) * math.sin(delta_lon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance_in_km = radius * c

    return distance_in_km