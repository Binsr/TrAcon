
class Messages:

    def __init__(self):
        pass

    def helpMessage(self):

        print("Help command: |-h|\n\n                        ~ This is TrAcon help menu ~\n\n"
              "Use: \n\n"
              "-----------------------------------------------------------------------------"
              "\nTo run with C type: "
              " ./tracon TARGET_FILE {1} OUTPUT_FILE {2} [Option] [Option-Argument]  \n"
              "-----------------------------------------------------------------------------\n"
              "To run with Python type: "
              " python3 tracon.py TARGET_FILE {} OUTPUT_FILE {} [Option] [Option-Argument]  "
              "\n-----------------------------------------------------------------------------\n"
              "\n {} Represents optional arguments: (To get clear picture of example use ./tracon -e)\n"
              "   \n"
              "\n {1} Is encoding of TARGET_FILE \n\n {2} is encoding of OUTPUT_FILE"
              "\n-----------------------------------------------------------------------------")

        # Options
        print("\nOptions: \n"
              "         -----------------------------------------------------------------------------\n"
              "          [-c] -- Convert-option used for converting between different writings\n\n"
              "          convert [option-argument]:\n\n"
              "             [latin-to-cir] -- use this argument to get converted file as outfile from Latin to Cirilic "
              "\n                              (example: ~$ ./tracon file1 file2 -c latin-to-cir )\n"
              "         -----------------------------------------------------------------------------")
        print("          [-t] -- Translate-option used for translating from Lang1 to lang2\n"
              "\n          translate [option-argument]: "
              "\n\n             [eng-fran] -- use this argument to get translated file as output file from English to Franch\n"
              "\n             [eng-ital] -- use this argument to get translated file as output file from English to Italian\n")
        print("Encodings: \n"
              "           ------------------------------------------------------------------------------\n\n"
              "          {no} -- use if you dont want outfile encoded or if your imput file is not encoded\n\n"
              "          {utf8} -- use if you want output file in UTF-8 encoding or your inptput file is UTF-8 encoded\n\n"
              "                        ***DEFAULT ENCODING FOR BOUTH TARGET AND OUT FILE IS from UTF-16 to UTF-16***\n")
        print("^ To get example use [-e] ^\n")

    def versionMessage(self):
        print("\n    ~ ~ ~ TrAcon version: 1.2.0 ~ ~ ~\n")

    def errorMessage(self,givenArg): #Za popravku
        print("\ntranslator: \n\n " + givenArg + " is not TrAcon command. See help menu by using commands: \n\n"
                                                     "  [-hc] for running with ./ "
                                                     "\n  [-hp] for runnig with python\n\n")

    def examlpeMessage(self):

        print("\nHere is your example:  \n"
              " \n ./tracon TARFILE OUTFILE -t eng-fran \n"
              "\n ./tracon TARFILE utf8 OUTFILE utf16 -t eng-fran\n"
              "                                                          "
              "           you lazy AF today  ;) \n\n")




