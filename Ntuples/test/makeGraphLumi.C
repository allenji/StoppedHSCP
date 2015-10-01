// Start from:
// http://root.cern.ch/root/html534/tutorials/graphs/graph.C.html  

#include <iostream>  
using std::cout;
using std::endl;

#include "TCanvas.h" 
#include "TGraph.h" 
#include "TH1.h" 
#include "TFile.h" 
#include "TFrame.h" 
#include "TLegend.h" 

void makeGraphLumi() {
  //Draw a simple graph
  // To see the output of this macro, click begin_html <a href="gif/graph.gif">here</a>. end_html
  //Author: Rene Brun
   
  TCanvas *c1 = new TCanvas("c1","A Simple Graph Example",200,10,700,700);

  c1->SetLeftMargin(0.15);  
  c1->SetBottomMargin(0.15);  
  c1->SetRightMargin(0.15);  
  // c1->SetFillColor(42);
  c1->SetGrid();

  const Int_t n = 7;
  // Values below are taken from the rates for a whole run, from WBM.  
  Double_t lumi[7] =         {  2000e30, 2000e30, 2200e30, 1930e30, 2200e30, 2500e30, 2050e30}; 
  Double_t rate[7] =         {   114189,  110482,  109970,  107303,  121126,  133603,  116501}; 
  Double_t lumiPerBunch[7] = {  1.94e30, 1.94e30, 1.87e30, 1.89e30, 1.89e30, 2.15e30, 1.76e30}; 

  TGraph* grData = new TGraph(n, lumi, rate);  
  grData->SetLineColor(2);
  grData->SetLineWidth(4);
  grData->SetMarkerColor(2);
  grData->SetMarkerStyle(21);
  grData->SetTitle("");
  grData->GetXaxis()->SetLimits(0, 2600e30);  
  grData->GetXaxis()->SetTitle("luminosity [cm^{-2}sec^{-1}]");
  grData->GetXaxis()->SetTitleSize(0.05);  
  grData->GetXaxis()->SetLabelSize(0.05); 
  grData->GetYaxis()->SetTitle("L1_SingleJetC20_NotBptxOR unprescaled rate [Hz]");
  grData->GetYaxis()->SetTitleSize(0.042);  
  grData->GetYaxis()->SetTitleOffset(1.5);  
  grData->GetYaxis()->SetLabelSize(0.045);  
  grData->SetMinimum(0);  
  grData->Draw("AP");
  grData->Fit("pol1");  


  // TCanvas::Update() draws the frame, after which one can change it
  c1->Update();
  c1->GetFrame()->SetBorderSize(12);
  c1->Modified();
  c1->SaveAs("lumi.pdf");  




  const Int_t n2 = 7;
  // These values are from Andrea Bocci & WBM.  
  Double_t lumi2[7] =         {  1.9e33, 1.5e33 };
  Double_t rate2[7] =         {  120000, 100000 };

  TGraph* grData = new TGraph(n2, lumi2, rate2);  
  grData->SetLineColor(2);
  grData->SetLineWidth(4);
  grData->SetMarkerColor(2);
  grData->SetMarkerStyle(21);
  grData->SetTitle("");
  grData->GetXaxis()->SetLimits(0, 2600e30);  
  grData->GetXaxis()->SetTitle("luminosity [cm^{-2}sec^{-1}]");
  grData->GetXaxis()->SetTitleSize(0.05);  
  grData->GetXaxis()->SetLabelSize(0.05); 
  grData->GetYaxis()->SetTitle("L1_SingleJetC20_NotBptxOR unprescaled rate [Hz]");
  grData->GetYaxis()->SetTitleSize(0.042);  
  grData->GetYaxis()->SetTitleOffset(1.5);  
  grData->GetYaxis()->SetLabelSize(0.045);  
  grData->SetMinimum(0);  
  grData->Draw("AP");
  grData->Fit("pol1");  


  // TCanvas::Update() draws the frame, after which one can change it
  c1->Update();
  c1->GetFrame()->SetBorderSize(12);
  c1->Modified();
  c1->SaveAs("lumi.pdf");  





  // TGraph* grData2 = new TGraph(n, lumiPerBunch, rate);  
  // grData2->SetLineColor(2);
  // grData2->SetLineWidth(4);
  // grData2->SetMarkerColor(2);
  // grData2->SetMarkerStyle(21);
  // grData2->SetTitle("");
  // grData2->GetXaxis()->SetTitle("luminosity per bunch [cm-2sec-1]");
  // grData2->GetYaxis()->SetTitle("L1_SingleJetC20_NotBptxOR (unprescaled rate) [Hz]");
  // grData2->SetMinimum(0);  
  // grData2->Draw("AP");

  // c1->Update();
  // c1->GetFrame()->SetBorderSize(12);
  // c1->Modified();
  // c1->SaveAs("lumiPerBunch.pdf");  

}  // end void makeGraphMET() {


