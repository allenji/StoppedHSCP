#include <iostream>
#include <iomanip>

#include <math.h>
/***************************************************************************** 
  * Project: RooFit                                                           * 
  *                                                                           * 
  * This code was autogenerated by RooClassFactory                            * 
  *****************************************************************************/ 

 // Your description goes here... 

#include "RooHCSPInOrbitPdf.h" 

#ifndef __CINT__
#include "RooAbsReal.h" 
#include "RooAbsCategory.h" 
#include "RooRandom.h" 
#endif

 ClassImp(RooHCSPInOrbitPdf) 

   RooHCSPInOrbitPdf::RooHCSPInOrbitPdf(const char *name, const char *title, 
					RooAbsReal& _bx,
					RooAbsReal& _logtau)
     : RooAbsPdf(name,title),
       bx("bx","bx",this,_bx),
       logtau("logtau","logtau",this,_logtau),
       mLogTauCache (0),
       mCacheReady (false)
{ 
  for (int i = 0; i < BX_IN_ORBIT; ++i) {
    mInstantLumi[i] = 0;
    mSensitiveBX[i] = true;
  }
} 

RooHCSPInOrbitPdf::~RooHCSPInOrbitPdf () {
}

RooHCSPInOrbitPdf::RooHCSPInOrbitPdf(const RooHCSPInOrbitPdf& other, const char* name) :  
  RooAbsPdf(other,name), 
  bx("bx",this,other.bx),
  logtau("logtau",this,other.logtau),
  mLogTauCache (other.mLogTauCache),
  mCacheReady (other.mCacheReady)
{
  for (int i = 0; i < BX_IN_ORBIT; ++i) {
    mInstantLumi[i] = other.mInstantLumi[i];
    mSensitiveBX[i] = other.mSensitiveBX[i];
  }
  if (mCacheReady) for (int i = 0; i < BX_IN_ORBIT; ++i) mLumiCache[i] = other.mLumiCache[i];
} 

RooHCSPInOrbitPdf& RooHCSPInOrbitPdf::operator=(const RooHCSPInOrbitPdf& other) {
  bx = other.bx;
  logtau = other.logtau;
  mLogTauCache = other.mLogTauCache;
  mCacheReady = other.mCacheReady;
  for (int i = 0; i < BX_IN_ORBIT; ++i) {
    mInstantLumi[i] = other.mInstantLumi[i];
    mSensitiveBX[i] = other.mSensitiveBX[i];
  }
  if (mCacheReady) for (int i = 0; i < BX_IN_ORBIT; ++i) mLumiCache[i] = other.mLumiCache[i];
  return *this;
} 

 Double_t RooHCSPInOrbitPdf::evaluate() const 
 { 
   int current_bin = int (floor (bx+0.5));
   if (current_bin < 0 || current_bin >= BX_IN_ORBIT) return 0;
   fillCache();
   double correction = exp ((bx - current_bin)*BX_TIME/exp(logtau));
//    std::cout << "RooHCSPInOrbitPdf::evaluate()-> " << double(bx) << '/' << current_bin 
// 	     << '/' << mLumiCache [current_bin] << '/' << correction 
// 	     << " > " << mLumiCache [current_bin] * correction 
// 	     << std::endl;
   if (!getSensitive(current_bin)) {
     std::cout << "RooHCSPInOrbitPdf::evaluate-> request PDF for insensitive BX " << current_bin << std::endl;
   }
   return mLumiCache [current_bin] * correction;
 } 

Int_t RooHCSPInOrbitPdf::getAnalyticalIntegral(RooArgSet& allVars, RooArgSet& analVars, const char* /*rangeName*/) const  
{
  //return 0;
  if (matchArgs(allVars,analVars,bx)) return 1 ;
  return 0 ;
}


