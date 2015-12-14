from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'Ntuples_2015cosmics_smallSample'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../python/stoppedHSCPTree_RECO_2015_cfg.py'

config.Data.inputDataset = '/NoBPTX/Commissioning2015-PromptReco-v1/RECO'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 500
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Cosmics15/cosmics15_CRAFT_238443_239517_json.txt'
config.Data.runRange = '239305-239517' # '193093-194075'
config.Data.outLFNDirBase = '/store/user/wji/'
config.Data.publication = False

config.Site.storageSite = 'T2_US_Purdue'
