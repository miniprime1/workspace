print("R Calculator v1.0")
print("")
print("Options")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
option = readline(prompt="Enter option: ")

print("")
a = strtoi(readline(prompt="Enter 1st input: "))
b = strtoi(readline(prompt="Enter 2nd input: "))

print("")
if (option == "1") {
  r = a+b
  print(paste("Result:", a, "+", b, "=", r))
} else if (option == "2") {
  r = a-b
  print(paste("Result:", a, "-", b, "=", r))
} else if (option == "2") {
  r = a*b
  print(paste("Result:", a, "*", b, "=", r))
} else if (option == "2") {
  r = a/b
  print(paste("Result:", a, "/", b, "=", r))
} else {
  print("Error: invalid choice.")
}