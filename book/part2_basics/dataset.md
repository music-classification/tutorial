# Datasets
## Overview

There already exists a great comprehensive [list of MIR datasets](https://github.com/ismir/mir-datasets/blob/master/outputs/mir-datasets.md).
In this book, we focus on some important datasets and *discussion* of them including some secrets that worth spreading.  
Over time, researchers have adopted different strategies to create and release datasets. 
This resulted in various pros and cons, and traps.   

These are some important but rarely discussed aspects.

### Availabilities of audio signal
   - This basic and fundamental requirement is already difficult. This is because, well, music is usually copyright-protected. 
   The solutions are i) just-do-it,  ii) distribute the features, iii) use copyright-free music, iv) distribute the IDs.
 

### Hidden traps! 

..Because some of the dataset creation procedure was not perfect.

   - How shall we split them
     - Many datasets don't have a official dataset split, and this caused many problems. Usually, wrong split gets us an incorrectly optimistic result, which incentives us to overlook the problem.   
   - How noisy the labels are?
     - No annotation is perfect, but on a varying level. Why? How? 
     - Regarding the inherent noisiness of the label (subjectivity, fuzzy definition, etc), what is the practical/meaningful best performance?
   - How realistic the audio signals are?
     - We want our research (and the resulting models) to be practical. A lot of this depends on how similar the dataset is to the real, target data.    

---

Now, let's look into actual datasets.

## [Gtzan Music Genre (2002)](http://marsyas.info/downloads/datasets.html)

<iframe width="100%" height="270" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1333468174&color=%2374f0ed&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/user-537934052" title="Keunwoo Choi" target="_blank" style="color: #cccccc; text-decoration: none;">Keunwoo Choi</a> · <a href="https://soundcloud.com/user-537934052/sets/gtzan-music-genre" title="Gtzan Music Genre" target="_blank" style="color: #cccccc; text-decoration: none;">Gtzan Music Genre</a></div>

```{note}
- Audio is directly available
- 100 items x 10 genres x 30-second mp3 files.
- Single-label genre classification
```


