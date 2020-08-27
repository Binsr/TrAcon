# TrAcon
File translator and convertor

This is a tool used to translate files using Google translate API.
At this stage it works with Java poperty files formated in Jaspersoft.

Example:
 javaFile.properties:
  someKey= "Ovo je test string"
  
 tracon -t javaFile.properties javaFileEng.properties -eng
 Result:
  javaFileEng.properties:
    someKey= "This is test string"

There is also update command that find new messages added in parent file and update all child files.
