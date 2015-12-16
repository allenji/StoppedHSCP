# Marissa Rodenburg, February 2012
#
# Makes a pretty stopping efficiency plot called summer11Reproduction_stoppingEff_requireHBEB.pdf
#

import sys, os, time
from array import array
from ROOT import *
from math import *
# Run this in batch mode
#ROOT.gROOT.SetBatch()

output = TFile('summer12Reproduction_stoppingEff.root', 'RECREATE')

# stop and gluino points
gluinox2012 = array('d',
                [200.0, 400.0, 600.0, 800.0, 1000.0, 1200.0, 1400.0, 1600.0, 1800.0, 2000.0, 2200.0, 2400.0, 2600.0])
gluinoyNum2012 = array('d',
                [6781.,5541.,5390.,5112.,5432.,5317.,5702.,5822.,6247.,6499.,6792.,7138.,7323.])
gluinoyDen2012 = array('d',
                [98893., 99405., 99410., 98459., 99306., 99013., 99411., 98800., 99353., 98629., 98218., 99336., 97690.])
gluinoxErr2012 = array('d',[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
gluinoyErr2012 = array('d',[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
gluinoy2012 = array('d',[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])

stopx2012 = array('d',
              [200.0, 400.0, 600.0, 800.0, 1000.0, 1200.0, 1400.0, 1600.0, 1800.0, 2000.0, 2200.0, 2400.0, 2600.0])
stopyNum2012 = array('d',
                 [5494.,4797.,4449.,4215.,4205.,4076.,3993.,4156.,4097.,3896.,4045.,4088.,3745.])
stopyDen2012 = array('d',
                 [95902.,96352.,99608.,100000.,100000.,100000.,100000.,99690.,99543.,100000.,98752.,99096.,100000.,98476.])
stopy2012 = array('d',[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
stopxErr2012 = array('d',[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
stopyErr2012 = array('d',[0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])

for i in xrange(0, len(gluinox2012)):
    gluinoy2012[i] = gluinoyNum2012[i]/gluinoyDen2012[i]
    gluinoyErr2012[i] = gluinoy2012[i]*sqrt(1.0/gluinoyNum2012[i] + 1.0/gluinoyDen2012[i])

for i in xrange(0, len(stopx2012)):
    stopy2012[i] = stopyNum2012[i]/stopyDen2012[i]
    stopyErr2012[i] = stopy2012[i]*sqrt(1.0/stopyNum2012[i] + 1.0/stopyDen2012[i])

# TGraphs
geff_gluino2012 = TGraphErrors(len(gluinox2012), gluinox2012, gluinoy2012, gluinoxErr2012, gluinoyErr2012)
geff_stop2012   = TGraphErrors(len(stopx2012), stopx2012, stopy2012, stopxErr2012, stopyErr2012)

geff_gluino2012.SetTitle(';M [GeV/c^{2}];#varepsilon_{stop}')
geff_gluino2012.SetMarkerStyle(8)
geff_gluino2012.SetMarkerSize(2)
geff_gluino2012.SetMarkerColor(kRed)
geff_gluino2012.SetLineColor(kRed)
geff_gluino2012.SetLineWidth(4)

geff_stop2012.SetTitle(';m [GeV];#varepsilon_{stop}')
geff_stop2012.SetMarkerStyle(8)
geff_stop2012.SetMarkerSize(2)
geff_stop2012.SetMarkerColor(kBlue)
geff_stop2012.SetLineColor(kBlue)
geff_stop2012.SetLineWidth(4)
#geff_stop2012.SetLineStyle(7)

c1 = TCanvas('c1', '', 1400,1000)
c1.SetGrid()

mg = TMultiGraph()
mg.Add(geff_gluino2012)
mg.Add(geff_stop2012)
mg.SetMaximum(0.2)
mg.SetMinimum(0.0)
mg.SetTitle(';m [GeV];#varepsilon_{stopping}')
mg.Draw('aple')

gPad.Modified()
mg.GetXaxis().SetLimits(200,2600)

leg = TLegend(0.50, 0.65 ,0.89, 0.89)
leg.SetTextFont(42)
leg.AddEntry(geff_gluino2012, '2015,stopped gluinos, #tilde{g} #tilde{g}', 'l')
leg.AddEntry(geff_stop2012, '2015,stopped stops, #tilde{t} #tilde{t}', 'l')
leg.SetHeader("CMS Simulation #sqrt{s} = 13 TeV")
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
c1.Print('Fall15_stoppingEff_requireHBEB.pdf')
