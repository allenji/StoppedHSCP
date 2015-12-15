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
config.Data.lumiMask = '/home/weifengji/StoppedParticles_Run2/ProcessDataRun2/CMSSW_7_4_8/src/StoppedHSCP/Ntuples/data/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_Silver.txt'
config.Data.runRange = '254231-260627' # '193093-194075'
config.Data.outLFNDirBase = '/store/user/wji/'
config.Data.publication = False

config.Site.blacklist = ['T2_US_Nebraska']
config.Site.storageSite = 'T2_US_Purdue'

config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException
    from multiprocessing import Process

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    def forkAndSubmit(config): 
        p = Process(target=submit, args=(config,))
        p.start()
        p.join() 

    #for dataset in ['/NoBPTX/Run2015C-PromptReco-v1/RECO','/NoBPTX/Run2015C-PromptReco-v2/RECO','/NoBPTX/Run2015C-PromptReco-v3/RECO']:
    for dataset in ['/NoBPTX/Run2015C-PromptReco-v1/RECO','/NoBPTX/Run2015D-PromptReco-v3/RECO', '/NoBPTX/Run2015D-PromptReco-v4/RECO']:
        config.Data.inputDataset = dataset
        config.General.requestName = dataset.split('/')[2]+'_15Dec2015'
       # crabCommand('submit', config = config)
        forkAndSubmit(config)
        
