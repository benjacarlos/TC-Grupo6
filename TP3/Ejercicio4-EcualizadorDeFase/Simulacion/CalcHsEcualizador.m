clc
%% Declaro todads mis variables
syms R1 R2 R3 C1 C2 s L;
% Declaro todas las impedancias
R21 = L * R2;
R22 = (1-L) * R2;
cap1 = 1/(s*C1);
cap2 = 1/(s*C2);

% Primer transformacion
Za = simplify( (R21*cap1) / (R21+R22+cap1) );
Zb = simplify( (R22*cap1) / (R21+R22+cap1) );
Zc = simplify( (R21*R22) / (R21+R22+cap1) );

% Sumo las resistencias en serie que me quedaron
Z_a = simplify(Za + R1);
Z_b = simplify(Zb + R1);
Z_c = simplify(Zc + cap2);

% Segunda transformacion
Zab = simplify( (Z_a*Z_b + Z_b*Z_c + Z_c*Z_a ) / (Z_c ) );
Zbc = simplify( (Z_a*Z_b + Z_b*Z_c + Z_c*Z_a ) / (Z_a ) );
Zca = simplify( (Z_a*Z_b + Z_b*Z_c + Z_c*Z_a ) / (Z_b ) );


%   ESTO ESTABA MAL
% Zab = simplify( (Z_a*Z_b) / (Z_c + Z_a + Z_b ) );
% Zbc = simplify( (Z_b*Z_c) / (Z_c + Z_a + Z_b ) );
% Zca = simplify( (Z_c*Z_a) / (Z_c + Z_a + Z_b ) );

% Calculo los coeficientes de Zab, Zbc y Zca
% Zab
[n_ab,d_ab] = numden(Zab);
num_ab = simplify(coeffs(n_ab, s) );
den_ab = simplify(coeffs(d_ab, s) );
% Zbc
[n_bc,d_bc] = numden(Zbc);
num_bc = simplify(coeffs(n_bc, s) );
den_bc = simplify(coeffs(d_bc, s) );
% Zca
[n_ca,d_ca] = numden(Zca);
num_ca = simplify(coeffs(n_ca, s) );
den_ca = simplify(coeffs(d_ca, s) );

%% Ultimo paso

Z3 = Zab;
Z2 = simplify(1/ ( (1/Zbc) + (1/R3) ));
Z1 = simplify(1/ ( (1/Zca) + (1/R3) ));

% Calculo los coeficientes de Z1, Z2 y Z3
% Z1
[n_1,d_1] = numden(Z1);
num_1 = simplify(coeffs(n_1, s) ).'
den_1 = simplify(coeffs(d_1, s) ).'
% Z2
[n_2,d_2] = numden(Z2);
num_2 = simplify(coeffs(n_2, s) ).'
den_2 = simplify(coeffs(d_2, s) ).'
% Z1
[n_3,d_3] = numden(Z3);
num_3 = simplify(coeffs(n_3, s) ).'
den_3 = simplify(coeffs(d_3, s) ).'

%% TRANSFERENCIA

H = simplify(-Z2/Z1);
[numerador,denominador]=numden(H);
Nume = simplify(coeffs(numerador, s)).'
Deno = simplify(coeffs(denominador, s)).'



