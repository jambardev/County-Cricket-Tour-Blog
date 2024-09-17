# County Cricket Tour Blog:

This blog site is a page that allows lovers of county cricket to come together and share their experiences of the 18 different county grounds.

The live application can be viewed here:

https://county-cricket-blog-a93042f7114f.herokuapp.com/

# Purpose and Target Audience:

**Problem Statement:**
County cricket is becoming an under appreciated form of the game with much of the online space taken up by international or franchise cricket. It can be hard for followers of the county game to find a space for a more reasoned, friendly discourse about county cricket specifically.

**Purpose:**
This app will allow people who love and follow county cricket around the country to come together as a community. Share their thoughts on the game and the experience of attending matches. It will also allow for tips about making the most of the different host stadiums.

**Target Audience:**
The target audience is quite simply anyone who loves county cricket.

# User Stories

* As the site owner I want the site to be easy and self explanatory to navigate.
* As a user I want to be able to review the posts of other people and add comments.
* As a user I want to be able to create a profile, which will allow me to create posts and view my previous ones.
* As the site owner I want users to be able to read about the site on the "about" page.
* As the site owner I want to ensure all log in details are secure.

# Wireframe & Initial Design:

### Home Page

* Laptop

<img width="639" alt="image" src="https://github.com/user-attachments/assets/08cf70af-0367-45f1-9f4b-eb495aef44e5">

* Mobile

<img width="233" alt="image" src="https://github.com/user-attachments/assets/17078a55-3ad5-4e1d-9158-b7918861423b">

### Login/Register

* Laptop

<img width="565" alt="image" src="https://github.com/user-attachments/assets/3fe81df8-49e1-4a50-a0e7-7a232f276538">

* Mobile

<img width="224" alt="image" src="https://github.com/user-attachments/assets/4382c60c-a7ea-438d-883e-6ca6b5eb7915">

### About

* Laptop

<img width="568" alt="image" src="https://github.com/user-attachments/assets/b1ccd8c2-fe3f-478d-8fbd-1fe80f769ad0">

* Mobile

<img width="240" alt="image" src="https://github.com/user-attachments/assets/89b1325c-b7fa-4b9f-8fde-0222a69042dc">

### Single Post

* Laptop

<img width="562" alt="image" src="https://github.com/user-attachments/assets/16d5ac34-3bd7-4e0b-9544-55172e7b0feb">

* Mobile

<img width="239" alt="image" src="https://github.com/user-attachments/assets/aef06306-af50-4d70-95d1-a9dc78762945">

# Agile

To plan and create this project I used the Agile principles in conjuction with a projectboard on Github. This was the first time I had used Agile as an individual developer rather than as a part of a Hackathon team. However whilst I did not need to assign tasks I still found it useful to set out a plan to work through the project and work towards fulfilling the acceptance criteria of User Stories.

<img width="1439" alt="image" src="https://github.com/user-attachments/assets/decb7ac6-59ff-46d7-9d3d-a20e3153fb9b">

# Design Choices

As the main purpose of this project was the functionality of the site I did not focus too much on the design of the site. However my main aim was for a easy to navigate site that enhanced the user experience and layed out the information of the blog posts in a clear way.

## Colour Scheme

I selected the main colours of the site with cricket in mind. The dark read of the navigation options and page titles was based on a cricket ball. The green of the header and footer the pitch. The backgroudnd white the colours worn during county cricket.

#8B0000 - Dark red for the navigation options and page titles

#56ad56 - Green for the header and footer

## Database Design

Below is a simple database design for the project, created on Excel. This was important to visualise how my models would relate to each other and shows the data needed for each model.

<img width="733" alt="image" src="https://github.com/user-attachments/assets/e08dd2d7-532e-4368-b2a9-9d422030eb70">

## User Flow Chart

I used Lucidchart to create a simple user flow chart to demonstrate how a user would be able to move through the site.

<img width="693" alt="image" src="https://github.com/user-attachments/assets/618a7e55-965e-4fa1-b087-aa47c47569da">

# Main Features:

### Home Page

The home page of the site shows the latest posts from the community. These are viewable for anyone visiting the site and you can click on a post to view the content in detail. However to create a new post or comment on an existing one a user must be authorised. From the home page you can also access, the about, register and login pages.

<img width="1293" alt="image" src="https://github.com/user-attachments/assets/b636b25a-d5c0-462e-ae61-4bec93a75a43">

### About page

The about page of the site gives a brief introduction and some basic guidelines, i.e always be kind. It also has what is the stock photo for the site currently. A county game taking place at the Riverside ground in Durham, taken by myself.

