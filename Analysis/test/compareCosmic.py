import ROOT as rt

inputFile = "/home/weifengji/testV2/processDataAnalysis/CMSSW_7_4_5_ROOT5/src/histosV3/histograms.root"
inputFile2 = "/home/weifengji/testV2/processDataAnalysis/CMSSW_7_4_5_ROOT5/src/histos0T/histograms.root"

H_ref = 800;
W_ref = 800;
W = W_ref
H  = H_ref

T = 0.08*H_ref
B = 0.12*H_ref
L = 0.12*W_ref
#R = 0.04*W_ref
R = 0.15*W_ref

canvas = rt.TCanvas("c2","c2",50,50,W,H)
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
h1 = file.Get("cosmics/hcosjetphi")
file2 = rt.TFile(inputFile2, "READ")
h2 = file2.Get("cosmics/hcosjetphi")
h2.SetLineColor(2)
h1.Scale(h2.Integral() / h1.Integral())

h1.Draw()
h2.Draw("same")

leg = rt.TLegend(0.562814,0.660622,0.878141,0.819948,"","brNDC")
leg.SetBorderSize(0)
leg.SetTextSize(0.035)
leg.SetFillStyle(0)
leg.SetTextFont(42)
leg.AddEntry(h1,  "3.8T", "l")
leg.AddEntry(h2, "0T",  "l")

leg.Draw("same")

canvas.cd()
canvas.Update()
canvas.SaveAs("cosmicjetphi.pdf")
