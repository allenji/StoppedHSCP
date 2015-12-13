
#include "StoppedHSCP/Analysis/interface/CosmicsHistograms.h"

#include "TMath.h"

#include <sstream>
#include <iostream>

using namespace std; 

CosmicsHistograms::CosmicsHistograms(TFile* file, Cuts* cuts) :
  cuts_(cuts),
  base_()
{
 
  // create directory structure
  file->mkdir("cosmics");
  base_ = file->GetDirectory("cosmics");

  book();

  maxNEvtsToPrint_ = 10;
  NEvtsPrinted_    = 0;


}

CosmicsHistograms::~CosmicsHistograms() {

}



void CosmicsHistograms::book() {

  base_->cd("");

  // time
  hbx_ = new TH1D("hcosbx", "BX number", 3564, 0., 3564.);
  hjetN_ = new TH1D("hjetN", "Number of jets", 10, 0., 10.);
  hjete_ = new TH1D("hcosjete", "Jet E", 18, 0., 900.);
  hsubljete_ = new TH1D("hcossubljete", "Subleading jet E", 50, 0., 500.);
  hjeteta_ = new TH1D("hcosjeteta", "Leading jet #eta", 70, -3.5, 3.5);
  hjetphi_ = new TH1D("hcosjetphi", "Leading jet #phi", 72, -1 * TMath::Pi(),  TMath::Pi());
  hjetetaphi_ = new TH2D("hcosjetetaphi", "Leading jet pos", 70, -3.5, 3.5, 72, -1 * TMath::Pi(),  TMath::Pi());

  hnm1bx_ = new TH1D("hcosnm1bx", "BX number", 3564, 0., 3564.);
  hnm1jete_ = new TH1D("hcosnm1jete", "Jet E", 50, 0., 100.);
  hnm1jeteta_ = new TH1D("hcosnm1jeteta", "Leading jet #eta", 70, -3.5, 3.5);
  hnm1jetphi_ = new TH1D("hcosnm1jetphi", "Leading jet #phi", 72, -1 * TMath::Pi(),  TMath::Pi());
  hnm1jetetaphi_ = new TH2D("hcosnm1jetetaphi", "Leading jet pos", 70, -3.5, 3.5, 72, -1 * TMath::Pi(),  TMath::Pi());

}


void CosmicsHistograms::fill(StoppedHSCPEvent& event) {

  // events passing halo veto but not cosmic veto
  if (!cuts_->cosmicVeto() && cuts_->haloVeto()) {

    if (NEvtsPrinted_ < maxNEvtsToPrint_) {
      cout << "Found event classified as cosmic background.  Run:lumi:event =  " 
	   << event.run << ":" 
	   << event.lb << ":"
	   << event.id << endl;
      NEvtsPrinted_++;  
    }
  


    hbx_->Fill(event.bx);
    hjetN_->Fill(event.jet_N);

    if (event.jet_N > 0) {
      hjete_->Fill(event.jetE[0]);
      hjeteta_->Fill(event.jetEta[0]);
      hjetphi_->Fill(event.jetPhi[0]);
      hjetetaphi_->Fill(event.jetEta[0], event.jetPhi[0]);
    }
    if (event.jet_N > 1) {
      hsubljete_->Fill(event.jetE[1]);
    }

  }

  // N-1 noise
  if (cuts_->cutNMinusOne(5)) {

    hnm1bx_->Fill(event.bx);
    
    if (event.jet_N > 0) {
      hnm1jete_->Fill(event.jetE[0]);
      hnm1jeteta_->Fill(event.jetEta[0]);
      hnm1jetphi_->Fill(event.jetPhi[0]);
      hnm1jetetaphi_->Fill(event.jetEta[0], event.jetPhi[0]);
    }

  }


}


void CosmicsHistograms::save() {

  base_->cd("");

  hbx_->Write("",TObject::kOverwrite);
  hjetN_->Write("",TObject::kOverwrite);
  hjete_->Write("",TObject::kOverwrite);
  hsubljete_->Write("",TObject::kOverwrite);
  hjeteta_->Write("",TObject::kOverwrite);
  hjetphi_->Write("",TObject::kOverwrite);
  hjetetaphi_->Write("",TObject::kOverwrite);

  hnm1bx_->Write("",TObject::kOverwrite);
  hnm1jete_->Write("",TObject::kOverwrite);
  hnm1jeteta_->Write("",TObject::kOverwrite);
  hnm1jetphi_->Write("",TObject::kOverwrite);
  hnm1jetetaphi_->Write("",TObject::kOverwrite);


}


void CosmicsHistograms::summarise() {


}
