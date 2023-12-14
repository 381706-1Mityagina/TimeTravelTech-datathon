# CV model preparation 

## Dataset
The Wikiart Dataset is a collection of art images obtained from www.wikiart.org.

[Original Dataset](https://www.kaggle.com/datasets/steubk/wikiart/data) contains 80020 unique images from 1119 different artists in 27 styles.

For this work, the original dataset was reduced.

Only 5 artists left:

    "camille pissarro",
    "claude monet",
    "edgar degas",
    "ivan aivazovsky",   
    "vincent van gogh",

Put [train dataset](https://drive.google.com/file/d/1PbmAYTS0EVYwBK9mTTNmvr-ngK85kBxR/view?usp=sharing) and [test dataset](https://drive.google.com/file/d/1O2n5LCYwE88QNBTfl8jBAPqRDZrG8NHn/view?usp=sharing) in "dataset" directory.

## Model

**InceptionV3** model was trained on 25 epochs

Test metrics:

    classes: ('camille pissarro', 'claude monet', 'edgar degas', 'ivan aivazovsky', 'vincent van gogh')
    precision: [0.84, 0.92, 0.86, 0.98, 0.94]
    recall: [0.83, 0.93, 0.86, 0.98, 0.94]
    fscore: [0.84, 0.93, 0.86, 0.98, 0.94]

    mean precision: 0.91
    mean recall: 0.91
    mean fscore: 0.91

Put [inceptionV3](https://drive.google.com/file/d/1PX24dwQyEKfwcCWMAT5EFV_a3gRYgAMC/view?usp=sharing) in "models" directory.
