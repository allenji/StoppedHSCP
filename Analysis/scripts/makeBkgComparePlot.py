#!/usr/bin/env python

import ROOT as rt
import os

from optparse import OptionParser
from ROOT import SetOwnership

H_ref = 800;
W_ref = 800;
W = W_ref
H  = H_ref

T = 0.08*H_ref
B = 0.12*H_ref
L = 0.12*W_ref
#R = 0.04*W_ref
R = 0.15*W_ref

def MakeComparePlots(background,scenario,inputFile,inputFile2,legend1,legend2,livetime1,livetime2):
# set background
  bkg = str(background)
  scn = str(scenario)
  if bkg=="Noise":
    bkg="noise"
    path="noise"
    title="Noise Background"
  elif bkg=="Cosmic":
    bkg="cos"
    path="cosmics"
    title="Cosmic Background"
  elif bkg=="Halo":
    bkg="halo"
    path="halo"
    title="Halo Background"
  else:
    print "Incorrect background tag!"
  
  if scn=="EtaPhi":
    scn="jetetaphi"
    xlabel="Leading jet #eta"
    ylabel="Leading jet #phi"
    canvas = rt.TCanvas(bkg+scn+"1",bkg+scn+"1",50,50,W,H)
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
    
    canvas1 = rt.TCanvas(bkg+scn+"2",bkg+scn+"2",50,50,W,H)
    canvas1.SetFillColor(0)
    canvas1.SetBorderMode(0)
    canvas1.SetFrameFillStyle(0)
    canvas1.SetFrameBorderMode(0)
    canvas1.SetLeftMargin( L/W )
    canvas1.SetRightMargin( R/W )
    canvas1.SetTopMargin( T/H )
    canvas1.SetBottomMargin( B/H )
    canvas1.SetTickx(0)
    canvas1.SetTicky(0)
    
    canvas.cd()

    file = rt.TFile(inputFile, "READ")
    path=path+"/h"+bkg+scn
    h1 = file.Get(path)
    h1.SetDirectory(0)
    file2 = rt.TFile(inputFile2, "READ")
    h2 = file2.Get(path)
    h2.SetDirectory(0)
    h1.Scale(1.0/float(livetime1))
    h2.Scale(1.0/float(livetime2))
    h1.SetMinimum(0)
    h2.SetMinimum(0)
    h1.SetMaximum(1.1 * max(h1.GetMaximum(), h2.GetMaximum()))
    h2.SetMaximum(1.1 * max(h1.GetMaximum(), h2.GetMaximum()))
    h1.SetTitle(title+";"+xlabel+";"+ylabel)
    
    #canvas.cd()
    h1.Draw("COLZ")
    leg = rt.TLegend(0.662814,0.260622,0.978141,0.419948,"","brNDC")
    SetOwnership(leg,0)
    leg.SetBorderSize(0)
    leg.SetTextSize(0.035)
    leg.SetFillStyle(0)
    leg.SetTextFont(42)
    leg.AddEntry(h1,  legend1, "l")

    leg.Draw("same")

    canvas1.cd()
    h2.SetTitle(title+";"+xlabel+";"+ylabel)
    h2.Draw("COLZ")
    leg2 = rt.TLegend(0.662814,0.260622,0.978141,0.419948,"","brNDC")
    SetOwnership(leg2,0)
    leg2.SetBorderSize(0)
    leg2.SetTextSize(0.035)
    leg2.SetFillStyle(0)
    leg2.SetTextFont(42)
    leg2.AddEntry(h2, legend2,  "l")

    leg2.Draw("same")
    return [canvas,canvas1]
#indent all the following codes until the end of the function

# set scenario
  else:
    if scn=="Energy":
      scn="jete"
      xlabel="Leading jet E[GeV]"
    elif scn=="Phi":
      scn="jetphi"
      xlabel="Leading jet #phi"
    elif scn=="Eta":
      scn="jeteta"
      xlabel="Leading jet #eta"
    else:
      print "Incorrect scenario input tag!"

    canvas=rt.TCanvas(bkg+scn,bkg+scn,50,50,W,H)
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
    
    path=path+"/h"+bkg+scn
    file=rt.TFile(inputFile, "READ")
    h1 = file.Get(path)
    h1.SetDirectory(0)
    file2 = rt.TFile(inputFile2, "READ")
    h2 = file2.Get(path)
    h2.SetDirectory(0)
    h2.SetLineColor(2)
    h1.Scale(1.0/float(livetime1))
    h2.Scale(1.0/float(livetime2))
    h1.Draw()
    h2.Draw("same")
    h1.SetMinimum(0)
    h1.SetMaximum(1.1 * max(h1.GetMaximum(), h2.GetMaximum()))
    h1.SetTitle(title+";"+xlabel+";Rate [Hz]")
    
    leg = rt.TLegend(0.562814,0.660622,0.878141,0.819948,"","brNDC")
    SetOwnership(leg,0)
    #leg.SetDirectory(0)
    leg.SetBorderSize(0)
    leg.SetTextSize(0.035)
    leg.SetFillStyle(0)
    leg.SetTextFont(42)
    leg.AddEntry(h1,  legend1, "l")
    leg.AddEntry(h2, legend2,  "l")
    #rt.SetOwnership(h1,False)

    leg.Draw("same")

    canvas.cd()
    canvas.Update()
    #rt.SetOwnership(canvas,False)

    return canvas

def Main(inputFile,inputFile2,legend1,legend2,livetime1,livetime2,output):
  count=0
  BACKGROUND = ["Cosmic","Noise","Halo"]
  SCENARIO = ["Energy","EtaPhi","Phi","Eta"]
  end = len(BACKGROUND)*len(SCENARIO)
  print end
  for i in BACKGROUND:
    for j in SCENARIO:
      canvas1=MakeComparePlots(i,j,inputFile,inputFile2,legend1,legend2,livetime1,livetime2)
      if count==0:
        if j=="EtaPhi":
          canvas1[0].SaveAs(output+"/compareBkgPlot.pdf(")
          canvas1[1].SaveAs(output+"/compareBkgPlot.pdf")
          outfile.cd()
          canvas1[0].Write()
          canvas1[1].Write()
        else:
          canvas1.SaveAs(output+"/compareBkgPlot.pdf(")
          outfile.cd()
          canvas1.Write()
      elif count==(end-1):
        if j=="EtaPhi":
          canvas1[0].SaveAs(output+"/compareBkgPlot.pdf")
          canvas1[1].SaveAs(output+"/compareBkgPlot.pdf)")
          outfile.cd()
          canvas1[0].Write()
          canvas1[1].Write()
        else:
          canvas1.SaveAs(output+"/compareBkgPlot.pdf)")
          outfile.cd()
          canvas1.Write()
      else:
        if j=="EtaPhi":
          canvas1[0].SaveAs(output+"/compareBkgPlot.pdf")
          canvas1[1].SaveAs(output+"/compareBkgPlot.pdf")
          outfile.cd()
          canvas1[0].Write()
          canvas1[1].Write()

        else:
          canvas1.SaveAs(output+"/compareBkgPlot.pdf")
          outfile.cd()
          canvas1.Write()

      count=count+1
#      outfile.cd()
      #canvas1.Write()

  
#*****************************************************************************
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
  rt.gStyle.SetOptStat(0)
  
  command = "mkdir "+options.output
  os.system(command)

  outfile=rt.TFile(options.output+"/histograms.root","RECREATE")


  Main(options.histogram1,options.histogram2,options.legend1,options.legend2,options.livetime1,options.livetime2,options.output)

  outfile.Close()
