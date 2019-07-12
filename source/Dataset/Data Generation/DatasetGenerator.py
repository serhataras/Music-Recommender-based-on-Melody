from __future__ import print_function

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

# We'll need numpy for some mathematical operations
import numpy as np
# matplotlib for displaying the output
import matplotlib.pyplot as plt
import matplotlib.style as ms
ms.use('seaborn-muted')
#matplotlib inline
# and IPython.display for audio output
import IPython.display
# Librosa for audio
import librosa
# And the display module for visualization
import librosa.display
#pickle library to
import glob
import errno
import eyed3

import pickle
import time

def get_Metadata(path):
        try:
                audio = eyed3.load(path)
                #print (path)
                if hasattr(audio.tag, 'title'):
                        if hasattr(audio.tag, 'artist'):
                                if hasattr(audio.tag, 'genre'):
                                        if( (audio.tag.title!= None)):
                                                if(str(audio.tag.genre) != None):
                                                        if(audio.tag.artist != None):
                                                                #if(audio.tag.artist != None):
                                                                data = {"artist": audio.tag.artist,
                                                                        "album": audio.tag.album,
                                                                        "title": audio.tag.title,
                                                                        "genre":  str(audio.tag.genre),
                                                                        "release_date": str(audio.tag.best_release_date),
                                                                        "duration": str(audio.info.time_secs)
                                                                        }
                                                                return data
                                        else:
                                                print("Metadata is not compatible, skiping this song!")
                                                return None
                else:
                        print("Metadata is not compatible, skiping this song!")
                        return None
        except:
                pass

class DatasetGenerator:
        def __init__(self):
                self.data = None 
        def loadSong(self,path):
                y, sr = librosa.load(path)
                return y,sr
        def extract(self,song,song_id):
                songMeta = get_Metadata(song)
                try:    
                        if(songMeta):  
                                y, sr = librosa.load(song)
                                tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
                                chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
                                #rmse = librosa.feature.rmse(y=y)
                                #cent = librosa.feature.spectral_centroid(y=y, sr=sr)
                                #spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
                                #rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
                                #zcr = librosa.feature.zero_crossing_rate(y)
                                mfcc = librosa.feature.mfcc(y=y, sr=sr)
                                #y_harm = librosa.effects.harmonic(y)
                                #tuning = librosa.estimate_tuning(y=y_harm, sr=sr)
                                S = librosa.feature.melspectrogram(y, sr=sr, n_mels=40) 
                                # Convert to log scale (dB). We'll use the peak power (max) as reference.
                                log_S = librosa.power_to_db(S, ref=np.max)
                                #for coefficient in mfcc:
                                        #mfcc_features.append(np.mean(coefficient))
                                data = np.hstack((chroma_stft.mean(1), mfcc.mean(1), S.mean(1),log_S.mean(1)))
                                data = np.append(data,[tempo])
                                print(data.shape) 
                                file_Name = "/media/neo/My Passport/Dataset/"+str(song_id)+".data"
                                # open the file for writing
                                fileObject = open(file_Name,'wb')
                                pickle.dump(song_id,fileObject) 
                                pickle.dump(songMeta,fileObject)
                                pickle.dump(data,fileObject) 
                                fileObject.close()
                                return True
                        else:
                                return False
                except:
                        pass
        def get_data(self):
                return self.data

# main ()

#start = time.time()

path = './MusicData/*.mp3'
songs = glob.glob(path)
count = 0 
np.set_printoptions(threshold=np.inf)

dataset = DatasetGenerator()
for song in songs:
        print("Processing --["+str(count)+"]")
        if(dataset.extract(song,count)):    
                count += 1   
