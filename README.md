## How to Use

- Open main.py
- You will see 3 options. 1: Get a City's Weather 2: Compare Cities 3: Quit
1. Get a City's Weather
Calls the API and asks user to enter a city, state/country. This will tell the weather API what city info to get.
By pressing the ENTER key with no text entered, this will default it to show Johnson City, Tennessee weather info.

2. Compare Cities
Calls the API twice. I had to do it this way because I would have to pay for a higher subscription to do multiple batch calls at once. 
By pressing the ENTER key with no text entered, this will default it to show New York City and Santa Monica, which will compare their temp differences.

3. Quit
This will quit app.


## Issues
1. I had issues initally just calling the API. The weatherstack documentation did not want me to use python but I am stubborn and refused to use a different language.
2. The APICall method was found using the weatherstack docs and an AI converting it from Javascript to Python, so I could actually use it.
3. the for loop array template was made by AI, but I filled it in with the parameters that weatherstack uses.
4. the while True loop was stolen from my other coding projects. All it does is reloop the method if the user enters y/Y. Else, sends user back to menu. I had to make a couple while loops though, because I need to recall the APICall as well.
