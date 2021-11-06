# Music Classification: Beyond Supervised Learning, Towards Real-world Applications
## About the book

This is a book written for a [tutorial session](https://ismir2021.ismir.net/tutorials/) of [the 22nd International Society for Music Information Retrieval Conference](https://ismir2021.ismir.net/), Nov 8-12, 2021 in an online format. The [ISMIR conference](https://ismir.net/) is the world’s leading research forum on processing, searching, organising and accessing music-related data.


## Motivation
**Lower the barrier**: As deep learning emerges, music classification research has entered a new phase, and many data-driven approaches have been proposed to solve the problem. However, researchers sometimes use jargon in various ways. Also, some implementation details and evaluation methods are ambiguously described in the papers, blocking access to the information without personal contact. These are tremendous obstacles when new researchers want to dive into this fascinating research area. Through this book, we would like to lower the barrier for newcomers and reduce miscommunication between researchers by sharing the secrets.

**Cope with data issue**: Another issue that we are facing under the deep learning era is the exhaustion of labeled data. Labeling musical attributes requires strong domain knowledge and a significant amount of time for listening; hence expensive. Because of this, deep learning researchers started actively utilizing large-scale unlabeled data. This book introduces the recent advances in semi- and self-supervised learning that enables music classification models to step further beyond supervised learning.

**Narrow the gap**: Music classification has been applied to solve real-world problems successfully. However, some important procedures and considerations for real-world applications are rarely discussed as research topics. In this book, based on the various industry experiences of the authors, we try our best to raise awareness of these questions and provide answers and perspectives. We hope this helps academia and industries harmonize better together.

## About the authors

<p align = "left">
<img src = "https://i.imgur.com/QGazkla.jpg" width=100>
</p>

[**Minz Won**](https://minzwon.github.io/) is a Ph.D candidate at the 
[Music Technology Group (MTG) of Universitat Pompeu Fabra](https://www.upf.edu/web/mtg) in Barcelona, Spain. 
His research focus is music representation learning. 
Along with his academic career, he has put his knowledge into practice with industry internships at 
Kakao Corp., Naver Corp., Pandora, Adobe, and he recently joined ByteDance as a research scientist. 
He contributed to the winning entry in the WWW 2018 Challenge: Learning to Recognize Musical Genre.

<p align = "left">
<img src = "https://i.imgur.com/PegbqPJ.jpg" width=100>
</p>

[**Janne Spijkervet**](https://jspijkervet.com/) graduated from the University of Amsterdam in 2021 with her 
Master's thesis titled "Contrastive Learning of Musical Representations". The paper with the same title was published 
in 2020 on self-supervised learning on raw audio in music tagging. She has started at ByteDance as 
a research scientist (2020 - present), developing generative models for music creation. 
She is also a songwriter and music producer, and explores the design and use of machine learning technology in her music.

<p align = "left">
<img src = "https://i.imgur.com/7NFzRYd.jpg" width=100>
</p>

[**Keunwoo Choi**](https://keunwoochoi.github.io/) is a senior research scientist at ByteDance, developing machine learning 
products for music recommendation and discovery. He received a Ph.D degree from 
[Queen Mary University of London (c4dm)](https://c4dm.eecs.qmul.ac.uk/) in 2018. As a researcher, he also has been 
working at Spotify (2018 - 2020) and several other music companies as well as open-source projects such as 
[`Kapre`](https://kapre.readthedocs.io/en/latest/), `librosa`, and `torchaudio`. 
He also writes [some music](https://www.youtube.com/channel/UC6WGQvwwM3M7sX98zJ14XPA).


## Software

We use Jupyter Book{cite}`executable_books_community_2020_4539666`, Librosa 0.8.1{cite}`mcfee2015librosa` {cite}`brian_mcfee_2021_4792298`, Pytorch{cite}`paszke2019pytorch`, Torchaudio{cite}`yang2021torchaudio`, Matplotlib{cite}`hunter2007matplotlib`, and Numpy{cite}`harris2020array`.


## Citing this book
```
@book{musicclassification:book,
	Author = {Minz Won, Janne Spijkervet, and Keunwoo Choi},
	Month = Nov.,
	Publisher = {https://music-classification.github.io/tutorial},
	Title = {Music Classification: Beyond Supervised Learning, Towards Real-world Applications},
	Year = 2021,
	Url = {https://music-classification.github.io/tutorial}
}
```
