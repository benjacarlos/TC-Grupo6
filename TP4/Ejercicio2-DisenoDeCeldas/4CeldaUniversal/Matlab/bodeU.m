clear all;
% f = linspace(100,10e6,128);
% f = w/(2*pi);
s = tf('s');

B = 5/8;
% B = 3/80;
W0 = 2*pi*16E3;

[b,a] = cheby2(3,50,) 

% H = (1 - (1/(( (1/(1/B * (s/W0 + W0/s))))^2 + 1.0977343 * ((1/(1/B * (s/W0 + W0/s)))) + 1.1025103)));
% 
% 
% poles=roots(cell2mat(H.Den));
% zeros=roots(cell2mat(H.Num));
% 
% close all
% opt = bodeoptions();
% opt.FreqUnits = 'Hz';
% opt.PhaseVisible='off';
% 
% %%%%%%%Bode phase%%%%%%%
% [mag,pha,wout] = bode(H, opt);
% 
% mag = squeeze(mag);
% pha = squeeze(pha);
% 
% semilogx(wout/(2*pi), 20*log10(mag),'LineWidth',1);
% 
% xlabel('frecuencia [Hz]');
% ylabel('magnitud [dB]');
% 
% % xlim([1e3 1e6]);
% 
% title('Diagrama de magnitud');
% legend({'Teorico','Simulado','Experimental'},'Location','southwest');
% grid on
% hold off;
