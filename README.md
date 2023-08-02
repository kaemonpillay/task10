# MySite
## This is the first interactive website i have built

## The entire purpose (besides asssignment submission) was to demonstrate the effective use of CSS, HTML and Django 
## The use of Django also encompassed user authentication, registration, login and logout pages as well as utilizing the polls functions


# Installation Guide:

# Creating A Virtual Environment
## In addition to downloaing all the files, you will need to install a virtual environment in order to run this website properly
## Assuming that you have already installed Django and pip to your local computer, follow the below inputs in your command terminal to create the virtual environment 
1. Change your directory to the main file using cd
2. Input "python3 -m venv venv"
3. Input "source venv/bin/activate" for MacOS or the appropriate function on your OS
4. Input "pip install django"
5. Navigate to where the manage.py file is and input "python manage.py runserver"
6. You should now be given a web address that will enable you to access the website

# Creating a Docker Image
1. Create a new file called Dockerfile with no extention
2. Add the following to the file:
   FROM nginx
   COPY . /usr/share/nginx/html
3. In your command terminal run: docker build -t my-website ./
4. In your command terminal run: docker run -d -p 80:80 my-website
5. Create a new repository on Docker
6. In your command terminal run: docker tag my-website [user]/[repo] (where user is your username on Docker and repo is your link to the repository on Docker
7. In your command terminal run: docker login
8. In your command terminal run: docker push [user]/[repo]

# Usage
## If a user is not registered, you will be prompted to register using the page below via http://127.0.0.1:8000/register/ (see screenshot below)
![Screenshot 2023-07-24 at 18 11 36 (2)](https://github.com/kaemonpillay/MySite/assets/139888793/e82f6cef-0e80-4cfd-9cb5-0d8448f882c2)

## Once registered, you will be taken to the login page where you can use your credentials to login to the main site (see screenshot below)
![Screenshot 2023-07-24 at 18 13 22 (2)](https://github.com/kaemonpillay/MySite/assets/139888793/643b95ca-5ecf-4861-b37e-76c4ea049418)

## After login is completed succesfully, you will be taken to the main page (see screenshot below)
![Screenshot 2023-07-24 at 18 14 29 (2)](https://github.com/kaemonpillay/MySite/assets/139888793/cc0333a0-3998-46c7-a845-5e5d8bdcecc0)

## The other two pages can be accessed by two options:
1. By manaually entering the web addresses:"http://127.0.0.1:8000/polls/" and "http://127.0.0.1:8000/about_us/"
2. Or by clicking the "Find out more about us!" hyperlink on the top of the main page or by selecting one of the two options at the bottom of the page
3. The about us page contains a link to the polls

## The about us page should look like this:
![Screenshot 2023-07-24 at 18 17 46 (2)](https://github.com/kaemonpillay/MySite/assets/139888793/eb60516e-8d2a-4777-ab88-3d43ddc2300f)

## The polls page should look like this:
![Screenshot 2023-07-24 at 18 18 24 (2)](https://github.com/kaemonpillay/MySite/assets/139888793/6b30feb1-8987-4979-a98e-b04d63bc60d1)

## My github respository can be accessed here: https://github.com/kaemonpillay/MySite



