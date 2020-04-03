import codec
import convertor
import translator
import re
import pfReader

class PFhandle:

    def __init__(self,tFile,option,opArg):
        self.targFile= tFile
        self.tFile= open(tFile,'r')
        self.option= option
        self.opArg= opArg
        self.oFile= None
        self.i = 0 #line counter

    def markFile(self,oFile):
        oFile.write("#Translated from: " + self.targFile + " from: " + self.opArg)
        oFile.write("\n\n")

    def countTranslated(self):
        print("Property: " + str(self.i) + ' :processed')
        self.i += 1

    def processFile(self,outFile,en1= None,en2= None): #tEn oEn promeni kad stignes u ove nazive en1 en2
        self.oFile= open(outFile,'w')

        self.markFile(self.oFile)

        if self.option == '-c':
            self.convertFile(en1,en2)
        elif self.option == '-t':
            self.translateFile(en1,en2)
        else:
            print("ProcessFile Failed")
            exit(1)

    def convertFile(self,en1,en2): #Napravi da bude modularno kao i translate
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

    def translateLine(self,forTrans,tEn,oEn):

        coder = codec.Codec()
        tran = translator.Translator(self.opArg)

        decodedStr = coder.decodeString(forTrans, tEn)
        translated = tran.translateString(decodedStr)
        codedStr = coder.codeTranslated(translated, oEn)
        return codedStr

    def translateFile(self,tEn,oEn):

        reader= pfReader.pfReder(self.tFile)
        res= reader.readNext()
        while res:
            if res['type'] == 'empty':
                self.oFile.write('\n')

            if res['type'] == 'comment':
                self.oFile.write(res['value'])


            if res['type'] == 'property':
                property= res['value']['property']
                forTrans= res['value']['string']

                codedStr= self.translateLine(forTrans,tEn,oEn)
                self.oFile.write(property+" "+codedStr)
                self.oFile.write('\n\n')
                self.countTranslated()

            res= reader.readNext()
