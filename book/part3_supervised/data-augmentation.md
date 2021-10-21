# Audio Data Augmentations

In this chapter, we will discuss common transformations that we can apply to audio signals. We will refer to these as "audio data augmentations".

Data augmentations are a set of methods that add modified copies to a dataset, from the existing data. This process creates many variations of natural data, and can act as a regulariser to reduce the problem of overfitting. It can also help deep neural networks become robust to complex variations of natural data, which improves their generalisation performance.

In the field of computer vision, the transformations that we apply to images are often very self-explanatory. Take this image, for example. It becomes fairly obvious that we have applied various amounts of gaussian blurring on this image.

![alt text](images/sphx_glr_plot_transforms_007.png "Logo Title Text 1")

Naturally, we cannot translate transformations from the vision domain directly to the audio domain. Before we explore a battery of audio data augmentations, we now list the currently available code libraries:

| Name  | Author | Framework | Language  | License  |  Link |
|---|---|---|---|---|---|
| Muda | B. McFee et al. (2015) | General Purpose | Python  | ISC License | [source code](https://github.com/bmcfee/muda) |
| Audio Degradation Toolbox | M. Mauch et al. (2013) | General Purpose | MATLAB  | GNU General Public License 2.0 | [source code](https://code.soundsoftware.ac.uk/projects/audio-degradation-toolbox) |
| rubberband | - | General Purpose | C++ | GNU General Public License (non-commercial) | [website](https://breakfastquay.com/rubberband/), [pyrubberband](https://github.com/bmcfee/pyrubberband)
| audiomentations | I. Jordal (2021) | General Purpose | Python | MIT License | [source code](https://github.com/iver56/audiomentations)
| tensorflow-io | tensorflow.org | TensorFlow | Python | Apache 2.0 License | [tutorial](https://www.tensorflow.org/io/tutorials/audio)
| torchaudio | pytorch.org | PyTorch | Python | BSD 2-Clause "Simplified" License | [source code](https://github.com/pytorch/audio)
|  torch-audiomentations | Asteroid (2021) | PyTorch | Python | MIT License | [source code](https://github.com/asteroid-team/torch-audiomentations)
| torchaudio-augmentations | J. Spijkervet (2021) | PyTorch | Python | MIT License | [source code](https://github.com/Spijkervet/torchaudio-augmentations) |

```{note}
In these examples and the accompanying code, we assume the shape of audio ordered in our array is follows:

(channel, time)
```






Audio = CHANNEL x SAMPLES

```{warning}
- The audio quality varies by samples (though it was intended) and it is not annotated
- There are heavy artist repetition, which are very often ignored during dataset split
- The labels don't seem to be 100% correct (which makes the 100%-accuracy models questionable)
```

```{tip}
 - Use other, bigger and better datasets
 - Use a [cleaned version and split](https://github.com/coreyker/dnn-mgr/tree/master/gtzan)
```

```{note}
- Designed for tagging problem 
- Audio is directly available. They're from [magnatune.com](http://magnatune.com/), a marketplace of indie music. John Buckman, the founder of magnatune contributed these files. 
- 5,405 tracks (25,863 x 29-second clips), 230 artists, 446 albums, 188 tags.
```