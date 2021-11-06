# Architectures
### Overview
This tutorial mainly covers deep learning approaches for music classification. Before we jump into the details of different deep architectures, let's check some essential attributes of music classification. 

<p align = "center">
<img src = "https://i.imgur.com/he0L4nX.png" width=650>
</p>
<p align = "center">
Music classification model
</p>

As shown in the figure above, a music classification model consists of preprocessing, front end, and back end modules. We have already checked the preprocessing steps to extract different input representations in the previous section. The front end of the music classification model captures local acoustic characteristics such as timbre, pitch, or existence of a particular instrument. Then the back end summarizes the sequence of the extracted features from the front end module. Based on the architecture design, sometimes, the front and back end boundary can be ambiguous.

<p align = "center">
<img src = "https://i.imgur.com/LYeb263.png" width=450>
</p>
<p align = "center">
</p>


Another critical attribute of music classification is song-level training vs instance-level training. Although our goal is to make song-level predictions, music classification models often use only short audio segments during the training (instance-level training). Instance-level training is justified by the intuition – humans can predict music tags within just a few seconds. For example, people would not spend 3 minutes to determine whether a track is rock music. As shown in the figure above, when we train the model with an instance level, we have more training examples, and the task becomes more difficult as the model needs to predict only with short audio segments. In consequence, one can expect more robust music tagging models. After training, when the model predicts in a song-level, the instance-level predictions are aggregated using max-pooling, average-pooling, or majority vote. 

We summarize important attributes of music classification models as follow:

<style>
td {
  font-size: 12px
}
</style>
|Model|Preprocessing|Input length|Front end|Back end|Training|Aggregation|
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
|FCN|STFT|29.1s|2D CNN|.|song-level|.|
|VGG-ish / Short-chunk CNN|STFT|3.96s|2D CNN|Global max pooling|instance-level|Average|
|Harmonic CNN|STFT|5s|2D CNN|Global max pooling|instance-level|Average|
|MusiCNN|STFT|3s|2D CNN|1D CNN|instance-level|Average|
|Sample-level CNN|.|3s|1D CNN|1D CNN|instance-level|Average|
|CRNN|STFT|29.1s|2D CNN|RNN|song-level|.|
|Music tagging transformer|STFT|5s-30s|2D CNN|Transformer|instance-level|Average|


<!--|FCN|오른쪽정렬|중앙정렬|
|VGG-ish / Short-chunk CNN|오른쪽정렬|중앙정렬|
|Harmonic CNN|오른쪽정렬|중앙정렬|
|MusiCNN|오른쪽정렬|중앙정렬|
|Sample-level CNN|오른쪽정렬|중앙정렬|
|CRNN|오른쪽정렬|중앙정렬|
|Transformer|오른쪽정렬|중앙정렬|
-->
### Fully Convolutional Network (FCN), {cite}`choi2016automatic`
Motivated by the huge success of convolutional neural networks (CNN) in computer vision, MIR researchers adopted the successful architectures to solve automatic music tagging problems. The fully convolutional network (FCN) is one of the early deep learning approaches for music tagging, which comprises four convolutional layers. Each layer is followed by batch normalization, rectified linear unit (ReLU) non-linearity, and a max-pooling layer. 3x3 convolutional filters are used to capture spectro-temporal acoustic characteristics of an input Mel spectrogram. 
<p align = "center">
<img src = "https://i.imgur.com/P0E0zU8.png" width=650>
</p>
<p align = "center">
Fully convolutional network
</p>
The input length of FCN is 29.1s, yielding a 96x1366 Mel spectrogram. Different sizes of strides are used for max-pooling layers ((2, 4), (4, 5), (3, 8), (4, 8)) to increase the size of receptive fields to cover the entire input Mel spectrogram.



### VGG-ish / Short-chunk CNN, {cite}`won2020evaluation`
VGG-ish model and Short-chunk CNN are very similar to FCN except for their inputs. Instead of learning song-level representation, they utilize instance-level (chunk-level) training. 


Since the input length is shorter than FCN's inputs, the VGG-ish model and Short-chunk CNN does not need to increase the size of receptive fields with sparse strides. Instead, Short-chunk CNN, for example, consists of 7 convolutional layers with dense max-pooling (2, 2), which fits a 3.69s audio chunk. When its input becomes longer, the model summarizes the features using global max pooling.



### Harmonic CNN, {cite}`won2019automatic`
Convolutional modules of Harmonic CNN are identical to Short-chunk CNN, but it uses slightly different inputs. Harmonic CNN takes advantage of trainable band-pass filters and harmonically stacked time-frequency representation inputs. In contrast with fixed Mel filterbanks, trainable filters bring more flexibility to the model. And harmonically stacked representation preserves spectro-temporal locality while keeping the harmonic structures through the channel of the input tensor in the first convolutional layer.
<p align = "center">
<img src = "https://i.imgur.com/WRBoq51.png" width=650>
</p>
<p align = "center">
Harmonic CNN
</p>
If the convolution filter (red square) in the most front representation captures the activation around 200Hz, the filter in the second channel captures the activation around 400Hz, and 600Hz and 800Hz for the third and the fourth channel, respectively. Since harmonic structure plays an important role in timbre perception, this spectro-temporal-harmonic representation can be helpful in automatic music tagging. Harmonic CNN is trained with 5s audio segments, and the instance-level predictions are aggregated using global average pooling.


