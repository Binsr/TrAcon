# TrAcon
File translator and convertor
This is a tool used to translate Java property file formated in Jaspersoft and generate new file with translated properties.
Example:
 javaFile.properties:
  someKey= "Ovo je test string"
  
 tracon -t javaFile.properties javaFileEng.properties -eng
 Result:
  javaFileEng.properties:
    someKey= "This is test string"

