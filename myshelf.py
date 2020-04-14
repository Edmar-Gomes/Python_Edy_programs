import shelve

shelfFile = shelve.open("c://users/edmarg//documents//Python_Edy_programs//mydata.txt")
cats = ["Zophie","Pooka","Simon"]
shelfFile['cats'] = cats
shelfFile.close()
