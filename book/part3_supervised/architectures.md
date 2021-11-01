# Architectures
### Overview
This tutorial mainly covers deep learning approaches for music classification. Before we jump into the details of different deep architectures, let's check some important attributes of music classification models. 

<p align = "center">
<img src = "https://i.imgur.com/he0L4nX.png" width=650>
</p>
<p align = "center">
Music classification model
</p>

As shown in figure above, a music classification model consists of preprocessing, front end, and back end modules. We have already checked preprocessing steps to extract different input representation in previous section. Front end of the music classification model captures local acoustic characteristics such as timbre, pitch, or existance of a certain instrument. Then the back end summarizes the sequence of the extracted features from front end module. Based on the architecture design, sometimes the boundary of front end and back end can be ambiguous.

<p align = "center">
<img src = "https://i.imgur.com/LYeb263.png" width=300>
</p>
<p align = "center">
</p>


Another important attribute of music classification is song-level training vs instance-level training. Although our goal is to make song-level predictions, we can only use short segments of audio during the training. Instance-level training is justified by our intuition – humans can predict music tags within just a few seconds. For example, people would not spend 3 minutes to determine whether a track is rock music. As shown above, when we train the model in an instance-level, we have more training examples and the task becomes more difficult as the model needs to predict only with short audio segments. In consequence, one can expect more robust music tagging models. After training, when model predicts in a song-level, the instance-level predictions are aggregated using max-pooling, average-pooling, or majority vote. 

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
|Music tagging transformer|STFT|15s|2D CNN|Transformer|instance-level|Average|


<!--|FCN|오른쪽정렬|중앙정렬|
|VGG-ish / Short-chunk CNN|오른쪽정렬|중앙정렬|
|Harmonic CNN|오른쪽정렬|중앙정렬|
|MusiCNN|오른쪽정렬|중앙정렬|
|Sample-level CNN|오른쪽정렬|중앙정렬|
|CRNN|오른쪽정렬|중앙정렬|
|Transformer|오른쪽정렬|중앙정렬|
-->
### Fully Convolutional Network (FCN)
Motivated from a huge success of convolutional neural networks (CNN) in the field of computer vision, MIR researchers adopted the successful architectures to solve automatic music tagging problems. Fully convolutional network (FCN) is one of the early deep learning approaches for music tagging which comprises of 4 convolutional layers. Each layer is followed by batch normalization, rectified linear unit (ReLU) non-linearity, and a max-pooling layer. 3x3 convolutional filters are used to capture spectro-temporal acoustic characteristics of an input Mel spectrogram. 
<p align = "center">
<img src = "https://i.imgur.com/P0E0zU8.png" width=500>
</p>
<p align = "center">
Fully convolutional network
</p>
Input length of FCN is 29.1s, yielding 96x1366 Mel spectrogram. Different sizes of strides are used for max-pooling layers ((2, 4), (4, 5), (3, 8), (4, 8)) to increase the size of receptive fields to cover the entire input Mel spectrogram.



### VGG-ish / Short-chunk CNN
VGG-ish model or Short-chunk CNN are very similar to FCN except their inputs. Instead of learning song-level representation, they utilize instance-level (chunk-level) training. 


Since the input length is shorter than FCN's inputs, vgg-ish model and Short-chunk CNN does not need to increase the size of receptive fields with sparse strides. Instead, Short-chunk CNN, for example, consists of 7 convolutional layers with dense max-pooling (2, 2) which fits a 3.69s audio chunk. When its input becomes longer, the model summarizes the features using global max pooling.




### Harmonic CNN
Convolutional modules of Harmonic CNN are identical to Short-chunk CNN but it uses slightly different inputs. Harmonic CNN takes adventage of trainable band-pass filters and harmonically stacked time-frequency representation inputs. In contrast with fixed Mel filterbanks, trainable filters bring more flexibility to the model. And harmonically stacked representation preserves spectro-temporal locality while keeping the harmonic structures through the channel of the input tensor in the first convolutional layer.
<p align = "center">
<img src = "https://i.imgur.com/WRBoq51.png" width=500>
</p>
<p align = "center">
Harmonic CNN
</p>
If the convolution filter (red square) in the most front representation captures the activation around 200Hz, the filter in the second channel captures the activation around 400Hz, and 600Hz and 800Hz for the third and the fourth channel, respectively. Since harmonic structure plays an important role in timbre perception, this spectro-temporal-harmonic representation can by useful for automatic music tagging. Harmonic CNN is trained with 5s audio segments and the instance-level predictions are aggregated using global average pooling.


