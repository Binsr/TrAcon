import re

class Codec:
    def __init__(self):
        pass

    def isUTFhex(self, chr):
        try:
            chr.encode().decode('unicode_escape')
        except:
            return False
        return True


    #DA HENDLUJE I NULL

    def decodeString(self,string,encoding=None):
        if encoding is'no':
            return string
        elif encoding is None: #Default UTF16
            return self.decodeUTFhex(string)
        if encoding is 'utf8':
            return self.decodeUTFeight(string)

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

    def decodeUTFhex(self,string):
            decodedStr= ''
            i= 0
            while i < len(string):
                if string[i] == '\\' and i+6 < len(string):
                    if self.isUTFhex(string[i:i+6]) and string[i] is not string[i+1]:
                        decodedStr+= string[i:i+6].encode().decode('unicode_escape')
                        i+= 6
                        continue

                decodedStr+= string[i]
                i+=1
            return decodedStr

    def codeTranslated(self,string,oEn):
        if oEn == None:
            return self.codeHexTran(string)
        if oEn == 'no':
            return string

    def codeHexTran(self,string):

        i = 0
        outStr= ''
        while i < len(string):
            chr= str(string[i].encode('utf-8'))
            if len(chr) == 4:
                outStr+= chr[2]
            else:
                x= "".join(["\\u%s" % hex(ord(l))[2:].zfill(4) for l in string[i]])
                outStr+= x
            i+=1

        return outStr




    def eliminatewhitespaces(self,string):
        #eliminisi ih
        whitespce= re.search(r"^\s*",string)
        i=-1
        if string[-1] == '\\':
            i= -2
        return string[whitespce.end():i]

    def elimBackslash(self,string):
        if len(string) < 2:
            return string

        if string[-1] is '\\':
            return string[:-1]
        else:
            return string