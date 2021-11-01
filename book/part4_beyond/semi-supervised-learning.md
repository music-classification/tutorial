# Semi-supervised learning
In a realistic scenario, we have few labeled data and abundant unlabeled data. The Million Song Dataset (MSD), for example, although it includes 1 million tracks, only 24% of them are labeled with at least one of the top-50 music tags. As a result, most previous works in MSD tagging only used the 24% of data in a supervised fashion while 76% are being discarded. 
<p align = "center">
<img src = "https://i.imgur.com/l4gUJcC.png" width=300>
</p>
Semi-supervised learning is a machine learning approach that utilizes both small-sized labeled data and large-scale unlabeled data. In this section, we explore a successful semi-supervised approache, Noisy student training, to take advantage of unlabeled data to improve music classification performance.
### Noisy student training
Noisy student training is a teacher-student learning framework that leverages both labeled and unlabeled data. In teacher-student learning, a teacher model is first trained with labeled data in a supervised scheme and then, a student model is trained to mimic the teacher's behavior by optimizing the teacher model's prediction. Noisy student training adds noise in this teacher-student pipeline. Let's check each step of noisy student training in detail.
<p align = "center">
<img src = "https://i.imgur.com/raPcC8d.png">
</p>
Step 1 in the figure above is identical to the supervised learning that have been introduced in previous sections. A teacher model is trained in this step using labeled data (pseudocode line 1-6). In Step 2, the trained teacher model generates pseudo-labels of unlabeled data (pseudocode line 12). Parameters of the teacher model is not updated in this process (dotted lines).

```{tip}
The pseudo-labels can be continuous (soft) vectors or one-hot encoded (hard) vectors. Original paper reported that both soft and hard labels worked but soft labels worked slightly better for out-of-domain unlabeled data.
```
Now a student model can be optimized using labels (pseudocode line 10-11, follow orange lines) and pseudo-labels (pseudocode line 12-15, follow blue lines). In this process, strong data augmentation is applied for unlabeled data (pseudocode line 13) so that the student model performs beyond mimicking the teacher model. Current state-of-the-art music tagging models (short-chunk ResNet and Music tagging transformer) are further improved by using the noisy student training.

```{tip}
A trained student model can be another teacher model to iterate the noisy student training process. However, different from the results in image classification, performance gain was not observed in music tagging with the MSD. 
```
### Knowledge expansion and distillation
In a semi-supervised pipeline, the size of the student model can be bigger than the teacher model. As a student model leverages larger-scale data, it can learn more information with larger parameters. This can be interpreted as knowledge expansion.

On the other hand, we can also reduce the size of the student model. In this case, student model is trained to mimic or outperform the teacher model with fewer parameters. This process is knowledge distillation and the distilled student model is benefitial for applications with less computing power.
