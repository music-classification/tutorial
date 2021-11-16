# Semi-Supervised Learning
In many realistic scenarios, we have limited labeled data and abundant unlabeled data. For example, in the Million Song Dataset (MSD), only 24% of them are labeled with at least one of the top-50 music tags. As a consequence, most the existing MSD tagging research discarded the 76% of the audio included in MSD.

<p align = "center">
<img src = "https://i.imgur.com/l4gUJcC.png" width=300>
</p>
Semi-supervised learning is a machine learning approach that utilizes both (small-scale) labeled data and (large-scale) unlabeled data. In general, semi-supervised models are optimized to minimize two loss functions: a supervised loss, and an unsupervised loss. The ratio of two loss functions is parameterized by λ in the following equation.
<p align = "center">
<img src="https://render.githubusercontent.com/render/math?math=Loss%20%3D%20Loss_%7Bsupervised%7D%20%2B%20%5Clambda%5Ccdot%20Loss_%7Bunsupervised%7D" width=360>
</p>

Semi-supervised learning is a broad concept of a hybrid approach of supervised learning and semi-supervised learning. In detail, many variants have been proposed.


- In self-training, a teacher model is first trained with labeled data. Then the trained teacher model predicts the labels of unlabeled data. A student model is optimized to predict both the labels of labeled data and the pseudo-labels (the prediction by teacher) of unlabeled data {cite}`yalniz2019billion`. 


- Consistency training constrains models to generate noise invariant predictions {cite}`simard2003best`. Unsupervised loss of consistency training is formalized as follow:
<p align = "center">
<img src="https://render.githubusercontent.com/render/math?math=Loss_%7Bunsupervised%7D%20%3D%20D(p(y%7CA(x)%2C%5Ctheta)%2C%20p(y%7CA(x)%2C%5Ctheta))" width=400>
</p> 
<p style="margin-left:40px;">where <i>x</i> is an unlabeled input, <i>A</i> is stochastic data augmentation, and <i>D</i> is a distance metric such as mean squared errors. Note that the data augmentation <i>A</i> is stochastic; hence the two outputs <i>A(x)</i> in the equation are different. By applying the consistency regularization, the model can generalize better as it is exposed to more diverse data points. (This concept is also utilized in contrastive learning {cite}`chen2020simple`, which will be covered in the next section: self-supervised learning.) </p>

<p align = "center">
<img src = "https://imgur.com/Iv6jFtz.png" width=650>
</p>
<p align = "center">
Consistency training
</p>



- Entropy regularization minimizes the entropy of the model's predictions. A straightforward implementation is to directly minimize the entropy of the predictions for unlabeled data {cite}`grandvalet2005semi`. But this can be also achieved in an implicit manner by training with one-hot encoded pseudo-labels {cite}`lee2013pseudo`. In this case, the model first makes a prediction using unlabeled data. The prediction is then modified to be an one-hot vector.

<p align = "center">
<img src = "https://imgur.com/jaNBIf5.png" width=520>
</p>
<p align = "center">
Entropy regularization
</p>



- Some previous works incorporate multiple semi-supervised approaches together {cite}`berthelot2019mixmatch`, {cite}`xie2020self`.


- Other semi-supervised methods includes graph-based approaches {cite}`zhu2003semi` and generative modeling {cite}`kingma2014semi`.

In this section, we explore a specific semi-supervised approach: Noisy student training {cite}`xie2020self`. Noisy student training is a self-training process that constrains the student model to be noise-invariant.

```{warning}
In some papers, SSL stands for semi-supervised learning, but others use the acronym to represent self-supervised learning. To avoid confusion, we do not use abbreviations of semi- and self-supervised learning in this book.
```

### Noisy student training, {cite}`xie2020self`
Noisy student training is a kind of teacher-student learning (self-training). In the typical teacher-student learning, a teacher model is first trained with labeled data in a supervised scheme. Then, a student model is trained to resemble the teacher model by learning to predict the pseudo-labels, the prediction of the teacher model. What makes noisy student training special is to add noise to the input.
<p align = "center">
<img src = "https://i.imgur.com/raPcC8d.png">
</p>
<p align = "center">
Noisy student training
</p>
Here are the detailed steps. Step 1 in the figure above is identical to the supervised learning that has been introduced in previous sections. A teacher model is trained in this step using labeled data (pseudocode line 1-6). In Step 2, the trained teacher model generates pseudo-labels of unlabeled data (pseudocode line 12). Parameters of the teacher model are not updated in this process (dotted lines).

```{tip}
The pseudo-labels can be continuous (soft) vectors or one-hot encoded (hard) vectors. The original paper reported that both soft and hard labels worked, but soft labels worked slightly better for out-of-domain unlabeled data.
```
Now, a student model can be optimized using both labels (pseudocode line 10-11, follow orange lines) and pseudo-labels (pseudocode line 12-15, follow blue lines). In this process, strong data augmentation is applied for unlabeled data (pseudocode line 13) and this makes the student model perform beyond the teacher model. The current state-of-the-art music tagging models (short-chunk ResNet and Music tagging transformer) can be further improved by using the noisy student training.

```{tip}
A trained student model can be another teacher model to iterate the noisy student training process. However, different from the results in image classification, no significant performance gain was observed in music tagging with the MSD. 
```
### Knowledge expansion and distillation
In noisy student training, the size of the student model is not necessarily smaller than the size of the teacher model. As a student model is exposed with larger-scale data with more difficult environments (noise), it can learn more information than the teacher model. One can interpret this method as knowledge expansion {cite}`xie2020self`.

On the other hand, we can also reduce the size of the student model for the sake of model compression. This process is called knowledge distillation and it is suitable for applications with less computing power {cite}`kim2016sequence`.


<p align = "center">
<img src = "https://imgur.com/Y7QpJUp.png" width=520>
</p>
<p align = "center">
MSD tagging performance
</p>

As shown in the table, both Short-chunk ResNet and Music tagging transformer can be improved with data augmentation (DA). Then the models are further improved with noisy student training in both knowledge expansion (KE) and knowledge distillation (KD) manners  {cite}`won2021semi`.


```{tip}
- Tensorflow implementation of noisy student training [[Github](https://github.com/google-research/noisystudent)]
- PyTorch implementation of noisy student training for music tagging [[Github](https://github.com/minzwon/semi-supervised-music-tagging-transformer.git)]
```