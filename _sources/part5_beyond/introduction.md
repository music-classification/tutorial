## Introduction

Supervised learning of deep neural networks has seen many breakthroughs in music information retrieval. Across tasks like music classification, to source seperation or music recommendation, large neural networks that use a supervised optimization scheme have reached state-of-the-art results by way of using large, human-annotated datasets.

These large parameterised networks are data-hungry; they require many independent and identically distributed (i.i.d.) datapoints to generalize well in the task they are trained on. Especially in music, it can be hard to manually annotate, and the annotations often suffer from a single sources of truth. There is no single oracle: depending on the context, music theoretical background and cultural background, a song's analysis can yield different results. In this chapter we observe a machine learning method that attempts to learn from unlabeled i.i.d. datapoints: self-supervised learning. We will first consider the term pre-training, how it is linked to self-supervised learning and its inherent caveats. Then, we will introduce the concept of self-supervised learning and review some key papers in this line of work at this moment of writing (October 2021).
## Pre-training
The weights of neural networks have to be initialized before commencing the training on a target task. This initialization currently does not hold any apriori knowledge on the task at hand. To gain the weights that belong to a global minimum in our task is not an easy feat currently, especially for smaller, annotated datasets. However, we can choose to pre-train our network on a large annotated dataset to inject some information into the weights of our network, to help it steer our optimization scheme in the direction of our global minimum. This increasingly popular way to learn embeddings from large datasets of audio, and use these to train more shallow classifiers on smaller datasets, is referred to as pre-training.

However, pre-training also yields many caveats that have to be considered. Music datasets can be very biased towards certain concepts: they are represented more often and this will be picked up by our machine learning models. Even though we cannot clearly observe the bias by inspecting the weights of a trained network, it is now embedded in the pre-trained weights and will transfer downstream.

Also, the weights from a network trained on a different audio task often do not transfer well. When we use the pre-trained weights of a network that is trained on speech signals, one could make a clear argument why these weights are not helpful when our downstream task is to classify music.

Another challenge to consider, is that rare musical concepts (obviously) appear less in labeled datasets. In order to scale to these rarer concepts, we need a lot more data to account for this. This is generally known as the "long tail problem", which is named after the data distribution we obtain when analyzing concepts in a dataset.


## Self-supervised learning
In self-supervised learning, we obtain a supervisory signal from the data by leveraging its underlying structure. Generally, this can be done on the data itself, or in the space of the data representations. For example, we can predict part of the data from other parts of the data. Or, we can predict the future from events that occured in the past. In short - we predict the occluded from the visible, and we can control what events to occlude. Perhaps one task already sounds familiar and almost analogous: language modeling.

Within the last two years, many different self-supervised methods have been proposed, in particular for vision tasks, and resulted in great improvements over supervised methods when labeled datapoints are scarce. Recently, they even started to perform better than equivalent networks trained in a supervised manner. 


```{note}
**Learning scheme**

It is worth visiting the general learning scheme of this line of work:
1. First, we pre-train a neural network using a self-supervised objective (the pretext task).
2. In order to test the effectiveness of the learned representations, the pre-trained networks' weights are "frozen", and;
3. A linear evaluation on (part of) the supervised dataset is performed to compare against existing benchmarks.

The linear evaluation scheme involves training a supervised linear classifier (a fully-connected layer followed by a softmax) using the representations extracted from the self-supervised network, and (a subset of) the labels associated with the data.
```

## Should I use self-supervised learning?
Self-supervised learning can be beneficial in the following situations:
- The amount of labeled data available is scarce, and you do not want to sacrifice the size, and the expressivity, of your model.
- Create more general-purpose representations that are not tightly coupled with a single use case, and can be used for multiple downstream tasks.
- Improve the robustness of your network.


You should take these considerations into account:
- A pre-trained model will have weights that reflect (and augment!) the biases embedded in a dataset.
- The pretext task used as the self-supervised learning objective is important to analyze and reflect on, as it can yield many assumptions for the downstream task.