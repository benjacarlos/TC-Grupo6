%% PRUEBA PARA TRANSFERENCIA LARGA

syms s;

R1=10000;
R2=50000;
R3=10*R;
L=0.5;
C2=15e-9;
C1=10*C2;

% TRANSFERENCIA LARGA
H=-(1/R3 + (C2*s*(R1 + R2 - L*R2 + C1*R1*R2*s))/(2*R1 + R2 + C2*R1^2*s + C2*L*R2^2*s - C2*L^2*R2^2*s + 2*C1*R1*R2*s + C2*R1*R2*s + C1*C2*R1^2*R2*s^2 + 2*C1*C2*L*R1*R2^2*s^2 - 2*C1*C2*L^2*R1*R2^2*s^2))/(1/R3 + (C2*s*(R1 + L*R2 + C1*R1*R2*s))/(2*R1 + R2 + C2*R1^2*s + C2*L*R2^2*s - C2*L^2*R2^2*s + 2*C1*R1*R2*s + C2*R1*R2*s + C1*C2*R1^2*R2*s^2 + 2*C1*C2*L*R1*R2^2*s^2 - 2*C1*C2*L^2*R1*R2^2*s^2))
[numerador,denominador]=numden(H);
Nume = simplify(coeffs(numerador, s)).'
Deno = simplify(coeffs(denominador, s)).'

% SACO LOS VALORES DEL BODE
[MAG, PHASE, W] = bode(H);
HdB = 20*log10(squeeze(MAG));
fase = squeeze(PHASE);
f = W/(2*pi);

% PLOTEO
hold on
semilogx(f,HdB);
grid minor
xlabel('Frecuencia (Hz)');
ylabel('Magnitud (dB)');
title('Magnitude Bode Diagram');
print -dpdf 'Magnitud';


