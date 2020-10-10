close all;
DatosMedidos1=csvread('bodeGIC.csv',2);
DatosMedidos2=csvread('ZoutbodeGIC.csv',2);

R = 1e3;

zoutm = R.*(10.^(DatosMedidos1(:,2)./20)- 10.^(DatosMedidos2(:,2)./20))./(10.^(DatosMedidos2(:,2)./20));

semilogx(DatosMedidos1(:,1),zoutm,'k','LineWidth',1)
grid on;
xlim([.4e3 2e6]);
title('Impedancia de Salida');
xlabel('frecuencia [Hz]');
ylabel('Impedancia [Omega]');