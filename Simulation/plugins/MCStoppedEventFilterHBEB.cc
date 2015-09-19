// -*- C++ -*-
//
// Package:    MCStoppedEventFilterHBEB
// Class:      MCStoppedEventFilterHBEB
// 
/**\class MCStoppedEventFilterHBEB MCStoppedEventFilterHBEB.cc 

 Description: This filter requires that there is at least one stopped point in order
              to continue processing.

 Implementation: Checks if the stopping point is in HB or EB region. If there is more than one stopping particles in one event, only the first one is checked temporarily.
    
*/
//
// Original Author:  Weifeng Ji
//         Created:  Fri Jun 12 10:18:50 EDT 2015
// $Id$


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "TLorentzVector.h"

//
// class declaration
//

class MCStoppedEventFilterHBEB : public edm::EDFilter {
public:
  explicit MCStoppedEventFilterHBEB(const edm::ParameterSet&);
  ~MCStoppedEventFilterHBEB();
  
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  
private:
  virtual void beginJob() ;
  virtual bool filter(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
  virtual bool beginRun(edm::Run&, edm::EventSetup const&);
  virtual bool endRun(edm::Run&, edm::EventSetup const&);
  virtual bool beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  virtual bool endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
  
  // ----------member data ---------------------------
  std::string mStopPointProducer_;
  //edm::InputTag stoppedParticlesXLabel_;
};

//
// constructors and destructor
//
MCStoppedEventFilterHBEB::MCStoppedEventFilterHBEB(const edm::ParameterSet& iConfig) :
  mStopPointProducer_(iConfig.getUntrackedParameter<std::string>("stopPointInputTag", "g4SimHits"))
{
  //stoppedParticlesXLabel_ = iConfig.getParameter<edm::InputTag>("StoppedParticlesXLabel");
}


MCStoppedEventFilterHBEB::~MCStoppedEventFilterHBEB() {}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
MCStoppedEventFilterHBEB::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<std::vector<float> > xs;
	edm::Handle<std::vector<float> > ys;
	edm::Handle<std::vector<float> > zs;
	edm::Handle<std::vector<float> > ts;
  iEvent.getByLabel(mStopPointProducer_, "StoppedParticlesX", xs);
  iEvent.getByLabel(mStopPointProducer_, "StoppedParticlesY", ys);
  iEvent.getByLabel(mStopPointProducer_, "StoppedParticlesZ", zs);
  iEvent.getByLabel(mStopPointProducer_, "StoppedParticlesTime", ts);
  if (!(xs->size()>0)){
    return false;
  }

	bool inhb = false;
	bool ineb = false;
	
	double particle_R = sqrt(xs->at(0)*xs->at(0)+ys->at(0)*ys->at(0))/10.;
	TLorentzVector v = TLorentzVector(xs->at(0),ys->at(0),zs->at(0),ts->at(0));
	double particle_eta = v.PseudoRapidity();

	if (particle_R>=184.0&&particle_R<=295.0&&fabs(particle_eta)<1.3&&fabs(zs->at(0))<5000.0) inhb = true;
	if (particle_R>=131.0&&particle_R<=184.0&&fabs(particle_eta)<1.479&&fabs(zs->at(0)<3760.0)) ineb = true;

	if (inhb||ineb)
		return true;
	else 
		return false;

/*  if (xs->size() > 0)
    return true;
  else
    return false;
*/
}

// ------------ method called once each job just before starting event loop  ------------
void MCStoppedEventFilterHBEB::beginJob() {}

// ------------ method called once each job just after ending the event loop  ------------
void MCStoppedEventFilterHBEB::endJob() {}

// ------------ method called when starting to processes a run  ------------
bool MCStoppedEventFilterHBEB::beginRun(edm::Run&, edm::EventSetup const&) { 
  return true;
}

// ------------ method called when ending the processing of a run  ------------
bool MCStoppedEventFilterHBEB::endRun(edm::Run&, edm::EventSetup const&) {
  return true;
}

// ------------ method called when starting to processes a luminosity block  ------------
bool MCStoppedEventFilterHBEB::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&) {
  return true;
}

// ------------ method called when ending the processing of a luminosity block  ------------
bool MCStoppedEventFilterHBEB::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&) {
  return true;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void MCStoppedEventFilterHBEB::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(MCStoppedEventFilterHBEB);
