#!/bin/bash
DIR=/eos/uscms/store/user/ohindric/MC/13TEV/RunIIFall15_76_25ns/NTuple_V8/miniaod2_try_2

ls $DIR/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIIFall15MiniAODv2-PU25nsPoisson50_76X_mcRun2_asymptotic_v12-v1/ur*root > tt_PowhegP8_PU50.txt
ls $DIR/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIIFall15MiniAODv2-premixPU50_deterministic_76X_mcRun2_asymptotic_v12-v3/ur*root > tt_PowwhegP8_PU50det.txt
ls $DIR/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIIFall15MiniAODv2-premixPU50_nondeterministic_76X_mcRun2_asymptotic_v12-v1/ur*root > tt_PowwhegP8_PU50nondet.txt


sed -i 's#/eos/uscms#root://cmseos.fnal.gov/#' *.txt
