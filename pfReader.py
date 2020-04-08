import re
import codec

class pfReder:

    def __init__(self,file):
        self.file= file

    def readNext(self):

        coder= codec.Codec()
        output= {'type':None,'value':None}

        forTrans= ' '

        line= self.file.readline()
        if line.isspace():
            return {'type':'empty'}

        if len(line) == 0:
            return False

        if re.search(r"^#.*", line) is not None:
            output['type']= 'comment'
            output['value']= line
            return output

        pos = re.search(r"[=]", line)
        if pos is not None:
            befEqStr = line[0:pos.end()]
            aftEqStr = coder.elimBackslash(line[pos.end():-1])  # DO -1 zbog novih redova

            output['type']= 'property'
            output['value']= {'property':befEqStr,'string': ' '}
            forTrans = ''
            forTrans+= aftEqStr

        while True:
            line= self.file.readline()
            if len(line) == 0:
                output['value']['string'] = forTrans
                return output

            if line.isspace():
                output['value']['string'] = forTrans
                return output
            noSpaces = coder.eliminatewhitespaces(line)
            forTrans += coder.elimBackslash(noSpaces)

