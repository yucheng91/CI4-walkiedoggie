# Walkie Doggie

New Initiative by SoSD by bringing volunteery dog-walking closer to you.

[Click here for website](https://yc-walkiedoggie.herokuapp.com/)

_Developed By Yu Cheng_

## Index
1. Introduction
2. UI/UX
3. Technologies Used
4. Features
5. Testing
6. Development & Deployment
7. Credit

## Introduction
This website WalkieDoggie serve as a new side project for SoSD (Save Our Street Dogs) to bring the shelter dog closer to people around Singapore hoping to educate the public about dog shelter and create potential adoption opportunities for the shelter dog.

## UI/UX 
### Design
The design of the webpage has been created via Bootstrap (and deployed some element from StartBootstrap template). The main goal of the design is to ensure that everything is mobile-responsive and easy to navigate. 

### User Stories
Several user stories have been considered during the development and set up
- _As the user, I should be able to understand the purpose of the website at first glance_
- _As the user, I should be able to navigate the page with ease with the use of icon and buttons_
- _As the user, adding a post should be simple and hassle-free for me_

### Wireframe
_Please refer to wireframe folder_

## Technologies Used
1. HTML/CSS
2. Bootstrap
3. Heroku (for deployment)
4. Postgesql
5. Uploadcare (with pyuploadcare as a plugin)
6. Stripes (for payment)
7. Django (for set up of the webpage)
8. FontAwesome
9. Google Fonts
10. Django Crispy Form (Plugin to add the bootstrap element to Django form)
11. Whitenoise (to serve static files)

## Features
- Main page: introduction of the SoSD
- Walking Dog: introduction of the dogs participated in the programme.  
_(Only Admin is able to add/edit/delete admin post)_
- Cover Dog: a simple contest/platform where our registered users can submit and the public can vote for their favourite photo.  
_(User is able to create a new post, while Admin can edit/delete the post, voting is open to all)_
- Doggonation: donation for the main SoSD via Stripes.
_(Donation are welcome from everyone)_
- Login/Logout/Register page

## Testing
The layout has been tested on Windows laptop/MacBook /iPad Mini(2018) /Pixel 2 XL/iPhone SE covering various screen-size. Browsers used for testing are Microsoft Edge, Google Chrome & Apple Safari. The following are the finding :

- Uploading image with another size/orientation other than landscape may affect the alignment of the table. Compulsory crop function with a standard ratio (based on most of the images) is deployed under image upload to ensure the consistency of the image site.
- Media Query has been used in CSS to ensure all the text stays in the card for Cover Dog page.
- The font is readable throughout devices and button are decent-sized for easy navigation in smaller devices.

#### Test Account (username : password)
```
yucheng91 : coconuty (superuser aka Admin)
sam123 : coconuty (normal user)
```

#### Test Case:
- Create a Walking Dog post with a normal user.  
_Expect: no Add New button seen, if navigate to ../walkingdog/create link, "nothing to see here" page will appear_ (result: pass)
- Navigate Walking/Cover Dog with superuser.  
_Expect: Add new button to appear on both pages, expanding the card shows Edit/Delete button_ (result: pass)
- Uploading a photo with different aspect ratio.  
_Expect : crop function prompted_ (result:pass)
- Vote/Like the photo via the heart button.  
_Expect: heart received count to go up by 1 per press_ (result: pass)
- Donating less than $10.  
_Expect: field error prompted about minimum donation $10_ (result: pass)
- Leaving empty space in the donation page and proceed with the donation button.  
_Expect: error page_ (result: pass)
- Leaving empty space in upload post field.  
_Expect: field error prompted_ (result: pass)
- Keying in invalid password/user.  
_Expect: Error page_ (result: pass)
- Register with the same email address.  
_Expect: Error prompt on used email_ (result: pass)

## Development & Deployment
Most of the development has been developed on GitHub via Django and deployed on Heroku as final product.

[Click here for website](https://yc-walkiedoggie.herokuapp.com/)

### Development on Django
For people who clone the repository, all the necessary installation has been included in the requirements.txt in this file via ```pip install -r requirements.txt```

For starter:
- install Django via ```pip3 install django==2.2.4```
- Proceed with creating new project ```django-admin startproject ProjectName .```
- Create the app (such as account/post) for the project with ```django-admin startapp AppName```
- Set the allowed host in settings.py to enable testing on AWS ```ALLOWED_HOSTS = [os.environ.get("C9_HOSTNAME"), ‘127.0.0.1']``` and added the app name under ```INSTALLED_APPS```
- Stripes/Uploadcare + Pyuploadcare installation via CIL
- Create a gitignore file with the list to ignore upon my git push to GitHub to save on resources when we need to deploy it on Heroku.

### Deployment on Heroku
The site is deployed using the following methods:

For starter:
- install Heroku via command ```sudo snap install --classic heroku```
- Login through bash ```heroku login -i```
- Create the app (deployment repo on heroku) through ```heroku create <app_name>```
- followed by ```git remote -v```
- Install gunicorn via ```pip3 install gunicorn```
- Create a file called Procfile under the root of the folder and add this line ```web: gunicorn <PROJECT_FOLDER>.wsgi:application```
- Add-on Postgresql via ```heroku addons:create heroku-postgresql``` where all information will be stored
- install the database with ```sudo pip3 install dj_database_url```
- Create requirements file with ```pip3 freeze --local > requirement.txt```
- followed by ```git add```, ```git commit -m "<message>"``` and ```git push heroku master``` to push it to heroku site
- Import the environment variables (previously on .bashrc) to heroku app using Heroku CLI by the following method to ensure all the plugin app are connected and usable :
```
heroku config:set STRIPE_PUBLISHABLE_KEY=pk_test_aaa
heroku config:set STRIPE_SECRET_KEY=sk_test_bbb
…

```
- Perform ```git add``` and ```git push heroku master``` to ensure all everything is up to date.
- Create Superuser aka admin via ```heroku run python manage.py createsuperuser```
- Normal user can sign up through the deployed website itself through register

## Credit

### Design 
- icons8.com - Financial icon as the logo
- webgradients.com - Providing CSS code for the background gradient code on navbar & footer.
- flaticon.com
- Startbootstrap for the layout basic layout & CSS template
- pixabay.com (for the site photos)

### Acknowledgements 
- SoSD (for all the shelter dogs picture & contents)
- Code Institute for the support through LMS 

