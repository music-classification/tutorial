# Dataset Creation

## Creation
  - How to collect; what to consider when collecting dataset
    - Diversity (style, language, era, ..)
    - Out-of-distribution cases
      - Data augmentation
  - Updating dataset from time to time
  - Split
    - Put enough effort into validation/testing sets
      - With enough size of validation and testing sets; to reduce variance
      - Manually verified test set if possible


## Management    
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
