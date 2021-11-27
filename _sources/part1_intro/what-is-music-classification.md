# What is Music Classification?

Music classification is a music information retrieval (MIR) task whose objective is the computational understanding of music semantics. For a given song, the classifier predicts relevant musical attributes. Based on the task definition, there are a nearly infinite number of classification tasks – from genres, moods, and instruments to broader concepts including music similarity and musical preferences. The retrieved information can be further utilized in many applications including music recommendation, curation, playlist generation, and semantic search.


### Single-label classification
<p align = "center">
<img src = "https://imgur.com/zET3gNR.png" width=650>
</p>
<p align = "center">
Which record store would you prefer to go?
</p>

Let's say there are two record stores in your town. 'ABC Records' curates all the records in alphabetic order, while 'MIR Records』' categorizes their stocks based on musical genres. When you already know what you want to buy, 'ABC Records' is a good place to go as you can search by the alphabetic index. However, when you want to browse and discover new music, 'MIR Records' will be preferable as you can visit the section with your favorite genre. Like this, well-designed categorization (i.e., music classification) helps customers browse music more efficiently. This record store scenario can be interpreted as a single-label classification task. One item can be in a single section; hence categories (genres in this example) are exclusive.


<p align = "center">
<img src = "https://i.imgur.com/jkgJD4Z.png" width=400>
</p>
<p align = "center">
An example of single-label classification
</p>

```{warning}
Genres are not always exclusive to each other. One song can belong to multiple genres.
```



### Multi-label classification
Different from the example above, one item may belong to multiple categories. For example, one song can be Disco and K-Pop simultaneously, and these categories are not exclusive to each other. Also, listeners would like to browse music by instruments, languages, moods, or context, not only musical genres. We can handle these multiple musical attributes with multi-label classification. The multi-label classification is often referred to as "music tagging" since it puts various music tags for a given song. 

<p align = "center">
<img src = "https://i.imgur.com/Csgtubf.png" width=400>
</p>
<p align = "center">
An example of multi-label classification
</p>

Multi-label classification is handled as a binary classification for each musical attribute. For each label, the system determines whether a given song is positive to the label or not. In contrast with single-label classification, labels are not exclusive, and multiple tags can exist together.


### Music classification tasks
There can be an almost infinite number of music classification tasks based on product requirements. Among them, the most explored music classification tasks in MIR research are listed as follow:

- Genre classification {cite}`tzanetakis2002musical`
- Mood classification {cite}`kim2010music`
- Instrument identification {cite}`herrera2003automatic`
- Music tagging {cite}`lamere2008social`

We discuss music classification tasks in more detail later in this chapter.  

```{note}
Music tagging subsumes all other classification tasks as any class (label) can be musical tags.
```


### Applications
The explosion of digital music has dramatically changed our music consumption behavior. Massive music libraries are available through streaming platforms, and it is impossible to browse the entire collections item-by-item. As a result, we need robust knowledge management systems more than ever. Music classification is a technique that supports knowledge management. Music classification models enhance users' music experience through many applications, including recommendation, curation, playlist generation, semantic search, and analysis of listening behavior. 
<p align = "center">
<img src = "https://i.imgur.com/TyvMfNX.png" width=580>
</p>
<p align = "center">
Applications of music classification. Screenshots captured from Resso, Apple music, Pandora, and Spotify
</p>

- Recommendation: Once we have labeled or predicted musical attributes, a system can recommend music to users based on frequently consumed musical attributes of the users. Unlike [collaborative filtering](https://en.wikipedia.org/wiki/Collaborative_filtering), a prevalent recommender system using user-item interactions, this content-based recommendation does not suffer from [cold-start problems](https://en.wikipedia.org/wiki/Cold_start_(recommender_systems)) and popularity bias {cite}`celma2010music`.
- Curation: As we checked from the previous record store example, well-designed music curation helps users browse enormous music libraries efficiently. Hence, music streaming services curate music by genres, subgenres, or moods. Human agents can manually do this process, but music classification models can replace human efforts.
- Playlist generation: The usage of music classification models in playlist generation is similar to the use in music recommendation. But playlist generation needs to consider the order of the songs and more user context.
- Listening behavior analysis: Most modern streaming services provide annual reports of personal listening trends. This report helps users to understand their taste better and is basically fun!

<!--- Curation
- Semantic search
- Content-based recommendation
- Playlist generation
- Analysis

-->