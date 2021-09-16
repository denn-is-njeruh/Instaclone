## Project Name
**PhiInsta**

## Author 
**Dennis Njeru**


## Description
This is a clone application of the photo-website Instagram

## Features
As a user of the application you will be able to:
1. Register and sign in to start using the application.
2. Upload pictures on the application.
3. View your profile with all the photos.
4. Follow other users and see their pictures on your timeline.
5. Like a picture and leave comments on it.


### Installation and setup instructions
1. Clone this repo: git clone https://github.com/denn-is-njeruh/Instaclone.git
2. The repo comes in a zipped or compressed format. Extract to your prefered location and open it.
3. open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer  [here](https://realpython.com/pipenv-guide/)
3. To run the app, you'll have to run the following commands in your terminal

        pipenv install -r requirements.txt

4. On your terminal,Create database gallery using the command below.

        CREATE DATABASE gallery;

5. Migrate the database using the command below

        make migrate

6. Then serve the app, so that the app will be available on localhost:8000, to do this run the command below

        make serve
7. Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.


## Running the tests
Use the command given below to run automated tests.

        make test gallery


## Technologies Used
* Django - Web Framework
* Python - For functionality
* HTML - For building Mark Up pages/User Interface
* CSS - For Styling User Interface


## Known Bugs
No known bugs at the moment.


## Contacts
* Email: dennis.njeru@student.moringaschool.com 
* LinkedIn: https://www.linkedin.com/in/dennis-gitonga-227246193/

## Live Link



## License 
[GNU GPL v3.0](./LICENSE)


Copyright (c) [2021] **Dennis Njeru**
