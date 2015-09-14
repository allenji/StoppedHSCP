#!/usr/bin/env python

import ROOT as rt
import os

from optparse import OptionParser

H_ref = 800;
W_ref = 800;
W = W_ref
H  = H_ref

T = 0.08*H_ref
B = 0.12*H_ref
L = 0.12*W_ref
#R = 0.04*W_ref
R = 0.15*W_ref


def MakeCompareNoiseJetEnergy(inputFile,inputFile2,legend1,legend2,livetime1,livetime2,output):
#inputFile = "/home/weifengji/testV2/processDataAnalysis/CMSSW_7_4_5_ROOT5/src/histosV3/histograms.root"
#inputFile2 = "/home/weifengji/testV2/processDataAnalysis/CMSSW_7_4_5_ROOT5/src/histos0T/histograms.root"

  #H_ref = 800;
  #W_ref = 800;
  #W = W_ref
  #H  = H_ref

  #T = 0.08*H_ref
  #B = 0.12*H_ref
  #L = 0.12*W_ref
  #R = 0.04*W_ref
  #R = 0.15*W_ref

  canvas = rt.TCanvas("cNoiseE","cNoiseE",50,50,W,H)
  canvas.SetFillColor(0)
  canvas.SetBorderMode(0)
  canvas.SetFrameFillStyle(0)
  canvas.SetFrameBorderMode(0)
  canvas.SetLeftMargin( L/W )
  canvas.SetRightMargin( R/W )
  canvas.SetTopMargin( T/H )
  canvas.SetBottomMargin( B/H )
  canvas.SetTickx(0)
  canvas.SetTicky(0)

  file = rt.TFile(inputFile, "READ")
  h1 = file.Get("noise/hnoisejete")
  file2 = rt.TFile(inputFile2, "READ")
  h2 = file2.Get("noise/hnoisejete")
  h2.SetLineColor(2)
  h1.Scale(1.0/float(livetime1))
  h2.Scale(1.0/float(livetime2))
  h1.Draw()
  h2.Draw("same")
  h1.SetMinimum(0)
  h1.SetMaximum(1.1 * max(h1.GetMaximum(), h2.GetMaximum()))  
  h1.SetTitle(";Jet E [GeV];Rate [Hz]")  

  leg = rt.TLegend(0.562814,0.660622,0.878141,0.819948,"","brNDC")
  leg.SetBorderSize(0)
  leg.SetTextSize(0.035)
  leg.SetFillStyle(0)
  leg.SetTextFont(42)
  leg.AddEntry(h1,  legend1, "l")
  leg.AddEntry(h2, legend2,  "l")

  leg.Draw("same")

  canvas.cd()
  canvas.Update()
  canvas.SaveAs(output+"/compareNoiseJetEnergy.pdf")
  outfile.cd()  
  canvas.Write()  

def MakeCompareNoiseJetPhi(inputFile,inputFile2,legend1,legend2,livetime1,livetime2,output):
  canvas2 = rt.TCanvas("c2","c2",50,50,W,H)
  canvas2.SetFillColor(0)
  canvas2.SetBorderMode(0)
  canvas2.SetFrameFillStyle(0)
  canvas2.SetFrameBorderMode(0)
  canvas2.SetLeftMargin( L/W )
  canvas2.SetRightMargin( R/W )
  canvas2.SetTopMargin( T/H )
  canvas2.SetBottomMargin( B/H )
  canvas2.SetTickx(0)
  canvas2.SetTicky(0)

  file = rt.TFile(inputFile, "READ")
  h3 = file.Get("noise/hnoisejetphi")
  file2 = rt.TFile(inputFile2, "READ")
  h4 = file2.Get("noise/hnoisejetphi")
  h4.SetLineColor(2)
  h3.Scale(1.0/float(livetime1))
  h4.Scale(1.0/float(livetime2))
  if(h3.Integral()>h4.Integral()):
    h3.Draw()
    h4.Draw("same")
  else:
    h4.Draw()
    h3.Draw("same")

  leg2 = rt.TLegend(0.562814,0.660622,0.878141,0.819948,"","brNDC")
  leg2.SetBorderSize(0)
  leg2.SetTextSize(0.035)
  leg2.SetFillStyle(0)
  leg2.SetTextFont(42)
  leg2.AddEntry(h3,  legend1, "l")
  leg2.AddEntry(h4, legend2,  "l")

  leg2.Draw("same")

  canvas2.cd()
  canvas2.Update()
  canvas2.SaveAs(output+"/compareNoiseJetPhi.pdf")

