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
        else:
            outMsg.errorMessage('tmp')
            exit(1)

    if len(sys.argv) > 4:
        validator= av.ArgVal(sys.argv)
        if validator.validArgs() == "error":
            outMsg.errorMessage("tmp") #EDITUJ OVE PORUKE
            exit(1)

        sorArg= validator.getSortedArgs()
        tFile= sorArg[0]
        tEn= sorArg[1]
        oFile= sorArg[2]
        oEn= sorArg[3]
        option= sorArg[4]
        optArg= sorArg[5]
        print(str(sorArg[0]))
        try:
            with open(tFile,'r') as targetFile:
                procesor= pf.PFhandle(targetFile,option,optArg)
                procesor.processFile(oFile,tEn,oEn)
        except IOError:
            print("IO?")
            outMsg.errorMessage('tmp')
            exit(1)

if __name__ == '__main__':
    Main()