Double_t RooHCSPInOrbitPdf::analyticalIntegral(Int_t code, const char* rangeName) const 
{
  assert(code==1);
  double bxmin = bx.min(rangeName);
  double bxmax = bx.max(rangeName);
  if (bxmin >= bxmax) return 0;

  int first_bin = int (floor (bxmin+0.5));
  double firstFraction = 1;
  if (first_bin < 0)  first_bin = 0;
  else firstFraction = first_bin - bxmin + 0.5;

  int last_bin = int (floor (bxmax+0.5));
  double lastFraction = 1;
  if (last_bin + 1 >= BX_IN_ORBIT) last_bin = BX_IN_ORBIT - 1;
  else lastFraction = bxmax - first_bin + 0.5;

  fillCache();
  double result = mLumiCache[first_bin] * firstFraction + mLumiCache[last_bin] * lastFraction;
  if (first_bin == last_bin) {
    result -= mLumiCache[first_bin];
  }
  else {
    for (int iBX = first_bin + 1; iBX < last_bin; ++iBX) {
      result += mLumiCache[iBX];
    }
  }
  //  std::cout << "RooHCSPInOrbitPdf::analyticalIntegral->" << bxmin << '/' << bxmax << '/' << result << std::endl;
  return result;
}


void RooHCSPInOrbitPdf::fillCache () const 
{
  // evaluate in assumption tau << Tsection
  if (mCacheReady && fabs (double (logtau) - mLogTauCache) < 0.001) return; // no need to remake cache
  std::cout << "RooHCSPInOrbitPdf::fillCache-> ..." << this << "  "
	    << mCacheReady << '/' << double (logtau) << '/' << mLogTauCache
	    << std::endl;
  mLogTauCache = double (logtau);
  mCacheReady = true;
  double lifetime = exp (mLogTauCache);
  
  const double eTTau = 1.-exp (-BX_IN_ORBIT*BX_TIME/lifetime);
  const double eDTTau = exp (-BX_TIME / lifetime);
  
  // now add contribution to the LUMI bunches from itself
  // assume point-like interaction in the middle of time slice
  for (int iBX = 0; iBX < BX_IN_ORBIT; ++iBX) {
    if (mInstantLumi [iBX] > 0) {
      double contribution0 = mInstantLumi [iBX] * 
	(exp (BX_TIME / 2. / lifetime) -1.) / (exp (BX_TIME / lifetime) -1.);
      mLumiCache[iBX] = contribution0; // itself
      mLumiCache[iBX] += (1. - eTTau) / eTTau; // shadows
      mSensitiveBX[iBX] = false;; // insensitive for measurements
      //      std::cout << "1 " << iBX << '/' << mLumiCache[iBX] << std::endl;
    }
    else  mLumiCache[iBX] = 0;
  }

  // now contribution from previous bunches
  double delayFactor = 1;

  for (int iOffset = 1; iOffset < BX_IN_ORBIT; ++iOffset) {
    delayFactor *= eDTTau;
    for (int iBX0 = 0; iBX0 < BX_IN_ORBIT; ++iBX0) {
      // if (mInstantLumi [iBX0] > 0) continue;  // no HSCP in LUMI bunches
      int iBX = iBX0 - iOffset;
      if (iBX < 0) iBX += BX_IN_ORBIT;
      //      std::cout << "offset/bx0/bx: " << iOffset << '/' << iBX0 << '/' << iBX << std::endl;
      if (mInstantLumi [iBX] <= 0) continue; // no contribution from empty bunches
      double contribution = mInstantLumi [iBX] * delayFactor / eTTau;
      //      std::cout << "RooHCSPInOrbitPdf::fillCache->" << iBX << '/' << contribution << '/' << mInstantLumi [iBX] << '/' << delayFactor << '/' << eTTau << std::endl;
      mLumiCache[iBX0] += contribution;
      if (contribution > 1.) {
	//	std::cout << "3 " << iBX << '/' << iOffset << '/' << iBX0 << '/' << contribution << std::endl;
	  }
    }
  }

  // get integrals
  double integralInLumi = 0;
  double integralOffLumi = 0;
  double integralAllLumi = 0;

  for (int i = 0; i < BX_IN_ORBIT; ++i) {
    integralAllLumi += mLumiCache[i];
    if (mInstantLumi [i] > 0) integralInLumi += mLumiCache[i];
    else if (getSensitive(i)) integralOffLumi += mLumiCache[i];
  }

  if (integralOffLumi > 0) {
    for (int i = 0; i < BX_IN_ORBIT; ++i) {
      if (getSensitive(i)) mLumiCache[i] /= integralOffLumi;
      else mLumiCache[i] = 0;
    }
  }
  mOffLumiFraction = integralOffLumi /  integralAllLumi;

  std::cout << "RooHCSPInOrbitPdf::fillCache->" 
	    << " OFF collisions LUMI fraction:" << mOffLumiFraction
	    << "  IN collisions LUMI fraction:" << integralInLumi / integralAllLumi
	    << "  DEAD LUMI fraction:" << 1.-(integralInLumi+integralOffLumi) / integralAllLumi  
	    << std::endl;
}

