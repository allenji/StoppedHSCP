# Modify these variables to switch masses, input stopped points files, and flavor of RHadron
SPARTICLE_MASS=1000
NEUTRALINO_MASS=894
OUTPUTFILE='Weifengrun100events_GRun_stage2_GEN-HLT_gluino_0506' + str(SPARTICLE_MASS)+'_'+str(NEUTRALINO_MASS)+'.root'

import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2015_cff')
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
#process.load('Configuration.StandardSequences.GeometryDB_cff')
#process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
#process.load('HLTrigger.Configuration.HLT_7E33v3_cff')
#process.load('HLTrigger.Configuration.HLT_2013_cff')
#process.load('HLTrigger.Configuration.HLT_FULL_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        #input = cms.untracked.int32(1000)
        )

process.options = cms.untracked.PSet(
#		SkipEvent = cms.untracked.vstring('StdException')
       SkipEvent = cms.untracked.vstring( 'g4SimHits','G4HadronicProcess')
		#SkipEvent = cms.untracked.vstring('hltCsc2DRecHits','CSCRecHitDProducer'
		)

# Input source
process.source = cms.Source ("PoolSource",
                             fileNames=cms.untracked.vstring(
    #'root://eoscms//eos/cms/store/user/jalimena/gluino_GEN-SIM/C01AE68D-29FE-E111-802B-0030487F92B5.root'
       # 'file:../stage1/step1_gluino500.root'
	#'file:/home/wulsin/stoppedParticles/Run2Signal/CMSSW_7_1_13/src/EXO-RunIIWinter15GS-00268.root'
	'file:/home/weifengji/StoppedParticles/CMSSW_7_1_13/src/EXO-RunIIWinter15GS-00268.root'
    )
                             )

# Output definition
process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
                                        #    outputCommands = cms.untracked.vstring('drop *_*_*_SIM',
                                        #   'keep *_*_Stopped*_SIM',
                                        #   'keep *_generator_*_SIM',
                                        #   'keep *_*_*_HLT'),
                                        splitLevel = cms.untracked.int32(0),
                                        eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
                                        outputCommands = process.RAWSIMEventContent.outputCommands,
                                        fileName = cms.untracked.string(OUTPUTFILE),
                                        dataset = cms.untracked.PSet(
    filterName = cms.untracked.string(''),
                    dataTier = cms.untracked.string('')
    ),
                                        SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring('filter_step')
    )
                                        )

process.RAWSIMoutput.outputCommands.append('drop *_*_*_SIM')
process.RAWSIMoutput.outputCommands.append('keep *_*_Stopped*_SIM')
process.RAWSIMoutput.outputCommands.append('keep *_generator_*_SIM')
process.RAWSIMoutput.outputCommands.append('keep *_VtxSmeared_*_HLT')

process.eventFilter = cms.EDFilter("MCStoppedEventFilter",
                                   #   StoppedParticlesXLabel = cms.InputTag("StoppedParticlesX")
                                   )

# Additional output definition

# Other statements
#process.GlobalTag.globaltag = 'START53_V7A::All'
process.GlobalTag.globaltag = 'MCRUN2_71_V0::All'
#process.GlobalTag.globaltag = 'START71_V8A::All'