def MakeCompareNoiseJetEta(inputFile,inputFile2,legend1,legend2,livetime1,livetime2,output):
  canvas3 = rt.TCanvas("c3","c3",50,50,W,H)
  canvas3.SetFillColor(0)
  canvas3.SetBorderMode(0)
  canvas3.SetFrameFillStyle(0)
  canvas3.SetFrameBorderMode(0)
  canvas3.SetLeftMargin( L/W )
  canvas3.SetRightMargin( R/W )
  canvas3.SetTopMargin( T/H )
  canvas3.SetBottomMargin( B/H )
  canvas3.SetTickx(0)
  canvas3.SetTicky(0)

  file = rt.TFile(inputFile, "READ")
  h5 = file.Get("noise/hnoisejeteta")
  file2 = rt.TFile(inputFile2, "READ")
  h6 = file2.Get("noise/hnoisejeteta")
  h6.SetLineColor(2)
  h5.Scale(1.0/float(livetime1))
  h6.Scale(1.0/float(livetime2))

  if(h5.Integral()>h6.Integral()):
    h5.Draw()
    h6.Draw("same")
  else:
    h6.Draw()
    h5.Draw("same")

  leg3 = rt.TLegend(0.562814,0.660622,0.878141,0.819948,"","brNDC")
  leg3.SetBorderSize(0)
  leg3.SetTextSize(0.035)
  leg3.SetFillStyle(0)
  leg3.SetTextFont(42)
  leg3.AddEntry(h5,  legend1, "l")
  leg3.AddEntry(h6, legend2,  "l")

  leg3.Draw("same")

  canvas3.cd()
  canvas3.Update()
  canvas3.SaveAs(output+"/compareNoiseJetEta.pdf")

def MakeCompareNoiseJetEtaPhi(inputFile,inputFile2,legend1,legend2,livetime1,livetime2,output):
  canvas3 = rt.TCanvas("c4","c4",50,50,2*W,H)
  canvas3.SetFillColor(0)
  canvas3.SetBorderMode(0)
  canvas3.SetFrameFillStyle(0)
  canvas3.SetFrameBorderMode(0)
  canvas3.SetLeftMargin( L/W )
  canvas3.SetRightMargin( R/W )
  canvas3.SetTopMargin( T/H )
  canvas3.SetBottomMargin( B/H )
  canvas3.SetTickx(0)
  canvas3.SetTicky(0)

  pad1=rt.TPad("p1","p1",0,0,0.5,1)
  pad2=rt.TPad("p2","p2",0.5,0,1,1)
  file = rt.TFile(inputFile, "READ")
  h1 = file.Get("noise/hnoisejetetaphi")
  file2 = rt.TFile(inputFile2, "READ")
  h2 = file2.Get("noise/hnoisejetetaphi")
  h1.Scale(1.0/float(livetime1))
  h2.Scale(1.0/float(livetime2))

  pad1.Draw()
  pad1.cd()
  h1.Draw("COLZ")
  leg = rt.TLegend(0.662814,0.260622,0.978141,0.419948,"","brNDC")
  leg.SetBorderSize(0)
  leg.SetTextSize(0.035)
  leg.SetFillStyle(0)
  leg.SetTextFont(42)
  leg.AddEntry(h1,  legend1, "l")

  leg.Draw("same")
  pad1.Update()

  canvas3.cd()
  pad2.Draw()
  pad2.cd()
  h2.Draw("COLZ")
  leg2 = rt.TLegend(0.662814,0.260622,0.978141,0.419948,"","brNDC")
  leg2.SetBorderSize(0)
  leg2.SetTextSize(0.035)
  leg2.SetFillStyle(0)
  leg2.SetTextFont(42)
  leg2.AddEntry(h2, legend2,  "l")

  leg2.Draw("same")
  pad2.Update()
  #canvas3.cd()
  #canvas3.Update()
  canvas3.SaveAs(output+"/compareNoiseJetEtaPhi.pdf")





def Main(inputFile,inputFile2,legend1,legend2,livetime1,livetime2,output):
  MakeCompareNoiseJetEnergy(inputFile,inputFile2,legend1,legend2,livetime1,livetime2,output)
  MakeCompareNoiseJetPhi(inputFile,inputFile2,legend1,legend2,livetime1,livetime2,output)
  MakeCompareNoiseJetEta(inputFile,inputFile2,legend1,legend2,livetime1,livetime2,output)
  MakeCompareNoiseJetEtaPhi(inputFile,inputFile2,legend1,legend2,livetime1,livetime2,output)

#**********************************************************************
if __name__=="__main__":
  parser = OptionParser()
  parser.add_option("-P","--histogram1",
                    dest="histogram1",
                    default=None,
                    help="Specify the full path of the 1st histogram.")
  parser.add_option("-p","--histogram2",
                    dest="histogram2",
                    default=None,
                    help="Specify the full path of the 2nd histogram.")
  parser.add_option("-L","--legend1",
                    dest="legend1",
                    default=None,
                    help="Specify the legend of the 1st histogram.")
  parser.add_option("-l","--legend2",
                    dest="legend2",
                    default=None,
                    help="Specify the legend of the 2nd histogram.")
  parser.add_option("-T","--livetime1",
                    dest="livetime1",
                    default=1,
                    help="Specify the trigger livetime from 1st histogram.")
  parser.add_option("-t","--livetime2",
                    dest="livetime2",
                    default=1,
                    help="Specify the trigger livetime from 2nd histogram.")
  parser.add_option("-o","--output",
                    dest="output",
                    default="compareNoise",
                    help="Specify the name of output directory.")
  (options,args)=parser.parse_args()
   
  rt.gROOT.SetBatch()
  rt.gStyle.SetOptStat(0)  # no stats box  

  command = "mkdir "+options.output

  os.system(command)

  outfile = rt.TFile(options.output + "/" + options.output + ".root", "RECREATE")  

  Main(options.histogram1,options.histogram2,options.legend1,options.legend2,options.livetime1,options.livetime2,options.output)

  outfile.Close()  