Int_t RooHCSPInOrbitPdf::getGenerator(const RooArgSet& directVars, RooArgSet &generateVars, Bool_t /*staticInitOK*/) const
{
  if (matchArgs(directVars,generateVars,bx)) return 1 ;  
  return 0 ;
}

void RooHCSPInOrbitPdf::generateEvent(Int_t code)
{
  assert(code==1) ;
  fillCache ();
  while (1) {
    double randomNumber = RooRandom::randomGenerator()->Uniform (0, 1);
    double bxgen = -1;
    double integral = 0;
    for (int iBX = 0; iBX < BX_IN_ORBIT; ++iBX) {
      double sumMin = integral;
      integral += mLumiCache[iBX];
      double sumMax = integral;
      if (sumMax > randomNumber) {
	bxgen = (iBX) - 0.5 + (randomNumber - sumMin) / (sumMax - sumMin);
	break;
      }
    }
    if (bxgen <= -1) {
      std::cout << "RooHCSPInOrbitPdf::generateEvent-> we should never get here" << std::endl;
    }
    if (bxgen >= bx.min() && bxgen <= bx.max()) {
      bx = bxgen;
      return;
    }
  }
}

void RooHCSPInOrbitPdf::setInstantLumi (int fBX, double fLumi) {
  if (fBX > 0 && fBX < BX_IN_ORBIT) {
    mInstantLumi [fBX] = fLumi;
    mSensitiveBX [fBX] = false;
  }
  mCacheReady = false;
}

void RooHCSPInOrbitPdf::setInsensitive (int fBX) {
  if (fBX > 0 && fBX < BX_IN_ORBIT) {
    mSensitiveBX [fBX] = false;
  }
  mCacheReady = false;
}

double RooHCSPInOrbitPdf::offLumiFraction () const {
  fillCache ();
  return mOffLumiFraction;
}

// ====================== RooHCSPBkgInOrbitPdf ============================

ClassImp(RooHCSPBkgInOrbitPdf) 
  
  RooHCSPBkgInOrbitPdf::RooHCSPBkgInOrbitPdf(const char *name, 
					     const char *title, 
					     RooAbsReal& _bx,
					     const RooHCSPInOrbitPdf* lumiPdf)
: RooAbsPdf(name,title),
  bx("bx","bx",this,_bx),
  mCacheReady (false)
{
  for (int i = 0; i < BX_IN_ORBIT; ++i) {
    mSensitiveBX [i] = lumiPdf ? lumiPdf->getSensitive (i) : false;
  }
} 

RooHCSPBkgInOrbitPdf::~RooHCSPBkgInOrbitPdf () {
}

RooHCSPBkgInOrbitPdf::RooHCSPBkgInOrbitPdf(const RooHCSPBkgInOrbitPdf& other, const char* name) :  
  RooAbsPdf(other,name), 
  bx("bx",this,other.bx),
  mCacheReady (other.mCacheReady)
{
  for (int i = 0; i < BX_IN_ORBIT; ++i) mSensitiveBX [i] = other.mSensitiveBX [i];
}

RooHCSPBkgInOrbitPdf& RooHCSPBkgInOrbitPdf::operator=(const RooHCSPBkgInOrbitPdf& other) {
  bx = other.bx;
  mCacheReady = other.mCacheReady;
  for (int i = 0; i < BX_IN_ORBIT; ++i) mSensitiveBX [i] = other.mSensitiveBX [i];
  return *this;
} 


