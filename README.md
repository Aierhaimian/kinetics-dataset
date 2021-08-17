# Kinetics datasets

Kinetics is a collection of large-scale, high-quality datasets of URL links of up to 650,000 video clips that cover 400/600/700 human action classes, depending on the dataset version. The videos include human-object interactions such as playing instruments, as well as human-human interactions such as shaking hands and hugging. Each action class has at least 400/600/700 video clips. Each clip is human annotated with a single action class and lasts around 10 seconds.

The Kinetics project publications can be found here: https://deepmind.com/research/open-source/kinetics.

# Updates
17th of August 2021 -- forkd from [cvdfoundation/kinetics-dataset](https://github.com/cvdfoundation/kinetics-dataset). The dataset directory structure has been reorganized, download.sh and extract.sh have been rewritten, and organize.py has been added to classify the video in its category directory. Therefore, the dataset can be directly used for training, testing and inference.

4th of August 2021 -- replaced corrupted videos in the kinetics-700-2020 test set (these were typically shorter than 9s as well). There are still 5% of the videos in the test set that are shorter than 9s, but genuinely so (e.g. because they are like that in youtube). 

# Download Videos


CVDF currently hosts the videos in the Kinetics-400 and Kinetics-700-2020 datasets.

### Dataset directory

```
.
├── README.md
├── download.sh
├── extract.sh
├── kinetics_400
│   ├── annotations
│   │   ├── test.csv
│   │   ├── train.csv
│   │   └── val.csv
│   ├── readme.md
│   ├── test
│   ├── train
│   └── val
├── kinetics_600
│   ├── annotations
│   │   ├── test.csv
│   │   ├── train.txt
│   │   └── val.txt
│   ├── readme.md
│   ├── test
│   ├── train
│   └── val
├── kinetics_700
│   ├── K700_2020_readme.txt
│   ├── annotations
│   │   ├── test.csv
│   │   ├── train.csv
│   │   └── val.csv
│   ├── test
│   ├── train
│   └── val
├── link_path
│   ├── k400_test_path.txt
│   ├── k400_train_path.txt
│   ├── k400_val_path.txt
│   ├── k600_test_path.txt
│   ├── k600_train_path.txt
│   ├── k600_val_path.txt
│   ├── k700_test_path.txt
│   ├── k700_train_path.txt
│   └── k700_val_path.txt
└── organize.py

```

It is easy to classify the video in its category directory, by:

```
python3 organize.py --dataset=kinetics_400 --types=train
```
Then, the video will be classified with its label in "kinetics_400/train/label_name" folder(category_name, e.g. abseiling).

### Kinetics-400

The train/val/test splits are subdivided into many files. The lists of links to video files can be found in "link_path" directory or here:

https://s3.amazonaws.com/kinetics/400/train/k400_train_path.txt

https://s3.amazonaws.com/kinetics/400/val/k400_val_path.txt

https://s3.amazonaws.com/kinetics/400/test/k400_test_path.txt

It is easy to obtain a specific split (e.g. train), by:
```
bash download.sh ./link_path/k400_train_path.txt
```
Then, extract `*.tar.gz` files by:
```
bash extract.sh ./link_path/k400_train_path.txt
```

The links/annotations can be found the annotations subfolders or here:

https://s3.amazonaws.com/kinetics/400/annotations/train.csv

https://s3.amazonaws.com/kinetics/400/annotations/val.csv

https://s3.amazonaws.com/kinetics/400/annotations/test.csv

A readme file can be found in:

http://s3.amazonaws.com/kinetics/400/readme.md


### Kinetics-600

The train/val/test splits are subdivided into many files. The lists of links to video files can be found in "link_path" directory or here:

https://s3.amazonaws.com/kinetics/600/train/k600_train_path.txt

https://s3.amazonaws.com/kinetics/600/val/k600_val_path.txt

https://s3.amazonaws.com/kinetics/600/test/k600_test_path.txt

The links/annotations can be found the annotations subfolders or here:

https://s3.amazonaws.com/kinetics/600/annotations/train.txt

https://s3.amazonaws.com/kinetics/600/annotations/val.txt

https://s3.amazonaws.com/kinetics/600/annotations/test.csv

A readme file can be found in:

http://s3.amazonaws.com/kinetics/600/readme.md


### Kinetics-700-2020

The train/val/test splits are subdivided into many files. The lists of links to video files can be found "link_path" directory or here:

https://s3.amazonaws.com/kinetics/700_2020/train/k700_2020_train_path.txt

https://s3.amazonaws.com/kinetics/700_2020/val/k700_2020_val_path.txt

https://s3.amazonaws.com/kinetics/700_2020/test/k700_2020_test_path.txt

The links/annotations can be found the annotations subfolders or here:

https://s3.amazonaws.com/kinetics/700_2020/annotations/train.csv

https://s3.amazonaws.com/kinetics/700_2020/annotations/val.csv

https://s3.amazonaws.com/kinetics/700_2020/annotations/test.csv

A readme file can be found in:

http://s3.amazonaws.com/kinetics/700_2020/K700_2020_readme.txt

# Downstream annotations

We also host annotations for AVA-Kinetics and Countix, which both use Kinetics-700 videos. 

To download annotations for AVA-Kinetics:
https://s3.amazonaws.com/kinetics/700_2020/annotations/ava_kinetics_v1_0.tar.gz

To download annotations for countix:
https://s3.amazonaws.com/kinetics/700_2020/annotations/countix.tar.gz


