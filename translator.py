import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/binsr/PycharmProjects/GoogleCloudKey_myServiceAccount.json"
from google.cloud import translate_v2 as translate
import transliterate as tr

class Translator:

    def __init__(self,opArg):
        self.opArg= opArg
        self.translate_client = translate.Client()

    def translateString(self,string): #OVO MOZE DA SE NAPRAVI DA BUDE LEPSE TIPA {fren:fr,germ:'de'}
        if self.opArg == 'fren':
            return self.fren(string)
        elif self.opArg == 'ital':
            return self.ital(string)
        elif self.opArg == 'srbL':
            return self.srbL(string)
        elif self.opArg == 'srbC':
            return self.srbC(string)
        elif self.opArg == 'germ':
            return self.german(string)
        elif self.opArg == 'span':
            return self.spanish(string)
        elif self.opArg == 'rus':
            return self.russian(string)
        else:
            print("TranslateString Failed")
            exit(1)

    def fren(self,string):
        outStr= self.translate_client.translate(string,target_language='fr') #Google API vraca utf8 pa moramo da dekodiramo
        outStr= outStr['translatedText']
        return outStr

    def ital(self, string):
        outStr = self.translate_client.translate(string, target_language='it')  # Google API vraca utf8 pa moramo da dekodiramo
        outStr = outStr['translatedText']
        return outStr

    def srbC(self, string):
        outStr = self.translate_client.translate(string, target_language='sr')  # Google API vraca utf8 pa moramo da dekodiramo
        outStr = outStr['translatedText']
        return outStr

    def srbL(self,string):
        outStr = self.translate_client.translate(string, target_language='sr')  # Google API vraca utf8 pa moramo da dekodiramo
        outStr = outStr['translatedText']
        lat = tr.translit(outStr,'sr',reversed=True)
        return lat

    def german(self, string):
        outStr = self.translate_client.translate(string, target_language='de')  # Google API vraca utf8 pa moramo da dekodiramo
        outStr = outStr['translatedText']
        return outStr

    def spanish(self,string):
        outStr = self.translate_client.translate(string, target_language='es')  # Google API vraca utf8 pa moramo da dekodiramo
        outStr = outStr['translatedText']
        return outStr
    def russian(self,string):
        outStr = self.translate_client.translate(string, target_language='ru')  # Google API vraca utf8 pa moramo da dekodiramo
        outStr = outStr['translatedText']
        return outStr