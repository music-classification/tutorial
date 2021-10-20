# Datasets

We already have a great comprehensive [list of MIR datasets](https://github.com/ismir/mir-datasets/blob/master/outputs/mir-datasets.md).
In this book, we focus on *discussion* of datasets. 
We will review several important music tagging datasets. Over time, researchers have adopted different strategies to create and release datasets. 
This also resulted in various pros and cons, and traps.   

These are some important but rarely discussed aspects.

 - Availabilities of audio signal
   - This basic and fundamental requirement is already difficult. This is because, well, music is usually copyright-protected. 
   The solutions are i) just-do-it,  ii) distribute the features, and iii) use copyright-free music.
 - Hidden traps!
   - How shall we split them
     - Many datasets don't have a official dataset split, and this caused many problems. Usually, wrong split gets us an incorrectly optimistic result, which incentives us to overlook the problem.   
   - How noisy the labels are?
     - No annotation is perfect, but on a varying level. Why? How? 
   - How realistic the audio signals are?
     - We want our research (and the resulting models) to be practical. A lot of this depends on how similar the dataset is to the real, target data. 

## [Gtzan Music Genre (2002)](http://marsyas.info/downloads/datasets.html)
```{note}
- Audio is directly available
- 100 items x 10 genres x 30-second mp3 files.
- Single-label genre classification
```

<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1333468174%3Fsecret_token%3Ds-vEmb6LcHis4&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/user-537934052" title="Keunwoo Choi" target="_blank" style="color: #cccccc; text-decoration: none;">Keunwoo Choi</a> · <a href="https://soundcloud.com/user-537934052/sets/gtzan-music-genre/s-vEmb6LcHis4" title="Gtzan Music Genre" target="_blank" style="color: #cccccc; text-decoration: none;">Gtzan Music Genre</a></div>


