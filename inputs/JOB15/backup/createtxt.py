import os,sys


def collectfiles(dirname):
	content = os.listdir(dirname)
	files = [os.path.join(dirname, c) for c in content if c.startswith('ur_') and c.endswith('.root')]
	if len(files) != 0:
		print dirname, len(files)
		return files

	files = []
	for c in content:
		if c == 'failed':
			continue
		newpath = os.path.join(dirname, c)
		if os.path.isdir(newpath) == True:
			files += collectfiles(newpath)

	return files	

setnames = {}

setnames['DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'] = 'DYJets.txt'
setnames['WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8'] = 'WJets.txt'
setnames['WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8'] = 'WJets.txt'
setnames['QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8'] = 'QCDEM50.txt'
setnames['QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8'] = 'QCDEM80.txt'
setnames['QCD_Pt-80to120_EMEnriched_TuneCUETP8M1_13TeV_pythia8'] = 'QCDEM120.txt'
setnames['QCD_Pt-120to170_EMEnriched_TuneCUETP8M1_13TeV_pythia8'] = 'QCDEM170.txt'
setnames['QCD_Pt-170to300_EMEnriched_TuneCUETP8M1_13TeV_pythia8'] = 'QCDEM300.txt'
setnames['QCD_Pt-300toInf_EMEnriched_TuneCUETP8M1_13TeV_pythia8'] = 'QCDEMInf.txt'
setnames['QCD_Pt-30to50_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8'] = 'QCDMu50.txt'
setnames['QCD_Pt-50to80_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8'] = 'QCDMu80.txt'
setnames['QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8'] = 'QCDMu120.txt'
setnames['QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8'] = 'QCDMu170.txt'
setnames['QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8'] = 'QCDMu300.txt'
setnames['QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8'] = 'QCDMu470.txt'
setnames['QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8'] = 'QCDMu600.txt'
setnames['QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8'] = 'QCDMu800.txt'
setnames['QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8'] = 'QCDMu1000.txt'
setnames['QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8'] = 'QCDMuInf.txt'
setnames['ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1'] = 'STs.txt'
setnames['ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1'] = 'STt.txt'
setnames['ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1'] = 'Wtbar.txt'
setnames['ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1'] = 'Wt.txt'
setnames['TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8'] = 'tt_aMCatNLO.txt'
setnames['TT_TuneCUETP8M1_13TeV-powheg-pythia8'] = 'tt_PowhegP8.txt'
setnames['TT_TuneCUETP8M1_13TeV-powheg-scaledown-pythia8'] = 'tt_scaledown_PowhegP8.txt'
setnames['TT_TuneCUETP8M1_13TeV-powheg-scaleup-pythia8'] = 'tt_scaleup_PowhegP8.txt'
setnames['TT_TuneCUETP8M1_mtop1695_13TeV-powheg-pythia8'] = 'tt_mtop1695_PowhegP8.txt'
setnames['TT_TuneCUETP8M1_mtop1755_13TeV-powheg-pythia8'] = 'tt_mtop1755_PowhegP8.txt'
setnames['TT_TuneEE5C_13TeV-powheg-herwigpp'] = 'tt_PowhegHpp.txt'
setnames['SingleElectron'] = 'DATAEL.txt'
setnames['SingleMuon'] = 'DATAMU.txt'
setnames['TT_TuneCUETP8M1down_13TeV-powheg-pythia8'] = 'tt_PowhegTuneDown.txt'
setnames['TT_TuneCUETP8M1up_13TeV-powheg-pythia8'] = 'tt_PowhegTuneUp.txt'

		

dirname = sys.argv[1]


dirs = os.listdir(dirname)
for d in dirs:
	newpath = os.path.join(dirname, d)
	files = []
	if os.path.isdir(newpath) == False: continue
	if d not in setnames:
		print 'No short name for', d
		continue
	files = collectfiles(newpath)
	
	files = [f.replace('/eos/uscms', 'root://cmseos.fnal.gov/') for f in files]	
	f = open(setnames[d], 'w')
	for n in files:
		f.write(n+'\n')

	f.close()
	