process.generator = cms.EDProducer("Pythia6HSCPGun",
                                   readFromFile = cms.untracked.bool(False),
                                   stoppedData = cms.string(''),
                                   PGunParameters = cms.PSet(
    MinPhi = cms.double(-3.14159265359),
    ParticleID = cms.vint32(11),
    neutralinoMass = cms.double(NEUTRALINO_MASS),
    MinEta = cms.double(-10),
    sparticleMass = cms.double(SPARTICLE_MASS),
    MaxEta = cms.double(10),
    MaxPhi = cms.double(3.14159265359),
    diJetGluino = cms.bool(False),
    #decayTable = cms.string('src/stage2ParticlesTable.txt') #for crab
    decayTable = cms.string('../../../stage2ParticlesTable.txt') #for interactive
    ),
                                   pythiaPylistVerbosity = cms.untracked.int32(2),
                                   gluinoHadrons = cms.bool(True),
                                   stopHadrons = cms.bool(False),
                                   pythiaHepMCVerbosity = cms.untracked.bool(False),
                                   maxEventsToPrint = cms.untracked.int32(1),
                                   PythiaParameters = cms.PSet(
    processParameters = cms.vstring('IMSS(1)=11          ! User defined processes',
                                    #'IMSS(11)=1          ! allow process with gravitino as LSP!',                                    
                                    'IMSS(21) = 33       ! LUN number for SLHA File (must be 33) ',
                                    'IMSS(22) = 33       ! Read-in SLHA decay table ',
                                    #'MDME(89,1) = 0       ! tau decay to whatever     ',
                                    #'MDME(90,1) = 1       ! tau decay to mu and neutrinos     ',
                                    #'MDME(91,1) = 0       ! tau decay to whatever     ',
                                    #'MDME(92,1) = 0       ! tau decay to whatever     ',
                                    #'MDME(93,1) = 0       ! tau decay to whatever     ',
                                    #'MDME(94,1) = 0       ! tau decay to whatever     ',
                                    #'MDME(95,1) = 0       ! tau decay to whatever     ',
                                    #'MDME(96,1) = 0       ! tau decay to whatever     ',
                                    #'MDME(97,1) = 0       ! tau decay to whatever     ',
                                    #'MDME(98,1) = 0       ! tau decay to whatever     ',
                                    #'MDME(99,1) = 0       ! tau decay to whatever     ',
                                    #'MDME(100,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(101,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(102,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(103,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(104,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(105,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(106,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(107,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(108,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(109,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(110,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(111,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(112,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(113,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(114,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(115,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(116,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(117,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(118,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(119,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(120,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(121,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(122,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(123,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(124,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(125,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(126,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(127,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(128,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(129,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(130,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(131,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(132,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(133,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(134,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(135,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(136,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(137,1)= 0       ! tau decay to whatever     ',
                                    #'MDME(138,1)= 0       ! tau decay to whatever     '
                                    ),
    parameterSets = cms.vstring('processParameters',
                                'SLHAParameters'),
    SLHAParameters = cms.vstring('SLHAFILE=stage2ParticlesTable.txt') # this file needs to be where you do cmsenv
    )
                                   )

process.genParticles = cms.EDProducer("GenParticleProducer",
                                      saveBarCodes = cms.untracked.bool(True),
                                      src = cms.InputTag("generator"),
                                      #src = cms.InputTag("VtxSmeared"),
                                      abortOnUnknownPDGCode = cms.untracked.bool(False),
                                      )

process.ProductionFilterSequence = cms.Sequence(process.generator)

# FR Extra stuff
process.load('StoppedHSCP/Simulation/StoppedParticleEvtVtxGenerator_cfi')
process.VtxSmeared.verbose = True

#Unknown particles is OK
process.genParticles.abortOnUnknownPDGCode = False

#Don't use shower library
process.g4SimHits.HCalSD.UseShowerLibrary = False
# FR END Extra stuff
# for HLT
#if hasattr(process, 'hltCsc2DRecHits'):
#    process.hltCsc2DRecHits.wireDigiTag  = cms.InputTag("simMuonCSCDigis","MuonCSCWireDigi")
#    process.hltCsc2DRecHits.stripDigiTag = cms.InputTag("simMuonCSCDigis","MuonCSCStripDigi")
# for the L1 emulator
#if hasattr(process, 'cscReEmulTriggerPrimitiveDigis'):
#    process.cscReEmulTriggerPrimitiveDigis.CSCComparatorDigiProducer = cms.InputTag("simMuonCSCDigis","MuonCSCComparatorDigi")
#    process.cscReEmulTriggerPrimitiveDigis.CSCWireDigiProducer = cms.InputTag("simMuonCSCDigis","MuonCSCWireDigi")

# Path and EndPath definitions
process.filter_step = cms.Path(process.eventFilter)
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.filter_step,process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.raw2digi_step,process.L1Reco_step,process.endjob_step,process.RAWSIMoutput_step])
# filter all path with the production filter sequence
for path in process.paths:
    getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq

from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1



#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs

process = customisePostLS1(process)
