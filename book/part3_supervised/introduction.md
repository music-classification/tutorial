# Introduction
In this section, we will discuss a learning paradigm that uses annotated data to solve tasks: supervised learning. Deep neural networks currently achieve state-of-the-art results in music classification. An input data of either raw waveforms of music, spectrograms, or other audio features or transformations, are fed to a neural networks that is often many layers deep and wide, and can be constructed in many different ways. We call these "deep learning architectures". We will discuss the most successful and commonly used deep learning architectures for solving music classification tasks.

In order to learn from the input data, the neural network also requires a source of truth. We often call this the *ground truth* data, *annotations* or *labels* of the dataset. To reach state-of-the-art performance, deep neural networks often need many different labeled ground truth examples to learn from.

Creating or getting access to large datasets is often an expensive, let alone a hard process. Therefore, we will also observe and gain an understanding of how we can help a model to generalize by way of making variations the input data, in ways that make sense for musical data.

To put everything in perspective, we will give a practical example of implementing a supervised model for the task of music classification on the GTZAN dataset.

In the next section, we will first discuss common deep learning architectures that are used for solving the music classification task by way of supervised learning.