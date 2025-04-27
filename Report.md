# 🌍 Climate science - A detailed visualization of post-industrial temperature change over the world

## Introduction

We have all been exposed to the relentless climate change news, but the depth of investigation was lacking. I wanted to really understand what the evolution of the climate. I will take you on in my journey of exploration and hopefully learn something along the way. My first investigation is about the trend of temperature over the last 150 years. This report is a work in progress that will look at multiple key factors often quoted by news media but rarely understood by the public (or myself for that matter).

1. Temperature evolution from pre-industrial levels to today
2. Sea level rise
3. CO_2 levels 

## 1. Temperature evolution from pre-industrial levels to today 
### Introduction
We have seen unprecedented rise in temperature during the first two decades of the 21st century. This projects aim at visualizing this evolution and interpreting the results.  

### Methodology
#### Data source
I have gathered the entie library of data available on the [NOAA website](https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00861/html) or you can [download it directly](https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd_all.tar.gz). This dataset represent the entire records for over 90'000 land weather stations.
#### Programming language
This project will be done using Pyhton. You can download the program on the official [website](https://www.python.org/)

#### Import relevant packages
```python   
import os
import csv
import pandas as pd
import re
import dask.dataframe as dd
import numpy as np
```
##### os
OS is a standard library module that lets you interact with the computers operating system. In this case I will use it to check for the existance of the folders I use the data from. It is not mandatory but can be useful in instances where you need to interact with the os. 
##### csv
CSV is a very simple module that allows you to read and write csv files in python. In this project I will use some csv files for temporary storage and operations with pandas
##### pandas 
Pandas is the go to package for data manipulation and analysis for structured data. 

