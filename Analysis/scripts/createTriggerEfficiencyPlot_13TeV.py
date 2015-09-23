# Marissa Rodenburg, February 2012
#
# Makes a pretty stopping efficiency plot called summer11Reproduction_stoppingEff_requireHBEB.pdf
#

import sys, os, time
from array import array
from ROOT import *
from math import *

# Run in batch mode
#ROOT.gROOT.SetBatch()

output = TFile('summer12_stoppingEff.root', 'RECREATE')

# 2012 stop and gluino points
gluinox2012 = array('d',
                [400.,600.,800.,1000.,1200.,1400.,1600.,1800.,2000.,2200.,2400.,2600.])
gluinoyNum2012 = array('d',
                [3503.,3409.,3225.,3423.,3391.,3608.,3738.,3935.,4161.,4339.,4580.,4690.])
gluinoyDen2012 = array('d',
                [5541.,5390.,5112.,5432.,5317.,5702.,5822.,6247.,6499.,6792.,7138.,7323.])
gluinoxErr2012 = array('d',[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
gluinoyErr2012 = array('d',[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
gluinoy2012 = array('d',[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])

stopx2012 = array('d',
                  [300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900., 1000.])
stopyNum2012 = array('d',
                     [2119.,1895.,1742.,1730.,1617.,1526.,1536.,1447.])
stopyDen2012 = array('d',
                     [3213.,2861.,2687.,2518.,2449.,2259.,2242.,2189.,])

stopy2012 = array('d',[0.,0.,0.,0.,0.,0.,0.,0.])
stopxErr2012 = array('d',[0.,0.,0.,0.,0.,0.,0.,0.])
stopyErr2012 = array('d',[0.,0.,0.,0.,0.,0.,0.,0.])

for i in xrange(0, len(gluinox2012)):
    gluinoy2012[i] = gluinoyNum2012[i]/gluinoyDen2012[i]
    gluinoyErr2012[i] = gluinoy2012[i]*sqrt(1.0/gluinoyNum2012[i] + 1.0/gluinoyDen2012[i])

for i in xrange(0, len(stopx2012)):
    stopy2012[i] = stopyNum2012[i]/stopyDen2012[i]
    stopyErr2012[i] = stopy2012[i]*sqrt(1.0/stopyNum2012[i] + 1.0/stopyDen2012[i])

# TGraphs
geff_gluino2012 = TGraphErrors(len(gluinox2012), gluinox2012, gluinoy2012, gluinoxErr2012, gluinoyErr2012)
geff_stop2012   = TGraphErrors(len(stopx2012), stopx2012, stopy2012, stopxErr2012, stopyErr2012)

geff_gluino2012.SetTitle(';M [GeV/c^{2}];#varepsilon_{trigger}')
geff_gluino2012.SetMarkerStyle(8)
geff_gluino2012.SetMarkerSize(2)
geff_gluino2012.SetMarkerColor(kRed)
geff_gluino2012.SetLineColor(kRed)
geff_gluino2012.SetLineWidth(4)

geff_stop2012.SetTitle(';m [GeV];#varepsilon_{trigger}')
geff_stop2012.SetMarkerStyle(8)
geff_stop2012.SetMarkerSize(2)
geff_stop2012.SetMarkerColor(kBlue)
geff_stop2012.SetLineColor(kBlue)
geff_stop2012.SetLineWidth(4)
#geff_stop2012.SetLineStyle(7)

c1 = TCanvas('c1', '', 1400,1000)
c1.SetGrid()

#blank.Draw()
#geff_gluino.Draw('ALPE1 same')
#geff_stop.Draw('ALPE1 same')

mg = TMultiGraph()
mg.Add(geff_gluino2012)
#mg.Add(geff_stop2012)
mg.SetMaximum(1.0)
mg.SetMinimum(0.0)
mg.SetTitle(';M [GeV/c^{2}];#varepsilon_{trigger}')
mg.Draw('aple')

gPad.Modified()
mg.GetXaxis().SetLimits(400,2600)

leg = TLegend(0.50, 0.25 ,0.89, 0.49)
leg.SetTextFont(42)
leg.AddEntry(geff_gluino2012, '2015 gluinos, #tilde{g} #tilde{g}, E_{gluon} = 100 GeV', 'l')
#leg.AddEntry(geff_stop2012, '2012 stops, #tilde{t} #tilde{t}, E_{top} = 180 GeV', 'l')
leg.SetHeader("CMS Simulation, #sqrt{s} = 13 TeV")
leg.SetFillColor(kWhite)
leg.SetBorderSize(0)
leg.Draw()

output.Write()
geff_gluino2012.Write()
geff_stop2012.Write()
mg.Write()
c1.RedrawAxis()

c1.RedrawAxis()

#time.sleep(10)
c1.Print('fall15_triggerEff_requireHBEB.pdf')
