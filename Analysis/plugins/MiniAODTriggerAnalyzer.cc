// system include files
#include <memory>
#include <cmath>


// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/PatCandidates/interface/Jet.h" 
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1D.h"
#include "TH2D.h"


class MiniAODTriggerAnalyzer : public edm::EDAnalyzer {
   public:
      explicit MiniAODTriggerAnalyzer(const edm::ParameterSet&);
      ~MiniAODTriggerAnalyzer() {}

   private:
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;

      edm::EDGetTokenT<edm::TriggerResults> triggerBits_;
      edm::EDGetTokenT<pat::TriggerObjectStandAloneCollection> triggerObjects_;
      edm::EDGetTokenT<pat::PackedTriggerPrescales> triggerPrescales_;
  edm::InputTag jets_;

  TH1D* hjetpt;  
  TH1D* hjetptL1;  
  TH2D* hjetptOfflineVsL1;  

  bool verbose_;  

};

MiniAODTriggerAnalyzer::MiniAODTriggerAnalyzer(const edm::ParameterSet& iConfig):
    triggerBits_(consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("bits"))),
    triggerObjects_(consumes<pat::TriggerObjectStandAloneCollection>(iConfig.getParameter<edm::InputTag>("objects"))),
    triggerPrescales_(consumes<pat::PackedTriggerPrescales>(iConfig.getParameter<edm::InputTag>("prescales"))), 
    jets_ (iConfig.getParameter<edm::InputTag> ("jets")), 
    verbose_(iConfig.getParameter<bool> ("verbose"))  
{

    

  edm::Service<TFileService> fs;
  hjetpt   = fs->make<TH1D>("hjetPt"   , ";Offline jet p_{T} [GeV]", 100, 0, 100 );
  hjetptL1 = fs->make<TH1D>("gjetPtL1" , ";L1SingleJetC20NotBptxOR seed filter p_{T} [GeV]", 100, 0, 100 );
  hjetptOfflineVsL1 = fs->make<TH2D>("hjetPtOfflineVsL1" , ";L1SingleJetC20NotBptxOR seed filter p_{T} [GeV];Offline jet p_{T} [GeV]" , 100, 0, 100, 50, 0, 100);


}

void MiniAODTriggerAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    edm::Handle<edm::TriggerResults> triggerBits;
    edm::Handle<pat::TriggerObjectStandAloneCollection> triggerObjects;
    edm::Handle<pat::PackedTriggerPrescales> triggerPrescales;

    iEvent.getByToken(triggerBits_, triggerBits);
    iEvent.getByToken(triggerObjects_, triggerObjects);
    iEvent.getByToken(triggerPrescales_, triggerPrescales);

    edm::Handle<std::vector<pat::Jet> > jets;
    iEvent.getByLabel (jets_, jets);

    double leadingJetPt = 0.001;  
    if (jets->size ())  {
      // first jet is always leading jet (https://github.com/cms-sw/cmssw/blob/CMSSW_7_4_X/PhysicsTools/PatAlgos/plugins/PATJetProducer.cc#L406)
      const pat::Jet &leadingJet = jets->at (0);
      leadingJetPt = leadingJet.pt();  
    }
    
    for (pat::TriggerObjectStandAlone obj : *triggerObjects) { // note: not "const &" since we want to call unpackPathNames
      if (obj.hasFilterLabel("hltL1sL1SingleJetC20NotBptxOR")) {
	hjetptL1->Fill(obj.pt());  
	hjetpt  ->Fill(leadingJetPt);  
	hjetptOfflineVsL1->Fill(obj.pt(), leadingJetPt);   
      }
    }


    if (verbose_) { 
      const edm::TriggerNames &names = iEvent.triggerNames(*triggerBits);
      std::cout << "\n === TRIGGER PATHS === " << std::endl;
      for (unsigned int i = 0, n = triggerBits->size(); i < n; ++i) {
        std::cout << "Trigger " << names.triggerName(i) << 
	  ", prescale " << triggerPrescales->getPrescaleForIndex(i) <<
	  ": " << (triggerBits->accept(i) ? "PASS" : "fail (or not run)") 
		  << std::endl;
      }
      std::cout << "\n === TRIGGER OBJECTS === " << std::endl;
      for (pat::TriggerObjectStandAlone obj : *triggerObjects) { // note: not "const &" since we want to call unpackPathNames
        obj.unpackPathNames(names);
        std::cout << "\tTrigger object:  pt " << obj.pt() << ", eta " << obj.eta() << ", phi " << obj.phi() << std::endl;
	hjetpt->Fill(obj.pt());  
        // Print trigger object collection and type
        std::cout << "\t   Collection: " << obj.collection() << std::endl;
        std::cout << "\t   Type IDs:   ";
        for (unsigned h = 0; h < obj.filterIds().size(); ++h) std::cout << " " << obj.filterIds()[h] ;
        std::cout << std::endl;
        // Print associated trigger filters
        std::cout << "\t   Filters:    ";
        for (unsigned h = 0; h < obj.filterLabels().size(); ++h) std::cout << " " << obj.filterLabels()[h];
        std::cout << std::endl;
        std::vector<std::string> pathNamesAll  = obj.pathNames(false);
        std::vector<std::string> pathNamesLast = obj.pathNames(true);
        // Print all trigger paths, for each one record also if the object is associated to a 'l3' filter (always true for the
        // definition used in the PAT trigger producer) and if it's associated to the last filter of a successfull path (which
        // means that this object did cause this trigger to succeed; however, it doesn't work on some multi-object triggers)
        std::cout << "\t   Paths (" << pathNamesAll.size()<<"/"<<pathNamesLast.size()<<"):    ";
        for (unsigned h = 0, n = pathNamesAll.size(); h < n; ++h) {
	  bool isBoth = obj.hasPathName( pathNamesAll[h], true, true ); 
	  bool isL3   = obj.hasPathName( pathNamesAll[h], false, true ); 
	  bool isLF   = obj.hasPathName( pathNamesAll[h], true, false ); 
	  bool isNone = obj.hasPathName( pathNamesAll[h], false, false ); 
	  std::cout << "   " << pathNamesAll[h];
	  if (isBoth) std::cout << "(L,3)";
	  if (isL3 && !isBoth) std::cout << "(*,3)";
	  if (isLF && !isBoth) std::cout << "(L,*)";
	  if (isNone && !isBoth && !isL3 && !isLF) std::cout << "(*,*)";
        }
        std::cout << std::endl;
      }
      std::cout << std::endl;
    }  // if (verbose_)  
}

//define this as a plug-in
DEFINE_FWK_MODULE(MiniAODTriggerAnalyzer);
