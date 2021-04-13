import uuid

print("UUID Generator v1.0")
print("Copyright (c) 2020 miniprime1")

while True:
    print()
    for i in range(10): print(uuid.uuid4())
    input('Press enter key to generate more...')
