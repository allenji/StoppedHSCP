{
  // Marissa Rodenburg, March 2012
  // This script is used to produce the plot summer12_8TeV_detectionEff.pdf
  //
  // From root:
  // [0] .x StoppedHSCP/Analysis/scripts/energyscan_fit.C
  //

  TCanvas canvas;
  canvas->SetGrid();
  gStyle->SetOptTitle(0);
  gStyle->SetOptStat(0);
  //gStyle->SetOptFit();

  Int_t nG400points=3;
  Int_t nG700points=3;
  Int_t nG1200points=3;
  //Int_t nGtotalpoints = nG400points+nG700points+nG1200points;
  Int_t nGtotalpoints = 9;

  Double_t bothxG[nGtotalpoints] = {50.,50.,50.,100.,100.,100.,150.,150.,150.};
  // selected EB+HB
  Double_t countBoth[nGtotalpoints] = {35.,46.,35.,1843.,1900.,2060.,2409.,2548.,2711.};
  // stopped EB+HB
  Double_t totalBoth[nGtotalpoints] = {5112.,5317.,5822.,5112.,5317.,5822.,5112.,5317.,5822.};
  Double_t bothyG[nGtotalpoints];
  Double_t bothyGplus1[nGtotalpoints];
  Double_t bothyGminus1[nGtotalpoints];
  Double_t bothErrG[nGtotalpoints];
  for (int ib = 0; ib < nGtotalpoints; ib++) {
    bothyG[ib] = countBoth[ib]/totalBoth[ib];
    bothErrG[ib] = bothyG[ib]*TMath::Sqrt(1./countBoth[ib]+1./totalBoth[ib]);
    std::cout<<bothyG[ib]<<"\t"<<countBoth[ib]<<"\t"<<totalBoth[ib]<<std::endl;;

    bothyGplus1[ib] = bothyG[ib] + bothErrG[ib];
    bothyGminus1[ib] = bothyG[ib] - bothErrG[ib];
  }

  Double_t xaxisG400[nG400points] = {50.,100.,150.};
  Double_t countG400[nG400points] = {35.,1843.,2409.};
  Double_t totalG400[nG400points] = {5112.,5112.,5112.};
  Double_t yaxisG400[nG400points];
  Double_t errorG400[nG400points];
  for (int ig = 0; ig < nG400points; ig++) {
    yaxisG400[ig] = countG400[ig]/totalG400[ig];
    errorG400[ig] = yaxisG400[ig]*TMath::Sqrt(1./countG400[ig]+1./totalG400[ig]);
  }
  
  Double_t xaxisG700[nG700points] = {50.,100.,150.};
  Double_t countG700[nG700points] = {46.,1900.,2548.};
  Double_t totalG700[nG700points] = {5317.,5317.,5317.};
  Double_t yaxisG700[nG700points];
  Double_t errorG700[nG700points];
  for (int ig = 0; ig < nG700points; ig++) {
    yaxisG700[ig] = countG700[ig]/totalG700[ig];
    errorG700[ig] = yaxisG700[ig]*TMath::Sqrt(1./countG700[ig]+1./totalG700[ig]);
  }
  
  Double_t xaxisG1200[nG1200points] = {50.,100.,150.};
  Double_t countG1200[nG1200points] = {35.,2060.,2711.};
  Double_t totalG1200[nG1200points] = {5822.,5822.,5822.};
  Double_t yaxisG1200[nG1200points];
  Double_t errorG1200[nG1200points];
  for (int ig = 0; ig < nG1200points; ig++) {
    yaxisG1200[ig] = countG1200[ig]/totalG1200[ig];
    errorG1200[ig] = yaxisG1200[ig]*TMath::Sqrt(1./countG1200[ig]+1./totalG1200[ig]);
  }


  TGraphErrors *gluino800   = new TGraphErrors(nG400points, xaxisG400, 
					       yaxisG400, 0, errorG400);
  TGraphErrors *gluino1200   = new TGraphErrors(nG700points, xaxisG700, 
  					       yaxisG700, NULL, errorG700);
  TGraphErrors *gluino1600  = new TGraphErrors(nG1200points, xaxisG1200, 
					       yaxisG1200, NULL, errorG1200);
  TGraphErrors *gluino      = new TGraphErrors(nG400points+nG1200points, bothxG, 
					       bothyG,NULL,NULL);
  TGraphErrors *gluinoPlus  = new TGraphErrors(nG400points+nG1200points, bothxG, 
					       bothyGplus1, NULL, NULL);
  TGraphErrors *gluinoMinus = new TGraphErrors(nG400points+nG1200points, bothxG, 
					       bothyGminus1, NULL, NULL);

  gluino->SetTitle("gluino800 stopping efficiency;E_{gluon}(E_{top}) [GeV];#varepsilon_{RECO}");
  gluino800->SetTitle("gluino800 stopping efficiency;E_{gluon}(E_{top}) [GeV];#varepsilon_{RECO}");
  gluino1200->SetTitle("gluino1200 stopping efficiency;E_{gluon} [GeV];#varepsilon_{RECO}");
  gluino1600->SetTitle("gluino1600 stopping efficiency;E_{gluon}(E_{top}) [GeV];#varepsilon_{RECO}");

  gluino->SetMarkerSize(0.1);
  gluino->SetMarkerColor(kWhite);

  gluino800->SetLineColor(kRed);
  gluino800->SetMarkerColor(kRed);
  gluino800->SetMarkerStyle(24);
  gluino800->SetMarkerSize(1.15);
  
  gluino1200->SetLineColor(kRed+2);
  gluino1200->SetMarkerColor(kRed+2);
  gluino1200->SetMarkerStyle(26);
  gluino1200->SetMarkerSize(1.15);
  
  gluino1600->SetLineColor(kRed+3);
  gluino1600->SetMarkerColor(kRed+3);
  gluino1600->SetMarkerStyle(25);
  gluino1600->SetMarkerSize(1.15);

  gluino800->SetLineWidth(2);
  gluino1200->SetLineWidth(2);
  gluino1600->SetLineWidth(2);

  gluino->SetMaximum(0.53);
  gluino->GetXaxis()->SetLimits(40,390); // HOW WE SET THE X RANGE ON THE PLOT
  //gluino->Draw("AP"); //AP 
  gluino1200->Draw("AP");
  gluino800->Draw("P same");
  gluino1600->Draw("P same");
 // gluinoPlus->Draw("P same");
  //gluinoMinus->Draw("P same");

  
  TF1* gfit = new TF1("gfit","[0]*TMath::Erf([1]*x-[2])+[3]",0,500);
  gfit.SetParameters(0.25,0.034,2.33,0.25);
  TF1* gfitp = new TF1("gfitp","[0]*TMath::Erf([1]*x-[2])+[3]",0,500);
  gfitp->SetParameters(0.25,0.034,2.33,0.25);
  gfitp->SetFillStyle(1001); //1001
  gfitp->SetFillColor(kRed-10);
  gfitp->SetLineColor(kRed-10);
  gfitp->SetLineWidth(7);
 // gfitp->Draw("FC same");
  TF1* gfitm = new TF1("gfitm","[0]*TMath::Erf([1]*x-[2])+[3]",0,500);
  gfitm->SetParameters(0.25,0.034,2.33,0.25);
  gfitm->SetFillStyle(1001);
  gfitm->SetFillColor(10);
  gfitm->SetLineColor(kRed-10);
  gfitm->SetLineWidth(7);
  //gfitm->Draw("FC same");
  

  
  gluino->Fit(gfit);
  gluinoPlus->Fit(gfitp);
  gluinoMinus->Fit(gfitm);
  double gmax = gfit->GetMaximum();
  std::cout << "=================gluino max = "
	    << gmax
	    <<"=================" << std::endl;

  double gavg =0;
  double gsystematic = 0;
  for (int i = 8; i<nGtotalpoints; i++) {
    std::cout << bothyG[i] << " - " << gmax << " = " << fabs(bothyG[i] - gmax) <<std::endl;
    gavg += fabs(bothyG[i] - gmax);
    if (fabs(bothyG[i] - gmax) > gsystematic)
      gsystematic = fabs(bothyG[i] - gmax);
  }
  gavg /= (nGtotalpoints-8);
  std::cout << "Systematic error on det eff: " << gsystematic/gmax << std::endl << std::endl;
  
  
  /****** REPEAT FOR STOP ********/
  
  Int_t nS300points=5;
  Int_t nS400points=6;
  Int_t nS600points=4;
  Int_t nS1000points=7;
  Int_t nSallpoints=nS300points+nS400points+nS600points+nS1000points;

  // selected EB+HB
  Double_t countBothS[nSallpoints] = {589,
				      721,
				      665,
				      589,
				      750,
				      854,
				      937,
				      869,
				      920,
				      1040,
				      833,
				      917,
				      954,
				      868,
				      1507,
				      1420,
				      855,
				      1452,
				      1404,
				      1383,
				      1370,
				      1243};

  // stopped EB+HB
  Double_t totalBothS[nSallpoints] = {3218,
				      3217,
				      2861,
				      2519,
				      2857,
				      3144,
				      3215,
				      2858,
				      2865,
				      3219,
				      2502,
				      2865,
				      2859,
				      2515,
				      4322,
				      4322,
				      2514,
				      4418,
				      4421,
				      4317,
				      4368,
				      4016};
  // visible energy (top energy)
  Double_t bothxS[nSallpoints] = {89,
				  98,
				  98,
				  99,
				  111,
				  118,
				  130,
				  141,
				  189,
				  192,
				  192,
				  210,
				  231,
				  250,
				  250,
				  300,
				  317,
				  351,
				  400,
				  450,
				  500,
				  510};

  Double_t bothyS[nSallpoints];
  Double_t bothErrS[nSallpoints];
  Double_t bothySplus1[nSallpoints];
  Double_t bothySminus1[nSallpoints];
  for (int ib = 0; ib < nSallpoints; ib++) {
    bothyS[ib] = countBothS[ib]/totalBothS[ib];
    bothErrS[ib] = bothyS[ib]*TMath::Sqrt(1./countBothS[ib]+1./totalBothS[ib]);

    bothySplus1[ib] = bothyS[ib] + bothErrS[ib];
    bothySminus1[ib] = bothyS[ib] - bothErrS[ib];
  }

  Double_t xaxisS300[nS300points] = {89,
				     98,
				     118,
				     130,
				     192};
  Double_t countS300[nS300points] = {589,
				     721,
				     854,
				     937,
				     1040};
  Double_t totalS300[nS300points] = {3218,
				     3217,
				     3144,
				     3215,
				     3219};
  Double_t yaxisS300[nS300points];
  Double_t errorS300[nS300points];
  for (int is = 0; is < nS300points; is++) {
    yaxisS300[is] = countS300[is]/totalS300[is];
    errorS300[is] = yaxisS300[is]*TMath::Sqrt(1./countS300[is]+1./totalS300[is]);
  }

  Double_t xaxisS400[nS400points] = {98,
				     111,
				     141,
				     189,
				     210,
				     231};
  Double_t countS400[nS400points] = {665,
				     750,
				     869,
				     920,
				     917,
				     954};
  Double_t totalS400[nS400points] = {2861,
				     2857,
				     2858,
				     2865,
				     2865,
				     2859};
  Double_t yaxisS400[nS400points];
  Double_t errorS400[nS400points];
  for (int is = 0; is < nS400points; is++) {
    yaxisS400[is] = countS400[is]/totalS400[is];
    errorS400[is] = yaxisS400[is]*TMath::Sqrt(1./countS400[is]+1./totalS400[is]);
  }
  
  
  // STOP 600
  Double_t xaxisS600[nS600points] = {99,
				     192,
				     251,
				     299};
  Double_t countS600[nS600points] = {589,
				     833,
				     868,
				     855};
  Double_t totalS600[nS600points] = {2519,
				     2502,
				     2515,
				     2514};
  Double_t yaxisS600[nS600points];
  Double_t errorS600[nS600points];
  for (int is = 0; is < nS600points; is++) {
    yaxisS600[is] = countS600[is]/totalS600[is];
    errorS600[is] = yaxisS600[is]*TMath::Sqrt(1./countS600[is]+1./totalS600[is]);
  }
  // STOP 1000
  Double_t xaxisS1000[nS1000points] = {250.,300.,351.,400.,450.,500.,510.,};
  Double_t countS1000[nS1000points] = {1507,
				       1420,
				       1452,
				       1404,
				       1383,
				       1370,
				       1243};
  Double_t totalS1000[nS1000points] = {4322,
				       4322,
				       4418,
				       4421,
				       4317,
				       4368,
				       4016};
  Double_t yaxisS1000[nS1000points];
  Double_t errorS1000[nS1000points];
  for (int is = 0; is < nS1000points; is++) {
    yaxisS1000[is] = countS1000[is]/totalS1000[is];
    errorS1000[is] = yaxisS1000[is]*TMath::Sqrt(1./countS1000[is]+1./totalS1000[is]);
  }
  
  TGraphErrors *stop300 = new TGraphErrors(nS300points, xaxisS300, 
					   yaxisS300, 0, errorS300);
  TGraphErrors *stop400 = new TGraphErrors(nS400points, xaxisS400, 
					   yaxisS400, 0, errorS400);
  TGraphErrors *stop600 = new TGraphErrors(nS600points, xaxisS600, 
					   yaxisS600, 0, errorS600);
  TGraphErrors *stop1000 = new TGraphErrors(nS1000points, xaxisS1000, 
					   yaxisS1000, errorS1000);
  TGraphErrors *stop = new TGraphErrors(nSallpoints, bothxS, 
					bothyS, 0, bothErrS);
  TGraphErrors *stopPlus = new TGraphErrors(nSallpoints, bothxS, 
					    bothySplus1, NULL, NULL);
  TGraphErrors *stopMinus = new TGraphErrors(nSallpoints, bothxS, 
					     bothySminus1, NULL, NULL);

  stop300->SetTitle("stop300 stopping efficiency;E_{gluon|top} [GeV];#varepsilon_{RECO}");
  stop400->SetTitle("stop400 stopping efficiency;E_{gluon|top} [GeV];#varepsilon_{RECO}");
  stop600->SetTitle("stop600 stopping efficiency;E_{gluon|top} [GeV];#varepsilon_{RECO}");
  stop1000->SetTitle("stop1000 stopping efficiency;E_{gluon|top} [GeV];#varepsilon_{RECO}");
  stop->SetTitle("stopping efficiency;E_{gluon|top} [GeV];#varepsilon_{RECO}");

  stop->SetMarkerSize(0.0);
  stop->SetMarkerColor(kWhite);
  stop->SetLineColor(kBlue);

  stop300->SetLineColor(kBlue-4);  
  stop300->SetMarkerColor(kBlue-4);// kBlue-4
  stop300->SetMarkerStyle(20);     // 20
  stop300->SetMarkerSize(1.15);
  stop400->SetLineColor(kBlue+1);
  stop400->SetMarkerColor(kBlue+1);// kBlue+1
  stop400->SetMarkerStyle(22);     // 22
  stop400->SetMarkerSize(1.15);
  stop600->SetLineColor(kBlue+3);
  stop600->SetMarkerColor(kBlue+3);// kBlue+3
  stop600->SetMarkerStyle(21);     // 23
  stop600->SetMarkerSize(1.15);
  stop1000->SetLineColor(kCyan+3);
  stop1000->SetMarkerColor(kCyan+3);// kBlue+3
  stop1000->SetMarkerStyle(34);     // 24
  stop1000->SetMarkerSize(1.15);

  stop300->SetLineWidth(2);
  stop400->SetLineWidth(2);
  stop600->SetLineWidth(2);
  stop1000->SetLineWidth(2);

  //stop->Draw("P same");  
  //stopPlus->Draw("p same");
  //stopMinus->Draw("p same");
  //stop600->Draw("P same");
  //stop400->Draw("P same");
  //stop300->Draw("P same");
  //stop1000->Draw("P same");
  
  TF1* sfit = new TF1("sfit","[0]*TMath::Erf([1]*x-[2])+[3]",0,400);
  sfit.SetParameters(20, 0.001, -1., -22);
  //sfit->SetParameters(0.323,0.034,2.33,-0.0084);
  //TF1* sfit = new TF1("sfit","[0]*TMath::Erf(0.034*x-2.33)+[1]",0,500);
  //sfit->SetParameters(0.323,-0.0084);
  sfit->SetLineColor(kBlue-9); // 10
  sfit->SetRange(50,370);

  TF1* sfitp = new TF1("sfitp","[0]*TMath::Erf([1]*x-[2])+[3]",0,400);
  sfitp.SetParameters(20, 0.001, -1., -22);

  //sfit.SetParameters(0.25,0.034,2.33,0.25);
  //TF1* sfitp = new TF1("sfitp","[0]*TMath::Erf(0.034*x-2.33)+[1]",0,500);
  //sfitp->SetParameters(0.323,-0.0084);
  sfitp->SetLineColor(kBlue-9); // 10
  sfitp->SetRange(50,370);
  sfitp->SetFillStyle(1001); // 1001
  sfitp->SetFillColor(kBlue-9); // 10
  sfitp->SetLineWidth(7);
  //sfitp->Draw("FC same");

  TF1* sfitm = new TF1("sfitm","[0]*TMath::Erf([1]*x-[2])+[3]",0,400);
  sfitm.SetParameters(20, 0.001, -1., -22);

  //sfit.SetParameters(0.25,0.034,2.33,0.25);
  //TF1* sfitm = new TF1("sfitm","[0]*TMath::Erf(0.034*x-2.33)+[1]",0,500);
  //sfitm->SetParameters(0.323,-0.0084);
  sfitm->SetLineColor(kBlue-9); // 10
  sfitm->SetLineWidth(7);
  sfitm->SetFillColor(10); // 10
  sfitm->SetFillStyle(1001);
  sfitm->SetRange(50,370);
  //sfitm->Draw("FC same");

  //sfit->SetLineColor(kBlue-10);
  //sfit->Draw("f same");
  //stop600->Draw("P same");
  //stop400->Draw("P same");
  //stop300->Draw("P same");
  //stop1000->Draw("P same");

  //stop->Fit(sfit);
  stopPlus->Fit(sfitp);
  stopMinus->Fit(sfitm);
  
  double smax = sfit->GetMaximum();
  std::cout << "=================stop max = "
	    << smax
	    <<"=================" << std::endl;

  double savg =0;
  double ssystematic = 0;
  for (int i = 6; i<nSallpoints; i++) {
    std::cout << bothyS[i] << " - " << smax << " = " << fabs(bothyS[i] - smax) <<std::endl;
    savg += fabs(bothyS[i] - smax);
    if (fabs(bothyS[i] - smax) > ssystematic)
      ssystematic = fabs(bothyS[i] - smax);
  }
  gavg /= (nGtotalpoints-8);
  std::cout << "Systematic error on det eff: " << ssystematic/smax << std::endl << std::endl;


  /****** LEGEND ********/
  
  leg = new TLegend(0.55,0.15,0.9,0.45,NULL,"brNDC");
  leg->SetTextFont(42);
  leg->SetHeader("CMS Simulation,  #sqrt{s} = 13 TeV");
  leg->AddEntry(gluino800,"m_{#tilde{g}} = 800 GeV","ep");
  leg->AddEntry(gluino1200,"m_{#tilde{g}} = 1200 GeV","ep");
  leg->AddEntry(gluino1600,"m_{#tilde{g}} = 1600 GeV","ep");
  //leg->AddEntry(stop300,"m_{#tilde{t}} = 300 GeV","ep");
  //leg->AddEntry(stop400,"m_{#tilde{t}} = 400 GeV","ep");
  //leg->AddEntry(stop600,"m_{#tilde{t}} = 600 GeV","ep");
  //leg->AddEntry(stop1000,"m_{#tilde{t}} = 1000 GeV","ep");
  leg->SetFillColor(kWhite);
  leg->SetBorderSize(0);
  leg->Draw();
  
  canvas->RedrawAxis();

  canvas->Print("summer12_8TeV_detectionEff.pdf");

}
