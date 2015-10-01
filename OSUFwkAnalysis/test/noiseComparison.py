#!/usr/bin/env python
intLumi = -1  

###################
# 'color' options #
###################
## 'black'
## 'red'  
## 'green'
## 'purple'
## 'blue'  
## 'yellow'
## default: cycle through list


####################
# 'marker' options #
####################
## 'circle'
## 'square'
## 'triangle'
## default: 'circle'

####################
#  'fill' options  #
####################
## 'solid'
## 'hollow'
## default: 'solid'


input_sources = [
    { 'condor_dir' : 'studyNoise',
      'dataset' : 'Run251883',
      'channel' : 'HcalNoise',
      'legend_entry' : 'Run 251883',
      'marker' : 'triangle',
    },
    { 'condor_dir' : 'studyNoise',
      'dataset' : 'Run254790',
      'channel' : 'HcalNoise',
      'legend_entry' : 'Run 254790',
      'fill' : 'hollow',
    },
    { 'condor_dir' : 'studyNoise',
      'dataset' : 'Run256676',
      'channel' : 'HcalNoise',
      'legend_entry' : 'Run 256676',
      'color' : 'blue', 
      'marker'  : 'square', 
      'fill' : 'hollow',
    },
]


