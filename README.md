*echarts*

echarts地图可视化模板-基于python
---



@yangcheng


```python
import numpy as np
import json
import codecs

import echarts
from haversine import calculate_the_center_point
from coord_converse import wgs84togcj02, gcj02tobd09

def visualize(coordinate):
    output_file='echarts.html'
    nums = len(coordinate)
    names = ['p' + str(i) for i in range(nums)]
    colors = ['gold'] * nums
    symbols = ['circle'] * nums

    #coordinate = [[lat0, lng0], [lat1, lng1], ...]
    lats, lngs = np.array(zip(*coordinate))

    #WGS84 converse to BD09(intermediate: GCJ02)
    lngs, lats = wgs84togcj02(lngs, lats)
    lngs, lats = gcj02tobd09(lngs, lats)

    coordinate = np.vstack((lngs,lats)).T

    central_lng, central_lat = calculate_the_center_point(coordinate)

    startPoint = "{\nx: %s,\ny: %s\n}" % (central_lng, central_lat,)

    option_data = generate_option_data(names, colors, symbols)

    geoCoord = generate_geoCoord(names,coordinate)

    echarts_html = echarts.ECHARTS.format(startPoint=startPoint,option_data=option_data,geoCoord=geoCoord)

    echarts_html = echarts_html.replace(echarts.left,'{')
    echarts_html = echarts_html.replace(echarts.right,'}')

    output_file = output_file + '.html' if output_file.split('.')[-1] != 'html' else output_file

    with codecs.open(output_file, 'w', encoding='utf8') as html:
        html.write(echarts_html)
 
 
 def generate_option_data(names, colors, symbols):
    data = u"{name:'%s',value:{colorValue:'%s'},symbol:'%s'}"
    option_data = ''
    nums = len(names)
    for k,(name, color, symbol) in enumerate(zip(names, colors, symbols)):
        if k == nums-1:
            option_data += data % (name,color,symbol) + '\n'
        else:
            option_data += data % (name,color,symbol) + ',\n'
    
    return option_data

def generate_geoCoord(names,coordinate):
    if isinstance(coordinate, np.ndarray):
        coordinate = coordinate.tolist()
    geoCoord = dict(zip(names, coordinate))
    geoCoord = json.dumps(geoCoord, ensure_ascii=False, encoding='utf-8')
    geoCoord = geoCoord.replace('],', '],\n')
    return geoCoord
    
if __name__ == '__main__':
    coordinate = [
	[13.7384619517, 100.5609031209],
	[13.7455625134, 100.5626363308],
	[13.7565705087, 100.5459990912],
	[13.7612351636, 100.5261591264],
	[13.7576074396, 100.4965828831],
	[13.7512687035, 100.4922660627],
	[13.7452260638, 100.5236787536]
    ]
    visualize(coordinate)
```

- [地图可视化](https://echarts.baidu.com/)
- [echarts可视化大全](https://www.echartsjs.com/examples/#chart-type-line)
- [echarts可视化栗子1](https://echarts.baidu.com/examples/editor.html?c=map-polygon)
- [echarts文档](https://echarts.baidu.com/option.html#series-map.markPoint)

