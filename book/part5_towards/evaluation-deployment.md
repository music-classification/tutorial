# Evaluation and Deployment

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