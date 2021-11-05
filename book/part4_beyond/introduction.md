# Beyond supervision

<p align = "center">
<img src = "https://i.imgur.com/ojSewi1.png" width=600>
</p>
<p align = "center">

</p>


In previous sections, we learned how to facilitate music classification in a data-driven fashion when we have labeled music audio. The main motivation of building music classification models was to save human efforts of manually labeling musical attributes. However, modern deep learning models are data-hungry. As a result, ironically, human agents need to label more data to train a better-performing model. In this section and the next section, we explore training methods that we can choose beyond supervised learning instead of manually labeling more data. 



In a real-world scenario, we have a large-scale music library, but only a few of them are manually labeled. Also, sometimes existing labels have different taxonomies from the target task that we would like to solve. To tackle the issue of a limited amount of labeled data, transfer learning takes advantage of pretrained models that are trained with external data, and semi-/self-supervised approaches utilize abundant unlabeled data. Let's check the motivation, concepts, and implementation of each training scheme.
