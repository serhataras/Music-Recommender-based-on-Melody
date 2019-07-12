
The dataset is generated using eye3D and Librosa libraries.

All songs that are eligible to be analysed must have valid metadata information embedded to their ID3V keys. 



#files must opened with rb option, which tells it must read binary file                
#f = open('./data/1.obj', 'rb')
#       DO Not 
#       THE
#       ORDER

"""
song_id = pickle.load(f)#song_id
songMeta = pickle.load(f)#songMeta  
tempo = pickle.load(f)#tempo  
beats = pickle.load(f)#beats  
chroma_stft = pickle.load(f)#chroma_stft  
rmse = pickle.load(f)#rmse  
cent = pickle.load(f)#cent  
spec_bw = pickle.load(f)#spec_bw  
rolloff= pickle.load(f)#rolloff  
zcr = pickle.load(f)#zcr  
mfcc = pickle.load(f)#mfcc  
y_harm = pickle.load(f)#y_harm  
tuning = pickle.load(f)#tuning  
mel = pickle.load(f)#S mel  
log_S = pickle.load(f)#log_S  

f.close()



"""
# The hierarcy of the meta data dictionary
#   data = {"artist":.. "album":... "title": ... "genre":... "release_date": ... "time":...}


# All possible specturums from mfcc 
# 'mfcc1', 'mfcc2',
# 'mfcc3', 'mfcc4', 'mfcc5', 'mfcc6', 'mfcc7', 'mfcc8', 'mfcc9', 
# 'mfcc10', 'mfcc11', 'mfcc12', 'mfcc13', 'mfcc14', 'mfcc15',,
# 'mfcc16', 'mfcc17', 'mfcc18', 'mfcc19', 'mfcc20'

#To read the cooeficiets, use the following code snippet
# for coefficient in mfcc:
#               features.append(np.mean(coefficient))



"""
print(song_id)
print(songMeta['artist'])
print(songMeta['album'])
print(songMeta['title'])
print(songMeta['genre'])
print(songMeta['release_date'])
print(songMeta['duration'])
print(tempo)
print(len(log_S))
"""
