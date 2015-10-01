import FWCore.ParameterSet.Config as cms

process = cms.Process("OSUAnalysisHcalNoise147")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:root://cmsxrootd.fnal.gov///store/data/Run2015C/HcalHPDNoise/MINIAOD/PromptReco-v3/000/256/259/00000/22F52B0F-5459-E511-A6E8-02163E013960.root')
)
process.HcalNoiseCutCalculator = cms.EDProducer("CutCalculator",
    collections = cms.PSet(
        electrons = cms.InputTag("slimmedElectrons"),
        eventvariables = cms.VInputTag(cms.InputTag("MyVariableProducer","eventvariables")),
        genjets = cms.InputTag("slimmedGenJets"),
        jets = cms.InputTag("slimmedJets"),
        mcparticles = cms.InputTag("packedGenParticles"),
        mets = cms.InputTag("slimmedMETs"),
        muons = cms.InputTag("slimmedMuons"),
        photons = cms.InputTag("slimmedPhotons"),
        primaryvertexs = cms.InputTag("offlineSlimmedPrimaryVertices"),
        superclusters = cms.InputTag("reducedEgamma","reducedSuperClusters"),
        taus = cms.InputTag("slimmedTaus"),
        triggers = cms.InputTag("TriggerResults","","HLT"),
        trigobjs = cms.InputTag("selectedPatTrigger"),
        uservariables = cms.VInputTag(cms.InputTag("MyVariableProducer","uservariables"))
    ),
    cuts = cms.PSet(
        cuts = cms.VPSet(cms.PSet(
            cutString = cms.string('pt > -1'),
            inputCollection = cms.vstring('jets'),
            numberRequired = cms.string('>= 1')
        )),
        name = cms.string('HcalNoise'),
        triggers = cms.vstring('HLT_GlobalRunHPDNoise_v')
    )
)


process.MyVariableProducer = cms.EDProducer("MyVariableProducer",
    collections = cms.PSet(
        electrons = cms.InputTag("slimmedElectrons"),
        eventvariables = cms.VInputTag(cms.InputTag("MyVariableProducer","eventvariables")),
        genjets = cms.InputTag("slimmedGenJets"),
        jets = cms.InputTag("slimmedJets"),
        mcparticles = cms.InputTag("packedGenParticles"),
        mets = cms.InputTag("slimmedMETs"),
        muons = cms.InputTag("slimmedMuons"),
        photons = cms.InputTag("slimmedPhotons"),
        primaryvertexs = cms.InputTag("offlineSlimmedPrimaryVertices"),
        superclusters = cms.InputTag("reducedEgamma","reducedSuperClusters"),
        taus = cms.InputTag("slimmedTaus"),
        triggers = cms.InputTag("TriggerResults","","HLT"),
        trigobjs = cms.InputTag("selectedPatTrigger"),
        uservariables = cms.VInputTag(cms.InputTag("MyVariableProducer","uservariables"))
    )
)


process.objectSelector0 = cms.EDFilter("JetObjectSelector",
    collectionToFilter = cms.string('jets'),
    collections = cms.PSet(
        electrons = cms.InputTag("slimmedElectrons"),
        eventvariables = cms.VInputTag(cms.InputTag("MyVariableProducer","eventvariables")),
        genjets = cms.InputTag("slimmedGenJets"),
        jets = cms.InputTag("slimmedJets"),
        mcparticles = cms.InputTag("packedGenParticles"),
        mets = cms.InputTag("slimmedMETs"),
        muons = cms.InputTag("slimmedMuons"),
        photons = cms.InputTag("slimmedPhotons"),
        primaryvertexs = cms.InputTag("offlineSlimmedPrimaryVertices"),
        superclusters = cms.InputTag("reducedEgamma","reducedSuperClusters"),
        taus = cms.InputTag("slimmedTaus"),
        triggers = cms.InputTag("TriggerResults","","HLT"),
        trigobjs = cms.InputTag("selectedPatTrigger"),
        uservariables = cms.VInputTag(cms.InputTag("MyVariableProducer","uservariables"))
    ),
    cutDecisions = cms.InputTag("HcalNoiseCutCalculator","cutDecisions")
)


process.HcalNoiseCutFlowPlotter = cms.EDAnalyzer("CutFlowPlotter",
    cutDecisions = cms.InputTag("HcalNoiseCutCalculator","cutDecisions")
)


process.HcalNoiseInfoPrinter = cms.EDAnalyzer("InfoPrinter",
    collections = cms.PSet(
        electrons = cms.InputTag("slimmedElectrons"),
        eventvariables = cms.VInputTag(cms.InputTag("MyVariableProducer","eventvariables")),
        genjets = cms.InputTag("slimmedGenJets"),
        jets = cms.InputTag("slimmedJets"),
        mcparticles = cms.InputTag("packedGenParticles"),
        mets = cms.InputTag("slimmedMETs"),
        muons = cms.InputTag("slimmedMuons"),
        photons = cms.InputTag("slimmedPhotons"),
        primaryvertexs = cms.InputTag("offlineSlimmedPrimaryVertices"),
        superclusters = cms.InputTag("reducedEgamma","reducedSuperClusters"),
        taus = cms.InputTag("slimmedTaus"),
        triggers = cms.InputTag("TriggerResults","","HLT"),
        trigobjs = cms.InputTag("selectedPatTrigger"),
        uservariables = cms.VInputTag(cms.InputTag("MyVariableProducer","uservariables"))
    ),
    cutDecisions = cms.InputTag("HcalNoiseCutCalculator","cutDecisions"),
    eventsToPrint = cms.VEventID(),
    printAllEvents = cms.bool(False),
    printAllTriggers = cms.bool(False),
    printCumulativeObjectFlags = cms.bool(False),
    printCutDecision = cms.bool(False),
    printEventDecision = cms.bool(False),
    printEventFlags = cms.bool(False),
    printObjectFlags = cms.bool(False),
    printTriggerDecision = cms.bool(False),
    printTriggerFlags = cms.bool(False),
    printVetoTriggerFlags = cms.bool(False),
    valuesToPrint = cms.VPSet()
)


