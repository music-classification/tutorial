# Introduction

@minz

We designed music classification models to save the effort of manually annotating musical attributes. However, modern deep learning models are data-hungry. As a result, ironically, human annotators need to label more data to train a better model.

In this section, we are going to explore training methods that we can choose instead of labeling more data when we do not have enough labeled data. Transfer learning takes advantage of other labeled data and semi-/self-supervised approaches utilize abundant unlabeled data. For each approach, we introduce their motivation, concepts, experimental results, and implementation.