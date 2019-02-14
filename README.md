*echarts*

echarts地图可视化模板
---

```python
import numpy as np
import echarts
from coord_converse import wgs84togcj02, gcj02tobd09

#coordinate = [[lat0, lng0], [lat1, lng1], ...]
lats, lngs = np.array(zip(*coordinate))

#WGS84 converse to BD09(intermediate: GCJ02)
lngs, lats = wgs84togcj02(lngs, lats)
lngs, lats = gcj02tobd09(lngs, lats)

coordinate = np.vstack((lngs,lats)).T

central_lng, central_lat = calculate_the_center_point(coordinate)

echarts_html = echarts.ECHARTS.format(startPoint=startPoint,option_data=option_data,geoCoord=geoCoord)
    
echarts_html = echarts_html.replace(echarts.left,'{')
echarts_html = echarts_html.replace(echarts.right,'}')
with codecs.open(output_file, 'w', encoding='utf8') as html:
  html.write(echarts_html)
```
