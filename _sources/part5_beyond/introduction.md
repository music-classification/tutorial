## Introduction

Supervised learning of deep neural networks has seen many breakthroughs in music information retrieval. Across tasks from music classification to source separation and music recommendation, large neural networks that use a supervised optimization scheme have reached state-of-the-art results by using large, human-annotated datasets.

These large parameterised networks are data-hungry; they require many independent and identically distributed (i.i.d.) data points to generalize well in the task they are trained on. Especially in music, it can be hard to manually annotate, and the annotations often suffer from a single source of truth. There is no single oracle: depending on the context, music theoretical background and cultural background, a song's analysis can yield different results. This was the motivation of the previous chapter, semi-supervised learning. 

In this chapter, we introduce another training strategy that attempts to learn from unlabeled i.i.d. data points: self-supervised learning. We first consider the term pre-training, how it is linked to self-supervised learning and its inherent caveats. Then, we introduce the concept of self-supervised learning and review some key papers in this line of work at this moment of writing (November 2021).

### Pre-training
The weights of neural networks have to be initialized before commencing the training on a target task. This initialization currently does not hold any apriori knowledge on the task at hand. Gaining the weights that belong to a global minimum in our task is not an easy feat currently, especially for smaller, annotated datasets. 

One solution is to pre-train our network on a large annotated dataset to help it steer the optimization scheme in the right direction. This is called pre-training and gaining popularity more and more.

However, classical pre-training have many caveats. Music datasets can be biased towards certain concepts, which will be reflected in the trained model -- and to its application to the target task. The source task and the target task won't be the same, and the negative effective of this difference is hard to predict.

Another challenge is that there are some musical concepts that rarely appear in labeled datasets. This means we would need a huge dataset to have enough representations of those rarity. 


### Self-supervised learning
In self-supervised learning, we obtain a supervisory signal from the data by leveraging its underlying structure. Generally, this can be done on the data itself, or in the space of the data representations. For example, we can predict part of the data from other parts of the data. Or, we can predict the future from events that occurred in the past. In short - we let the model predict the occluded from the visible while we control what to occlude. This has been a very popular approach in language modeling in the past 10 years.

Within the last two years, many different self-supervised methods have been proposed, in particular for vision tasks, and resulted in great improvements over supervised methods when labeled datapoints are scarce. Recently, they even started to perform better than equivalent networks trained in a supervised manner. 


```{note}
**Learning scheme**

It is worth visiting the general learning scheme of this line of work:
1. First, we pre-train a neural network using a self-supervised objective (the pretext task).
2. In order to test the effectiveness of the learned representations, the pre-trained networks' weights are "frozen", and;
3. A linear evaluation on (part of) the supervised dataset is performed to compare against existing benchmarks.

The linear evaluation scheme involves training a supervised linear classifier (a fully-connected layer followed by a softmax) using the representations extracted from the self-supervised network, and (a subset of) the labels associated with the data.
```

### Should I use self-supervised learning?
Self-supervised learning can be beneficial in the following situations:
- The amount of labeled data available is scarce
- You do not want to sacrifice the size and the expressivity of your model.
- You need general-purpose representations that are not less tightly coupled with a single use case.


You should take these considerations into account:
- A pre-trained model will have weights that reflect (and augment!) the biases embedded in a dataset.
- The pretext task used as the self-supervised learning objective is important to analyze and reflect on, as it can yield many assumptions for the downstream task.