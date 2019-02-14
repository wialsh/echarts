# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 10:40:05 2019

@author: wialsh
"""

import numpy as np


## https://blog.csdn.net/yzyssg1/article/details/76120617/
## verification: http://www.gpsspg.com/maps.htm
x_pi = np.pi * 3000.0 / 180.0
a = 6378245.0  # semi-major axis
ee = 0.00669342162296594323  # flattening


def gcj02tobd09(lng, lat):
    z = np.sqrt(lng * lng + lat * lat) + 0.00002 * np.sin(lat * x_pi)

    theta  = np.arctan2(lat, lng) + 0.000003 * np.cos(lng * x_pi)

    bd_lng = z * np.cos(theta) + 0.0065
    bd_lat = z * np.sin(theta) + 0.006
    return [bd_lng, bd_lat]


def bd09togcj02(bd_lon, bd_lat):
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = np.sqrt(x * x + y * y) - 0.00002 * np.sin(y * x_pi)

    theta = np.arctan2(y, x) - 0.000003 * np.cos(x * x_pi)

    gg_lng = z * np.cos(theta)
    gg_lat = z * np.sin(theta)

    return [gg_lng, gg_lat]


def wgs84togcj02(lng, lat):

    if out_of_china(lng, lat):
        return lng, lat

    dlat = transformlat(lng - 105.0, lat - 35.0)
    dlng = transformlng(lng - 105.0, lat - 35.0)

    radlat = lat / 180.0 * np.pi

    magic = np.sin(radlat)
    magic = 1 - ee * magic * magic

    sqrtmagic = np.sqrt(magic)

    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * np.pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * np.cos(radlat) * np.pi)

    mglat = lat + dlat
    mglng = lng + dlng

    return [mglng, mglat]


def gcj02towgs84(lng, lat):

    if out_of_china(lng, lat):
        return lng, lat

    dlat = transformlat(lng - 105.0, lat - 35.0)
    dlng = transformlng(lng - 105.0, lat - 35.0)

    radlat = lat / 180.0 * np.pi

    magic = np.sin(radlat)
    magic = 1 - ee * magic * magic

    sqrtmagic = np.sqrt(magic)

    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * np.pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * np.cos(radlat) * np.pi)

    mglat = lat + dlat
    mglng = lng + dlng

    return [lng * 2 - mglng, lat * 2 - mglat]

def lnglat2mercator(lng, lat):
    """ arbitrary CSYS input. """
    x = lng * 20037508.34 / 180.0
    y = np.log(np.tan((90.0 + lat) * np.pi / 360.0)) / (np.pi / 180.0)
    y *= 20037508.34 / 180.0
    return x, y

def transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + 0.1 * lng * lat + 0.2 * np.sqrt(np.fabs(lng))

    ret += (20.0 * np.sin(6.0 * lng * np.pi) + 20.0 * np.sin(2.0 * lng * np.pi)) * 2.0 / 3.0
    ret += (20.0 * np.sin(lat * np.pi) + 40.0 * np.sin(lat / 3.0 * np.pi)) * 2.0 / 3.0
    ret += (160.0 * np.sin(lat / 12.0 * np.pi) + 320 * np.sin(lat * np.pi / 30.0)) * 2.0 / 3.0
    return ret


def transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + 0.1 * lng * lat + 0.1 * np.sqrt(np.fabs(lng))

    ret += (20.0 * np.sin(6.0 * lng * np.pi) + 20.0 * np.sin(2.0 * lng * np.pi)) * 2.0 / 3.0
    ret += (20.0 * np.sin(lng * np.pi) + 40.0 * np.sin(lng / 3.0 * np.pi)) * 2.0 / 3.0
    ret += (150.0 * np.sin(lng / 12.0 * np.pi) + 300.0 * np.sin(lng / 30.0 * np.pi)) * 2.0 / 3.0
    return ret


def out_of_china(lng, lat):
    res = False
    try:
        import psycopg2
        import config as cfg
        if not isinstance(lng, float):
            lng, lat = lng[0], lat[0]

        db = psycopg2.connect(**cfg.DB_CONF_195)
        cursor = db.cursor()
        exe = "select st_contains(geom, ST_GeomFromText('POINT(%s %s)',4326)) as is_contained " \
              "from china_mwmmap_tbl_wjh where geom is not NULL" % (lng, lat)
        cursor.execute(exe)
        in_china = cursor.fetchall()[0][0]
        db.close()
        cursor.close()
        if not in_china:
            res = True
    except:
        if lng < 72.004 or lng > 137.8347:
            res = True
        elif lat < 0.8293 or lat > 55.8271:
            res = True
    return res


if __name__ == '__main__':
    lng = 113.332656

    lat = 23.152902
    lng, lat = bd09togcj02(lng, lat)
    print(lng, lat)
    lng, lat = gcj02towgs84(lng, lat)
    print(lng, lat)

    result1 = gcj02tobd09(lng, lat)

    result2 = bd09togcj02(lng, lat)

    result3 = wgs84togcj02(lng, lat)

    result4 = gcj02towgs84(lng, lat)

    print(result1, result2, result3, result4)

    lng, lat = wgs84togcj02(lng, lat)
    print(gcj02tobd09(lng, lat))
