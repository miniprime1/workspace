fprintf("Lissajous Curve\n\n");

a = input("Enter a: ");
b = input("Enter b: ");
m = input("Enter m: ");
n = input("Enter n: ");
alpha = input("Enter alpha: ");
beta = input("Enter beta: ");

t = linspace(0, 2*pi, 1000);
x = a * sin(m*t + alpha);
y = b * sin(n*t + beta);

plot(x, y, 'b');
legend('Lissajous Curve');