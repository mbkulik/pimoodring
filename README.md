# PiMoodRing

This project is the capstone project for Picademy Providence 2017. This project is meant to 
run on a RaspberryPi. It may install and run on other systems, YMMV

##setup

Install the required python packages.

### Python 2
```
pip install -r requirements.txt --user
python -m textblob.download_corpora
```

### Python 3
```
pip3 install -r requirements.txt --user
python3 -m textblob.download_corpora
```

### Twitter API

add a keys.py file with your corresponsing Twitter API credentials
It should adhere to the below format
```
#!/usr/bin/env python
#keys.py
#visit http://dev.twitter.com to create an application and get your keys
keys = dict(
	consumer_key =          'XXX',
	consumer_secret =       'XXX',
	access_token =          'XXX',
	access_token_secret =   'XXX',
)
```

## running

1. moodring.py
	- starts a twitter stream looking for #picademy and/or #pimoodring and performs a sentiment analysis on the tweet content

2. PiMoodRing GUI.py
	- a GUI to allow user specifed searches of twitter for sentiment analysis