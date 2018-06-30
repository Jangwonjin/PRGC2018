# Pattern Recognition Grand Challenge 2018 
The goal of Pattern Recognition Grand Challenge (PRGC) 2018 is to predict a subject's emotional state from the fMRI image of his or her brain. In the PINES dataset below, 183 subjects' fMRI images and emotional states are provided. Build a model to predict a subject's emotional state (Y) from an fMRI image (X).

Dataset
----------------------------------------------------------
### 1. *fMRI data*
<https://neurovault.org/collections/503/>

This dataset contains single trial responses to 30 images from the International Affective Picture Set from 182 subjects. These data were used to train the Picture Induced Negative Emotion Signature described in Chang et al., 2015.

The details of the experiment can be seen in Gianaros et al., 2014 (doi:10.1016/j.biopsych.2013.10.012).

- Negative photographs (Pictures: 2053, 3051, 3102, 3120, 3350, 3500, 3550, 6831, 9040, 9050, 9252, 9300, 9400, 9810, 9921) depicted bodily illness and injury (10 photographs), acts of aggression (2 photographs), members of hate groups (1 photograph), transportation accidents (1 photograph) and human waste (1 photograph).

- Neutral photographs (Pictures: 5720, 5800, 7000, 7006, 7010, 7040, 7060, 7090, 7100,7130, 7150, 7217, 7490, 7500, 9210) depicted inanimate objects (10 photographs) or neutral scenes (5 photographs).

### 2. *Emotion level data*
- <https://s3-eu-west-1.amazonaws.com/pstorage-plos-3567654/2129473/S1_Data.csv>

- Subject's reponses are stored in column Rating.

### 3. *Data visualization*
![dataset](/img/class_img.png)

Results
========================================================================
Ver1.
---------------------------------------------------------------------
### Multiclass
| x | y | z |
| :----------: | :----------: | :----------: |
| ![multi_x](/img/ver1/result_multi_x.png) | ![multi_y](/img/ver1/result_multi_y.png) | ![multi_z](/img/ver1/result_multi_z.png) |

### Randomforest
| x | y | z |
| :----------: | :----------: | :----------: |
| ![random_x](/img/ver1/result_random_x.png) | ![random_y](/img/ver1/result_random_y.png) | ![random_z](/img/ver1/result_random_z.png) |

### SGDClassifier
| x | y | z |
| :----------: | :----------: | :----------: |
| ![sgd_x](/img/ver1/result_sgd_x.png) | ![sgd_y](/img/ver1/result_sgd_y.png) | ![sgd_z](/img/ver1/result_sgd_z.png) |

Ver2.
---------------------------------------------------------------------
### *XYZ*
| **SGDClassifier** | **KNN** |
| :----------: | :----------: |
| ![sgd](/img/ver2/xyz/bbox_SGD.png) | ![KNN](/img/ver2/xyz/bbox_knn.png) |
| **Multiclass** | **Randomforest** |
| ![multi](/img/ver2/xyz/bbox_multiclass.png) | ![random](/img/ver2/xyz/bbox_randomforest.png) |

### *YZX*
| **SGDClassifier** | **KNN** |
| :----------: | :----------: |
| ![sgd](/img/ver2/yzx/bbox_sgd.png) | ![KNN](/img/ver2/yzx/bbox_knn.png) |
| **Multiclass** | **Randomforest** |
| ![multi](/img/ver2/yzx/bbox_multi.png) | ![random](/img/ver2/yzx/bbox_random.png) |

I achievd 54% accuracy. 

Reference
--------------------------------------------------------------------------
[A Sensitive and Specific Neural Signature for Picture-Induced Negative Affect](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002180)

