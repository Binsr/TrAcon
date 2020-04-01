import codec
import convertor
import translator
import re


class PFhandle:

    def __init__(self,tFile,option,opArg):
        self.tFile= tFile
        self.option= option
        self.opArg= opArg
        self.oFile= None
        self.i = 0 #line counter

    def countLine(self):
        print("Line: " + str(self.i) + ' :processed')
        self.i += 1


    def processFile(self,outFile,en1= None,en2= None): #tEn oEn promeni kad stignes u ove nazive en1 en2
        self.oFile= open(outFile,'w')

        if self.option == '-c':
            self.convertFile(en1,en2)
        elif self.option == '-t':
            self.translateFile(en1,en2)
        else:
            print("ProcessFile Failed")
            exit(1)

    def convertFile(self,en1,en2):
            con= convertor.Convertor(self.opArg)
            coder= codec.Codec()
            for line in self.tFile:
                self.countLine()
                if re.search(r"^#.*", line) is not None:
                    self.oFile.write(line)  # Uklanja razmak izmedju 2 linije istog komentara
                    continue
                pos = re.search(r"[=]", line)
                if pos is not None:

                    befEqStr= line[0:pos.end()]
                    aftEqStr= line[pos.end():-1]
                    self.oFile.write(befEqStr)

                    decStri= coder.decodeString(aftEqStr,en1) # STRING -> DEKODIRANJE -> KONVERTOVANJE -> KODIRANJE -> ZAPIS

                    conStri= con.convLine(decStri, True)

                    codedStri= coder.codeString(conStri,en2)

                    self.oFile.write(codedStri)
                    self.oFile.write('\n')
                else:
                    decStri= coder.decodeString(line,en1) # PRETRVORI U JEDNU FUNKCIJU

                    conStri= con.convLine(decStri, False)

                    codedStri= coder.codeString(conStri,en2)

                    self.oFile.write(codedStri)
            self.oFile.close()

    def translateFile(self,tEn,oEn):


        tran = translator.Translator(self.opArg)
        coder = codec.Codec()
        property= ''
        forTrans= ''
        for line in self.tFile:
            self.countLine()
            if re.search(r"^#.*", line) is not None:
                self.oFile.write(line)  # Uklanja razmak izmedju 2 linije istog komentara
                continue
            pos = re.search(r"[=]", line)
            if pos is not None:
                befEqStr = line[0:pos.end()]
                aftEqStr = coder.elimBackslash(line[pos.end():-1]) #DO -1 zbog novih redova

                decodedStr= coder.decodeString(forTrans,tEn)

                translated= tran.translateString(decodedStr)

                codedStr= coder.codeTranslated(translated,oEn)

                self.oFile.write(property+" "+codedStr)
                self.oFile.write('\n\n')
                property= befEqStr
                forTrans= aftEqStr

            else:
                noSpaces= coder.eliminatewhitespaces(line)
                forTrans+= coder.elimBackslash(noSpaces)

        befEqStr = line[0:pos.end()]
        aftEqStr = coder.elimBackslash(line[pos.end():-1])  # DO -1 zbog novih redova

        decodedStr = coder.decodeString(forTrans, tEn)

        translated = tran.translateString(decodedStr) #OVO DUPLIRANJE ODSTRANITI FUNKCIJA MOZE BITI TRANSLATELINE()
        codedStr = coder.codeTranslated(translated,oEn)
        self.oFile.write(property+ " " +codedStr)




    def stringLoad(self):
        pass