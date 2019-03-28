# Music Genre Classifier

## Downloading the dataset

The GTZAN dataset(used in the well known paper in genre classification " Musical genre classification of audio signals " by G. Tzanetakis and P. Cook in IEEE Transactions on Audio and Speech Processing 2002) consists of 1000 audio tracks each 30 seconds long. It contains 10 genres, each represented by 100 tracks in .au format can be downloaded from http://marsyas.info/downloads/datasets.html .

## Preprocessing

All the audio files originally in .au format is converted to .wav format using pydub to make it compatiable to python's wave module for reading audio files.

## Feature extraction

To classify our audio clips we extract 8 features namely chroma frequency, spectral centroid, spectral bandwidth, spectral roll off, zero crossing rate,beats per minute, rms value and Mel-Frequency Cepstral Coefficients using python's librosa module. These 8 features are appended to give a 57 length feature vector which is extracted in a csv file.

## Classification

Once the feature vector was obtained, different classifiers were trained on the training set of feature vectors. The parameters used for different classifiers were obtained by manual tuning.

## Results

The top performing classifiers on the dataset were observed to be SVM with rbf kernel and a neural network based classifier performing with an accuracy of 85% and 83% on test set respectively.

![neural network based classifier](https://github.com/ezio69/Music-Genre-Classifier/blob/master/neural_network_cm.png)       ![SVM](https://github.com/ezio69/Music-Genre-Classifier/blob/master/svm_cm.png)
