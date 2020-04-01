import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/binsr/PycharmProjects/GoogleCloudKey_myServiceAccount.json"
from google.cloud import translate_v2 as translate


class Translator:

    def __init__(self,opArg):
        self.opArg= opArg
        self.translate_client = translate.Client()

    def translateString(self,string):
        if self.opArg == 'eng-fran':
            return self.engFran(string)
        else:
            print("TranslateString Failed")
            exit(1)

    def engFran(self,string):
        outStr= self.translate_client.translate(string,target_language='fr') #Google API vraca utf8 pa moramo da dekodiramo
        outStr= outStr['translatedText']
        return outStr
        # return outStr.encode().decode('utf-8')
