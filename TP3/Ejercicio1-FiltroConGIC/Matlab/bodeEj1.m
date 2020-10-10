clear all;
f = linspace(100,10e6,128);
% f = w/(2*pi);
s   = tf('s');

w0ideal = 13e3;
Qideal = 4;
R6ideal = 8.8e3;
R = 2.2e3;
C = 34.965e-9;

h3 = (s^2*C^2*R^2 - s*C*R^2/R6ideal + 1)/(s^2*C^2*R^2 + s*C*R^2/R6ideal+1);

%%%%%%%%Cargar los csv%%%%%%%%
DatosSimulados=csvread('bodesim.csv',2);
DatosMedidos=csvread('bodeGIC.csv',2);

% theoryBode(H);
close all
opt = bodeoptions();
opt.FreqUnits = 'Hz';
opt.PhaseVisible='off';

%%%%%%%Bode phase%%%%%%%
% [mag1,pha1,wout1]=bode(h1, opt);
% [mag2,pha2,wout2]=bode(h2, opt);
[mag3,pha3,wout3]=bode(h3, opt);

% mag1 = squeeze(mag1);
% pha1 = squeeze(pha1);
% 
% mag2 = squeeze(mag2);
% pha2 = squeeze(pha2);

mag3 = squeeze(mag3);
pha3 = squeeze(pha3);

% semilogx(wout/(2*pi), pha1,'LineWidth',1);
% semilogx(wout/(2*pi), pha2,'LineWidth',1);
t=32;
for k = 1:(size(pha3)-t)
   pha3(k)=  pha3(k)-360;
end

semilogx(wout3/(2*pi), pha3,'LineWidth',1);
hold on;

t= 0;
f = zeros(size(DatosMedidos(:,1))-t);

for k = 1:(size(DatosMedidos(:,1))-t)
   f(k) =  DatosMedidos(k,1);
end
temp2 = zeros(size(DatosMedidos(:,3))-t);

for k = 1:(size(DatosMedidos(:,1))-t)
   temp2(k) =  DatosMedidos(k,3);
end

semilogx(DatosSimulados(:,1),DatosSimulados(:,3),'r','LineWidth',1);
semilogx(f,temp2,'k','LineWidth',1);
% 
xlabel('frecuencia [Hz]');
ylabel('fase [grados]');

xlim([.1e3 3e6]);

title('Diagrama de fase');
legend({'Teorico','Simulado','Experimental'},'Location','northeast');
grid on
hold off;

%%%%%%%%%%Bode mag%%%%%%%%%%
figure;

% mag1 = h1*ones(size(wout3));
% mag2 = h2*ones(size(wout3));

% semilogx(wout3/(2*pi), 20*log10(mag1),'LineWidth',1);

% semilogx(wout3/(2*pi), 20*log10(mag2),'LineWidth',1);
semilogx(wout3/(2*pi), 20*log10(mag3),'LineWidth',1);
hold on;

% semilogx(wout3/(2*pi), 20*log10(mag2),'LineWidth',1);
% semilogx(wout3/(2*pi), 20*log10(mag3),'LineWidth',1);

%%%%%%%%%%Datos en dB%%%%%%%%
semilogx(DatosSimulados(:,1),DatosSimulados(:,2),'r','LineWidth',1);
semilogx(DatosMedidos(:,1),DatosMedidos(:,2),'k','LineWidth',1);     %,'Marker','o');
xlabel('frecuencia [Hz]');
ylabel('magnitud [dB]');

xlim([0.1e3 3e6]);

title('Diagrama de magnitud');
legend({'Teorico','Simulado','Experimental'},'Location','northeast');
% legend({'Infinito','Finito','Real'});
grid on
hold off;