The famous GTZAN dataset ([TODO: add citation]) deserves to be the [MNIST](https://en.wikipedia.org/wiki/MNIST_database) for music. 
[The first paper using this dataset](https://scholar.google.co.kr/citations?view_op=view_citation&hl=en&user=yPgxxpwAAAAJ&citation_for_view=yPgxxpwAAAAJ:u5HHmVD_uO8C) 
remains a foundational work in the modern music classification. The dataset was used in [more than 100 papers already in 2013](https://arxiv.org/abs/1306.1461).
It is popular since the concept of music genres and single-label classification is easy, simple, and straightforward.
30-second mp3 is small and short. With a lot of features and a power classifier, researchers these days can quickly achieve 
90+% (or even 95+% (or even 100%!)) accuracy. 

However, now we know that there are way too many issues with the dataset. This is summarized very well in [Bob L. Sturm's comprehensive survey](https://arxiv.org/abs/1306.1461). 
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

A tremendous number of following researchers owe its creator, George Tzanetakis, for the ~~copyright breach~~ dataset release.
Here's a quote from the website, where you can simply [one-click-download the dataset](http://opihi.cs.uvic.ca/sound/genres.tar.gz). 

> ..Unfortunately the database was collected gradually and very early on in my research so I have no titles (and obviously no copyright permission etc)..

This is not a viable option these days anymore. Let's see more modern approaches.   

## [MagnaTagATune, 2009](https://mirg.city.ac.uk/codeapps/the-magnatagatune-dataset)
```{note}
- Designed for tagging problem 
- Audio is directly available. They're from [magnatune.com](http://magnatune.com/), a marketplace of indie music. John Buckman, the founder of magnatune contributed these files. 
- 5,405 tracks (25,863 x 29-second clips), 230 artists, 446 albums, 188 tags.
```
<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1333473949%3Fsecret_token%3Ds-t6kAON9Vbi0&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/user-537934052" title="Keunwoo Choi" target="_blank" style="color: #cccccc; text-decoration: none;">Keunwoo Choi</a> · <a href="https://soundcloud.com/user-537934052/sets/magnatagatune/s-t6kAON9Vbi0" title="MagnaTagATune" target="_blank" style="color: #cccccc; text-decoration: none;">MagnaTagATune</a></div>

MagnaTagATune (**[LWM+09]**) has played a significant role since its release until even now (2021). It was used in pioneering research such as [DS14](https://ieeexplore.ieee.org/document/6854950), [CFS16](https://archives.ismir.net/ismir2016/paper/000009.pdf), [LPK+17](https://arxiv.org/abs/1703.01789), [WCS21][todo: add link], etc. [janne's. work]. etc.

"Tagging" is a specific kind of classification, and MagnaTagATune is one of the earliest tagging datasets that is in this scale and that comes with audio. The songs are all indie music, so use this dataset at your own risk - the property of the music/audio might not be as realistic as you want.

The gamification of the annotation process is worth mentioning. In this game called "Tag a Tune", two players were asked to tag a clip, then shown the other player's tagging results to finally judge if they were listening to the same clip or not.
This constraint-free annotation process has pros and cons; it is realistic, which is good; but it makes the label noisy, which is bad as a benchmark dataset.   

```{warning}
- Tags are weakly labeled and have synonyms
- DO NOT RANDOM SPLIT 25,863 clips! They're from the same track!
- There are various approaches how to split and whether to include below top-50 tags
- The score on this dataset is still improving, but only slightly. It means we might be near the glass ceiling.
```

This dataset turned out to be big enough to train some early deep neural network models such as 1D and 2D CNNs. Until late 2010s, MagnaTagATune was probably the most popular dataset in music tagging.  

```{tip}
- Use split from [] |
- If you split by yourself, do it by tracks (instead of clips) |
- Know you're dealing with an indie music|
- Know you're dealing with a weakly labeled dataset|
```

## [Million Song Dataset (2011)](http://millionsongdataset.com/)
```{note}
- Audio is not directly available. 
  - As of 2021, only a crawled version that contains ~99% of the preview clips is available by word of mouth.
- Literally a million tracks: By far the biggest dataset
- The provided last.fm tags are realistic
```
The million song dataset (MSD, [BEW+11]) is a monumental music dataset. It was ahead of time in every aspect -- size, quality, reliability, and various complementary features.

MSD has been *the* music dataset since the beginning of deep learning era. It enabled the first deep learning-based music recommendation system [**[ODS13]**](https://biblio.ugent.be/publication/4324554) and the first large-scale music tagging [**[CFS16]**](https://arxiv.org/abs/1606.00298). (+.. similarity search??)   

Researchers usually formulate the music tagging on MSD as a top-50 prediction task. This may be partially due to the convention of MagnaTagATune and earlier research, but it makes sense considering the sparsity of the tags. The tags in MSD are in an extremely long tail.

> in the MSD, .. there are
522,366 tags. This is outnumbering the 505,216 unique tracks..
>  
> .. the most popular tag is ‘rock’ which is associated with 101,071 tracks. However, ‘jazz’, the 12th most popular tag is used for only 30,152 tracks and ‘classical’, the 71st popular tag is used
11,913 times only. ..

 (from [**[CFC+]**](https://ieeexplore.ieee.org/abstract/document/8323324)
)

```{warning}
- Some splits have artist leakage
- It might be difficult to get the mp3s 
```

[The dataset split](https://github.com/keunwoochoi/MSD_split_for_tagging/) used in [**[CFS16]**](https://arxiv.org/abs/1606.00298) was based on simple random sampling. However, ... [todo; ask Minz]  

One critical downside of MSD is the availability of the audio. The creators of MSD adopted a very modern approach on this - while only distributing audio features and metadata, they released a code snippet for fetching 30-second audio previews from [7digital](https://us.7digital.com/). (Recently, people have reported the audio preview API does not work anymore. This means the audio is available only by word of mouth.)


```{tip}
- 🤫 Ask around for the audio!
- Use the recent split
- No music after 2011
```
- NSYNTH
- audioset
- openmic
- RWC
- some mood stuff

## FMA
```{note}
- basic specs
```


```{warning}
- etc etc
```


```{tip}
 - etc 
```
## MTG-Jamendo
```{note}
- basic specs
```


```{warning}
- etc etc
```


```{tip}
 - etc 
```
## AudioSet
```{note}
- basic specs
```


```{warning}
- etc etc
```


```{tip}
 - etc 
```
## NSynth
```{note}
- basic specs
```


```{warning}
- etc etc
```


```{tip}
 - etc 
```

---
## mood?
```{note}
- basic specs
```

```{warning}
- etc etc
```


```{tip}
 - etc 
```
---
## datasets
```{note}
- basic specs
```

```{warning}
- etc etc
```


```{tip}
 - etc 
```
---
## datasets
```{note}
- basic specs
```

```{warning}
- etc etc
```


```{tip}
 - etc 
```
---

## Availabilities of audio signal

Due to the copyright, sharing the original audio signal is not always allowed.
This makes people to come up with different solutions when releasing dataset.
Let's see what are the solutions and the consequence of the choices.  

### 1. Just distribute the audio signals.

..


The MagnaTagATune is one of the early examples where researchers found a copyright-free solution. 

-   

How is the 

- magnatagatune
- FMA (Copyright-free)
- MTG-Jamendo (Copyright-free)

### 2. Distribute the features
- MSD
- Kakao
- .. 

### 3. Distribute the IDs
- MSD
- AudioSet 


A traditional solution was to share a set of pre-computed features, instead of audio signals, as done with Million Song Dataset (+tbd). 



Introduce available datasets and their characteristics, links, etc. 

Genre classification: GTZAN, FMA, Ballroom, Extended ballroom, ...
Mood classification: MIREX, AudioSet subset, MSD subset, ...
Instrument identification: IRMAS, OpenMIC, NSYNTH, RWC, ...
Tagging: MTAT, MSD, MTG-Jamendo, Music4All, ...

