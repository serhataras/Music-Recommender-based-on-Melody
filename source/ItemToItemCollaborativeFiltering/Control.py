"""
Controller


artistleri distancea göre sortla sonra crossValidate çağır tek tek onun distanceına göre de
"""
from LSH import LSH
import CrossValArtist

class Control:
    data_size = 1164
    lsh = LSH("Dataset/", data_size) ##burası

    lsh.preprocess()
    lsh.generate_hashtable()

    listofArtists = []


    predictions = []
    totalResults = []

    for i in range(3,4):#data_size):
        #print("id: " + str(lsh.id[i]) + "; metadata: " + str(lsh.meta[i]))
        listofArtists.append(str(lsh.meta[i]["artist"]).lower())
        #print("neighbours: ")
        #print(list(map(lambda x:(x[1], x[2]), lsh.query(lsh.data[i]))))
        artist = str(lsh.meta[i]).lower()
        for j in range(1,8):
            print(list(map(lambda x:(x[1], x[2]), lsh.query(lsh.data[i])))[j][0])
            print(list(map(lambda x:(x[1], x[2]), lsh.query(lsh.data[i])))[j][1])
            print(str(lsh.meta[int(list(map(lambda x:(x[1], x[2]), lsh.query(lsh.data[i])))[j][0])]["artist"]).lower())
            distance= list(map(lambda x:(x[1], x[2]), lsh.query(lsh.data[i])))[j][1]
            predictedArtist = str(lsh.meta[int(list(map(lambda x:(x[1], x[2]), lsh.query(lsh.data[i])))[j][0])]["artist"]).lower()
            totalResults.append(CrossValArtist.crossValidate(artist,distance,predictedArtist))
#eğer tahmin ettiği sanatçı kendisiyse aynıysa crossValidate yapma

    print("\n\n\n\n\n\n")
    print(totalResults)