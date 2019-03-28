import os
import glob
from pydub import AudioSegment

audio_dir = '/home/surya/Desktop/Music Genre Classifier/data/genres/'  # Path of audio files
genres = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
extension_list = ('*.au')

print("Converting files to wav.......")

for genre in genres:
    os.chdir(audio_dir + genre)
    for extension in extension_list:
        for audio in glob.glob(extension):
            wav_filename = os.path.splitext(os.path.basename(audio))[0] + '.wav'
            AudioSegment.from_file(audio).export(wav_filename, format='wav')

print("Completed succesfully")
