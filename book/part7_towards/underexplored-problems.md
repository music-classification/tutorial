## What's under-explored in Academia

A fundamental reason: We don't trust the metadata.

### Speech/music classification
  **Although**
  - It seems easy
  - Many methods have achieved 100% accuracy in gtzan speech/music dataset,
  
  **It is interesting because**
  - The problem can be defined further such as:  
    - Clip-level decision --> short segment-level decision (say, 1 second)
    - More than binary decision - {100% Music -- many levels in between -- 100% speech} + {something neither music or speech} 

### Language classification
  **Although**
  - We were not doing it (nearly at all) because there was no public dataset
  
  **It is interesting because**
  - One of the main classification models in music recommendation system. 
  - As confirmed in papers, ByteDance / Spotify / YouTube have done it. 
  - https://scholar.google.co.kr/citations?view_op=view_citation&hl=en&user=ZrqdSu4AAAA J&sortby=pubdate&citation_for_view=ZrqdSu4AAAAJ:Dip1O2bNi0gC

### Mood recognition
  **Although**
  - It has been a bit abandoned because..
    - Tagging tasks sort of overshadowed it 
    - Hard to get a large-scale data // while we have to write deep learning papers!
    - Hard to evaluate (fundamentally, completely subjective)
    - Maybe a lot about lyrics, which are also hard to get.
  
  **It is interesting because**
  - Users still want to find some songs by mood.
    - Mood-based playlists/radio stations are popular!
  - https://scholar.google.com/scholar?q=music+mood+recognition+review&hl=en&as_sdt=0&as_vis=1&oi=scholart

### Year/decade/era 
  **Although**
  - No one does it explicitly
  - Metadata is supposed to cover this pretty well 
  - MSD includes it and it works pretty okay
  
  **It is interesting because**
  - And yes, there is demand! Metadata is NOT always there
  - Relevant to user's musical preference 

### Audio codec quality (mp3, wav, ..)
  **Although**
  - There's only little work so far
  - Music services are supposed to have only high-quality audio
  
  **It is interesting because**
  - Of course, there are music with low audio quality  
  - Indi music/Directly publishing + sample-based music producing = Increase of audio quality issue
  - There are so many fake CD quality/fake HD audio files
  - https://research.deezer.com/publication/2017/04/05/icassp-hennequin.html
  - Recording/prouction quality/low-quality

## Hierarchical Classification