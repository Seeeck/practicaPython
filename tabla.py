import sys


if (float(sys.argv[1]) >= 1 and float(sys.argv[2]) <= 9) and (float(sys.argv[2]) >= 1 and float(sys.argv[1]) <= 9):
    if '.' not in str(sys.argv[1]) and '.' not in str(sys.argv[2]):
        for i in range( int(sys.argv[1])):
            for n in range(1, int(sys.argv[2])):
                print(" * ", end='')
            print(" * ")
    else:
        print("Error")
else:
    print("Error")
