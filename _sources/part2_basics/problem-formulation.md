# Problem Formulation

In this section, we share our hands-on experiences of and details about music classification tasks. There are various types of music classification tasks, and a task can be formulated in different ways. The ideas and considerations are reflected when one constructs a new dataset. After then, users of the dataset follow what was assumed in the dataset.  

## Genre Classification

Music genre is one of the first things that come to people's mind when they talk about music. Every music listener knows at least some genre names. When talking about musical preferences, people assume they're supposed to talk about their favorite genres.

The simplest problem formulation of genre classification is to define a genre taxonomy that is **flat** and **mutually exclusive** (single-label classification). This is how the pioneering Gtzan genre classification dataset was constructed {cite}`tzanetakis2002musical`. The authors set 10 high-level genres:

> "blues, classical, country, disco, hip hop, jazz, metal, pop, reggae, rock".
 
Are they really flat? Musicologists can argue about it for a whole night. Are they mutually exclusive? Probably.. not. One can always find (or write) hybrid music by combining some important features of various genres. However, this simplification works to some extent (Every problem formulation is wrong, but some are useful.) We also suspect people naturally have the idea of mutual exclusiveness when they think of music genres. If that's true, the simplification is not only a bad thing. It was also adopted in Ballroom dataset {cite}`cano2006ismir`, FMA-small and FMA-medium {cite}`defferrard2016fma`, ISMIR 2004 genre {cite}`cano2006ismir`, etc.
 
We can find a different problem formulation in more modern datasets. The mutual exclusiveness assumption was loosened in Million Song Dataset {cite}`bertin2011million` (with tagtraum genre annotations {cite}`schreiber2015improving`). This allows a track to have more than one genre labels (=**multi-label classification**), which is probably more correct. This is also the usual case where genre classification is treated as a part of a tagging problem (since tags usually include various types of labels including genres) such as MTG-Jamendo {cite}`bogdanov2019mtg`.

Finally, a hierarchical genre taxonomy is considered in datasets such as FMA-Full {cite}`defferrard2016fma` and AcousticBrainz-Genre {cite}`bogdanov2019acousticbrainz`.

## Mood classification

The genre boundaries are already fuzzy, but perhaps not as much as those of mood. By definition, mood is 100% subjective; and then there is the difference between perceived mood (the mood of music) and induced mood (the mood one would feel when listening to the music) -- let alone a time-varying nature of it. In practice, MIR researchers have been brave enough to be ignorant about those details and formulate mood classification problems in various ways.

In general, the whole scene is similar to that of genre classification. Some early datasets are based on flat hierarchy (e.g., MoodsMIREX). When being a part of tagging problem, it's allowed to have multi-labeling (MSD, MTG-Jamendo) {cite}`bertin2011million`, {cite}`bogdanov2019acousticbrainz`.

But, there is something special in mood classification. Not all the researchers in mood understanding agreed to make a compromise and formulate it as a classification problem. As a result, some continuity was allowed when annotating mood of music.
 
The most common method is to annotate it in a **two-dimensional plane** where the axes represents arousal and valence. DEAP and Emomusic are examples {cite}`koelstra2011deap`, {cite}`soleymani20131000`. Sometimes, researchers even went further. For example, the music can be annotated in a three-dimensional space -- valence, arousal, and dominance. In another direction, there is time-varying annotation (every 1 second) in DEAM/Mediaeval {cite}`soleymani2016deam`.

## Instrument identification

Instrument identification is another interesting problem that is a bit different from all the others. When pop music is the target, researchers have no control in the range of the existing instruments - when sampling some tracks, it is not possible to limit the instruments to be in a pre-defined taxonomy. One can manually sample items so that there only exist some selected, target instruments. But what's the point when reality ignores the constraint?
 
That was, though, not a problem in the early days since researchers didn't dare to annotate all the instruments. In fact, in the very early days, the target of instrument identification model was not even music tracks -- instrument **samples** (e.g., 1-second clips that contains only a single note of one instrument) were the items to classify.
 
The problem became more realistic with datasets such as [IRMAS](https://www.upf.edu/web/mtg/irmas) {cite}`bosch2012comparison`. It has annotations of a single **'predominant' instrument** of an item. This means mutual exclusiveness is assumed and the problem becomes a single-label classification. It is subjective and noisy, but again - we always approximate anyway.

More recently, instrument identification was treated as **multi-label classification** in dataset such as OpenMIC-2018 {cite}`humphrey2018openmic`. Like other tasks, it is also a multi-label classification when being solved as a part of music tagging in MSD or MTG-Jamendo {cite}`bertin2011million`, {cite}`bogdanov2019acousticbrainz`.

We can (relatively) safely assume that Instrument annotation is, compared to others such as genres or mood, objective. This may sound good, but this makes it difficult for researchers to accept the noise in the label. When it comes to mood or genre, when the label doesn't seem quite right, researchers may still accept that as a result of inherent subjectivity. However, there are many, many unannotated existing instruments in OpenMIC-2018, MSD, and MTG-Jamendo -- in other words, we really know with high confidence that they are wrong! For this reason, we think that the future of instrument identification dataset might be a synthetic(ally mixed) dataset with 100% correct instrument labels.

## Music tagging

We already mentioned music tagging above, but what is it exactly? The progress of the computer and internet has given the privilege of labeling music to every single music listener -- the **democratization of annotation**. We call this process music tagging. Social music services such as Last.fm gathered these tags, and predicting these tags from the audio content became a task named music (auto-)tagging.

There is no constraint on which tag to use as long as the text field UI allows. Because of this freedom, tagging datasets are extremely **messy, noisy, and in a long-tail**. For example, million song dataset has 505,216 tracks with at least one last.fm tags and the total number of unique tags is.. 522,366 {cite}`bertin2011million`. There are more tags than the number of the tracks! Out of them, the 7th popular tag is.. "favorite". The 18th is "Awesome" (yes, it distinguishes lower/uppercases). 33th is "seen live". 37th "Favorite" (I told you). 41th is "Favourite".
 
Surprisingly, we can still solve this to some extent! How? Well, actually, many other tags -- especially the top ones -- are relevant to the music content. These are the top-15 tags after removing those mentioned fuzzy tags.

> 'rock', 'pop', 'alternative', 'indie', 'electronic', 'female vocalists', 'dance', '00s', 'alternative rock', 'jazz', 'beautiful', 'metal', 'chillout', 'male vocalists', 'classic rock',

There are genre, mood, and instruments -- each of which has been treated as a target category for automatic classification.
 
What is the exact point of solving a tagging problem if the tag taxonomy is merely a superset of other labels? Musically, the taxonomy and the occurrence of tags reflects what listeners care about. This means the knowledge a model learns can be more universally useful than that from other tasks. Practically, it is easier to collect music tags than collecting (expert-annotated) genre, mood, or instrument labels. This enabled researchers to train and evaluate deep learning models, and this is why tagging remains to be the most popular music classification problem.
