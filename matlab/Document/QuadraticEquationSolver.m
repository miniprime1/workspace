fprintf("Quadratic Equation Solver v1.0\n")
fprintf("[Equation: ax^2 + bx + c = 0]\n\n")

a = input("Enter a: ");
b = input("Enter b: ");
c = input("Enter c: ");

try
    fprintf("\nSolving Equation...")
    x1 = (-b+sqrt(b^2-(4*a*c)))/(2*a);
    x2 = (-b-sqrt(b^2-(4*a*c)))/(2*a);
    fprintf("\nDone!\n")
    fprintf("\nEquation: \n%fx^2 + %fx + %f = 0", a, b, c)
    fprintf("\n\nResult: \nx = %f, %f\n", x1, x2)
catch
    fprintf("\nError: cannot solve equation!\n")
end