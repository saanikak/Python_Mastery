#writing main method in python
import calendar as cal

def printcalendar():
    c = cal.month(2021, 1)
    print(__name__)
    return (c)

if __name__ == '__main__':
    print(printcalendar())