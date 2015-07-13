
# remove pieces of master config so it can run on RECO only

import FWCore.ParameterSet.Config as cms

import os 

from StoppedHSCP.Ntuples.stoppedHSCPTree_Master_cfg import *

process.ntuple.remove(process.gctDigis)
process.ntuple.remove(process.gtDigis)
process.ntuple.remove(process.l1extraParticles)
process.ntuple.remove(process.hcalDigis)

# 2012 trigger config
from StoppedHSCP.Ntuples.StoppedHSCP_Trigger2012_cff import *

process.hltHighLevel.HLTPaths = HLTPaths
process.stoppedHSCPTree.hltPathJetNoBptx = hltPathJetNoBptx
process.stoppedHSCPTree.hltPathJetNoBptxNoHalo = hltPathJetNoBptxNoHalo
process.stoppedHSCPTree.hltPathJetNoBptx3BXNoHalo = hltPathJetNoBptx3BXNoHalo
process.stoppedHSCPTree.hltPathJetE50NoBptx3BXNoHalo = hltPathJetE50NoBptx3BXNoHalo
process.stoppedHSCPTree.hltPathJetE70NoBptx3BXNoHalo = hltPathJetE70NoBptx3BXNoHalo

process.stoppedHSCPTree.hltL3Tag = hltL3Tag
process.stoppedHSCPTree.doDigis=False 


process.source= cms.Source("PoolSource",fileNames=cms.untracked.vstring(
#        'file:Run247920_numEvent5.root'
        'root://cmsxrootd.fnal.gov///store/data/Run2015A/NoBPTX/RECO/PromptReco-v1/000/247/920/00000/4C4BEC39-3913-E511-BA87-02163E011A13.root', 
    )
)


process.maxEvents.input = cms.untracked.int32(5) 
#process.source.eventsToProcess = cms.untracked.VEventRange("247920:1:28360")  
process.MessageLogger.cerr.FwkReport.reportEvery = 1 
#process.MessageLogger.cerr.threshold = cms.untracked.string('INFO')

# Apply lumi mask; comment out to process all events  
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes
myLumis = LumiList.LumiList(filename = os.environ['CMSSW_BASE']+'/src/StoppedHSCP/Ntuples/data/json_DCSONLY.txt').getCMSSWString().split(',')
process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
process.source.lumisToProcess.extend(myLumis)

#process.Tracer = cms.Service('Tracer')  



