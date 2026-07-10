import sys

def argv():
    try :
        print("hello, my name is",sys.argv[1])#store what we give into terminal running this program
                                            # python ram.py [anything],, it'll store that 
        '''it is using[1] for first index instead of[0] because [0] is the name of the program'''
    except IndexError:
        print("Too few arguments!!!")


def exit():
    if len(sys.argv) < 2 :
        sys.exit("Too few arguments")# terminate the program with message in perenthessis
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")
    else:
        print("hello,",sys.argv[1])

def slices():
    for arg in sys.argv[1:]:# give list from [a:b] a to b if nothing written in place of b it give all the values
        print(arg)

slices()
    

