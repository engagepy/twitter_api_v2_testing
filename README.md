![GitHub Workflow Status](https://img.shields.io/github/workflow/status/zora89/twitter_api_v2_testing/Python%20application?style=for-the-badge)

[![tw_core_app](https://circleci.com/gh/zora89/twitter_api_v2_testing.svg?style=shield)](https://app.circleci.com/pipelines/github/zora89)

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
## 6. Add api_token.py to repository and save variable BEARER_TOKEN

```
touch api_token.py 
```
```
BEARER_TOKEN = "YOUR_API_TOKEN"
```
## 7. Run the python script main.py 

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
## 8. Adjust the query parameter, save file and rerun

```
query = 'Tesla'
```

## 9. Now adjust the inference by adjusting the following words, note only strings are accepted. 

```
word_check_1 = "love"
word_check_2 = "hate"

```

## 10. To grasp the filters in more detail checkout this [Medium Article.](https://medium.com/@zorawar.purohit/python-beginners-research-with-twitter-api-v2-11f038c70368)