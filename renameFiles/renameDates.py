import shutil, os, re
import pyinputplus as pyip

#create a regex that matchs files with american date format

dataPattern = re.compile(r"""^(.*?) #all text before de date
    ((0|1)?\d)-                      #one or two digits for the month
    ((0|1|2|3)?\d)-                      #one or two digits for the day
    ((19|20)\d\d)                    #four digits for the year
    (.*?)$                           #all text after the date
    """, re.VERBOSE)


#Loop over the files in the working directory
for amerFilename in os.listdir("C://Users//EdmarG//Documents//Python_Edy_programs//automate_online-materials"):
    mo = dataPattern.search(amerFilename)
    #skip file without date
    if mo == None:
        continue

    #get different part of the file

    beforePart = mo.group(1)
    #print("primeiro texto" + beforePart)
    monthPart  = mo.group(2)
    #print("mes = " + monthPart)
    dayPart    = mo.group(4)
    #print("dia" + dayPart)
    yearPart   = mo.group(6)
    #print("ano "+ yearPart)
    afterPart  = mo.group(8)
    #print("ultimo texto "+ afterPart)

    #print("deep understand")
    #print(mo.group(3))
    #print(mo.group(5))
    #print(mo.group(7))

    #form the European-style filename
    euroFilename = beforePart + dayPart +"-"+ monthPart+ "-"+yearPart+afterPart

    #get full absolute file path
    absWorkingDir = os.path.abspath("C://Users//EdmarG//Documents//Python_Edy_programs//automate_online-materials")
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    #rename the files
    print(amerFilename)

    #shutil.move(amerFilename, euroFilename)  #uncomment after testing