### MusiCNN, {cite}`pons2019musicnn`
Instead of using 3x3 filters, the authors of MusiCNN proposed to use manually designed filter shapes for music tagging. Vertically long filters are designed to capture timbral characteristics that are relevant to instruments, while horizontally long filters are designed to capture temporal energy flux that is related to rhythmic patterns and tempo. 
<p align = "center">
<img src = "https://i.imgur.com/opVUKoE.png" width=650>
</p>
<p align = "center">
MusiCNN
</p>
To enforce the pitch-invariancy, the following max-pooling layer pools the maximum value across the frequency axis. Finally, the sequence of extracted timbral and temporal features are summarized in 1D convolutional layers. MusiCNN is trained with 3s audio segments, and the instance-level predictions are aggregated using global average pooling.


### Sample-level CNN, {cite}`lee2017sample`
Sample-level CNN and its variant tackle automatic music tagging in an end-to-end manner by directly using raw audio waveform as their inputs. 1x2 or 1x3 1D convolution filters are used to represent music. Each layer consists of 1D convolution, batch normalization, and ReLU non-linearity. Strided convolution is used to increase the size of the receptive field. 
<p align = "center">
<img src = "https://i.imgur.com/Q7z4vmv.png" width=650>
</p>
<p align = "center">
Sample-level CNN
</p>
In this approach, preprocessing steps (e.g., short-time Fourier transform) are not required. Instead, the model is deeper than spectrogram-based ones to model the counterpart of Mel filterbanks. The figure below shows the spectrum of learned convolution filters sorted by the frequency of the peak magnitude. The center frequency linearly increases in low frequency, but it goes non-linearly steeper in high frequency. This trend is more evident in deeper layers, and this characteristic can be found in Mel filterbanks. 
<p align = "center">
<img src = "https://i.imgur.com/YUIl1PH.png" width=650>
</p>
<p align = "center">
Spectrum of the filters in the sample-level convolution layers (x-axis: index of the filter, y-axis: frequency).
</p>
Sample-level CNN and its variant are trained with 3.69s audio segments, and the instance-level predictions are aggregated using global average pooling.


### Convolutional Recurrent Neural Network (CRNN), {cite}`choi2017convolutional`
Different from previously introduced instance-level models, the convolutional recurrent neural network (CRNN) is designed to represent music as a long sequence of multiple instances. A CRNN can be described as a combination of CNN and RNN. The CNN front end captures local acoustic characteristics (instance-level), and the RNN back end summarizes the sequence of instance-level features. 
<p align = "center">
<img src = "https://i.imgur.com/Am4drg2.png" width=350>
</p>
<p align = "center">
Convolutional recurrent neural network
</p>
Four convolutional layers with 3x3 filters are used in the CNN front end, and two-layer RNN with gated recurrent units (GRU) are used in the back end. CRNN uses 29.1s audio inputs and does not need a feature aggregation step since RNN summarizes the sequence.


### Music tagging transformer, {cite}`won2021semi`
The motivation of the convolutional neural network with self-attention (CNNSA) and Music tagging transformer is identical to CRNN's one. The front end captures local acoustic characteristics, and the back end summarizes the sequence. In the field of natural language processing, Transformer has shown its suitability in long sequence modeling by stacking self-attention layers. Both CNNSA and Music tagging transformer use the CNN front end, and the Transformer back end summarizes the instance-level features. 
<p align = "center">
<img src = "https://i.imgur.com/DsGDE5U.png" width=450>
</p>
<p align = "center">
Music tagging transformer
</p>
CNNSA uses the CNN front end of MusiCNN, and Music tagging transformer uses the CNN front end of Short-chunk ResNet. The input length can be varied from 5s to 30s.
<p align = "center">
<img src = "https://i.imgur.com/kTJ0kpd.png" width=650>
</p>
<p align = "center">
Tag-wise contribution heatmap of transformer
</p>
Another advantage of using a Transformer back end is interpretability. Since the attention mechanism is implemented with fully-connected layers, the model's behavior is very interpretable. The examples above show concatenated Mel spectrograms and their contribution to the tag predictions. The heatmap successfully highlights relevant parts of the audio for each tag.



### Which model should we use?
After exploring different architectures, the first natural question will be: So, what is the best model to choose? In previous work, experimental results in three datasets (MagnaTagATune, Million Song Data, MTG-Jamendo) are reported as follows.
<p align = "center">
<img src = "https://i.imgur.com/5rdBGjX.png" width=650>
</p>
<p align = "center">
Comparison of music tagging models
</p>


```{note}
Summary:
- For the best performance, use the Music tagging transformer.
- VGG-ish and Short-chunk CNN are simple but powerful choices.
When your training dataset is small, reducing the search space by using MusiCNN or Harmonic CNN is beneficial.
- Sample-level CNN becomes more powerful as the size of the dataset grows. But spectrogram-based models are more powerful yet.
```

```{tip}
- PyTorch implementation of introduced models are available online [[Github](https://github.com/minzwon/sota-music-tagging-models.git)]
- You can try an online demo of pretrained models [[Replicate.ai](https://replicate.ai/minzwon/sota-music-tagging-models)]
```


