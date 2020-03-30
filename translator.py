
#Samo prevodi string PR: ENG -> FR **NEMA VEZE SA ENKODIRANJEM

class Translator:

    def __init__(self,opArg):
        self.opArg= opArg

    def translateString(self,string):
        if self.opArg == 'eng-fran':
            return self.engFran(string)
        else:
            print("TranslateString Failed")
            exit(1)

    def engFran(self,string):
        outStr= string
        return outStr
