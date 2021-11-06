# Transfer Learning

<p align = "center">
<img src = "https://i.imgur.com/V5v19Xs.png" width=550>
</p>
The concept of transfer learning is to learn knowledge from solving one problem (source task) and apply the knowledge to solve other relevant problems (target task) {cite}`torrey2010transfer`. For example, if the model is able to perform instrument identification (source task), the learned knowledge will be useful to solve music genre classification (target task) since instrumentation helps classifying musical genres.

Like this, if there is a relevant source task with more scalable data, we fit our model to solve the source task, first. Then we optimize the pretrained network to solve our downstream target task. In this process, all learned parameters can be optimized during training, or only few last fully-connected layers can be optimized while other parameters to be frozen. For example, researchers pretrained a music tagging model using the Million Song Dataset. Then the model was transferred to solve downstream tasks such as genre classification, emotion recognition, audio event classification, etc {cite}`choi2017transfer`.

Music information can be classified into three categories based on the nature of the metadata elaboration: editorial, cultural, and acoustic. [CITATION] The aforementioned transfer learning experiment takes advantage of music tags in the Million Song Dataset which are mostly related to acoustic information (e.g., genre, instrument). However, those music tags still relies on human effort of labeling. Instead of targeting the acoustic information, we can also design the source task to predict editorial or cultural metadata.

### Pretext using editorial information
Editorial metadata is literally obtained by the editor. Written information of the song, such as artist names, album names, song titles, or released dates, can be included. In most cases, we have editorial information by default. As we can distinguish artists by their acoustic characteristics, a previous work proposed to use artist classification as its pretext task for music representation learning and transferred the learned representation to solve downstream music genre classification tasks. However, there are millions of artists which makes the pretext task to be unrealistic when with large-scale music libraries. To alleviate this issue, following researchers clustered the artists based on their acoustic characteristics, then generated artist group factors by topic modeling.
<p align = "center">
<img src = "https://i.imgur.com/36t82uv.png" width=550>
</p>

### Pretext using cultural information
Cultural information is produced by culture. One well-known approach of processing cultural information is collaborative filtering. Collaborative filtering models and predicts the interests of users from a collection of user-item interactions. As shown in figure below, a huge matrix of user-item interaction can be decomposed into two matrices with lower dimensionality using matrix factorization.
<p align = "center">
<img src = "https://i.imgur.com/MzUyz0t.png" width=550>
</p>
A previous work trained a pretext music representation model by targeting the song embeddings (blue-colored item embeddings in the figure) of collaborative filtering. The learned representation includes rich acoustic information because the song embeddings are derived from diverse user tastes of music. As representation power of collaborative filtering models become stronger with large-scale interactions and explicit user feedbacks, this pretext (source task) is especially beneficial in industries.






