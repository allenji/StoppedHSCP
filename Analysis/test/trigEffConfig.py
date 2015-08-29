#!/usr/bin/env python                                                                                                                                                                                    
intLumi = -1  # not yet calculated 
cutName = 'trigger'
input_sources = [
    { 'condor_dir' : 'trigEff2015A',  
      'dataset' :   'trigEff',
      'den_channel' : 'TrigDenominator',  
      'num_channel' : 'TrigNumerator',
      'legend_entry' : '2015A data (50 ns run)',
      'color' : 'black',
      'fill' : 'solid',
      'marker' : 'square',
      },
]
