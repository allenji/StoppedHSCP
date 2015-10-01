import FWCore.ParameterSet.Config as cms

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('Demo')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

#output file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (100)
)
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
#        '/store/user/ahart/AMSB_chargino500GeV_ctau100cm_step4.root'
#        'file:root://cmsxrootd.fnal.gov///store/data/Run2015B/HcalHPDNoise/MINIAOD/PromptReco-v1/000/251/883/00000/00D0C6AF-222D-E511-8F1A-02163E014629.root',  
#        'file:root://cmsxrootd.fnal.gov///store/data/Run2015C/HcalHPDNoise/MINIAOD/PromptReco-v1/000/254/790/00000/06E62D74-0E4A-E511-A5E3-02163E014269.root', 
#        'file:root://cmsxrootd.fnal.gov///store/data/Run2015D/HcalHPDNoise/MINIAOD/PromptReco-v3/000/256/676/00000/E648EA17-1F5F-E511-BF62-02163E0136D2.root', 
#        'file:HcalHPDNoise_MINIAOD_256676_numEvent100.root', 
#        'file:root://cmsxrootd.fnal.gov///store/data/Run2015D/HcalHPDNoise/MINIAOD/PromptReco-v3/000/256/729/00000/467D7DEF-7E5F-E511-986E-02163E011D9F.root', 
        'file:root://cmsxrootd.fnal.gov///store/data/Run2015D/HcalHPDNoise/MINIAOD/PromptReco-v3/000/256/801/00000/164025EB-C55F-E511-A111-02163E01434C.root', 
       )
)


###########################################################
##### Set up the analyzer #####
###########################################################

process.demo = cms.EDAnalyzer ("MiniAODTriggerAnalyzer",
  bits = cms.InputTag("TriggerResults","","HLT"),
  prescales = cms.InputTag("patTrigger"),
  objects = cms.InputTag("selectedPatTrigger"),
                               jets    = cms.InputTag("slimmedJets"),
                               verbose = cms.bool(False), 
)

process.p = cms.Path (process.demo)
