# MLOps

Academia and industry have different goals and focuses for good reasons. But it's useful to learn what are happening on the other side.   

---

![](_img_mlops-continuous-delivery-and-automation-pipelines-in-machine-learning-1-elements-of-ml.png)

This famous image from [Machine Learning: The High Interest Credit Card of Technical Debt, {cite}`43146`](https://research.google/pubs/pub43146/)
shows other modules besides ML Code in a ML system. There are so many of them that people even coined a new word, "MLOps". And a lot of topics in MLOps are completely out of the scope of academia. Again, there are good reasons for people in industry and academia have different scopes. But, it would be useful to know what are happening on the other side.   

## Dataset Creation
  - How to collect; what to consider when collecting dataset
    - Diversity (style, language, era, ..)
    - Out-of-distribution cases
      - Data augmentation
  - Updating dataset from time to time
  - Split
    - Put enough effort into validation/testing sets
      - With enough size of validation and testing sets; to reduce variance
      - Manually verified test set if possible


## Dataset Management    
  - Incremental datasets
    - How to label them?
    - How to preprocess them?
    - How to version them?
  - Expiration of music samples
    - In general, we'll want to add recent music samples from time to time.
  - Expiration of the music labels
    - Languages - well, probably not
    - Genre - we'll want a more up-to-date samples!
      - Emerging genres - we need to add more genres!
    - NLP models
      - Should be updated somehow frequently
    -       

## Evaluation is more than a single number
### Choice of metric(**s**)
- In paper, conciseness is a virtue!
  - For the sake of comparison, when writing paper, we prefer a single number such as AUC-ROC or PR-AUC.
- In industry, you always need to evaluate your model per tag because some tags might be more important than others.

### Optimize for your target metric

- High precision? or High recall?
  - Know your application!
- Thresholding or not?
  - Even after using softmax, sometimes we need thresholding
  - Target precision/recall would (and should) exist and be based on the application
    - Popular demand: high-precision / high-recall (rather than high-f1)
  - Confidence estimation can be done in a various way. 
    - Even with softmax, if the target is high precision, simply thresholding with value works. 


## Deployment
  - Reproducability of..
    - Software/your code!
    - Model 
    - Data processing pipeline
      - Decoding mp3, or if it's mp3 vs wav input, resampling algorithm, how to downmix, ..
        
  - Is your model actually useful for the whole catalog you have?
    - E.g., if album cover images are used in the model, are they going to be available for all the music tracks?
  -   


## Serving
- It's for ML Engineers! But at least we'd want to know things such as
  - The platform (Mobile? Server?)
  - Expected latency and throughput
- (to add more) 

### After segment-level prediction: Aggregation!

- segment -> prediction: how to?
  - We often ignore it when using public datasets (e.g., MSD) as they come with 30-second preview only 
- Simple Methods:
  - Average of model outputs
  - Average of model predictions (aka Major voting; when single-classification)
  - They work pretty okay; but there's nothing we can do for the failure cases. 
- Maybe -- to go further: 
  - We can train another model for the aggregation job
  - We can train an end-to-end model
    - Put (almost) a whole track into a batch and do the work! 
    - `MIR Transformer` is a shorter version of this.
    