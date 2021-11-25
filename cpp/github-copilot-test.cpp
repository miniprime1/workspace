// function that integrate a function from a to b
double integrate(double (*f)(double), double a, double b) {
  double h = (b - a) / 100;
  double sum = 0;
  for (double i = a; i < b; i += h) {
    sum += f(i) * h;
  }
  return sum;
}

// function that derive function at a
double derive(double (*f)(double), double a) {
  double h = 0.001;
  return (f(a + h) - f(a)) / h;
}

// function that get sum of function value from a to b
double sum(double (*f)(double), double a, double b) {
  double h = (b - a) / 100;
  double sum = 0;
  for (double i = a; i < b; i += h) {
    sum += f(i);
  }
  return sum;
}

