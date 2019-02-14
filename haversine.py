# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 17:33:53 2019

@author: wialsh
"""
import numpy as np
from numpy import radians, cos, sin, arcsin, sqrt

## https://en.wikipedia.org/wiki/Earth_radius
# WGS-84 ellipsoid, Mean radius of semi-axes (R1)
r = 6371008.7714  # meters


def radius2degree(rad):
    return rad * 180.0 / np.pi

def degree2radius(deg):
    return deg * np.pi / 180.0


def calculate_the_center_point(coords):
    """
    https://stackoverflow.com/questions/6671183/calculate-the-center-point-of-multiple-latitude-longitude-coordinate-pairs
    a much earlier question: https://stackoverflow.com/questions/491738/how-do-you-calculate-the-average-of-a-set-of-circular-data/491784#491784
    :param coords: [(lng0, lat0), (lng1, lat1), ...]
    :return: (central_lat, central_lng)
    """
    assert len(coords) != 0

    longitudes, latitudes = zip(*coords)
    
    lat_degs = np.array(latitudes)
    lng_degs = np.array(longitudes)
    
    lat_rads = degree2radius(lat_degs)
    lng_rads = degree2radius(lng_degs)
    
    nums = lat_degs.shape[0]
    
    x = (np.cos(lat_rads) * np.cos(lng_rads)).sum() / nums
    y = (np.cos(lat_rads) * np.sin(lng_rads)).sum() / nums
    z = np.sin(lat_rads).sum() / nums

    #np.arctan2/np.arctan get the same of the output result.
    #but input: np.arctan(y/x) \ np.arctan2(y,x), so the input x elem for np.arctan must unequal 0.
    central_lng = np.arctan2(y, x)
    central_square_root = np.sqrt(x * x + y * y)
    central_lat = np.arctan2(z, central_square_root)
    
    central_lat = radius2degree(central_lat)
    central_lng = radius2degree(central_lng)
    
    return central_lng, central_lat

def haversine(coord0, coord1):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)

    """
    rad0 = radians(coord0)
    rad1 = radians(coord1)

    lat0, lng0 = rad0.T
    lat1, lng1 = rad1.T

    dlng = lng1 - lng0
    dlat = lat1 - lat0

    a = sin(dlat / 2) ** 2 + cos(lat0) * cos(lat1) * sin(dlng / 2) ** 2
    c = 2 * arcsin(sqrt(a))
    distances = c * r
    return distances


def haversine_matrix(coordinate):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    :param coordinate: `list` or `numpy.ndarray`
        e.g. coordinate = [[13.734766, 100.58556],
                           [13.734672, 100.585709],
                           [13.775265, 100.572233],
                           [13.789008, 100.574075],
                           [13.734734, 100.585628]]
    :return:
    """
    rads = radians(coordinate)

    nums = rads.shape[0]

    lats, lngs = rads.T

    shifts_lats_x, shifts_lats_y = np.meshgrid(lats, lats)
    shifts_lngs_x, shifts_lngs_y = np.meshgrid(lngs, lngs)
    # shifts_x = np.vstack((shifts_lats_x.ravel(),shifts_lngs_x.ravel())).T
    # shifts_y = np.vstack((shifts_lats_y.ravel(),shifts_lngs_y.ravel())).T

    lat0, lng0 = shifts_lats_x.ravel(), shifts_lngs_x.ravel()
    lat1, lng1 = shifts_lats_y.ravel(), shifts_lngs_y.ravel()

    dlng = lng1 - lng0
    dlat = lat1 - lat0

    a = sin(dlat / 2) ** 2 + cos(lat0) * cos(lat1) * sin(dlng / 2) ** 2
    c = 2 * arcsin(sqrt(a))
    distances = c * r
    distances = distances.reshape((nums, nums))
    return distances