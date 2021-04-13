w=logspace(-1,2,100);
H=1./(1+w.^2).^0.5;
semilogx(w,H); grid on;