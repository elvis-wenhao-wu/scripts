from collections import namedtuple
from pyproj import CRS, Transformer
from pyproj.aoi import AreaOfInterest
from pyproj.database import query_utm_crs_info
def wgs84_to_utm(
        geolat: float, 
        geolong: float
    ) -> tuple[int, int]:
    """Transform GPS Coordinate to UTM Coordinate based on Melbourne area"""
    
    # melbourne area
    south_lat_degree, north_lat_degree = -38.2, -37.8
    west_lon_degree, east_lon_degree = 144.92, 145.2
    
    # GPS reference frame
    crs_4326 = CRS("WGS84")
    # UTM (Universal Transverse Mercator) - Australia/Melbourne datum
    utm_crs_list = query_utm_crs_info(
        datum_name="WGS 84",
        area_of_interest=AreaOfInterest(
            west_lon_degree=west_lon_degree,
            south_lat_degree=south_lat_degree,
            east_lon_degree=east_lon_degree,
            north_lat_degree=north_lat_degree,
        ),
    )
    utm_crs = CRS.from_epsg(utm_crs_list[0].code)
    # Transformation between two CRS
    transformer = Transformer.from_crs(crs_4326, utm_crs)
    
    # Transform Operations
    def _wgs84_to_utm(
            geolat: float, 
            geolong: float, 
        ) -> tuple[int, int]:
        """
        Transform GPS latitude and longitude to UTM X and Y coordinates
        >>> coord_wgs84 = (-37.798334, 144.960977) # University of Melbourne
        >>> wgs84_to_utm(coord_wgs84)
        utmxy(geox=320480.58189754176, geoy=5814601.629670657)
        """
        utmxy = namedtuple('utmxy', 'geox, geoy')
        coord_utm = (coord for coord in transformer.transform(geolat, geolong))
        coord_utm = utmxy(*coord_utm)
        return coord_utm
    
    return _wgs84_to_utm(geolat = geolat, geolong = geolong)
