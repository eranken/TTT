#include <vector>
#include <limits>
#include <iostream>
#include <algorithm>
#include <TLorentzVector.h>

using namespace std;

class Dilepton
{
	private:
		TLorentzVector* lt_ = 0; 
		TLorentzVector* ltbar_ = 0; 
		TLorentzVector* top_ = 0;
		TLorentzVector* tbar_ =0
		TLorentzVector* bt_ = 0; 
		TLorentzVector* btbar_ = 0; 
		TLorentzVector* nut_ = 0; 
		TLorentzVector* nutbar_ = 0;
		TLorentzVector* wt_ = 0;
		TLorentzVector* wtbar_ = 0;
		int pdgid_lt_ = 0;
		int pdgid_ltbar_ = 0;
		TLorentzVector* met_ = 0;

		bool calculated = false;

	public:
		void Init(TLorentzVector* lt, TLorentzVector* ltbar, TLorentzVector* bt, TLorentzVector* btbar, int pdgid_lt, int pdgid_ltbar);
		void Init(TLorentzVector* lt, TLorentzVector* ltbar, TLorentzVector* bt, TLorentzVector* btbar, int pdgid_lt, int pdgid_ltbar, TLorentzVector* nut, TLorentzVector* nutbar);
		void Reset();

		void Calculate()
		{
			if(!calculated)
			{
				calculated = true;
				met_=nut_+nutbar_;
				wt_=lt_+nut_;
				wtbar_=ltbar_+nutbar_;
				top_=wt_+bt_;
				tbar_=wtbar_+btbar_;
			}
		}

	TLorentzVector& Nut() {return(nut_);}	
	TLorentzVector& Nutbar() {return(nut_);}
	TLorentzVector& Wt() {Calculate(); return wt_;}
	TLorentzVector& Wtbar() {Calculate(); return wtbar_;}




}