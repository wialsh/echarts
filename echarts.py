# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 16:25:50 2019

@author: wialsh
"""

colors = ['#f7acbc','#ef5b9c','#feeeed','#d71345','#987165','#f26522','#c63c26','#853f04','#840228','#53261f','#8e3e1f','#deab8a','#845538','#dea32c','#b2d235','#5c7a29','#7fb80e','#1d953f','#73b9a2','#008792','#494e8f','#8552a1','#543044','#d1c7b7']

left  = '_left'
right = '_right'

#see echarts-test.html, visualize: double-click echarts-test.html file.
ECHARTS = u"""

<html>
  <head>
                <meta charset='utf-8'>
                <style type='text/css'>
                body _left
                margin: 0;
                _right
                #main _left
                height: 100%;
                _right
                </style>
                </head>
                <body>
                <div id='main'></div>
                <script src='http://echarts.baidu.com/build/dist/echarts.js'></script>
                <script type='text/javascript' src='http://api.map.baidu.com/api?v=2.0&ak=q9U1lWgCK1aBGVC1DVWrgWa7'></script>
                <script src='http://echarts.baidu.com/doc/asset/js/jquery.min.js'></script>
                <script>

                (function () _left
                require.config(_left
                paths: _left
                echarts:'http://echarts.baidu.com/doc/example/www/js'
                _right,
                packages: [
                _left
                name: 'BMap',
                location: 'http://lchiffon.github.io/reveal_slidify/echarts/require',
                main: 'main'
                _right
                ]
                _right);

                require(
                [
                'echarts',
                'BMap',
                'echarts/chart/map'
                ],
                function (echarts, BMapExtension) _left

                var BMapExt = new BMapExtension($('#main')[0], BMap, echarts,_left
                enableMapClick: false
                _right);
                var map = BMapExt.getMap();
                var container = BMapExt.getEchartsContainer();

                var startPoint = {startPoint};
                var point = new BMap.Point(startPoint.x, startPoint.y);
                map.centerAndZoom(point, 17);
                map.enableScrollWheelZoom(true);
                map.setMapStyle(_left
    styleJson: [
    _left
                    'featureType': 'land',
                    'elementType': 'geometry',
                    'stylers': _left
                              'color': '#081734'
                    _right
          _right,
          _left
                    'featureType': 'building',
                    'elementType': 'geometry',
                    'stylers': _left
                              'color': '#04406F'
                    _right
          _right,
         _left
                    'featureType': 'building',
                    'elementType': 'labels',
                    'stylers': _left
                    'visibility': 'off'
                    _right
          _right,
          _left
                    'featureType': 'highway',
                    'elementType': 'geometry',
                    'stylers': _left
                    'color': '#015B99'
                    _right
          _right,
          _left
                    'featureType': 'highway',
                    'elementType': 'labels',
                    'stylers': _left
                    'visibility': 'off'
                    _right
          _right,
          _left
                    'featureType': 'arterial',
                    'elementType': 'geometry',
                    'stylers': _left
                    'color':'#003051'
                    _right
          _right,
          _left
                    'featureType': 'arterial',
                    'elementType': 'labels',
                    'stylers': _left
                    'visibility': 'off'
                    _right
          _right,

          _left
                    'featureType': 'green',
                    'elementType': 'geometry',
                    'stylers': _left
                    'visibility': 'off'
                    _right
          _right,
          _left
                    'featureType': 'water',
                    'elementType': 'geometry',
                    'stylers': _left
                              'color': '#044161'
                    _right
          _right,
          _left
                    'featureType': 'subway',
                    'elementType': 'geometry.stroke',
                    'stylers': _left
                    'color': '#003051'
                    _right
          _right,
          _left
                    'featureType': 'subway',
                    'elementType': 'labels',
                    'stylers': _left
                    'visibility': 'off'
                    _right
          _right,
          _left
                    'featureType': 'railway',
                    'elementType': 'geometry',
                    'stylers': _left
                    'visibility': 'off'
                    _right
          _right,
          _left
                    'featureType': 'railway',
                    'elementType': 'labels',
                    'stylers': _left
                    'visibility': 'off'
                    _right
          _right,

          _left
                    'featureType': 'all',
                    'elementType': 'labels.text.stroke',
                    'stylers': _left
                              'color': '#313131'
                    _right
          _right,
          _left
                    'featureType': 'all',
                    'elementType': 'labels.text.fill',
                    'stylers': _left
                              'color': '#FFFFFF'
                    _right
          _right,
          _left
                    'featureType': 'manmade',
                    'elementType': 'geometry',
                    'stylers': _left
                    'visibility': 'off'
                    _right
          _right,
          _left
                    'featureType': 'manmade',
                    'elementType': 'labels',
                    'stylers': _left
                    'visibility': 'off'
                    _right
          _right,
          _left
                    'featureType': 'local',
                    'elementType': 'geometry',
                    'stylers': _left
                    'visibility': 'off'
                    _right
          _right,
          _left
                    'featureType': 'local',
                    'elementType': 'labels',
                    'stylers': _left
                    'visibility': 'off'
                    _right
          _right,
          _left
                    'featureType': 'subway',
                    'elementType': 'geometry',
                    'stylers': _left
                              'lightness': -65
                    _right
          _right,
          _left
                    'featureType': 'railway',
                    'elementType': 'all',
                    'stylers': _left
                              'lightness': -40
                    _right
          _right,
          _left
                    'featureType': 'boundary',
                    'elementType': 'geometry',
                    'stylers': _left
                              'color': '#8b8787',
                              'weight': '1',
                              'lightness': -29
                    _right
          _right
    ]
  _right);


option = _left
  color: ['gold','aqua','lime'],
  title : _left
    text: '',
    subtext: '',
    x:'center',
    textStyle : _left
      color: '#fff'
    _right
  _right,
  tooltip : _left
    show: true,
    trigger: 'item',
    formatter: function (v) _left
               if(v[2].tooltipValue!=null)_left
               return v[2].tooltipValue;
               _rightelse_left
               return v[1];
               _right
  _right_right,
  toolbox: _left
    show : true,
    orient : 'vertical',
    x: 'right',
    y: 'center',
    feature : _left
      mark : _leftshow: true_right,
      dataView : _leftshow: true, readOnly: false_right,
      restore : _leftshow: true_right,
      saveAsImage : _leftshow: true_right
    _right
  _right,
  series : [
    _left
      type:'map',
      mapType: 'none',
      data:[]
  
      ,markPoint : _left
        symbol:'emptyCircle',
      symbolSize :2.5,
      effect : _left
        show: true,
        type: 'scale',
        shadowBlur : 0
      _right,
      itemStyle:_left
      normal:_left
        label:_leftshow:false_right,
        color:function(param)_left
    return(param.data.value.colorValue);
  _right
      _right,
      emphasis: _left
        label:_leftshow:false_right
      _right
      _right,
      data : [{option_data}]
      _right,
      geoCoord: {geoCoord}
    _right,
    ]
_right;


var myChart = BMapExt.initECharts(container);
window.onresize = myChart.onresize;
BMapExt.setOption(option);
                _right
                );
                _right)();
</script>
  </body>
  </html>


"""