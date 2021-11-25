import sys
print("Python", sys.version, 'on', sys.platform)
print('Type "help", "copyright", "credits" or "license" for more information.')

while True:
  i = input(">>> ")
  if i == "exit()": break
  try: eval(i)
  except SyntaxError as s: exec(i)
  except Exception as e: print(str(e))