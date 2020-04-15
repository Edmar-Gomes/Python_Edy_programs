from time import sleep
while True:
    try:
        print ("polling.")
        #poll some resource
        sleep(1)
    except KeyboardInterrupt:
        break
        
