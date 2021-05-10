## LAB-3 for CZ3005 
#### Assignment 3:  Subway sandwich interactor
The prolog script offers different meal options, sandwich options, meat options, salad options, sauce options, top-up options, sides options etc. to create a customized list of person’s choice. The options should be intelligently selected based on previous choices. For example, if the person chose a veggie meal, meat options should not be offered. If a person chose healthy meal, fatty sauces should not be offered. If a person chose vegan meal, cheese top-up should not be offered. If a person chose value meal, no top-up should be offered.


## Technology used
* SWI-Prolog
* Flask framework (Python)

## Prolog File
`knowledge_base.pl`

## Instructions

##### Install Virtual Env
`$ pip3 install virtualenv`

##### Activating env
`$ source env/bin/activate`

##### Install requirements
`$ pip3 install -r requirements.txt`

##### Run command 
`$ python3 app.py`

##### Click on this link to view
http://localhost:5000/

## Additional information
For MacOS, homebrew's latest swi-prolog version is unstable. Hence it has to backtrack into using the following version instead.

`$ brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/09a94009142a6265b0b8e322463100610aeda964/Formula/swi-prolog.rb`
