import re
import transliterate as tr

class Convertor:

    def __init__(self,optionArgument):
        self.opArg= optionArgument

    def convLine(self,line,isFirst):
        if self.opArg == "latin-to-cir":
            return self.tagSafeConLatCir(line, isFirst)
        else:
            print("CONVERTOR FAILED")
            exit(1)

    # TREBA ODSTRANITI TAKO DA RADI FUNKCIJA I ZA OBICNE FAJLOVE
    def tagSafeConLatCir(self, line, isFirstLine):  # 3- argument odstraniti u nekom trenutku(resava gubljenje \ na kraju reda koji sadrzo = i tag)
        pattern = re.compile(r"<.+?>")
        tagReg = pattern.finditer(line)
        add = ''
        if line[len(line) - 1] is '\n':  # Trebalo bi prepraviti u nekom trenutku
            add = '\n'
        outStr = ''
        iter = 0
        tag = None
        for tag in tagReg:
            outStr += tr.translit(line[iter:tag.start()],'sr')
            outStr += line[tag.start():tag.end()]
            iter = tag.end()
        if tag is None:
            return tr.translit(line,'sr')
        outStr += tr.translit(line[iter:-1],'sr')
        if isFirstLine:
            outStr += '\\'
        outStr += add
        return outStr