process.HcalNoisePlotter = cms.EDAnalyzer("Plotter",
    collections = cms.PSet(
        electrons = cms.InputTag("slimmedElectrons"),
        eventvariables = cms.VInputTag(cms.InputTag("MyVariableProducer","eventvariables")),
        genjets = cms.InputTag("slimmedGenJets"),
        jets = cms.InputTag("objectSelector0"),
        mcparticles = cms.InputTag("packedGenParticles"),
        mets = cms.InputTag("slimmedMETs"),
        muons = cms.InputTag("slimmedMuons"),
        photons = cms.InputTag("slimmedPhotons"),
        primaryvertexs = cms.InputTag("offlineSlimmedPrimaryVertices"),
        superclusters = cms.InputTag("reducedEgamma","reducedSuperClusters"),
        taus = cms.InputTag("slimmedTaus"),
        triggers = cms.InputTag("TriggerResults","","HLT"),
        trigobjs = cms.InputTag("selectedPatTrigger"),
        uservariables = cms.VInputTag(cms.InputTag("MyVariableProducer","uservariables"))
    ),
    histogramSets = cms.VPSet(cms.PSet(
        histograms = cms.VPSet(cms.PSet(
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring('pt'),
            name = cms.string('jetPt'),
            title = cms.string('Jet Transverse Momentum; p_{T} [GeV]')
        ), 
            cms.PSet(
                binsX = cms.untracked.vdouble(100, -3, 3),
                inputVariables = cms.vstring('eta'),
                name = cms.string('jetEta'),
                title = cms.string('Jet Eta; #eta')
            ), 
            cms.PSet(
                binsX = cms.untracked.vdouble(100, -3.15, 3.15),
                inputVariables = cms.vstring('phi'),
                name = cms.string('jetPhi'),
                title = cms.string('Jet Phi; #phi')
            ), 
            cms.PSet(
                binsX = cms.untracked.vdouble(3, -1.5, 1.5),
                inputVariables = cms.vstring('charge'),
                name = cms.string('jetCharge'),
                title = cms.string('Jet Charge; charge')
            ), 
            cms.PSet(
                binsX = cms.untracked.vdouble(100, -3.15, 3.15),
                binsY = cms.untracked.vdouble(100, -3, 3),
                inputVariables = cms.vstring('phi', 
                    'eta'),
                name = cms.string('jetEtaPhi'),
                title = cms.string('Jet Eta vs. Phi; #phi; #eta')
            ), 
            cms.PSet(
                binsX = cms.untracked.vdouble(120, -0.1, 1.1),
                inputVariables = cms.vstring('chargedHadronEnergyFraction'),
                name = cms.string('jetChargedHadronEnergyFraction'),
                title = cms.string('Jet Charged Hadron Fraction')
            ), 
            cms.PSet(
                binsX = cms.untracked.vdouble(120, -0.1, 1.1),
                inputVariables = cms.vstring('neutralHadronEnergyFraction'),
                name = cms.string('jetNeutralHadronEnergyFraction'),
                title = cms.string('Jet Neutral Hadron Fraction')
            ), 
            cms.PSet(
                binsX = cms.untracked.vdouble(120, -0.1, 1.1),
                inputVariables = cms.vstring('neutralEmEnergyFraction'),
                name = cms.string('jetNeutralEMEnergyFraction'),
                title = cms.string('Jet Neutral EM Fraction')
            ), 
            cms.PSet(
                binsX = cms.untracked.vdouble(120, -0.1, 1.1),
                inputVariables = cms.vstring('chargedEmEnergyFraction'),
                name = cms.string('jetChargedEMEnergyFraction'),
                title = cms.string('Jet Charged EM Fraction')
            ), 
            cms.PSet(
                binsX = cms.untracked.vdouble(100, 0, 100),
                inputVariables = cms.vstring('pt'),
                name = cms.string('jetPtZoom'),
                title = cms.string('Jet Transverse Momentum; p_{T} [GeV]')
            )),
        inputCollection = cms.vstring('jets')
    )),
    verbose = cms.int32(0)
)


process.variableProducerPath = cms.Path(process.MyVariableProducer)


process.HcalNoise = cms.Path(process.HcalNoiseCutCalculator+process.HcalNoiseCutFlowPlotter+process.HcalNoiseInfoPrinter+process.objectSelector0+process.HcalNoisePlotter)


process.endPath = cms.EndPath()


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(100)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('hist_HcalNoise_2015_09_17_10h14m58s.root')
)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

process.schedule = cms.Schedule(*[ process.variableProducerPath, process.HcalNoise, process.endPath ])

