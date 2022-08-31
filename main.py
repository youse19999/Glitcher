import os
import random
path = "Kurashi.mp4"
mp4 = open('Kurashi.mp4','rb')
mp4s = open('Kurashi.mp4','rb')
mp4write = open('Kurashi.mp4','rb+')
get = 0
getchr = ""
mdatpos = 0
nowpos = 0
writepos = 0
r = 0
def getSize(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size
for x in range(getSize(mp4)):
    try:
        mp4.seek(x)
        #print(mp4.read(4))
        #print(mp4.read(4).decode('utf-8'))
        if "mdat" == mp4.read(4).decode('utf-8'):
            print("mdat")
            mdatpos = x
            break
    except:
        pass
print("mdat is " + str(mdatpos))
print("writing...")

print("write done")
writepos = mdatpos
writepos += 14
for x in range(300000):
    r = random.randint(24000, 28000)
    rr = random.randint(0, 4)
    writepos = writepos + r
    mp4write.seek(writepos)
    mp4write.write(b'fu')
    #mp4write.write(rr.to_bytes(1, 'little'))
    #print(rr.to_bytes(1, 'little'))
