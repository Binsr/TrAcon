import sys
import messages as m
import pfhandle as pf
import updateHandle
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
            outMsg.errorMessage()
            exit(1)

    if len(sys.argv) == 4:
        if sys.argv[3] == '-u':
            update= updateHandle.UpdateHandle()

            path= sys.argv[1]

            targetFile= sys.argv[2]
            # print("\n Do you wanna safe updating? (y/n)\n")
            # string = str(input())
            # safe= False
            # if string[0] == 'y':
            #     safe= True
            safe= False
            update.updateDir(path,targetFile,safe)

            exit(0)
        else:
            outMsg.errorMessage()
            exit(1)

    if len(sys.argv) > 4:
        validator= av.ArgVal(sys.argv)
        if validator.validArgs() == "error":
            outMsg.errorMessage() #EDITUJ OVE PORUKE
            exit(1)

        sorArg= validator.getSortedArgs()

        targetFile= sorArg[0]

        targetEncoding= sorArg[1]

        outFile= sorArg[2]

        outEncoding= sorArg[3]

        option= sorArg[4]

        optionArg= sorArg[5]

        if validator.getFileType() is 'property':
                procesor= pf.PFhandle(targetFile,option,optionArg)
                procesor.processFile(outFile,targetEncoding,outEncoding)
        else:
            print("Reg file funcionality coming soon")
            exit(0)
        outMsg.success()

if __name__ == '__main__':
    Main()