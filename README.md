# Mastermind

## Installation

### Requirements

- python 3.10.5
- pip

### Instructions

- clone this repository
- navigate to the root of the repository in your terminal
- enter ```pip install -r requirements.txt``` in the terminal

## How to test

- After installation, in the terminal, enter ```pytest```

## How to play

1. navigate to the root of the repository in your terminal
2. in the terminal, enter ```python src/mastermind.py```
3. Play the game!

## Tested on

- KDE Linux Mint 20.3
- Ubuntu 20.04

## Todo

- Store displayed messages from Interface class in a central location to allow easy translation to different languages
- Add more automated testing to Interface class
- break down main function in Interface class, it's too big
- Add graphical way to see status of https://www.random.org/integers/
- Add metrics to save gameplay data
    - highest score
    - lifetime player attempts
    - lifetime wins
    - lifetime losses
    - average attempt per game
- Add new logger class to save status of https://www.random.org/integers/ to a database
- update github actions file to test on multiple operating systems
- Fix testing so that check_status doesn't record to the log folder during a test
    - use python logging module
- Optimize checking for key existence in dictionary
    - using ```if key in dict``` is a loop, just check for ```if dict[key]```
- When checking site status, just try to get the random number
    - if it fails, we know the site is down
    - use try/except???