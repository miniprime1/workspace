import sys
import platform

class Scanner():
    def __init__(self):
        self.system = platform.system()
    
    def ReadLine(self):
        i = input()
        return i

    def ReadKey(self):
        if self.system == "Windows":
            import msvcrt
            ch = msvcrt.getch()
            return ch.decode("utf-8")
        else:
            import termios, tty
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                print(ch)
            return ch
    
if __name__ == '__main__':
    scanner = Scanner()
    print("Enter Str:", end=' ')
    str = scanner.ReadLine()
    print("Enter Chr:", end=' ')
    chr = scanner.ReadKey()
    print("Typed Str", str)
    print("Typed Chr:", chr)
