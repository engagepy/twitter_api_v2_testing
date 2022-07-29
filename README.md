# Python Script - Interact with Twitter API V2

![](https://github.com/zora89/twitter_api_v2_testing/actions/workflows/python-app.yml/badge.svg)
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/zora89/twitter_api_v2_testing/tree/main.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/zora89/twitter_api_v2_testing/tree/main)

<hr>
Note: tw_core_app.py == main.py 
<hr>

### 1. Create a local folder and *activate a virtual environment* 

### 2. Clone this repo

```
git clone https://github.com/zora89/twitter_api_v2_testing.git
```

### 3. Change directory to:

```
cd twitter_api_v2_testing
```

### 4. Install requirements 

```
pip install -r requirements.txt
```

### 5. Run main.py 

```
Python3 main.py 
```
<hr>
Note: Results log in terminal winow, scroll limits may prevent viewing all tweets scanned. Alternate can be to write to local file. 
<hr>

### 6. Use query variable to add your custom query in main.py as shown below :

```
query = 'Ather'
```

### 7. You can choose to retain filters such as: 

``` python
 '-is:retweet -#eximbank -btc -eth -nft -crypto -donation -donating -donate lang:en'
```

### 8. 👆 the -is:retweet is a fileter to avoid retweets in data, other filters help avoid trash/spam in data, add/remove thoughtfully


### 9. The following variables take in 2 words, and return a count of them past week

```
word_check_1 = "love"
word_check_2 = "hate"
```

### 10. Last result count represents subject specific tweet volume in past 7 days + search day (assumption based on 8 results)
