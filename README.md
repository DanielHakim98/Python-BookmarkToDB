# Project HTML to Python

* This project focuses on to load HTML file in Python and store it into a Dataframe.
* Steps:
   - Load "bookmarks.html" file into Python
   - Process the file content (Sorting,Grouping,Cleaning)
   - Store it in List/Dataframe
* Now, Lets focus on the first steps, Loading the file. The thing need to be considered is what data I want to store and the way I want to store it.
   - Store it in list of dictionary
   - In dictionary only contains 'id','title','topic','link'
* The steps for loading is complete. Now there are two lists for title and links.
---
13/1/22
* Parse HTML using BeautifulSoup, gather all data in a list of dictionary and convert them all into pandas dataframe.
* Testing with git on Windows. Previously, all repos were pushed from Unix-based VM. This is an alternative way to push the repo to Github.
* Read and understand more about the EOL used in Windows and Mac OS/Linux. This is important thing to know as I plan to work this file for cross-platform (Windows and Linux).
---
14/1/22
* Add .py file and make it into one class.
* Next feature: Export to DB (SQlite or MySQL)
---
4/3/22
* Add input request to allow more flexibility for the source filepath and save filepath.
* Next feature: Export to DB (SQlite or MySQL)
---
21/3/22
* Split python codes into three python files.
* Next task: Figure out the way to transfer data from dataframe to MySQL or SQLite3.
---