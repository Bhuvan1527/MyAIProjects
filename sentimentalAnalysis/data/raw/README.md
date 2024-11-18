---
license: apache-2.0
task_categories:
- text-classification
tags:
- sentiment analysis
- amazon
- reviews
- binary
- text data
- nlp
pretty_name: Amazon Reviewsfor Binary Sentiment Analysis
language:
- en
size_categories:
- 1M<n<10M
---
# Dataset Card for Dataset Name

The Amazon reviews polarity dataset is constructed by taking review score 1 and 2 as negative, and 4 and 5 as positive. Samples of score 3 is ignored. In the dataset, class 1 is the negative and class 2 is the positive. Each class has 1,800,000 training samples and 200,000 testing samples.


## Dataset Details

### Dataset Description

The files train.csv and test.csv contain all the training samples as comma-sparated values. There are 3 columns in them, corresponding to class index (1 or 2), review title and review text. The review title and text are escaped using double quotes ("), and any internal double quote is escaped by 2 double quotes (""). New lines are escaped by a backslash followed with an "n" character, that is "\n".

- **License:** Apache 2

### Dataset Sources [optional]

- **Link on Kaggle:** https://www.kaggle.com/datasets/yacharki/amazon-reviews-for-sa-binary-negative-positive-csv/data
- **DOI:** [@misc{xiang_zhang_yassir_acharki_2023,
	title={🛒 Amazon Reviews for Senti-Analysis Binary -N/P+},
	url={https://www.kaggle.com/dsv/5339021},
	DOI={10.34740/KAGGLE/DSV/5339021},
	publisher={Kaggle},
	author={Xiang Zhang and Yassir Acharki},
	year={2023}
}

## Uses

NLP

### Direct Use

Binary sentiment analysis


## Dataset Structure

The Dataset Contains 

Readme.md

test.csv

train.csv


## Dataset Card Contact

For more info visit : 

https://www.kaggle.com/datasets/yacharki/amazon-reviews-for-sa-binary-negative-positive-csv/data