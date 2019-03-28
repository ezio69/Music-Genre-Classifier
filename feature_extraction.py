import os
import csv
import librosa
import numpy as np

# creating a function to calculate features

def calculate_features(path):
    # loading the audio file
    x , sr = librosa.load(path)

    # creating empty lists to store the features
    mfcc_list = []
    final_list = []
    
    # calculating features
    chroma_stft = librosa.feature.chroma_stft(x, sr)
    spec_cent = librosa.feature.spectral_centroid(x, sr)
    spec_bw = librosa.feature.spectral_bandwidth(x, sr)
    rolloff = librosa.feature.spectral_rolloff(x, sr)
    zcr = librosa.feature.zero_crossing_rate(x)
    bpm = librosa.beat.tempo(x, sr)
    rms = librosa.feature.rms(x)
    mfcc = librosa.feature.mfcc(x, sr, n_mfcc=50)

    # taking the mean of every mfccs
    for i in mfcc :
        mfcc_list += [np.mean(i)]

    # final feature set of the audio sample
    
    final_list = [np.mean(chroma_stft), np.mean(spec_cent), np.mean(spec_bw), np.mean(rolloff), np.mean(zcr), np.median(bpm), np.mean(rms)] + mfcc_list
    return final_list
    
    
audio_path = '/home/surya/Desktop/Music Genre Classifier/wav files' # path of audio files

# creating a list to store feature set of all samples
list = [['filename','genre','chroma_stft','spec_cent','spec_bw','rolloff','zcr', 'bpm', 'rms'] + ['mfcc' + str(i) for i in range(1,51)]]

print('Creating CSV.......')

# looping through each file in audio_path
for wav_file in os.listdir(audio_path):
    file_path = '/home/surya/Desktop/Music Genre Classifier/wav files' + '/' + wav_file

    if wav_file[:5] == "blues" :
        list += [[wav_file, 'blues']+ calculate_features(file_path)]
    if wav_file[:9] == "classical" :
        list += [[wav_file, 'classical']+ calculate_features(file_path)]
    if wav_file[:7] == "country" :
        list += [[wav_file, 'country']+ calculate_features(file_path)]
    if wav_file[:5] == "disco" :
        list += [[wav_file, 'disco']+ calculate_features(file_path)]
    if wav_file[:6] == "hiphop" :
        list += [[wav_file, 'hiphop']+ calculate_features(file_path)] 
    if wav_file[:4] == "jazz" :
        list += [[wav_file, 'jazz']+ calculate_features(file_path)]
    if wav_file[:5] == "metal" :
        list += [[wav_file, 'metal']+ calculate_features(file_path)]
    if wav_file[:3] == "pop" :
        list += [[wav_file, 'pop']+ calculate_features(file_path)]
    if wav_file[:6] == "reggae" :
        list += [[wav_file, 'reggae']+ calculate_features(file_path)]
    if wav_file[:4] == "rock" :
        list += [[wav_file, 'rock']+ calculate_features(file_path)]
    

csv_data = list

# writing data in a csv file
with open('dataset_final5.csv','w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(csv_data)

csv_file.close()
print("CSV creation completed")

