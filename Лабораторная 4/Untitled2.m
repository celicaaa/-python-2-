clc
clear
a=0;
b=1;
n=22;
h=(b-a)/n;
x=0:h:b;
Y=f1(x);
plot(x,Y, '-R', 'Linewidth',3,'MarkerSize',3)
title('график подынтегральной функции')
grid on
hold on
 
fprintf('ответ по trapz:')
s1=trapz(x,Y);
fprintf('%.4f',s1)

fprintf('ответ по quad:')
s2=quad(x,Y)
fprintf('%.4f',s2)





