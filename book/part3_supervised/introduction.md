## Introduction
In this chapter, we discuss a learning paradigm, supervised learning, which fully relies on ground truth to solve music classification tasks. 


The state-of-the-art in music classification has been improved with various deep neural network architectures that are based on different goals and assumptions. We discuss the most successful and commonly used architectures in music classification.

We need some information to train a neural network model. We call this *ground truth*, *annotations*, or *labels* of the dataset. To reach state-of-the-art performance, deep neural networks often need many different labeled ground truth examples. 

Creating a large dataset is costly and tricky. As a solution, in this chapter, we introduce data augmentation -- a technique we use to increase the size of dataset. Data augmentation is deeply domain specific, and we discuss the methods for musical data.

Along this chapter, we implement a practical example of a supervised music classification model using GTZAN dataset. This will help the readers to put everything in perspective, 
