# There are 3 cases that we need to check
# f1 |encoding f2|
# f1 |f2 encoding|
# f1 |f2 option|

# > 5

#Options: -c -t
#en: utf8 no

#Needs to return List of Args

#Za sad propFile regularFile
import re

#Ako budes zeleo da poboljsas program dodaj mu da stavi fleg na pogresan argument

class ArgVal:

    def __init__(self,args):
        self.args= args
        self.fileType= None
        self.sortedArgs= []


    def validArgs(self): #Radi 2 stvari moze da se rastavi na 2 f-je
        i=0

        if self.isFile(self.args[1]):
            self.sortedArgs.append(self.args[1])
        else:
            return 'error'

        if self.isEncodeArg(self.args[2]):
            self.sortedArgs.append(self.args[2])
            if self.isFile(self.args[3]):
                self.sortedArgs.append(self.args[3])
                i=4
            else:
                return 'error'
        else:
            self.sortedArgs.append(None)
            if self.isFile(self.args[2]):
                self.sortedArgs.append(self.args[2])
                i=3
            else:
                return 'error'
        x=i

        while x < len(self.args):
            if self.isEncodeArg(self.args[x]):
                self.sortedArgs.append(self.args[x])
                break
            x+=1
        if x == len(self.args):
            self.sortedArgs.append(None)

        x=i

        while x < len(self.args):
            if self.isOption(self.args[x]):
                self.sortedArgs.append(self.args[x])
                break
            x+=1
        if x == len(self.args):
            return 'error'

        x=i

        while x < len(self.args):
            if self.isOpArg(self.args[x]):
                self.sortedArgs.append(self.args[x])
                x=0
                break
            x+=1
        if x == len(self.args):
            return 'error'

    def getFileType(self):
        return self.fileType

    def getSortedArgs(self):
        return self.sortedArgs

    def isOpArg(self,arg):
        if self.sortedArgs[-1] == '-c':
            if arg == 'latin-to-cir':
                return True
            else:
                return False
        elif self.sortedArgs[-1] == '-t':
            if arg == 'fren':
                return True
            elif arg == 'ital':
                return True
            elif arg == 'srb':
                return True
            elif arg == 'germ':
                return True
            elif arg == 'span':
                return True
            else:
                return False
        else:
            return False

    def isFile(self,file):
        if file.rfind('.') == '-1':
            return False
        posofDot= file.rfind('.')
        if file[posofDot+1:] == "properties":
            self.fileType= 'property'
            return True
        elif file[posofDot+1:-1] == "txt":
            self.fileType= 'regular'
            return True
        else:
            print("ISFILE")
            return False

    def isEncodeArg(self,arg):
        if arg == 'no':
            return True
        elif arg == 'utf8':
            return True
        else:
            return False

    def isOption(self,arg):
        if arg == '-c':
            return True
        elif arg == '-t':
            return True
        else:
            return False

