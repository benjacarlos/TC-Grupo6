% f = linspace(100,10e6,128);
% f = w/(2*pi);
close all;
clear all;

s   = tf('s');
Vin = 1;

t = 00;

R6 = 8.8e3;
R = 2.2e3;
C = 34.965e-9;

h = R*(s^2*C^2*R^3*R6 -s*C*R^3 +R*R6)/(s^2*C^2*R^4 + s*C*R^3);


DatosSimulados=csvread('zinsimulado.csv',2);
DatosMedidos=csvread('zinMedido.csv',1);


% theoryBode(H);
% close all
opt = bodeoptions();
opt.FreqUnits = 'Hz';
opt.PhaseVisible='off';

a = linspace(.01e3,10e6,128);

%%%%%%%Bode phase%%%%%%%
% [mag1,pha1,wout1]=bode(h1, opt);
% [mag2,pha2,wout2]=bode(h2, opt);
[mag3,pha3,wout3]=bode(h, a);

% mag1 = squeeze(mag1);
% pha1 = squeeze(pha1);
% 
% mag2 = squeeze(mag2);
% pha2 = squeeze(pha2);

mag3 = squeeze(mag3);
pha3 = squeeze(pha3);

% semilogx(wout1/(2*pi), pha1,'LineWidth',1);
% semilogx(wout2/(2*pi), pha2,'LineWidth',1);
% semilogx(wout3/(2*pi), pha3,'LineWidth',1);
% hold on;

f = zeros(size(DatosMedidos(:,1))-t);

for k = 1:(size(DatosMedidos(:,1))-t)
   f(k) =  DatosMedidos(k,1);
end


temp2 = zeros(size(DatosMedidos(:,7))-t);

for k = 1:(size(DatosMedidos(:,5))-t)
   temp2(k) =  DatosMedidos(k,7);
end


% semilogx(DatosSimulados(:,1),-DatosSimulados(:,3),'r','LineWidth',1);
% semilogx(f,-temp2,'k','LineWidth',1);
% % 
% xlabel('frecuencia [Hz]');
% ylabel('fase [grados]');
% 
% xlim([1e3 1e6]);
% title('Diagrama de fase');
% legend({'Teorico','Simulado','Experimental'},'Location','southwest');
% grid on
% hold off;

%%%%%%%%%%
figure;

% semilogx(wout1/(2*pi),mag1,'LineWidth',1);
% semilogx(wout3/(2*pi), mag3,'LineWidth',1);
semilogx(wout3/(2*pi), 20*log10(mag3),'LineWidth',1);
hold on;



% temp1 = zeros(size(DatosMedidos(:,5))-t);
% 
% for k = 1:(size(DatosMedidos(:,5))-t)
%    temp1(k) =  DatosMedidos(k,4)/DatosMedidos(k,6);
% end

% Vin./(10.^(./20))

semilogx(DatosSimulados(:,1),DatosSimulados(:,2),'r','LineWidth',1);
semilogx(DatosMedidos(:,1),20*log10(DatosMedidos(:,9)),'k','LineWidth',1); %    %'Marker','o'

% semilogx(DatosSimulados(:,1),Vin./(10.^(DatosSimulados(:,2)./20)),'r','LineWidth',1);
% semilogx(DatosMedidos(:,1),DatosMedidos(:,9),'k','LineWidth',1);     %,'Marker','o');
% 
% semilogx(DatosSimulados(:,1),DatosSimulados(:,2),'r','LineWidth',1);
% semilogx(DatosMedidos(:,1),DatosMedidos(:,2),'k','LineWidth',1);     %,'Marker','o');

%%%%%%%%%%Datos en dB%%%%%%%%
% semilogx(DatosSimulados(:,1),DatosSimulados(:,2),'r','LineWidth',1);
% semilogx(DatosMedidos(:,1),DatosMedidos(:,2),'k','LineWidth',1);     %,'Marker','o');
xlabel('frecuencia [Hz]');
ylabel('Impedancia [dB]');
% ylim([0 1.4e4]);
% xlim([.1e3 1e6]);
title('Impedancia de Entrada');
legend({'Teorico','Simulado','Experimental'},'Location','southwest');
% legend({'Infinito','Finito','Real'});
grid on
hold off;