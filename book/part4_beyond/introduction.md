# Beyond Supervision

<p align = "center">
<img src = "https://i.imgur.com/ojSewi1.png" width=600>
</p>
<p align = "center">

</p>


In previous sections, we learned how to facilitate music classification in a data-driven fashion when we have labeled music audio. The main motivation of building music classification models is to save human efforts of manually labeling musical attributes. However, modern deep learning models are data-hungry. As a result, ironically, we end up demanding a large amount of human effort again during dataset creation process. In the next two chapters, we explore training methods beyond supervised learning so that we can alleviate this irony.


In a real-world scenario, we may have a large-scale music library, but only a few of them might have manual labels. Also, sometimes, there is a discrepancy between the taxonomies of the existing training data and the target task. What can we do? As you'll learn from this chapter, one can adopt transfer learning which takes advantage of pretrained models. Semi- or self-supervised approaches can be another solution since they enable us to utilize abundant unlabeled data.
