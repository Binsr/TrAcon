import sys
import messages as m
import pfhandle as pf
import argsValidation as av

def Main():

    outMsg= m.Messages()
    if len(sys.argv) == 2:
        if sys.argv[1] == '-h':
            outMsg.helpMessage()
            sys.exit(0)
        if sys.argv[1] == '-v':
            outMsg.versionMessage()
            sys.exit(0)
        if sys.argv[1] == '-e':
            outMsg.examlpeMessage()
            sys.exit(0)
    if len(sys.argv) == 5:
        option= sys.argv[3]
        optArg= sys.argv[4]
        try:
            with open(sys.argv[1], 'r') as targetFile:
                outFile= sys.argv[2]
                procesor= pf.PFhandle(targetFile,option,optArg)
                procesor.processFile(outFile)
        except IOError:
            print("There is no file: " + sys.argv[1])
            exit(1)
    if len(sys.argv) == 6:
        option= sys.argv[4]
        optArg= sys.argv[5]
        if sys.argv[3] == 'no':
            try:
                with open(sys.argv[1], 'r') as targetFile:
                    outFile= sys.argv[2]
                    procesor= pf.PFhandle(targetFile,option,optArg)
                    procesor.processFile(outFile,None,'no')
            except IOError:
                print("There is no file: " + sys.argv[1])
                exit(1)



if __name__ == '__main__':
    Main()