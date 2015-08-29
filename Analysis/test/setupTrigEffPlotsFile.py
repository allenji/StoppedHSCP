#!/usr/bin/env python

# Sample usage:
# setupTrigEffPlotsFile.py -i histosV2  -c trigEff2015A
# makeEfficiencyPlots.py -l trigEffPlots.py -o efficiencyTrig.root  

import os
from optparse import OptionParser
parser = OptionParser()


parser.add_option("-i", "--inputDir", dest="inputDir", default="histos",
                  help="input directory containing histogram file") 
parser.add_option("-f", "--fileName", dest="fileName", default="histograms.root",
                  help="name of file containing histograms")  
parser.add_option("-c", "--condorDir", dest="condorDir", default="mycondorDir",
                  help="name of output condor directory")  
(arguments, args) = parser.parse_args()


from ROOT import TFile, TH1, TH1D

inputFile = TFile(arguments.inputDir + "/" + arguments.fileName, "READ") 

hNum = inputFile.Get("histograms/NoCuts/hjeteTrigEffNumer")  
hDen = inputFile.Get("histograms/NoCuts/hjeteTrigEffDenom")   

print "number of bins in hNum: ", hNum.GetNbinsX()
print "number of bins in hDen: ", hDen.GetNbinsX()

hNum2 = hNum.Clone()
hDen2 = hDen.Clone()

hNum2.SetDirectory(0)
hDen2.SetDirectory(0)

inputFile.Close()  

# Create new file
# dataset name:  datasetForTrig
# condor_dir
datasetName = "trigEff"
os.system("mkdir -p condor/" + arguments.condorDir) 
outputFile = TFile("condor/" + arguments.condorDir + "/" + datasetName + ".root", "RECREATE") 
outputFile.mkdir("TrigNumeratorPlotter")  
outputFile.mkdir("TrigDenominatorPlotter")  
outputFile.cd("TrigNumeratorPlotter")  
outputFile.mkdir("TrigNumeratorPlotter/Jet Plots")  
outputFile.cd("TrigNumeratorPlotter/Jet Plots")  
hNum2.SetName("hjete")
hNum2.SetTitle(";Leading jet energy [GeV]")  
hNum2.Write()
outputFile.cd("TrigDenominatorPlotter") 
outputFile.mkdir("TrigDenominatorPlotter/Jet Plots")  
outputFile.cd("TrigDenominatorPlotter/Jet Plots")  
hDen2.SetName("hjete")
hDen2.SetTitle(";Leading jet energy [GeV]")  
hDen2.Write()  
outputFile.Close()  






