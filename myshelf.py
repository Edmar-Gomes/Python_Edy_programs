import shelve

shelfFile = shelve.open("mydata")
cats = ["Zophie","Pooka","Simon"]
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open("mydata")
type(shelfFile)
shelfFile["cats"]
shelfFile.close() 