<img width="1440" alt="image" src="https://github.com/user-attachments/assets/748be14e-8970-48c1-a801-f65f23c10fc1">

### Register/Sign Up pages

These were created using the Django templates and allow a user to first register for the site and subsequently to login. Once logged in they can create posts/comment.

<img width="1436" alt="image" src="https://github.com/user-attachments/assets/de568dd9-afd1-4db4-a96c-c091402068e5">

<img width="1436" alt="image" src="https://github.com/user-attachments/assets/08ef234e-0288-4e6e-b2ca-78b6911ae325">

### Footer

Viewable on all pages, the footer contains links to social media sites. At some point in the future these will be links to profiles for the blog, at the moment they simply link to the homepages of each company. The footer, along with the header and navbar help provide consistency accross the site.

<img width="1438" alt="image" src="https://github.com/user-attachments/assets/bf11aee9-d50e-482b-bf79-56e8f9028776">

### A post

By clicking on the title of an individual post on the homepage a user can view the blog post in it's entirety. If it is the user's own post they can delete it from here. If it is a different users post comments can be left. Once submitted comments can be edited and deleted. There is also a small comment counter that shows how many comments have been left on each post.

<img width="1433" alt="image" src="https://github.com/user-attachments/assets/663dde00-f651-4745-8a0e-92eb5133f69d">

<img width="1432" alt="image" src="https://github.com/user-attachments/assets/a1e535f7-15ab-4d9e-8d31-3f1d9f514fb4">

### Creating a post

Users who are logged in can add a new post by clicking the "New Post" link on the nav bar and completing the form. The dropdowns give the option of selecting where you saw the game (all 18 county grounds are listed) and the visitors. Once submitted this post will appear on the homepage for other users to view it. The most recent post will appear at the top left of the page.

<img width="1437" alt="image" src="https://github.com/user-attachments/assets/2e6b3823-0510-470f-a207-b2febeed6bc5">

# Future Features

The current iteration of this project has been designed to meet the MVP of the task. In the future there are several features I would like to implement.

* The ability for a user to upload a photo to accompany each post.
* The ability for a user to edit a post once it is created. Currently it can be deleted but only comments can be edited.
* A profile page so a user can see all of their own posts.
* A logo or some artwork to make the homepage more interesting and visually appealing.

# Validation:

## HTML

I have used W3C validation service for the HTML and taken it from the page source of the live site.

| Page | Screenshot | Result |
| --- | --- | --- |
| Home | <img width="672" alt="image" src="https://github.com/user-attachments/assets/1ea40ab4-3b08-428d-be6e-d7c4260f7f40"> | Pass: No Errors |
| About | <img width="699" alt="image" src="https://github.com/user-attachments/assets/2d83072e-e961-4dfc-8eb4-507f526ce2f7"> | Pass: Validator suggests changing the height and width of the image to a digit, trialled this but it works better as 100% so have left it. |
| Individual Post | <img width="636" alt="image" src="https://github.com/user-attachments/assets/357ca54c-5743-43bd-bfbc-3d2157b91e64"> | Pass: Same issue as the about page with the image |
| Register | <img width="605" alt="image" src="https://github.com/user-attachments/assets/2ea8ca4b-a61b-4a75-9088-61b857ca997d"> | Pass: Errors shown in the validator. These are from the Django account templates, not issues I can fix. |
| Login | <img width="643" alt="image" src="https://github.com/user-attachments/assets/99718e72-561f-4e02-afd7-a7fe38e44cfe"> | Pass: No Errors |
| New Post | <img width="595" alt="image" src="https://github.com/user-attachments/assets/658d33e2-1a6c-4758-a932-105e23ad1e1b"> | Pass: No Errors |
| Edit Comment | <img width="616" alt="image" src="https://github.com/user-attachments/assets/8a1b001e-4229-4786-ba47-c837b5d40fea"> | Pass: No Errors |

## CSS

I have used the W3C Jigsaw validator for my CSS file.

It showed no errors as per the screenshot.

<img width="1407" alt="image" src="https://github.com/user-attachments/assets/cda480b8-33e1-41bb-b500-238728f82e38">

## Python

