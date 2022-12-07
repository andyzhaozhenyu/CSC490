## Classfication Model

> Our classification model is stored in the kvasir-capsule folder. We use the resNet 152 to figure this classfication problem.



## Data Distribution

All the training sets and validation sets are stored in the data folder. 

- The train folder includes five classes, each class includes one hundred images from the original dataset.

- Train_gan folder includes five classes, each class includes eighty images from the original dataset and twenty images generated by the generator.

- Train original and GAN include five classes, each class includes one hundred images from the original dataset and twenty images generated by the generator.
- Valid folder is the validation set for all three training set, this folder include five classes, each class includes one hundred images from the original dataset.



## Script

The model script is stored in the expriment folder which is called reset_152.py



### Commands

> All commands should be run in the experimental folder
>
> Here is the example:
>
> 

~~~bash
python resnet152_train.py train --data_train_folder ../data/train
~~~

***This command is used to train the model which use the image from the original dataset.***



~~~bash
python resnet152_train.py train --data_train_folder ../data/train_gan
~~~

***This command is used to train tge model which uses 400 images and another 100 images generated by the generator.***



~~~bash
python resnet152_train.py train --data_train_folder ../data/train_gan
~~~

***This command is used to train tge model which uses 500 images and another 100 images generated by the generator.***


### Reference
- https://www.kaggle.com/code/waltermaffy/dcgan-with-keras/notebook#GAN
- https://github.com/eriklindernoren/Keras-GAN/tree/master/dcgan
