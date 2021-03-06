close all;

s = tf('s');
opt = bodeoptions();
opt.FreqUnits = 'Hz';

w0ideal = 13e3;
Qideal = 4;
R6ideal = 8.8e3;
R = 2.2e3;
C = 34.965e-9;
% 
% 
% 
% Rideal = 2.2e3; R6ideal = 8.8e3; Cideal = 1/w0ideal/Rideal;
% Lideal = Rideal^2*Cideal;
% Hideal = 2*tf([Lideal/R6ideal, 0], [Lideal*Cideal, Lideal/R6ideal, 1]);
% 
% Rcalc = 2.2e3; R6calc = 8.8e3; Ccalc = 10^(-9)/(1/39+1/330);
% f0calc = 1/2/pi/Rcalc/Ccalc;
% relerrorf0calc = abs(f0ideal-f0calc)/f0ideal*100;
% 
% Lcalc = Rcalc^2*Ccalc;
% Hcalc = 2*tf([Lcalc/R6calc, 0], [Lcalc*Ccalc, Lcalc/R6calc, 1]);
% 
% H = Hcalc;
% 
% Zin = R6calc + 1/(s*Ccalc + 1/s/Lcalc);
% 
% %bode(Hideal, w, opt);
% %hold on;
% %bode(Hcalc, w, opt);
% %grid on;
% 
% w = 2*pi*logspace(1, 6, 1000);
% %superponedor('','tc_tp3_ej1_hf.csv', 'tc_tp3_ej1_hf_spice.csv', H, w, 'tc_tp3_ej1_hf');
% % 
%  w = 2*pi*logspace(2,6,1000);
% %superponedorZ('','tc_tp3_ej1_zin.csv', 'tc_tp3_ej1_zin_spice_x1.csv', Zin, w);
% %superponedorZ('','tc_tp3_ej1_zin.csv', 'tc_tp3_ej1_zin_spice_x10.csv', Zin, w);
% 
% 
% % zmag = findall(groot, 'Type', 'figure');  % Since version R2014b
% % zmag = zmag(2);
% % zmag = zmag.Children(2);
% % zmag.YLim = [0 200000];
% 
% % superponedorZsinH('','bode rochi.csv', 'tc_tp3_ej1_zout_spice_x1.csv', w, 'tc_tp3_ej1_zout');
% 

valoresR6 = [R6ideal/8, R6ideal/7, R6ideal/5, R6ideal, R6ideal*10];%R6ideal/50, R6ideal/30, R6ideal/10
% Hideal = 2*tf([Lideal/valoresR6(1), 0], [Lideal*Cideal, Lideal/valoresR6(1), 1]);
Hideal = (s^2*C^2*R^2 - s*C*R^2/valoresR6(1)+1)/(s^2*C^2*R^2 + s*C*R^2/valoresR6(1)+1);

pzopt = pzoptions();
pzopt.FreqUnits = 'Hz';
% pzopt.Grid = 'on';
pzopt.XLabel.String = 'Parte real';
pzopt.YLabel.String = 'Parte imaginaria';
pzopt.Title.String = ' ';
pzmap(Hideal, pzopt);
% grid on;
fig = gcf;
% fig.Position = [100 100 1000 500];
hold on;

for i=2:size(valoresR6,2)
    Hideal = (s^2*C^2*R^2 - s*C*R^2/valoresR6(i)+1)/(s^2*C^2*R^2 + s*C*R^2/valoresR6(i)+1);
    pzmap(Hideal, pzopt);
end
ax = gca;
% ax.XLim = [-1.7e5 1.7e5];
% ax.YLim = [-1.7e5 1.7e5];
legend({'0.5R','0.6R','0.8R','4R','40R'});%'0.08R','0.13R','0.4R',
hold off;