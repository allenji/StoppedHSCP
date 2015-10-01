import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *
import math
import os

################################################################################
##### Set up the 'process' object ##############################################
################################################################################

process = cms.Process ('OSUAnalysis')

# how often to print a log message
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

# input source when running interactively
# ---------------------------------------
process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring (
#                                 'file:HcalHPDNoise_MINIAOD_PromptReco-v3_256259_numEvent100.root',   
#                                 'file:root://cmsxrootd.fnal.gov///store/data/Run2015C/HcalHPDNoise/MINIAOD/PromptReco-v3/000/256/259/00000/22F52B0F-5459-E511-A6E8-02163E013960.root', 
#                                 'file:root://cmsxrootd.fnal.gov///store/data/Run2015B/HcalHPDNoise/MINIAOD/PromptReco-v1/000/251/244/00000/3AE34C69-6E27-E511-8FA1-02163E012158.root', 
#                                 'file:root://cmsxrootd.fnal.gov///store/data/Run2015C/HcalHPDNoise/MINIAOD/PromptReco-v1/000/254/790/00000/06E62D74-0E4A-E511-A5E3-02163E014269.root', 
#                                 'file:root://cmsxrootd.fnal.gov///store/data/Run2015B/HcalHPDNoise/MINIAOD/PromptReco-v1/000/251/883/00000/00D0C6AF-222D-E511-8F1A-02163E014629.root',  
                                 'file:root://cmsxrootd.fnal.gov///store/data/Run2015D/HcalHPDNoise/MINIAOD/PromptReco-v3/000/256/676/00000/E648EA17-1F5F-E511-BF62-02163E0136D2.root'
                             ),
)

# FIXME:  set_input does not work (because of error with /usr/bin/file) in CMSSW_7_4_5_ROOT5   
# argument can be a ROOT file, directory, or dataset name*
# *registered dataset names are listed in 'datasets' in:
#    https://github.com/OSU-CMS/OSUT3Analysis/blob/master/Configuration/python/configurationOptions.py

# sample direcotory
# set_input(process, "/store/user/ahart/BN_stopToBottom_M_800_10mm_Tune4C_8TeV_pythia8_lantonel-Summer12_DR53X-PU_S10_START53_V19-v1-ab45720b22c4f98257a2f100c39d504b_USER_1/")

# sample ROOT file
#set_input(process, "/store/user/ahart/BN_stopToBottom_M_800_10mm_Tune4C_8TeV_pythia8_lantonel-Summer12_DR53X-PU_S10_START53_V19-v1-ab45720b22c4f98257a2f100c39d504b_USER_1/stopToBottom_M_800_10mm_Tune4C_8TeV_pythia8_lantonel-Summer12_DR53X-PU_S10_START53_V19-v1-ab45720b22c4f98257a2f100c39d504b_USER_10_2_Dzw.root")

# sample dataset nickname
#set_input(process, "DYToTauTau_20")
#set_input(process, "DYToMuMu_20")

# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (10000)
)

################################################################################
##### Set up the 'collections' map #############################################
################################################################################

from OSUT3Analysis.AnaTools.osuAnalysis_cfi import collectionMap  # miniAOD

################################################################################
##### Set up any user-defined variable producers ###############################
################################################################################

variableProducers = []
variableProducers.append("MyVariableProducer")

################################################################################
##### Import the channels to be run ############################################
################################################################################

hcalNoise = cms.PSet(
    name = cms.string("HcalNoise"),
    triggers = cms.vstring("HLT_GlobalRunHPDNoise_v"), # TRIGGER
    cuts = cms.VPSet (
        # EVENT HAS GOOD PV
        cms.PSet (
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("pt > -1"), 
            numberRequired = cms.string(">= 1")
        ),
    )
)


################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from OSUT3Analysis.Configuration.histogramDefinitions import JetHistograms  
jetHistogramsExtra = cms.VPSet(
       cms.PSet (
            name = cms.string("jetPtZoom"),
            title = cms.string("Jet Transverse Momentum; p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pt"),
        )
)

JetHistograms.histograms = JetHistograms.histograms + jetHistogramsExtra  






################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, [hcalNoise], cms.VPSet (JetHistograms), collectionMap, variableProducers, False)

# uncomment to produce a full python configuration log file
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()