| App | File | Screenshot | Result |
| --- | --- | --- | --- |
| blog | admin | <img width="1099" alt="image" src="https://github.com/user-attachments/assets/481e3658-5ac6-40d3-8d59-e3d4f379a74f"> | Pass: No Errors |
| blog | apps | <img width="1102" alt="image" src="https://github.com/user-attachments/assets/1ee75a96-b7cd-4cb1-81e2-4e2219bb3fbd"> | Pass: No Errors |
| blog | forms | <img width="1112" alt="image" src="https://github.com/user-attachments/assets/a3dfe60d-0075-4899-b2f4-453463ca40b5"> | Pass: No Errors |
| blog | models | <img width="1123" alt="image" src="https://github.com/user-attachments/assets/39b056fb-f271-451f-9cc0-e913af6b6fa0">| Pass: No Errors |
| blog | tests | <img width="1104" alt="image" src="https://github.com/user-attachments/assets/b861580e-20ca-410f-a5dd-e6d0d9adb3d4"> | Pass: No Errors |
| blog | urls | <img width="1096" alt="image" src="https://github.com/user-attachments/assets/db9d762c-8e7c-435f-b825-60fc189253d4"> | Pass: No Errors |
| blog | views | <img width="1091" alt="image" src="https://github.com/user-attachments/assets/bea6fbc8-47cc-4341-8746-2866d699e10c"> | Pass: No Errors |
| countychamp | asgi | <img width="1112" alt="image" src="https://github.com/user-attachments/assets/d0d0c717-5fce-4def-b9a8-a9ca0ac97830"> | Pass: No Errors |
| countychamp | settings | <img width="1118" alt="image" src="https://github.com/user-attachments/assets/908e4697-a288-416e-a376-df4668889fd7">| Pass: No Errors |
| countychamp | urls | <img width="1121" alt="image" src="https://github.com/user-attachments/assets/0c6b9633-afb5-434b-8bc8-cbaaa4556270"> | Pass: No Errors |
| countychamp | wsgi | <img width="1095" alt="image" src="https://github.com/user-attachments/assets/e3c4eb5c-8efa-4dc2-b632-ffdbcde6a6d3"> | Pass: No Errors |

# Testing:

I have completed the following manual testing of my app on both a laptop and a mobile device.

## Browsers

I completed the testing on both Chrome and Safari. The functionality worked as expected on both, however on Safari there were some minor issues with the CSS and the navbar, as per the below image. 

<img width="1433" alt="image" src="https://github.com/user-attachments/assets/cf74ad09-990c-42bb-a1e1-aefbd76780c9">

## Links

| Link | Expected Outcome | Outcome |
| ------- | ---------------- | ----- |
| Home | Navigates to the home page when clicked | Pass |
| About | Navigates to the about the site page when clicked | Pass |
| Register (navbar) | Navigates to the register page when clicked | Pass |
| Login (navar) | Navigates to the login page when clicked | Pass |
| Login (within register page) | Navigates to the login page when clicked | Pass |
| Sign up (within login page) | Navigates to the register page when clicked | Pass |
| Post titles | Navigates to the individual post page for that post | Pass |
| Next (if more than 6 posts on page) | Navigates to the next set of blog posts | Pass |
| Previous (if not on first page of posts) | Navigates to the previous page of blog posts | Pass |
| Social media icons | Open a new window and navigates to the homepage of the relevant social media site | Pass |

## Functionality

Whilst testing the below functions I also tracked that the associated message would pop up, confirming the action that the user had taken.

