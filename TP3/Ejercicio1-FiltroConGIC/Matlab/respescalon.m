close all;

w0ideal = 13e3;
Qideal = 4;
R6ideal = 8.8e3;
R = 2.2e3;
C = 34.965e-9;
s = tf('s');

h3 = 0.5 *(s^2*C^2*R^2 - s*C*R^2/R6ideal + 1)/(s*(s^2*C^2*R^2 + s*C*R^2/R6ideal+1));

MedicionOsc1 = csvread('resim.csv',2);

impulse(h3);
hold on;
plot(MedicionOsc1(:,1),MedicionOsc1(:,2));
yline(0.5);
title('Respuesta al Escalon');
xlabel('Tiempo [s]');
ylabel('Tension [V]');
legend({'Teorico','Simulado','Entrada'},'Location','northeast');

grid on;