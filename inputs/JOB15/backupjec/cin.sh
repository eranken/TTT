#!/bin/bash
DIR=/eos/uscms/store/user/ohindric/MC/13TEV/RunIIFall15_76_25ns/NTuple_V8/miniaod2_3JETS_try_4

ls $DIR/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext1-v2/ur*root > DYJets.txt
ls $DIR/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext4-v1/ur*root >> DYJets.txt
ls $DIR/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_RunIIFall15MiniAODv1-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext2-v1/ur*root > WJets.txt



sed -i 's#/eos/uscms#root://cmseos.fnal.gov/#' *.txt
