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
#### Import relevant packages
<pre>```python  
import os
import csv```
</pre>


