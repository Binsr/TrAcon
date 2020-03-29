import re

class Codec:
    def __init__(self):
        pass

    def isUnicode(self, chr):
        try:
            chr.encode().decode('unicode_escape')
        except:
            return False
        return True

    #DA HENDLUJE I NULL

    def decodeString(self,string,encoding=None):
        if encoding == 'no':
            return string
        if encoding is None: #Default UTF16
            decodedStr= ''
            i= 0
            while i < len(string):
                if string[i] == '\\' and i+6 < len(string):
                    if self.isUnicode(string[i:i+6]) and string[i] is not string[i+1]:
                        decodedStr+= string[i:i+6].encode().decode('unicode_escape')
                        i+= 6
                        continue

                decodedStr+= string[i]
                i+=1
            return decodedStr
        else:
            print("BAD ENCODING")
            exit(1) #SAMO ZA MENE TREBA IZBACITI INACE

    def codeString(self,string,encoding= None):#DA LI JE UTF16 ili unicode escape
        if encoding == 'no':
            return string
        if encoding == None: #default UTF16
            outStr= ''
            i= 0
            while i < len(string):
                chr= string[i]
                if chr is '\n' or chr is '\t' or chr is '\\':
                    outStr+= chr
                    i+=1
                    continue
                chr= str(chr.encode('unicode_escape'))
                bsPos= re.search(r"[\\]", chr)
                if bsPos is not None:
                    if chr[bsPos.end()+1] is not "\\":
                        outStr+= chr[bsPos.end():-1]
                    else:
                        outStr+= '\\'
                else:
                    aPos= re.search(r"[']",chr)
                    outStr+= chr[aPos.end():aPos.end()+1]
                i+=1
            return outStr
        else:
            print("LOS ENCODING") #ISTO ZA MENE SAMO
            exit(1)