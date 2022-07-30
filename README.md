# Python Script for Reasearch via Twitter API V2

## Enables query search and additional layer of inference on the resulting data stream

### Note: tw_core_app.py == main.py 

## 1. Create a project-folder

```
cd project-folder
```

## 2. Create python env 

```
python3 -m venv env
```

## 3. Clone this repo

```
git clone https://github.com/zora89/twitter_api_v2_testing.git
```

## 4. Now cd into the twitter_api_v2_testing folder

```
cd twitter_api_v2_testing folder
```

## 5. Install dependencies from requirements.txt

```
pip install -r requirements.txt 
```

## 6. Run the python script main.py 

```
Python3 tw_core_app.py
```
>
Results will show up in the terminal window, and look something like this :

```
Research Query: Ather

Tweets Scanned 625

'love' count is 21 
'hate' count is 3

<<<<<<<<------------ TWEET VOLUME IN PAST 7 DAYS
Tweet Volume 48
Tweet Volume 64
Tweet Volume 66
Tweet Volume 98
Tweet Volume 100
Tweet Volume 102
Tweet Volume 114
Tweet Volume 35
```

Note: Scroll limit in terminal may prevent you from scrolling the entire volume returned. 
>
## 7. Adjust the query parameter, save file and rerun

```
query = 'Tesla'
```

## 8. Now adjust the inference by adjusting the following words, note only strings are accepted. 

```
word_check_1 = "love"
word_check_2 = "hate"

```

## 9. For understanding the filters in more details checkout the medium article @ 