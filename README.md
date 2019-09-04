# Walkie Doggie

New Initiative by SoSD

[Click here for website](https://yc-walkiedoggie.herokuapp.com/)

_Developed By Yu Cheng_

## Index
1. Introduction
2. UI/UX
3. Technologies Used
4. Features
5. Future Features
6. Testing
7. Deployment
8. Credit

## Introduction


## UI/UX 
### Design


### User Stories
Several user stories have been considered during the development and set up
- _As the user, I should be able to understand the purpose of the website at first glance_
- _As the user, I should be able to navigate the page with ease with the use of icon and buttons_
- _As the user, adding an post should be simple and hassle-free for me_

### Wireframe
_Please refer to wireframe folder_

## Technologies Used
1. HTML/CSS
2. Bootstrap
3. Heroku (for deployment)
4. Postgesql

## Features
- Main page : introduction of the website
- Walking Dog : introduction of the dogs participated in this programme
- Cover Dog : a simple contest/platform where our registered users can submit and vote for their favourite photo.
- Doggonation : donation for the main SoSD
- Login/Logout/Register page

## Future Features
- 

## Testing
The layout has been tested on Windows laptop/MacBook /iPad Mini(2018) /Pixel 2 XL/iPhone SE covering various screen-size. Browsers used for testing are Microsoft Edge, Google Chrome & Apple Safari.


### Test Account (username : password)
- sam123 : coconuty

Test Case:

## Deployment
Most of the development has been developed on GitHub and deployed on Heroku as final product.
[Click here for website](https://yc-walkiedoggie.herokuapp.com/)

The site is deployed using following methods:
- install Heroku via command ```sudo snap install --classic heroku```
- Login through bash ```heroku login -i```
- Create the app (deployment repo on heroku) through ```heroku create <app_name>```
- followed by ```git remote -v```
- Install gunicorn via ```pip3 install gunicorn```
- Created file called Procfile under root of the folder and add this line ```web gunicorn <python file without .py>:app```
- Create requirements file with ```pip3 freeze --local > requirement.txt```
- followed by ```git add```, ```git commit -m "<message>"``` and ```git push heroku master``` to push it to heroku site


## Credit

Design 
- icons8.com - Financial icon as the logo
- webgradients.com - Providing CSS code for the background gradient
- flaticon.com
- Startbootstrap template for the basic layout 

Acknowledgements 
- inspiration for this project is from mobile expenses management such as Monefy- Money Manager,Goodbudget