### MusiCNN
Instead of using 3x3 filters, the authors of MusiCNN proposed to use manually designed filter designs for music tagging. Vertically long filters are designed to capture timbral characteristics that are relevant to instruments, while horizontally long filters are designed to capture temporal energy flux which is related to rhythmic patterns and tempo. 
<p align = "center">
<img src = "https://i.imgur.com/opVUKoE.png" width=500>
</p>
<p align = "center">
MusiCNN
</p>
To enforce the pitch-invariancy, the following max-pooling layer pools the maximum value across the frequency axis. Finally, the sequence of extracted timbral and temporal features are summarized in 1D convolutional layers. MusiCNN is trained with 3s audio segments and the instance-level predictions are aggregated using global average pooling.


### Sample-level CNN
Sample-level CNN and its variant tackle automatic music tagging in an end-to-end manner by directly using raw audio waveform as their inputs. 1x2 or 1x3 1D convolution filters are used to represent music. Each layer consists of 1D convolution, batch normalization, and ReLU non-linearity. Strided convolution is used to increase the size of of receptive field. 
<p align = "center">
<img src = "https://i.imgur.com/Q7z4vmv.png" width=500>
</p>
<p align = "center">
Sample-level CNN
</p>
In this approach, preprocessing steps (e.g., short-time Fourier transform) are not required. Instead, the model is deeper than spectrogram-based models to model the counterpart of Mel filterbanks. A figure below shows spectrum of learned convolution filters which are sorted by the frequency of the peak magnitude. The center frequency linearly increases in low frequency but it goes non-linearly steeper in high frequency. This trend is more evident in deeper layers and this characteristic can be found in Mel filterbanks. 
<p align = "center">
<img src = "https://i.imgur.com/YUIl1PH.png" width=500>
</p>
<p align = "center">
Spectrum of the filters in the sample-level convolution layers (x-axis: index of the filter, y-axis: frequency).
</p>
Sample-level CNN and its variant are trained with 3.69s audio segments and the instance-level predictions are aggregated using global average pooling.


### Convolutional Recurrent Neural Network (CRNN)
Different from previously introduced instance-level models, convolutional recurrent neural network (CRNN) is designed to handle the long sequence of multiple instances. A CRNN can be described as a combinatino of CNN and RNN. The CNN front end captures local acoustic characteristics (instance-level) and the RNN back end summarizes the sequence of instance-level features. 
<p align = "center">
<img src = "https://i.imgur.com/Am4drg2.png" width=200>
</p>
<p align = "center">
Convolutional recurrent neural network
</p>
Four convolutional layers with 3x3 filters are used in CNN front end and two-layer RNN with gated recurrent units (GRU) are used in back end. CRNN uses 29.1s audio inputs and do not need feature aggregation step since RNN summarizes the sequence.


### Music tagging transformer
The motivation of convolutional neural network with self-attention (CNNSA) and Music tagging transformer are identical to CRNN's motivation. Front end captures local acoustic characteristics and back end summarizes the sequence. In a field of natural language processing, Transformer has shown its suitability in long sequence modeling by stacking self-attention layers. Both CNNSA and Music tagging transformer use Transformer back end to summarize instance-level features. 
<p align = "center">
<img src = "https://i.imgur.com/DsGDE5U.png" width=250>
</p>
<p align = "center">
Music tagging transformer
</p>
CNNSA uses CNN front end of MusiCNN and Music tagging transformer uses CNN front end of Short-chunk ResNet. The input length can be varied from 5s to 30s.
<p align = "center">
<img src = "https://i.imgur.com/kTJ0kpd.png" width=500>
</p>
<p align = "center">
Tag-wise contribution heatmap of transformer
</p>
Another advantage of using Transformer back end is interpretability. Since attention mechanism is implemented with fully-connected layers, model's behavior is very interpretable. Examples above show concatenated Mel spectrograms and their contribution to the tag prediction. The heatmap successfully highlights relevant part of audio for each tag.



### Which model should we use?
After the exploration of different architectures, the first natural question will be: So, what is the best model to choose? In a previous work, experimental results in three datasets (MagnaTagATune, Million Song Data, MTG-Jamendo) are reported as follow.
<p align = "center">
<img src = "https://i.imgur.com/5rdBGjX.png" width=500>
</p>
<p align = "center">
Comparison of music tagging models
</p>


```{note}
Summary:
- For the best performance, use Music tagging transformer.
- VGG-ish and Short-chunk CNN are simple but powerful choices.
- When your training dataset is small, it is beneficial to reduce the search space by using MusiCNN or Harmonic CNN.
- Sample-level CNN becomes more powerful as the size of dataset grows. But spectrogram-based models are more powerful yet.
```

```{tip}
- PyTorch implementation of introduced models are available online [[Github](https://github.com/minzwon/sota-music-tagging-models.git)]
- You can try online demo of pretrained models [[Replicate.ai](https://replicate.ai/minzwon/sota-music-tagging-models)]
```


