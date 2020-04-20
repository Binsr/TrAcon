
class Messages:

    def __init__(self):
        pass

    def helpMessage(self):

        print("Help command: |-h|\n\n"
              "                        ~ This is TrAcon help menu ~\n\n"
              ""
              "Use(1) for con/tran TARGET_FILE -> OUTPUT_FILE: \n\n"
              "TARGET_FILE AND OUTPUT_FILE can be paths (./pat/TARGET_FILE)\n\n"
              "-----------------------------------------------------------------------------"
              "\nTo run with C type: "
              " ./tracon TARGET_FILE {1} OUTPUT_FILE {2} [Option] [Option-Argument]  \n"
              "-----------------------------------------------------------------------------\n"
              "To run with Python type: "
              " python3 tracon.py TARGET_FILE {1} OUTPUT_FILE {2} [Option] [Option-Argument]  "
              "\n-----------------------------------------------------------------------------\n"
              "\n {} Represents optional arguments: (To get clear picture of example use ./tracon -e)\n"
              "\n"
              "\n          {1} Is encoding of TARGET_FILE \n"
              "\n          {2} is encoding of OUTPUT_FILE"
              "\n-----------------------------------------------------------------------------")

        # Options
        print("\nOptions: \n"
              "         -----------------------------------------------------------------------------\n"
              "          [-c] -- Convert-option used for converting between different writings\n\n"
              "          convert [option-argument]:\n\n"
              "             [latin-to-cir] -- use this argument to get converted file as outfile from Latin to Cirilic "
              "\n                              (example: ~$ ./tracon file1 file2 -c latin-to-cir )\n"
              "         -----------------------------------------------------------------------------")
        print("          [-t] -- Translate-option used for translating target file to chosen language\n"
              "\n          translate [option-argument]: \n"
              "\n             [fren] -- use this argument to get translated file as output file on French\n"
              "\n             [ital] -- use this argument to get translated file as output file on Italian\n"
              "\n             [srbL] -- use this argument to get translated file as output file on Serbian in latin\n"
              "\n             [srbC] -- use this argument to get translated file as output file on Serbian in Cirilic\n"
              "\n             [germ] -- use this argument to get translated file as output file on German\n"
              "\n             [span] -- use this argument to get translated file as output file on Spanish\n"
              "\n             [rus] -- use this argument to get translated file as output file on Russian\n")
        print("Encodings: \n"
              "          ------------------------------------------------------------------------------\n\n"
              "             {no} -- use if you dont want outfile encoded or if your imput file is not encoded\n\n"
              "             {utf8} -- use if you want output file in UTF-8 encoding or your input file is UTF-8 encoded\n\n"
              "                        ***DEFAULT ENCODING FOR BOUTH TARGET AND OUT FILE IS from UTF-16 to UTF-16***\n")

        print('\nUse(2) Updating all files in DIRECTORY for the TARGET_FILE changes:\n\n'
              '-----------------------------------------------------------------------------'
              '\nTo run with C type: ./tracon DIRECTORY_PATH TARGET_FILE -u\n'
              '-----------------------------------------------------------------------------'
              '\nTo run with Python type: python3 tracon.py DIRECTORY_PATH TARGET_FILE -u\n'
              '-----------------------------------------------------------------------------\n'
              '\nThis option only updates marked files in same directory.\n\n'
              'Marked files are the files that are product of translating file with tracon.\n\n'
              'The mark contains information about the parent of marked file\n\n')

        print("^ To get example use [-e] ^\n")

    def versionMessage(self):
        print("\n    ~ ~ ~ TrAcon version: 1.2.0 ~ ~ ~\n")

    def errorMessage(self):
        print("\n\nError: \n"
              "          Something went wrong :/\n\n")
    def examlpeMessage(self):
        print("\nHere is your example:  \n"
              " \n ./tracon TARFILE OUTFILE -t fren \n"
              "\n ./tracon TARFILE utf8 OUTFILE utf16 -t fren\n"
              "                                                          "
              "\n\n")
    def success(self):
        print("\n ~ ~ ~ Successfully completed ~ ~ ~\n")