The famous GTZAN dataset {cite}`tzanetakis2001gtzan` deserves to be the [MNIST](https://en.wikipedia.org/wiki/MNIST_database) for music. 
[The first paper using this dataset {cite}`tzanetakis2002musical`](https://scholar.google.co.kr/citations?view_op=view_citation&hl=en&user=yPgxxpwAAAAJ&citation_for_view=yPgxxpwAAAAJ:u5HHmVD_uO8C) 
remains a foundational work in the modern music classification. The dataset was used in [more than 100 papers already in 2013 according to a survey ({cite}`sturm2013gtzan`)](https://arxiv.org/abs/1306.1461).
It is popular since the concept of music genres and single-label classification is easy, simple, and straightforward.
30-second mp3 is small and short. With a lot of features and a power classifier, researchers these days can quickly achieve 
90+% (or even 95+% (or even 100%!)) accuracy. 

However, now we know that there are way too many issues with the dataset. This is summarized very well in [the aforementioned survey by Bob L. Sturm's survey {cite}`sturm2013gtzan`](https://arxiv.org/abs/1306.1461). 
We'll list a few.

```{warning}
- The audio quality varies by samples (though it was intended) and it is not annotated
- There are heavy artist repetition, which are very often ignored during dataset split
- The labels don't seem to be 100% correct (which makes the 100%-accuracy models questionable)
```

Because of these known issues, GTZAN doesn't seem to be as popular as it used to be in published research. 
Still, one may find it a simple benchmark dataset. In that case, please refer to [this repo](https://github.com/coreyker/dnn-mgr/tree/master/gtzan)
made by Corey Kereliuk and Bob Sturm and use a fault-filtered split.

```{tip}
 - Use other, bigger and better datasets
 - Use a [cleaned version and split](https://github.com/coreyker/dnn-mgr/tree/master/gtzan)
```

A tremendous number of following researchers owe its creator, George Tzanetakis, for the dataset release.
Here's a quote from the website, where you can simply [one-click-download the dataset](http://opihi.cs.uvic.ca/sound/genres.tar.gz). 

> ..Unfortunately the database was collected gradually and very early on in my research so I have no titles (and obviously no copyright permission etc)..

This is not a viable option these days anymore. Let's see more modern approaches.   

## [MagnaTagATune (2009)](https://mirg.city.ac.uk/codeapps/the-magnatagatune-dataset)

<iframe width="100%" height="270" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1333473949&color=%2374f0ed&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/user-537934052" title="Keunwoo Choi" target="_blank" style="color: #cccccc; text-decoration: none;">Keunwoo Choi</a> · <a href="https://soundcloud.com/user-537934052/sets/magnatagatune" title="MagnaTagATune" target="_blank" style="color: #cccccc; text-decoration: none;">MagnaTagATune</a></div>

```{note}
- Designed for tagging problem 
- Audio is directly available. They're from [magnatune.com](http://magnatune.com/), a marketplace of indie music. John Buckman, the founder of magnatune contributed these files. 
- 5,405 tracks (25,863 x 29-second clips), 230 artists, 446 albums, 188 tags.
```

MagnaTagATune {cite}`law2009evaluation` has played a significant role since its release until even now (2021). It was used in pioneering research such as {cite}`dieleman2014end`, {cite}`choi2016automatic`, {cite}`lee2017sample`, {cite}`won2021semi`, {cite}`spijkervet2021contrastive`, etc.

"Tagging" is a specific kind of classification, and MagnaTagATune is one of the earliest tagging datasets that is in this scale and that comes with audio. The songs are all indie music, so use this dataset at your own risk - the property of the music/audio might not be as realistic as you want.

The gamification of the annotation process is worth mentioning. In this game called "Tag a Tune", two players were asked to tag a clip, then shown the other player's tagging results to finally judge if they were listening to the same clip or not.
This constraint-free annotation process has pros and cons; it is realistic, which is good; but it makes the label noisy, which is bad as a benchmark dataset.   

There are various approaches how to split and whether to include below top-50 tags during training and/or testing. This hidden difference makes the comparison silently noisy. Finally, The authors of {cite}`won2020evaluation` decided to include items with top-50 tags only, both in training and testing. They then trained various types of models and shared the result in the paper. We recommend follow-up researchers to use the same split for a correct comparison. 

```{warning}
- Tags are weakly labeled and have synonyms
- DO NOT RANDOM SPLIT 25,863 clips! They're from the same track!
- Researchers used slightly different splits. 
- The score on this dataset is still improving, but only slightly. It means we might be near the glass ceiling.
```

This dataset turned out to be big enough to train some early deep neural network models such as 1D and 2D CNNs. Until late 2010s, MagnaTagATune was probably the most popular dataset in music tagging.



```{tip}
- Follow the split and refer to the numbers in {cite}`won2020evaluation`. 
- If you split by yourself, do it by tracks (instead of clips) |
- Know you're dealing with an indie music|
- Know you're dealing with a weakly labeled dataset|
```

## [Million Song Dataset (2011)](http://millionsongdataset.com/)
<iframe width="100%" height="270" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1334174407&color=%2300aabb&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/user-537934052" title="Keunwoo Choi" target="_blank" style="color: #cccccc; text-decoration: none;">Keunwoo Choi</a> · <a href="https://soundcloud.com/user-537934052/sets/million-song-dataset" title="Million Song Dataset" target="_blank" style="color: #cccccc; text-decoration: none;">Million Song Dataset</a></div>

```{note}
- Audio is not directly available. 
  - As of 2021, only a crawled version that contains ~99% of the preview clips is available by word of mouth.
- Literally a million tracks: By far the biggest dataset
- The provided last.fm tags are realistic
```

The million song dataset (MSD, {cite}`bertin2011million`) is a monumental music dataset. It was ahead of time in every aspect -- size, quality, reliability, and various complementary features.

MSD has been *the* music dataset since the beginning of deep learning era. It enabled the first deep learning-based music recommendation system {cite}`van2013deep` and the first large-scale music tagging {cite}`choi2016automatic`.   

Researchers usually formulate the music tagging on MSD as a top-50 prediction task. This may be partially due to the convention of MagnaTagATune and earlier research, but it makes sense considering the sparsity of the tags. The tags in MSD are in an extremely long tail.

> in the MSD, .. there are
522,366 tags. This is outnumbering the 505,216 unique tracks..
>  
> .. the most popular tag is ‘rock’ which is associated with 101,071 tracks. However, ‘jazz’, the 12th most popular tag is used for only 30,152 tracks and ‘classical’, the 71st popular tag is used
11,913 times only. ..

 (from {cite}`choi2018effects`)

```{warning}
- Some splits have artist leakage
- It might be difficult to get the mp3s 
```

[The dataset split](https://github.com/keunwoochoi/MSD_split_for_tagging/) used in {cite}`choi2016automatic` was based on simple random sampling. However, this resulted in potentially allowing information between splits as same artists appear in different split.   
To avoid this issue, the authors of {cite}`won2021semi` introduced CALS split - a cleaned and artist-level stratified split. This includes [TRAIN, VALID, TEST, STUDENT, NONE] sets where STUDENT set is a set of unlabeled items with respect to top-50 tags and can be used for semi-supervised and unsupervised learning. (NONE is a subset of discarded items since their artists appeared in TRAIN.)

One critical downside of MSD is the availability of the audio. The creators of MSD adopted a very modern approach on this - while only distributing audio features and metadata, they released a code snippet for fetching 30-second audio previews from [7digital](https://us.7digital.com/). (Recently, people have reported the audio preview API does not work anymore. This means the audio is available only by word of mouth.)


```{tip}
- 🤫 Ask around for the audio!
- Use the recent split
- No music after 2011
```

## [FMA (2017)](https://arxiv.org/abs/1612.01840)

<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1334749648&color=%2374f0ed&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/user-537934052" title="Keunwoo Choi" target="_blank" style="color: #cccccc; text-decoration: none;">Keunwoo Choi</a> · <a href="https://soundcloud.com/user-537934052/sets/free-music-archive-dataset" title="Free Music Archive dataset" target="_blank" style="color: #cccccc; text-decoration: none;">Free Music Archive dataset</a></div>

```{note}
- Rigorously processed metadata and split. Maintained nicely on Github.
- More than 100k full tracks of copyright-free indie music
- Artist-chosen genres in a hierarchy defind by the website (free music archive)
```

Free Music Archive dataset (FMA, {cite}`defferrard2016fma`) is a modern, large-scale dataset that contains full-tracks, instead of short preview clips. Along with MTG-Jamendo, it enables interesting research towards fully utilizing the information of the whole audio signal.

```{warning}
- Audio quality varies, and the music is quite "indie".
- Genre labels are i) from a pre-defined 163-genre hierarchy and ii) chosen by the artist. 
```

From a machine learning point of view, the second item in Warning is an advantage. However, it limits the development of realistic models.
  
```{tip}
- Good for genre classification/hierarchical classification.
- A full-track is available, which is rare in the community 
```
## [MTG-Jamendo (2019)](https://github.com/MTG/mtg-jamendo-dataset)
<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1342367305&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/user-537934052" title="Keunwoo Choi" target="_blank" style="color: #cccccc; text-decoration: none;">Keunwoo Choi</a> · <a href="https://soundcloud.com/user-537934052/sets/mtg-jamendo-dataset" title="MTG Jamendo Dataset" target="_blank" style="color: #cccccc; text-decoration: none;">MTG Jamendo Dataset</a></div>

```{note}
- 55,000 full audio tracks (320kbps MP3)
- 195 tags from genre, instrument, and mood/theme 
- Pre-defined split based on the target tasks (genre, instrument, mood/theme, top-50, overall.) 
```

MTG-Jamendo {cite}`bogdanov2019mtg` is a modern dataset that shares some pros of MSD and FMA. Its audio is readily and legally available, the audio is full-track and high-quality, contains various and realistic tags, and comes with properly defined splits.

There are some interesting properties of this dataset, too. Pop and rock is the top genres in most of the genre datasets, and that could be the same for your target test set. In MTG-Jamendo, the genre distribution is skewed towards some other genres: The most popular genres are Electronic (16,480 items), soundtrack (~8k), pop, ambient, and rock. For mood alone, MTG-Jamendo is still great but there are alternatives (more information is under Resources section).  

```{warning}
- Genre distribution is slightly unusual
```

The distribution mismatch between training, validation, and testing sets is a classic yet critical problem. This wouldn't be a problem if all the testing and evaluation is within the provided split of MTG-Jamendo. Otherwise, one would want to have a different sampling strategy to alleviate the issue. (To be fair, this is not only applicable for MTG-Jamendo.)

## [AudioSet (2017)](https://research.google.com/audioset/index.html)

- [Preview of AudioSet](https://research.google.com/audioset/eval/music.html).

```{note}
- Large scale (2.1 million in total), 1 million under music
- Fairly strongly labeled in terms of temporal resolution (labeled for 10-second segment)
- High-quality annotation
- Official and reliable split is provided
```

AudioSet {cite}`45857` is made for general audio understanding and not specifically for music. But, in their well-designed taxonomy, there is [a high-level category 'music'](https://research.google.com/audioset/ontology/music_1.html) that includes 'musical instrument', 'music genre', 'musical concepts', 'music role', and 'music mood'. In total, there are more than 1M items, each of which corresponds to a specific 10-second of YouTube video.
   
The annotation is considered to be more than quite reliable. Also, for each category, AudioSet provides the estimated accuracy of the annotation. 

```{warning}
- It includes music with a low audio quality 
- Only the video URLs are provided
- The exact version would vary by people
```

The varying audio quality might be a downside depending on the target application. The dataset includes [a live session](https://youtu.be/0TiEO149Ydc), [a noisy and amateur recording](https://youtu.be/-YIT4HBM__g), [music with a low SNR](https://youtu.be/0Ycad70UNwE), etc. 

To use AudioSet, one has to crawl the audio signal by themselves. Downloading YouTube video/audio is in a grey zone in terms of copyright, let alone the use of them.

Another issue is that the availabilities of the items in AudioSet are time-varying and country-dependent! Once the videos are taken down, that's it. Depending on the setting, some videos are just not available in some countries. Given the large size, this issue might not be critical in practice -- so far.  


## [NSynth (2017)](https://magenta.tensorflow.org/nsynth)

<iframe width="100%" height="270" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1334184460&color=%2374f0ed&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/user-537934052" title="Keunwoo Choi" target="_blank" style="color: #cccccc; text-decoration: none;">Keunwoo Choi</a> · <a href="https://soundcloud.com/user-537934052/sets/nsynth-dataset" title="NSynth Dataset" target="_blank" style="color: #cccccc; text-decoration: none;">NSynth Dataset</a></div>

```{note}
- '305,979 musical notes, each with a unique pitch, timbre, and envelope' as well as five different velocities
- 16 kHz, 4-second, monophonic. 
```
NSynth {cite}`engel2017neural` is 'a dataset of musical notes'. Yes, it is a music dataset. But is it a music *classification* dataset? Yes, in a sense that MNIST is an image dataset. We suggest using this dataset only as a simple proof of concept.  

```{warning}
- This dataset is great for a lot of purposes, not exactly for music classification
```

## Summary

We showed that many popular datasets are different (and flawed) in many aspects. This is applied to the datasets we did not discussed above. But that is a part of reality. In general, we strongly recommend investigating the dataset you use closely - audio, labels, split, etc. It is always helpful to talk to the other researchers -- the creators and the users of the dataset.

There's good news as well. The research community is learning lessons from the mistakes and adopting better data science practices. Recently, as a result, we witness the quality of datasets increases significantly. At the end of this book, we will revisit this in more detail and discuss what to consider when creating datasets.    

## Resources

- We barely cover mood-related datasets in this section. We would like to refer to [this repo](https://github.com/juansgomez87/datasets_emotion){cite}`GomezCanon2021SPM` which provides great information about music/mood datasets.
- [`mirdata`](https://mirdata.readthedocs.io/en/stable/index.html) {cite}`bittner2019mirdata` is handy Python package that helps researchers handle MIR datasets easily and correctly. Many classification datasets are included e.g., [the AcousticBrainz genre dataset](https://github.com/MTG/acousticbrainz-genre-dataset) {cite}`bogdanov2019acousticbrainz`.
