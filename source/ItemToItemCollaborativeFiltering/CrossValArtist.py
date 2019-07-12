from urllib.request import  urlopen
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import math
import numpy as np
import urllib.parse
import os
import pickle

##LiNK oluşturma + distance

#def crossValArtist(artistCompare):
#artist = "daft+punk" #artistCompare

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")
option.add_argument("--start-maximized")
prefs = {"profile.default_content_setting_values.notifications" : 2}
option.add_experimental_option("prefs",prefs)
#driver = webdriver.Chrome(chrome_options=option)

driver = webdriver.Chrome("/home/ubuntu/.local/lib/python3.6/site-packages/chromedriver",chrome_options= option)


#l-27imperatrice.html
#kings+of+leon.html

#s0
#gnodMap


def extractCoordinates(element):
    styleText = element.get_attribute('style')
    styleText = styleText.split(";")
    styleTextX = "s"
    styleTextX = styleText[1]

    return (styleTextX[styleTextX.find("ft:") + 4 : styleTextX.find("px")], 
    styleText[2][styleText[2].find("op:") + 4: styleText[2].find("px")])




def outputSimilar(artist):
    try:
        driver.get('https://www.music-map.com/' + artist)
        time.sleep(7)

        musics = {}

        centerPlace = extractCoordinates(driver.find_element_by_xpath('//*[@id="s0"]'))
        musics[artist] = centerPlace
        coordList = [] 
        for i in range(1,49):
            a= driver.find_element_by_xpath('//*[@id="s' + str(i) +'\"]')
            coords = extractCoordinates(a)
            musics[str(a.text)] = (str(coords[0]), str(coords[1]))
            coordList.append([float(coords[0]), float(coords[1])])

        absoluteCenter = np.array([float(centerPlace[0]),float(centerPlace[1])])
        #print("ABSolute is", absoluteCenter)

        coordList = np.array(coordList)
        #coordList = np.array([coordList])
        ##print(coordList)
        dist = np.linalg.norm(coordList - absoluteCenter, ord=2, axis=1) # calculate Euclidean distance (2-norm of difference vectors)
        sorted_B = coordList[np.argsort(dist)]

        #print(np.argsort(dist))

        #print("\n\n\n\n\n")
        #print(str(sorted_B))
        #print('\n')
        #print(sorted_B[-1][1])

        musics = dict((v,k) for k,v in musics.items())

        result = []
        #print('\n\n\n\n')
        #print(musics)

        sorted_B = sorted_B.astype(str)

        #print("DİSTANCE İS: ", dist)
        #print("\n\n")

        for i in range(len(sorted_B)):
            #print(str(sorted_B[i][0]) , str(sorted_B[i][1]))
            #print(" 1st one is", str(sorted_B[i][0])[-2:])
            #print("second one is", str(sorted_B[i][1])[-2:])
            if  str(sorted_B[i][0])[-2:] == '.0':
                #print("before", str(sorted_B[i][0]))
                sorted_B[i][0] = str(sorted_B[i][0])[:-2]
                #print("now donw", str(sorted_B[i][0]))
            
            if str(sorted_B[i][0])[-1] == '.':
                #print(".")
                sorted_B[i][0] = str(sorted_B[i][0])[:-1]

            if  str(sorted_B[i][1])[-2:] == '.0':
                #print("before", str(sorted_B[i][1]))
                sorted_B[i][1] = str(sorted_B[i][1])[:-2]
                #print("now done", str(sorted_B[i][1]))

            if str(sorted_B[i][1])[-1] == '.':
                #print(".2")
                sorted_B[i][0] = str(sorted_B[i][1])[:-1]


            ##print("FOR i:", i)
            #print(str((str(sorted_B[i][0]),str(sorted_B[i][1]))))
            #print(str((musics[(str(sorted_B[i][0]),str(sorted_B[i][1]))], dist[i])))    
            result.append((musics[(str(sorted_B[i][0]),str(sorted_B[i][1]))], dist[i]))

        #print('\n\n\n\n')
        #driver.quit()
        return result
    except:
        return -1


def validate(inputArtist, predictedArtist):
    artists= outputSimilar(inputArtist)
    #print(artists)
    for i in range(len(artists)):
        if str(artists[i][0]).lower() == str(predictedArtist).lower():
            return (910.55862 - artists[i][1])/910.55862
    return -1


"""


#print("\n\n\n\n\n")


for i in range(0,49):
    #print(driver.find_element_by_xpath('//*[@id="s' + str(i) +'\"]').get_attribute('style'))
"""

def crossValidate(artist, artistDistance, predictedArtist):
    if predictedArtist == artist:
        return (str(artist), artistDistance, 1)
    pathName = "/home/ubuntu/WEBSCALE/DatasetCrossVal/" + str(artist).lower()+ ".obj"
    if os.path.exists(pathName):
        with open(pathName, "rb") as file:
            similar = pickle.load(file)
    else:
        return 0 #artist not found at music api thing

    for i in range(len(similar)):
        if str(similar[i][0]).lower() == str(predictedArtist).lower():
            resultSim = (910.55862 - similar[i][1])/910.55862
            return (str(artist), artistDistance, resultSim)
    return -1 #match doesnt hold


"""
print(similar)
print(similar[1][0])

print(outputSimilar("wiz khalifa"))

"""
#matchlenirse artist, Berat distance, (910.55862 - artists[i][1])/910.55862 