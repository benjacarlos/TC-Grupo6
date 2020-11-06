clear all;
% f = linspace(100,10e6,128);
% f = w/(2*pi);
s   = tf('s');

C = 1E-9;

RA = 2E3;
RB = 10E3;

% Q0 = 1.5;
% HB = 10^(5.5/20);
% 
% Q1 = (21.01e3/(sqrt(1.44E11)))^(-1);
% ALF1 = 1/(2*Q0^2) * (1 - Q0/Q1) ;
% K1 = ALF1/(1+ALF1);
% H1 = Q0/Q1 * (1-K1);
% a1 = HB * H1/(2*Q0^2);
% 
% Q2 = (23.13e3/(sqrt(1.77E11)))^(-1);
% ALF2 = 1/(2*Q0^2) * (1 - Q0/Q2) ;
% K2 = ALF2/(1+ALF2);
% H2 = Q0/Q2 * (1-K2);
% a2 = HB * H2/(2*Q0^2);
% 
% R3 = 2*Q0/(sqrt(1.47e11)*C);
% R = R3/(4*Q0^2);
% 
% R1 = R/a1;
% R2 = R/(1-a1);
% 
% R6 = 2*Q0/(sqrt(1.77e11)*C);
% R = R6/(4*Q0^2);
% 
% R4 = R/a2;
% R5 = R/(1-a2);


% R1 = 56.45E3;
% R2 = 883;
% R3 = 7.8E3;
% R4 = 51.44E3;
% R5 = 804.5;
% R6 = 7.13E3;

h2 = 1.62E9 * s/(s^2 + 21.01e3 * s + 1.47e11) * s/(s^2 + 23.13e3 * s + 1.77e11);

% h31 = (-s* C* R2 * R3 *(RA+RB))/(s^2 * C^2 * R1 * R2 * R3 * RB + s * (C * R1 * R2 * RB + C * RB * R1 * R2 - C * R3 * RA * R1 - C * R2 * R3 * RA ) + RB * (R1 + R2));
% h32 = (-s* C* R5 * R6 *(RA+RB))/(s^2 * C^2 * R4 * R5 * R6 * RB + s * (C * R4 * R5 * RB + C * RB * R4 * R5 - C * R6 * RA * R4 - C * R5 * R6 * RA ) + RB * (R4 + R5));
% h3 = h31 * h32;

%%%%%%%%Cargar los csv%%%%%%%%
DatosSimulados=csvread('ej22bode2.csv',2);
DatosMedidos=csvread('bodeMedido.csv',1);

zinSimulados=csvread('ej22zin.csv',2);

% theoryBode(H);
close all
opt = bodeoptions();
opt.FreqUnits = 'Hz';
opt.PhaseVisible='off';

%%%%%%%Bode phase%%%%%%%
% [mag1,pha1,wout1]=bode(h1, opt);
[mag2,pha2,wout2]=bode(h2, opt);
% [mag3,pha3,wout3]=bode(h3, opt);

% mag1 = squeeze(mag1);
% pha1 = squeeze(pha1);

mag2 = squeeze(mag2);
pha2 = squeeze(pha2);

% mag3 = squeeze(mag3);
% pha3 = squeeze(pha3);

% semilogx(wout/(2*pi), pha1,'LineWidth',1);
semilogx(wout2/(2*pi), pha2,'LineWidth',1);

hold on;

% semilogx(wout3/(2*pi), pha3,'LineWidth',1);

% t= 10;
% f = zeros(size(DatosMedidos(:,1))-t);
% 
% for k = 1:(size(DatosMedidos(:,1))-t)
%    f(k) =  DatosMedidos(k,1);
% end
% temp2 = zeros(size(DatosMedidos(:,3))-t);
% 
% for k = 1:(size(DatosMedidos(:,1))-t)
%    temp2(k) =  DatosMedidos(k,3);
% end

semilogx(DatosSimulados(:,1),DatosSimulados(:,3),'r','LineWidth',1);
semilogx(DatosMedidos(:,1),DatosMedidos(:,3),'k','LineWidth',1);
% 
xlabel('frecuencia [Hz]');
ylabel('fase [grados]');

xlim([1e3 1e6]);

title('Diagrama de fase');
legend({'Teorico','Simulado','Experimental'},'Location','southwest');
grid on
hold off;
% 
%%%%%%%%%%Bode mag%%%%%%%%%%
figure;

% mag1 = h1*ones(size(wout3));
% mag2 = h2*ones(size(wout3));

% semilogx(wout3/(2*pi), 20*log10(mag1),'LineWidth',1);

semilogx(wout2/(2*pi), 20*log10(mag2),'LineWidth',1);

hold on;

% semilogx(wout3/(2*pi), 20*log10(mag3),'LineWidth',1);

% semilogx(wout3/(2*pi), 20*log10(mag2),'LineWidth',1);
% semilogx(wout3/(2*pi), 20*log10(mag3),'LineWidth',1);

%%%%%%%%%%Datos en dB%%%%%%%%
semilogx(DatosSimulados(:,1),DatosSimulados(:,2),'r','LineWidth',1);
semilogx(DatosMedidos(:,1),DatosMedidos(:,2),'k','LineWidth',1);     %,'Marker','o');
xlabel('frecuencia [Hz]');
ylabel('magnitud [dB]');

xlim([1e3 1e6]);

title('Diagrama de magnitud');
legend({'Teorico','Simulado','Experimental'},'Location','southwest');
% legend({'Infinito','Finito','Real'});
grid on
hold off;

% % % % % % % % % % % % % 
figure
semilogx(zinSimulados(:,1),10.^(zinSimulados(:,2)./20),'r','LineWidth',1);

xlabel('frecuencia [Hz]');
ylabel('Impedancia [Omega]');

xlim([1e3 1e6]);
grid on;
title('Impedancia de Entrada');

