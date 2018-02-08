# ML-CNN-Verification-Code-Recognition
This repo is about verification code recognition based on CNN. It introduced a new way to gain training dataset and recognition algorithm based on CNN. 

## Introduction
In general, we should grab the verification codes existed online and add anotation on them then put them into the trianing process. However, this method will bring other problems.

First of all, training dataset will require millions of pictures and it is really difficult to capture so many pictures without getting panalty from websites(where those pictures come from). If our scraper will need one second to capture one verification code picture on one IP address, then we only can get 80,000 pictures in one day. If we get penalty during this time, then it will take longer for us to collection needed pictures. 

Secondly, assueming that we already have 500,000 pictures, the next step for us is adding anotation on each picture. If we assume to use the content of verification code as labels, then we need 5 seconds on our laptop. If above assuption is true, then we need 29 days to finish labeling those 500,0000 pictures(calculated on 24 hours a day instead of 8 hours a day). We can also use the help of script to speed up this time consuming process. We name these 500,000 pictures from 1 to 500,000, then split them into multiple folders(For the sack of reducing mistakes and easily adjustment; also, it is not a good performance to save too many documents in one folder). Then we go through every folder and write down every correct label of picture into one txt file, one by one line. Finally, we rename every picture by reading the txt file line by line. Even though a verification code is made up for 4 digits and letters, one input will take about 2-3 seconds. Eventually, we still need 15 days to add anotation to 500,000 images which does not seems very reasonable for this project. So it becomes indispensable for us to look for another better solution. 

In fact, most of website use open source framework to generate verification code. Those frameworks work in a similar way so our inspiration becomes using framework as reference, generate similar verification code for training, which solves our training dataset in a better way.

Common features of verification codes including:

1. font color changing
2. background color and background picture changing
3. inserting noises such as lines and dots
4. trainsforming the whole picture

Based on the above discussion, we use python to implement a simple verification code. 

## Requirements

```
Python: 3.6
opencv: 3.3.0
PIL: 4.1.1
```

## Results
![generated verification code](https://github.com/Tingting-Chang/ML-CNN-Verification-Code-Recognition/blob/master/validate.jpg)


## References
[Reference 1](https://hbaaron.github.io/blog_2017/%E5%9F%BA%E4%BA%8E%E5%8D%B7%E7%A7%AF%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E5%AE%9E%E7%8E%B0%E9%AA%8C%E8%AF%81%E7%A0%81%E8%AF%86%E5%88%AB%EF%BC%88%E4%B8%80%EF%BC%89/)
[Reference 2](https://www.codeday.top/2017/01/11/21796.html)
