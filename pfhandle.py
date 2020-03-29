import codec
import convertor
import re

class PFhandle:

    def __init__(self,tFile,option,opArg):
        self.tFile= tFile
        self.option= option
        self.opArg= opArg
        self.oFile= None


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
            i = 0
            for line in self.tFile:
                print("Line: " + str(i) + ' :processed')
                i+=1
                if re.search(r"^#.*", line) is not None:
                    self.oFile.write(line)  # Uklanja razmak izmedju 2 linije istog komentara
                    continue
                pos = re.search(r"[=]", line)
                if pos is not None:

                    befEqStr= line[0:pos.end()]

                    self.oFile.write(befEqStr)

                    decStri= coder.decodeString(line[pos.end():-1],en1) # STRING -> DEKODIRANJE -> KONVERTOVANJE -> KODIRANJE -> ZAPIS

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

    def translateFile(self):
        pass


    def stringLoad(self):
        pass