| Feature | Expected Outcome | Outcome | Screenshot |
| ------- | ---------------- | ----- | --------- |
| Register | A new user can create a user profile | Pass | <img width="1237" alt="image" src="https://github.com/user-attachments/assets/b24529b0-dfcb-437e-80b2-92dc6d45a021"> |
| Login | An existing user can log in to the site and once logged in the message confirming this remains in the navbar | Pass | <img width="735" alt="image" src="https://github.com/user-attachments/assets/5dfc33f4-4821-48c8-bee7-5796324fc6e2"> |
| New post | An authorised user can create a new post | Pass | <img width="1229" alt="image" src="https://github.com/user-attachments/assets/59ff97d2-eb1f-49d9-b71a-3ba2b1b6109d"> |
| Delete own post | A  logged in user can delete their own posts, a second screen asks if they are sure | Pass | <img width="1229" alt="image" src="https://github.com/user-attachments/assets/af07467b-721a-4155-a6a8-cb8edf4baadc"> |
| Cannot delete other posts | A user cannot delete another users post | Pass | <img width="1230" alt="image" src="https://github.com/user-attachments/assets/40156028-8b24-493a-aa2f-2403197a39c0"> |
| Leave a comment | A user that is logged in can leave a comment on any post | Pass | <img width="1200" alt="image" src="https://github.com/user-attachments/assets/80513593-e75b-4615-a9a3-f562ed402e5d"> |
| Edit or delete own comment | A user that is logged in can edit or delete their own comment | Pass | <img width="1186" alt="image" src="https://github.com/user-attachments/assets/a13f2415-6ada-4084-9a25-05a3b28132d2"> |
| Cannot edit or delete other comments | A user that is logged in cannot edit or delete another users comments | Pass | <img width="1180" alt="image" src="https://github.com/user-attachments/assets/fba9bd36-744b-4545-8085-b605a4967ac6"> |
| Comment counter | The comment counter shows how many comments have been made on a post (Page made need to be reloaded) | Pass | <img width="1187" alt="image" src="https://github.com/user-attachments/assets/34309824-69c3-4ad9-9abb-9f526302bdab"> |
| Next/previous | Only 6 posts will be displayed on the home page. To see more a user must press the next button, which will then display the next 6 posts. Can go back a page by pressing previous. | Pass | <img width="1197" alt="image" src="https://github.com/user-attachments/assets/48cfcfe9-9e76-427e-8959-651d4a018af2"> |
| Logout | A user can log out, a second screen confirms this is what they want | Pass | <img width="1244" alt="image" src="https://github.com/user-attachments/assets/a2b8ad4f-96ca-406e-b767-1b6f3d3e1f19"> |
| Not logged in | If not logged in a user cannot add a post, comment, or edit any of their existing posts or comments | Pass | <img width="1199" alt="image" src="https://github.com/user-attachments/assets/5d109f47-0533-4fc9-89eb-0b08d75b1d3a"> |
| Pop up messages | All pop up messages show the users previous action | Pass | <img width="1219" alt="image" src="https://github.com/user-attachments/assets/564e5244-7be6-470a-8aba-2949df606a10"> |

## Lighthouse Audit Tool

I've tested my app using the Lighthouse tool to check for any major issues. Some of the scores could be better, but overall they are ok.

Home:

<img width="1370" alt="image" src="https://github.com/user-attachments/assets/4d4a0ca7-49b2-4815-8fb7-544beb35dbf4">

About:

<img width="1354" alt="image" src="https://github.com/user-attachments/assets/b5176fb0-a7cf-4519-876f-6dc50166d8ac">

Individual Post:

<img width="1349" alt="image" src="https://github.com/user-attachments/assets/73dce496-0c12-4d27-af7f-2c28224dca41">

Register:

<img width="1354" alt="image" src="https://github.com/user-attachments/assets/65ff6539-aba8-4d0e-94b1-3c726e7d44dc">

Login:

<img width="1359" alt="image" src="https://github.com/user-attachments/assets/8532739e-9aea-4deb-ab4f-2c2076f0987b">

## Responsive Design

I have tested my app on a MacBook Air with a 13" screen, an additional 16" monitor and on a Samsung Galaxy 7 mobile. I have used Chrome dev tools to look at a tablet sized screen.
Overall the app looks as it should accross all screen sizes.
The main areas of responsive design are the home page and the view for an individual post.
The home page when viewed as a desktop will show 6 posts in 2 rows of 3. A tablet will show 3 rows of 2 and a mobile will show a single column of posts.
When viewing an individual post the image is no longer visible on a mobile.
Another slight change for mobile devices is the layout of the navbar and title banner.

Laptop Home Page:

<img width="1431" alt="image" src="https://github.com/user-attachments/assets/9e755fc6-05d3-4ef1-b672-1a4b0ad45316">

Tablet Home Page:

<img width="406" alt="image" src="https://github.com/user-attachments/assets/25055c7d-bb3c-44cf-b264-11271a7d9039">

Mobile Home Page:

<img width="274" alt="image" src="https://github.com/user-attachments/assets/b2eaa7e6-5794-4850-b6f9-ad499f02a254">

Mobile Title and Navbar: 

<img width="287" alt="image" src="https://github.com/user-attachments/assets/881845e2-0b79-46eb-9097-b9ffcee642b0">

Tablet Title and Navbar:

<img width="415" alt="image" src="https://github.com/user-attachments/assets/1178352d-6f54-44ee-9b02-4fe88a71cdc1">

Laptop Title and Navbar:

<img width="1440" alt="image" src="https://github.com/user-attachments/assets/53bd49f0-91f5-4a11-9b80-367a9e0dedb5">

Laptop Individual Post:

<img width="1414" alt="image" src="https://github.com/user-attachments/assets/934d5bc5-deb8-41b7-8392-0f0b261dc350">

