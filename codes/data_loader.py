# coding: utf-8
import os
import random
import numpy as np
import soundfile as sf
from torch.utils import data

class GTZANLoader(data.Dataset):
    def __init__(self, data_path, split, num_chunks=8, input_length=None):
        self.data_path = data_path
        self.split = split
        self.num_chunks = num_chunks
        self.input_length = input_length
        self.get_songlist()
        self.genres = [
                       'blues', 
                       'classical',
                       'country',
                       'disco',
                       'hiphop',
                       'jazz',
                       'metal',
                       'pop',
                       'reggae',
                       'rock'
                       ]
        assert split in ['TRAIN', 'VALID', 'TEST']

    def __getitem__(self, index):
        wav, genre_ix = self.get_item(index)
        return wav.astype('float32'), genre_ix

    def get_songlist(self):
        split_fn = os.path.join('./split/%s_filtered.txt' % self.split.lower())
        with open(split_fn) as f:
            x = f.readlines()
        self.filelist = [line.strip() for line in x]

    def get_item(self, index):
        genre, fn = self.filelist[index].split('/')
        audio_fn = os.path.join(self.data_path, genre, fn)
        wav, fs = sf.read(audio_fn)
        wav = self.adjust_length(wav)
        return wav, self.genres.index(genre)

    def adjust_length(self, wav):
        if self.split == 'TRAIN':
            random_idx = random.randint(0, len(wav) - self.input_length - 1)
            wav = wav[random_idx:random_idx+self.input_length]
        else:
            hop = (len(wav) - self.input_length) // self.num_chunks
            wav = [wav[i*hop:i*hop+self.input_length] for i in range(self.num_chunks)]
        return np.array(wav)

    def __len__(self):
        return len(self.filelist)


def get_gtzan_loader(data_path, batch_size, split='TRAIN', num_chunks=8, num_workers=0, input_length=None):
    data_loader = data.DataLoader(dataset=GTZANLoader(data_path, split=split, num_chunks=num_chunks, input_length=input_length),
                                                      batch_size=batch_size,
                                                      shuffle=True,
                                                      drop_last=False,
                                                      num_workers=num_workers)
    return data_loader

