*echarts*

echarts地图可视化模板
---

```python
import echarts
echarts_html = echarts.ECHARTS.format(startPoint=startPoint,option_data=option_data,geoCoord=geoCoord)
    
echarts_html = echarts_html.replace(echarts.left,'{')
echarts_html = echarts_html.replace(echarts.right,'}')
with codecs.open(output_file, 'w', encoding='utf8') as html:
  html.write(echarts_html)
```
