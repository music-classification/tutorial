# Under-Explored Problems in Academia

Your choices as a researcher are affected by the circumstance such as     
 
|     \     | Has more freedom in | Has Bias towards   |
| --------- | ------------------- | ------------------ |
| Academia  | Choosing the topics | Publishable topics |
| Industry  | Using resources (time, budget, work force) | Profitable topics  |

As a result, we'll see each entity uses [A] to specialize in [B]. 
And that's great! But, for the same reason, some topics are getting little attention in academia.

## What makes a topic difficult to work on in academia?

- When it feels like it's solved → You can't write a paper about it anymore!
- When it's hard to create a dataset → In this data-driven era, it's a deal-breaker.
- When the problem is too new / there's no dataset for it → No way for sure.
- When it's difficult to evaluate → Don't feed Reviewer 2 a reason for rejection!  

## Let's talk about research topics

Disclaimer - This section is meant to be subjective. Also, as the content is based on the diagnosis of the current research field, it will expire as time goes by.

### Speech/music classification
  **Although**
  - It seems easy
  - Many methods have achieved 100% accuracy in Gtzan speech/music dataset {cite}`tzanetakis1999gtzan`,
  
  **It is an interesting problem because**
  - The model is needed anyway and there's no reliable public model since Gtzan speech/music dataset {cite}`tzanetakis1999gtzan` is pretty small
  - The problem can be defined further such as:  
    - Clip-level decision → short segment-level decision (say, 1 second)
    - More than binary decision - {100% Music -- many levels in between -- 100% speech} + {something neither music or speech} (e.g., {cite}`melendez2019open`, {cite}`hung2021avaspeechsmad`)

### Language classification
  **Although**
  - We were not doing it (nearly at all) because there was no public dataset
  
  **It is an interesting problem because**
  - It's one of the main components in music recommendation systems. 
  - It is popular in Industry - According to publication records, ByteDance {cite}`choi2021listen` / Spotify {cite}`roxbergh2019language` / YouTube {cite}`chandrasekhar2011automatic` have done it. 
  - There is a public dataset now {cite}`santana2020music4all`

### Mood recognition
  **Although**
  - It has lost popularity for these reasons:
    - Tagging tasks sort of overshadowed it 
    - Hard to get large-scale data // while we have to write deep learning papers!
    - Hard to evaluate (fundamentally, completely subjective)
    - Maybe a lot about lyrics, which are also hard to get.
  
  **It is an interesting problem because**
  - Users still want to find some songs by mood.
    - Mood-based playlists/radio stations are popular!
    - Check out [this repo](https://github.com/juansgomez87/datasets_emotion){cite}`GomezCanon2021SPM` for a comprehensive list of mood-related datasets

### Year/decade/era 
  **Although**
  - No one does it explicitly
  - Metadata is supposed to cover this pretty well 
  - MSD includes it and it works pretty okay {cite}`bertin2011million`
  
  **It is an interesting problem because**
  - And yes, there is demand! Metadata is NOT always there or correct
  - Relevant to user's musical preference 

### Audio codec quality (mp3, wav, ..)
  **Although**
  - Music services are supposed to always have high-quality audio
  
  **It is an interesting problem because**
  - There are many fake CD-quality/fake HD audio files
  - Indie music/Directly publishing + sample-based music producing = Increase of audio quality issue

### Hierarchical Classification
  **Although**
  - There are little datasets that have hierarchical taxonomies
  
  **It is an interesting problem because**
  - We can do a better job by learning the knowledge in the hierarchy
  - The users of your model may want it! Even if they did not explicitly want a label hierarchy, it might make more sense to have one based on the labels in demand.
  