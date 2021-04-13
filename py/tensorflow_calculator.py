import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()

a = tf.placeholder("float")
b = tf.placeholder("float")

add = tf.add(a, b)
sub = tf.subtract(a, b)
mul = tf.multiply(a, b)
div = tf.div(a, b)
sess = tf.Session()

print("Calculator v1.0")
print("[Powered by TensorFlow]\n")

print("Options")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter choice: ")
 
print()
if choice == "1":
    x = float(input("Enter 1st input: "))
    y = float(input("Enter 2nd input: "))
    print("\nResult")
    result = sess.run(add, feed_dict={a: x, b: y})
    print(x, "+", y, "=", result)

elif choice == "2":
    x = float(input("Enter 1st input: "))
    y = float(input("Enter 2nd input: "))
    print("\nResult")
    result = sess.run(sub, feed_dict={a: x, b: y})
    print(x, "-", y, "=", result)

elif choice == "3":
    x = float(input("Enter 1st input: "))
    y = float(input("Enter 2nd input: "))
    print("\nResult")
    result = sess.run(mul, feed_dict={a: x, b: y})
    print(x, "*", y, "=", result)

elif choice == "4":
    x = float(input("Enter 1st input: "))
    y = float(input("Enter 2nd input: "))
    print("\nResult")
    result = sess.run(div, feed_dict={a: x, b: y})
    print(x, "/", y, "=", result)
    
else:
    print("Error: Invalid Choice")