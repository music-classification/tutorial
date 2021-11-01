# Beyond supervision

<p align = "center">
<img src = "https://i.imgur.com/ojSewi1.png" width=500>
</p>
<p align = "center">

</p>


In previous sections, we learned how to facilitate music classification in a data-driven fashion when we have labeled music audio. The main motivation of building music classification models was to save human efforts of manually labeling musical attributes. However, modern deep learning models are data-hungry. As a result, ironically, human annotators need to label more data to train a better model. In this section and the next section, we are going to explore training methods that we can choose instead of manually labeling more data. 



In a real-world scenario, we have a large-scale music library but only few of them are labeled. Also, sometimes existing labels have different taxonomies from our target task. 
To tackle the issue of limited amount of labeled data, transfer learning takes advantage of other existing labels and semi-/self-supervised approaches utilize abundant unlabeled data. Let's check the motivation, concepts, and implementation of each approach.
