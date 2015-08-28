#!/bin/csh

mv $CMSSW_BASE/src/StoppedHSCP/Simulation/plugins/StoppedParticleEvtVtxGenerator.cc $CMSSW_BASE/src/IOMC/EventVertexGenerators/src
mv $CMSSW_BASE/src/StoppedHSCP/Simulation/plugins/StoppedParticleEvtVtxGenerator.h $CMSSW_BASE/src/IOMC/EventVertexGenerators/interface
rm $CMSSW_BASE/src/StoppedHSCP/Simulation/plugins/module.cc
