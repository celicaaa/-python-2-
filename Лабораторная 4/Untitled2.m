clc
clear
a=0;
b=1;
n=22;
h=(b-a)/n;
x=0:h:b;
Y=f1(x);
plot(x,Y, '-R', 'Linewidth',3,'MarkerSize',3)
title('������ ��������������� �������')
grid on
hold on
 
fprintf('����� �� trapz:')
s1=trapz(x,Y);
fprintf('%.4f',s1)

fprintf('����� �� quad:')
s2=quad(x,Y)
fprintf('%.4f',s2)





