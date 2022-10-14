<b> Overview </b>

Using the weather API api.weather.gov, find the average daytime temperature in four cities. Code should be written in python, and api calls must be made asynchronously. Keep in mind concepts of code reusability and software development best practices. Please create a GitHub repository to hold your code, and send me a link to your repo when you are finished.

<b> Details </b>

The URLs to get temperatures for the 4 cities are:

Salt Lake City, Utah
https://api.weather.gov/gridpoints/SLC/99,174/forecast
40.7607793,-111.8910474

Denver, Colorado
https://api.weather.gov/gridpoints/BOU/58,60/forecast
39.7321957,-105.0982033

Phoenix, Arizona
https://api.weather.gov/gridpoints/PSR/157,64/forecast
33.6054149,-112.125051

Tampa, Florida
https://api.weather.gov/gridpoints/TBW/70,98/forecast

27.9944826,-82.4542804

The api will return a field called "properties", and properties will have a field called "periods". For the daytime periods, average the temperatures. Keep in mind the periods array will return more than just daytime periods, and you will need to filter out the non-daytime ones.

<b> Expected Output </b>

List each city with the calculated average temperature in this form:

Salt Lake City Utah Average Temp:75.73

Phoenix Arizona Average Temp: 83.84

Denver Colorado Average Temp: 70.63

Tampa Florida Average Temp: 86.63

Your numbers will differ slightly as forecasts will change.

<b>Tips For Success</b>

Pay attention to styling and code reusability. Think of how the code you will write could be a standalone module and/or be incorporated into a larger project. Consider writing tests, at least one or two. Consider recovering data from threads rather than printing within the thread. Make the code readable and self-documenting. This is not meant to be time consuming, I know you have other things in your life. Show us your best work. Asking questions is encouraged.

When you are finished, please send us a link to the GitHub repository you created for this challenge (bitbucket is also okay).
