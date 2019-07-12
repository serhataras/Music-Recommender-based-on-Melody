import acoustid, chromaprint, sys, difflib

for k in range(1,10):
    for j in range(k,10):
        id1 = str(k)
        id2 = str(j)
        (duration, bytestring) = acoustid.fingerprint_file("mp3/" + id1 + ".mp3")
        (duration2, bytestring2) = acoustid.fingerprint_file("mp3/" + id2 + ".mp3")
        fingerprint = chromaprint.decode_fingerprint(bytestring)[0]
        fingerprint2 = chromaprint.decode_fingerprint(bytestring2)[0]

        diff = 0
        lenght = len(min(fingerprint, fingerprint2))
        for i in range(lenght):
            #print('{0:b}'.format(fingerprint[i] ^ fingerprint2[i]))
            diff += ('{0:b}'.format(fingerprint[i] ^ fingerprint2[i])).count("1")
        str_prnt = id1 + " vs " + id2 +" diff " + str(diff)
        print(str_prnt)

        if fingerprint[0] == fingerprint2[0]: 
            print("Equal")
        else:
            print("Not")