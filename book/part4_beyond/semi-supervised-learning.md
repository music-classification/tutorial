# Semi-Supervised Learning
In a realistic scenario, we have few labeled data and abundant unlabeled data. For example, the Million Song Dataset (MSD), although it includes 1 million tracks, only 24% of them are labeled with at least one of the top-50 music tags. As a result, most previous MSD tagging research only used 24% of data in a supervised fashion, while 76% were discarded. 

<p align = "center">
<img src = "https://i.imgur.com/l4gUJcC.png" width=300>
</p>
Semi-supervised learning is a machine learning approach that utilizes both small-sized labeled data and large-scale unlabeled data. Many techniques have been introduced to involve unlabeled data in the training pipeline so that the model can generalize better. The semi-supervised models are optimized to minimize two loss functions: a supervised loss, and an unsupervised loss. The ratio of two loss functions can be parameterized by a hyperparameter λ.
<p align = "center">
<img src="https://render.githubusercontent.com/render/math?math=Loss%20%3D%20Loss_%7Bsupervised%7D%20%2B%20%5Clambda%5Ccdot%20Loss_%7Bunsupervised%7D" width=360>
</p>
As semi-supervised learning is a broad concept that hybridizes supervised learning and semi-supervised learning, there are many different approaches to facilitate it.

- In self-training, a teacher model is first trained with labeled data. Then the trained teacher model predicts the labels of unlabeled data. A student model is optimized to predict the labels of labeled data and the pseudo-labels (teacher's predictions) of unlabeled data [CITATION]. 


- Consistency training constrains models to generate noise invariant predictions {cite}`simard2003best`. Unsupervised loss of consistency training is formalized as:
<p align = "center">
<img src="https://render.githubusercontent.com/render/math?math=Loss_%7Bunsupervised%7D%20%3D%20D(p(y%7CA(x)%2C%5Ctheta)%2C%20p(y%7CA(x)%2C%5Ctheta))" width=400>
</p> 
<p style="margin-left:40px;">where <i>x</i> is an unlabeled input, <i>A</i> is stochastic data augmentation, and <i>D</i> is a distance metric such as mean squared errors. Note that the data augmentation <i>A</i> is stochastic; hence the two outputs <i>A(x)</i> in the equation are different. By applying the consistency regularization, the model can generalize better. This concept is also utilized in contrastive learning, which will be covered in the next section: self-supervised learning. </p>

- Entropy regularization minimizes the entropy of the model's predictions {cite}`grandvalet2005semi`. It can be performed by directly minimizing the entropy of predictions. But also, this can be done by targeting one-hot encoded pseudo-labels. The model makes predictions using unlabeled data. Then the class with the maximum probability is picked up to represent the data (one-hot encoded pseudo-label). This process implicitly performs entropy regularization.


- Some previous works incorporate multiple semi-supervised approaches together.


- Also, there are more semi-supervised methods, including graph-based approaches and generative modeling.

In this section, we explore a successful semi-supervised approach: Noisy student training. Noisy student training is a self-training process that constrains the student model to gain noise invariant characteristics. Let's check how we can take advantage of unlabeled data to improve music classification performance.

```{warning}
In some papers, SSL stands for semi-supervised learning, but others use the acronym to represent self-supervised learning. To avoid confusion, we do not use abbreviations of semi- and self-supervised learning in this book.
```

### Noisy student training, {cite}`xie2020self`
Noisy student training is a teacher-student framework (self-training) that leverages both labeled and unlabeled data. In teacher-student learning, a teacher model is first trained with labeled data in a supervised scheme. Then, a student model is trained to mimic the teacher's behavior by optimizing the teacher model's predictions (pseudo-labels). Noisy student training adds noise to this teacher-student pipeline.
<p align = "center">
<img src = "https://i.imgur.com/raPcC8d.png">
</p>
Here are detailed steps. Step 1 in the figure above is identical to the supervised learning that has been introduced in previous sections. A teacher model is trained in this step using labeled data (pseudocode line 1-6). In Step 2, the trained teacher model generates pseudo-labels of unlabeled data (pseudocode line 12). Parameters of the teacher model are not updated in this process (dotted lines).

```{tip}
The pseudo-labels can be continuous (soft) vectors or one-hot encoded (hard) vectors. The original paper reported that both soft and hard labels worked, but soft labels worked slightly better for out-of-domain unlabeled data.
```
Now a student model can be optimized using both labels (pseudocode line 10-11, follow orange lines) and pseudo-labels (pseudocode line 12-15, follow blue lines). In this process, strong data augmentation is applied for unlabeled data (pseudocode line 13) so that the student model performs beyond mimicking the teacher model. Current state-of-the-art music tagging models (short-chunk ResNet and Music tagging transformer) are further improved by using the noisy student training.

```{tip}
A trained student model can be another teacher model to iterate the noisy student training process. However, different from the results in image classification, no significant performance gain was observed in music tagging with the MSD. 
```
### Knowledge expansion and distillation
In noisy student training, the size of the student model is not smaller than the size of the teacher model. As a student model leverages larger-scale data with more difficult environments (noise), it can learn more information than the teacher model. One can interpret this method as knowledge expansion {cite}`xie2020self`.

On the other hand, we can also reduce the size of the student model. In this case, the student model is trained to mimic or outperform the teacher model with fewer parameters, hence faster than the teacher model. This process is knowledge distillation, and the distilled student model is beneficial for applications with less computing power {cite}`kim2016sequence`.

```{tip}
- Tensorflow implementation of noisy student training [[Github](https://github.com/google-research/noisystudent)]
- PyTorch implementation of noisy student training for music tagging [[Github](https://github.com/minzwon/semi-supervised-music-tagging-transformer.git)]
```