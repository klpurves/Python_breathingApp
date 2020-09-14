
# Breathe event marking task

A simple task to facilitate event marking of inhales and exhales for the purposes of testing co-ordination with biophysiological wearables.

Aesthetics are intended to help guide the user through breathing and sequential button presses.

Purpose of the task is quick and dirty way to test an idea. Not designed for perfect user interface or use out side of this single purpose at the time being. May improve over time if it proves useful.

# Instructions

***PLEASE READ TO END BEFORE STARTING***

The script is written in python 3.6

## Dependencies

Requires the following packages to be installed.

```
numpy
pandas
matplotlib.pyplot
matplotlib.animation
datetime
matplotlib.widgets
matplotlib.patches
time
csv
matplotlib

```
if you have python 3 installed, run the following in the command line to install these packages.

```
pip3 install numpy pandas matplotlib.pyplot matplotlib.animation datetime matplotlib.widgets matplotlib.patches time csv matplotlib
```

## Usage

To start the app, use the command line to navigate to the folder which contains the ```simpleBreathe.py``` file.

Run this script from the command line using python3 ```python3 simpleBreathe.py``` (mac)

This will initiate the animated breathing task.

## Task Instructions

The task will collect a time stamp each time you click the centre button to pause or play the animation.

To test the skin conductance response when breathing in deeply (standard test of equipment), you should follow the following steps:

### 1. Push the centre button once
This will pause the task before you commence.
It will also Create event marker 1 with a time stamp.

### 2. Push the centre button once as you begin inhaling for 5 seconds

This will create event marker 2, the start of your deep inhalation.

### 3. Once you complete your inhale, press the centre button once and hold your breath for breath for 5 seconds.

This will create event marker 3, marking the end of your deep inhalation

### 4. Once you have completed holding your breath for 5 seconds, press the centre button and exhale slowly, for a count of 5 seconds.

This will create event marker 4, marking the beginning of your exhale.

### 5. Once you have completed your exhale, push the centre button once.

This will create event makrer 5, marking the end of the first round of the task.

### 6. Repeat steps 2 - 5 five times.

# Understanding the output

You will end up with a csv file (click_timeStamp.csv) in the same folder as the python task file.

It has 3 columns, click ClickCount, Date and time

if done correctly as per instructions above, your click counts will correspond with the following.

1. Start of the Task
2. Start of inhale (round 1)
3. End of inhale  (round 1)
4. Start of exhale  (round 1)
5. End of exhale (round 1)
6. start of inhale (round 2)
7. end of inhale (round 2)
8. start of exhale (round 2)
9. end of exhale (round 2)

and so on.

There should be 4 relevant task markers for each round

# Important notes

Because this is a minimum viable test of concept, the input and output is not foolproof or elegant. There are important limitations to bear in mind:

1. The csv will overwrite each time you do the task. If we need to run the task several times, this is an easy fix - please let me know and I can adapt.

2. There will be an event mark every time you click the centre button. If you click multple times, you will have multiple rows in your dataset. This will make it difficul to keep track of the events tht correspond with the task.

Again, if for some reason we need to use this task for other purposes, I can label event marks more intuitively. 

