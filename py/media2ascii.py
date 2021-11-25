import cv2

CHARS = '.,-~:;=!*#$@'
nw = 100

print("media2ascii v1.0")
print("Copyright (c) 2020 miniprime1\n")

print("Options")
print("1. image2ascii")
print("2. video2ascii")
option = input("Enter choice: ")

if option == '1':
  opath = input("\nEnter File Path: ")
  spath = input("Enter Save Path: ")
  f = open(spath, 'w')
  print("\n", end='')
  print("\x1b[2J", end='')
  img = cv2.imread(opath)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  h, w = img.shape
  nh = int(h / w * nw)
  img = cv2.resize(img, (nw * 2, nh))
  for row in img:
    for pixel in row:
      index = int(pixel / 256 * len(CHARS))
      f.write(CHARS[index])
      print(CHARS[index], end='')
    f.write('\n')
    print()
  f.close()
elif option == '2':
  opath = input("\nEnter File Path: ")
  cap = cv2.VideoCapture(opath)
  print("\n", end='')
  print("\x1b[2J", end='')
  while cap.isOpened():
    ret, img = cap.read()
    if not ret: break
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = img.shape
    nh = int(h / w * nw)
    img = cv2.resize(img, (nw * 2, nh))
    for row in img:
      for pixel in row: # pixel 0-255 -> CHARS 0-12
        index = int(pixel / 256 * len(CHARS))
        print(CHARS[index], end='')
      print()
    print('\x1b[H', end='')
else:
  print("Error: invalid choice!")
