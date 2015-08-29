# Modify these variables to switch masses, input stopped points files, and flavor of RHadron
SPARTICLE_MASS=1000
NEUTRALINO_MASS=894
OUTPUTFILE='stage2_GEN_SIM_Winter15_' + str(SPARTICLE_MASS)+'_'+str(NEUTRALINO_MASS)+'.root'

import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM2')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
#process.load('Configuration.Geometry.GeometryExtended2015_cff')
#process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
#process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')


process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(5)
        )

process.options = cms.untracked.PSet(
#		SkipEvent = cms.untracked.vstring('StdException')
       SkipEvent = cms.untracked.vstring( 'g4SimHits','G4HadronicProcess')
#       SkipEvent = cms.untracked.vstring( 'g4SimHits')
		#SkipEvent = cms.untracked.vstring('hltCsc2DRecHits','CSCRecHitDProducer'
		)

# Input source
process.source = cms.Source ("PoolSource",
                             fileNames=cms.untracked.vstring(
    #'root://eoscms//eos/cms/store/user/jalimena/gluino_GEN-SIM/C01AE68D-29FE-E111-802B-0030487F92B5.root'
       # 'file:../stage1/step1_gluino500.root'
	'file:/home/wulsin/stoppedParticles/Run2Signal/CMSSW_7_1_13/src/EXO-RunIIWinter15GS-00268.root'
	#'file:/home/weifengji/StoppedParticles/CMSSW_7_1_13/src/EXO-RunIIWinter15GS-00268.root'
	#'root://cmsxrootd.fnal.gov//store/mc/Summer12/HSCPgluino_M-1500_Tune4C_8TeV-pythia8/GEN-SIM/START52_V9-v4/00000/1A9D86AC-F5FA-E111-A85A-001EC9AA932E.root'
#	'file:/data/users/weifengji/condor/HSCPgluino_M100_13TeV/HSCPgluino_M100_13TeV001.root'
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
                    dataTier = cms.untracked.string('GEN-SIM')
    ),
                                        SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring('filter_step')
    )
                                        )

process.RAWSIMoutput.outputCommands.append('drop *_*_*_SIM')
process.RAWSIMoutput.outputCommands.append('keep *_*_Stopped*_SIM')
process.RAWSIMoutput.outputCommands.append('keep *_generator_*_SIM')
process.RAWSIMoutput.outputCommands.append('keep *_VtxSmeared_*_HLT')
#process.RAWSIMoutput.outputCommands.extend( [ "keep *_*_MuonCSCWireDigi_*" ] )
#process.RAWSIMoutput.outputCommands.extend( [ "keep *_*_MuonCSCStripDigi_*" ] )
process.RAWSIMoutput.outputCommands.extend( [
		"keep *_genParticlePlusGeant_*_*",
		] )

process.eventFilter = cms.EDFilter("MCStoppedEventFilter",
                                   #   StoppedParticlesXLabel = cms.InputTag("StoppedParticlesX")
                                   )
# Additional output definition

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_71_V1::All', '')

process.generator = cms.EDProducer("Pythia6HSCPGun",
                                   readFromFile = cms.untracked.bool(False),
                                   stoppedData = cms.string('/home/weifengji/StoppedParticles/CMSSW_7_3_2/src/stoppedPoint_HSCPgluino_M_1000_TuneCUETP8M1_13TeV_pythia8_cff_GEN_SIM_052715.txt'),
                                   PGunParameters = cms.PSet(
    MinPhi = cms.double(-3.14159265359),
    ParticleID = cms.vint32(11),
    neutralinoMass = cms.double(NEUTRALINO_MASS),
    MinEta = cms.double(-10),
    sparticleMass = cms.double(SPARTICLE_MASS),
    MaxEta = cms.double(10),
    MaxPhi = cms.double(3.14159265359),
    diJetGluino = cms.bool(False),
   # decayTable = cms.string('src/stage2ParticlesTable.txt') #for crab
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

process.genParticlePlusGeant = cms.EDProducer("GenPlusSimParticleProducer",
					      src = cms.InputTag("g4SimHits"), # use "famosSimHits" for FAMOS
					      setStatus = cms.int32(8), # set status = 8 for GEANT GPs
					      filter = cms.vstring("pt > 0.0"), # just for testing (optional)
					      genParticles = cms.InputTag("genParticles") # original genParticle list
					      )

process.ProductionFilterSequence = cms.Sequence(process.generator)

process.VtxSmeared = cms.EDProducer("StoppedParticleEvtVtxGenerator",
                            src = cms.InputTag("generator"),
                            readFromFile = cms.untracked.bool(False),
                            stoppedData = cms.string ("/home/weifengji/StoppedParticles/CMSSW_7_3_2/src/stoppedPoint_HSCPgluino_M_1000_TuneCUETP8M1_13TeV_pythia8_cff_GEN_SIM_052715.txt"),
                            timeOffsetMin = cms.double (-5.), # offset by 7.5 ns to adjast trigger time "0" with senter of 25ns interval
                            timeOffsetMax = cms.double (20.), # --"--
                            verbose = cms.untracked.bool (False),
#                           readDB = cms.bool(False)
)
#process.VtxSmeared.verbose = True

#Unknown particles is OK
process.genParticles.abortOnUnknownPDGCode = False

#Don't use shower library
process.g4SimHits.HCalSD.UseShowerLibrary = False
# FR END Extra stuff

# Path and EndPath definitions
process.filter_step = cms.Path(process.eventFilter)
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim+process.genParticlePlusGeant)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
#process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step)
process.schedule.extend([process.endjob_step,process.filter_step,process.RAWSIMoutput_step])
#process.schedule.extend([process.endjob_step,process.RAWSIMoutput_step])
# filter all path with the production filter sequence
for path in process.paths:
    getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq

from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1



#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs

process = customisePostLS1(process)
#outfile = open('dumpedConfigreadfromfile.py','w'); print >> outfile,process.dumpPython(); outfile.close()