Double_t RooHCSPBkgInOrbitPdf::evaluate() const 
{ 
  int current_bx = int (floor (bx + 0.5));
//   std::cout << "RooHCSPBkgInOrbitPdf::evaluate()-> " << double(bx) << '/' << current_bx
// 	    << '/' << mSensitiveBX [current_bx] 
// 	    << " > " << double ((current_bx >= 0 && current_bx <  BX_IN_ORBIT && mSensitiveBX [current_bx] <= 0) ? 1. : 0.)
// 	    << std::endl;
  if (current_bx >= 0 && current_bx <  BX_IN_ORBIT && mSensitiveBX [current_bx]) return 1;
  return 0;
} 

Int_t RooHCSPBkgInOrbitPdf::getAnalyticalIntegral(RooArgSet& allVars, RooArgSet& analVars, const char* /*rangeName*/) const  
{
  if (matchArgs(allVars,analVars,bx)) return 1 ;
  return 0 ;
}

Double_t RooHCSPBkgInOrbitPdf::analyticalIntegral(Int_t code, const char* rangeName) const 
{
  assert(code==1);
  double bxmin = bx.min(rangeName);
  double bxmax = bx.max(rangeName);
  if (bxmin >= bxmax) return 0;
  
  int first_bin = int (floor (bxmin+0.5));
  double firstFraction = 1;
  if (first_bin < 0)  first_bin = 0;
  else firstFraction = first_bin - bxmin + 0.5;
  
  int last_bin = int (floor (bxmax+0.5));
  double lastFraction = 1;
  if (last_bin + 1 >= BX_IN_ORBIT) last_bin = BX_IN_ORBIT - 1;
  else lastFraction = bxmax - first_bin + 0.5;
  
  fillCache();
  double result = (mSensitiveBX [first_bin] ? 1 : 0) * firstFraction 
    + (mSensitiveBX [last_bin] ? 1 : 0) * lastFraction;
  if (first_bin == last_bin && mSensitiveBX [last_bin]) result -= 1;
  else {
    for (int iBX = first_bin + 1; iBX < last_bin; ++iBX) {
      result += mSensitiveBX [iBX] ? 1 : 0;
    }
  }
  return result;
}

Int_t RooHCSPBkgInOrbitPdf::getGenerator(const RooArgSet& directVars, RooArgSet &generateVars, Bool_t /*staticInitOK*/) const
{
  if (matchArgs(directVars,generateVars,bx)) return 1 ;  
  return 0 ;
}

void RooHCSPBkgInOrbitPdf::generateEvent(Int_t code)
{
  assert(code==1) ;
  fillCache ();
  while (1) {
    double randomNumber = RooRandom::randomGenerator()->Uniform (0,  mEmptyBunches);
    double integral = 0;
    double bxgen = -1;
    for (int iBX = 0; iBX < BX_IN_ORBIT; ++iBX) {
      if (mSensitiveBX [iBX]) {
	integral += 1;
      }
      if (integral > randomNumber) {
	bxgen = iBX + (randomNumber - integral + 0.5);
	break;
      }
    }
    if (bxgen <= -1) {
      std::cout << "RooHCSPInOrbitPdf::generateEvent-> we should never get here" << std::endl;
    }
    if (bxgen >= bx.min() && bxgen <= bx.max()) {
      bx = bxgen;
      return;
    }
  }
}

void RooHCSPBkgInOrbitPdf::fillCache () const
{
  if (mCacheReady) return;
  mEmptyBunches = 0;
  for (int iBX = 0; iBX < BX_IN_ORBIT; ++iBX) if (mSensitiveBX[iBX])  mEmptyBunches++;
  mCacheReady = true;
}

void RooHCSPBkgInOrbitPdf::setSensitive (int fBX, bool fSensitive) {
  if (fBX > 0 && fBX < BX_IN_ORBIT) mSensitiveBX [fBX] = fSensitive;
  mCacheReady = false;
}