Tablet Individual Post:

<img width="410" alt="image" src="https://github.com/user-attachments/assets/bec37205-395e-4b80-907a-69684e48e60d">

Mobile Individual Post:

<img width="272" alt="image" src="https://github.com/user-attachments/assets/a9d1b320-99fe-4879-96a7-1a07c9242831">

# Tools and Technologies:

The technologies implemented in this app included HTML5, CSS, Bootstrap, Python and Django.

* Python used as the back-end programming language
* Django for the user authorisation templates
* Git used for version control
* GitHub used for secure online code storage
* Gitpod used as a cloud-based IDE for development.
* Bootstrap used for pre-built components.
* FontAwesome was used for the social media icons.
* Code Institute Database used as the Postgres database.
* Heroku used for hosting the deployed back-end site.
* Balsamiq used for the wireframes in the planning stage.
* LucidChart used to create the user flow diagram.
* Excel for my database diagram.

* Google and Chat GPT used when querying an error message.

# Languages Used:
* HTML5
* CSS
* Python

# Deployment:

I have used Heroku to deploy the project following the below steps. The link for the deployed project is https://county-cricket-blog-a93042f7114f.herokuapp.com/

## Deployment Steps:

### Create the Heroku App

- Create a Heroku account or login if you already have one.
- Once in the Heroku Dashboard, click on 'New' and then select 'Create New App'.
- Choose a unique name for your project, for instance "County Cricket Blog".
- Select the EU region.
- Click on "Create App".
- In the "Deploy" tab, choose GitHub as the deployment method.
- Connect your GitHub account and find/connect your GitHub repository.

### Set Up Environment Variables

- Create an `env.py` in the top level of the Django app.
- Import `os` in `env.py`.
- Set up necessary environment variables in the `env.py`, including the secret key and database URL.
- Update `settings.py` to use environment variables for secret key and database.
- Configure environment variables in the Heroku "Settings" tab under "Config Vars".
- Migrate the models to the new database connection in the terminal.
- Configure static files and template directories in `settings.py`.
- Add Heroku to the `ALLOWED_HOSTS` list.

### Create a Procfile and Push Changes

- Create a `Procfile` in the top level directory.
- Add the command to run the project in the `Procfile`.
- Add, commit, and push the changes to GitHub.

### Heroku Deployment

- In Heroku, navigate to the Deployment tab and deploy the branch manually.
- Monitor the build logs for any errors.
- Upon successful deployment, Heroku will display a link to the live site.
- Complete further testing on the live site and amend code if needed.

### Forking the Repository

Forking the GitHub Repository allows you to create a copy of the original repository and then make changes without affecting the original.

- Log in to GitHub or create an account.
- Visit the [repository link](https://github.com/jambardev/County-Cricket-Tour-Blog).
- Click on "Fork" at the top of the repository.

### Creating a Clone of the Repository

Creating a clone enables you to make a local copy of the repository.

- Navigate to the existing repository (https://github.com/jambardev/County-Cricket-Tour-Blog).
- Click on the <>Code button.
- Select the "HTTPS" option under the "Local" tab and copy the URL.
- Open your terminal and change the directory to your desired location.
- Use `git clone` followed by the copied repository URL.

# Bugs:

As with all developers I encountered several bugs when developing my project. The main one was to do with my post model. Originally I had a status field with the option for a post to be saved as a draft. However when draft was selected there was nowhere for the draft post to go. After a bit of trial and error I decided to remove this as an option so in the current version there is no status field. I also encountered some issues that were out of my control to do with the database which made the final stages of the project quite challenging.

An issue was also identified with the authorisation of users being overrided by copying and pasting the URL. I was able to solve this issue using login decorators for each view where it was required.

# Credits:

* My main resource for this project, particularly at the start when getting set up was the Code Institure project I think Terefore I Blog. For the most part I was able to follow the basic steps of setting up a blog project by following this walkthrough.

* For the Deployment section of this ReadMe document I have looked at the steps laid out by a fellow Code Institute student Katie Coughlan in her project Soujourn Scribbles for guidance. (https://github.com/katiejanecoughlan/sojourn-scribbles-V3/tree/main)

* I have also used Chat GPT, particularly to help establish the meaning of error codes.

* FontAwesome for the social media icons.

* Bootstrap for some basic CSS and button components.

* Balsamiq for the wireframes.

* LucidChart for the User Flow Diagram.

* The photo used on the site is my own.

* I would also like to thank for their help and guidance, the other members of my cohort, my facilitator Iris and the CI coding coach Martin.



































