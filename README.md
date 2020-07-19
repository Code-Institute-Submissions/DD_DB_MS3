# DD_DB_MS3
['My Vanity'](https://vanitymanager.herokuapp.com/), cosmetic manager (Milestone PJ 3 -CI FSC)

# My Vanity
Cosmetic Manager [(access here)](https://vanitymanager.herokuapp.com/)

**(MS Data Centric Development - Code Institute by Ángel González)**

This is a cosmetic manager, where you can add, edit, filter and sort your cosmetics. The WebApp is both available to be played in browser of portable device. The app supports users login and access to a database to store the entries.

---

## **Table of Contents**

1. [UX](#UX)
    * [User Stories](#User-Stories)
    * [Strategy](#Strategy)
    * [Wireframes](#Wireframes)
    * [Scope](#Scope)
    * [Structure](#Structure)
    * [Theming](#Theming)
2. [Features](#Features)
    * [Future Features](#Future-Features-Objectives)

3. [Testing](#Testing)
4. [Deployment](#Deployment)

    * [Tech Used](#Tech-Used)
    * [Github Pages](#Configuration-on-Heroku-Apps)
    * [Cloning Repository](#Cloning-the-GitHub-Repository)
    * [Running it localy](#Running-it-localy)

5. [Credits](#Credits)

    * [Images](#Images)
    * [Acknowledgements](#Acknowledgements)

6. [Contact](#Contact)

---
## UX
### User Stories
Users of this WebApp will be people wanting organize their amount of cosmetics and be able to access to it anywhere.

Examples could be (among many others):
* I'm on the shop and don't remember if I still own certain cosmetic or is over.
* I want to know the brand I use now because I mix it with the one I used before.
* I need to know when is my cosmetic going to perish because I need to buy replacement.

The site [(see full-size preview)](/packageapp/static/images/screencaptures/full-view-browser.png) is based on a flask templates system. This system consists of a "Base" and then different "Views" filling inside of it depending on the route taken by the user. The way this system works makes all transitions easy and smooth for the user, being highly intuitive; and in this specific WebApp, is supported with flashed prompts each time an action is completed, giving this way direct info to the user of progress made.

In the browser version, the user finds the calls to action in the center of the window [(see full-size preview)](/packageapp/static/images/screencaptures/full-view-browser.png) making it easier to focus on it and start engaging with the WebApp. In the portable device version, CTA's fill all the space [(see full-size preview)](/packageapp/static/images/screencaptures/full-view-phone.png).

Users also find the navbar deployable floating button with the menu in every view, [(see Features)](#Features), allowing easy an easy way for users to go to other views anytime they want.

### Strategy
The goal is that the user has a easy time inputting and/or editting their cosmetics and search and/or sort what they want in an intuitive way.

To achieve this, first, the design is clean and light and the theme used is composed of pastel colors [(see Theming)](#Theming). Secondly, and helped by the template system, the design is very stable and similar among all the views, getting to be familiar with the user in very few time.

The most ambitious goal, which wasn't part of the project itself due to requirements and time-frame, would be having a extrenal link to promoted products of certain kinds when the user's Vanity shows less than 5 products of said category, [(see Future Features)](#Future-Features-Objectives).

### Wireframes
Here are the first concept wireframes:

* [Index Page](/packageapp/static/wireframes/draft/Home.png "Index Page")

* [LogIn Prompt](/packageapp/static/wireframes/draft/LogIn.png "LogIn Prompt")

* Add and Edit forms: 

![Add Cosmetic](/packageapp/static/wireframes/draft/New_Prod.png "Add Cosmetic") 
![Edit Cosmetic](/packageapp/static/wireframes/draft/Edit_Prod.png "Edit Cosmetic") 

* [Search Cosmetics](/packageapp/static/wireframes/draft/Search_Result.png "Search Cosmetics")

Final concept wireframes:

* Index Page: 

    ![Browser-View](/packageapp/static/wireframes/idea/Home.png "Browser View")

* [LogIn Prompt](/packageapp/static/wireframes/idea/LogIn.png "LogIn Prompt")

* Add and Edit forms: 

    See [Features](#Features)

* [Search Cosmetics](/packageapp/static/wireframes/idea/Search_Result.png "Search Cosmetics")

### Scope
Considering the goals set at [Strategy](#Strategy), it has been necessary to create a very light display and I chosed to use a pastels based theme [(see Theming)](#Theming).

The project itself was very database oriented so I kept the scope smaller, focusing in the user experience of creating and managing its own micro-database.

Read more about future increase of Scope at [(Future Features)](#Future-Features-Objectives).

### Structure
Both in the browser and the portable device views structuring focus is on the simetry in the distribution of the CTA's and diferent displays. [(See full-size preview here)](/packageapp/static/images/screencaptures/full-view-browser.png), we will analize the device view:

  ![Full-view-phone](/packageapp/static/images/screencaptures/full-view-phone.png "Phone View")

The **navbar** floating button, displays on the top corner allways accesible.

The **CTA's or buttons** section, displays centered focusing attention.

The **messages** section, displays under the CTA's, avoiding also visual conflict with the background image. In the landing page acts as welcome message once logged, afterwards we will see about prompt flashed messages, [(see Features)](#Features).

### Theming
As mentioned, about the theming, coherence was a key issue in order to impact in a more intuitive and friendly UX.

The special font for the titles, messages and CTA's is [Satisfy](https://fonts.google.com/specimen/Satisfy) from Google Fonts. This font goes really well with the pastels theme. The font for the rest of the site is the default Materialize CSS, [Roboto](https://fonts.google.com/specimen/Roboto), which is very clear and ideal for the display of information.

The background picture, also used for the favicon, was taken and adjusted in [Canva](https://www.canva.com/).

Color palette, as mentioned before, sticks to pastel tones that are commonly associated with the cosmetic world.

---

## Features
As explained, this WebApp consists on a template system so let's focus on the different views:

* **Site Icon**: a personalized WebApp icon displays on the browser. Also, it appears in the case someone bookmarks the game page.

    ![Favicon](/packageapp/static/images/favicon.png "Favicon")

* **Navbar**: display position allways stays on the right top corner of the screen. Is composed of just material icons, although a tooltip displays when they are hovered over. Here we can see the user icon swap once logged in, preventing accidental shut down of the session.

    ![Navbar-loggedoff](/packageapp/static/images/screencaptures/floating-navbar.png "Navbar logged off") ![Navbar-loggedin](/packageapp/static/images/screencaptures/floating-navbar-off.png "Navbar logged in")

* **User system**: this system was needed to allow each user to create a "share" on the database and allow the items be personal and not accessed by others for editing or deletion. We also protected the views and user is asked to login in order to access any of the WebApp functions. Here we can see the login prompt:

    ![Sign In prompt](/packageapp/static/images/screencaptures/sign-in.png "Sign In prompt")

    *New?*: this sentence is linked to a [(SignUp form)](/packageapp/static/images/screencaptures/sign-up.png) for new users to proceed. At the same time this form is linked to the SignIn in case user already has an acc.

* **Add and Edit forms**: two of the main functionalities are both create cosmetics for your vanity and afterwards edit them in case you replace them, change the size, the due date, etc... Both forms have field validations and in the case of edition field are pre-filled by existent cosmetic information. Here are displayed the browser clipped versions, but click and you can see the [(portable device)](/packageapp/static/images/screencaptures/add-product-form-phone.png) display, although that one would need scrolling:

    ![Add Product](/packageapp/static/images/screencaptures/add-product-form.png "Add Product") ![Edit Product](/packageapp/static/images/screencaptures/edit-product-form.png "Edit Product")

    *About validation*: all field marked with * are required before submit is available. Specifically: datepickers are read-only to avoid text inputs, type and subtype fields are selectable to keep the database as organized as possible and integer fields have a range determined and is prompted to user in the case is not complied.

* **Vanity Display**: here is met the main functionallity of the WebApp. Browser preview:

    ![My Cosmetics](/packageapp/static/images/screencaptures/products-full-browser.png "My Cosmetics")

    *Search Bar*: the search bar is composed of three diferent options: search by brand, filter by type and sort by date (3 sort options). All the three fields are quite descriptive and they affect the output once the search button is clicked. Only extra feature to indicate is the hiding of the search by brand field in the smaller devices to allow the design to stay clean and symetric, check it out [(here)](/packageapp/static/images/screencaptures/products-phone.png).

    *CTA's*: the interactive buttons on this view all have text and icon, on smaller devices text hides, leaving the icon alone for better design.

    *Display Section*: products found for the user or following the filters applied are displayed in a card format with the types and brand as title and some relevant information underneath. Every card contains two cta's for edit and delete the item. One thing to remark is that when the display produces no results at all, the user is prompted to either try another search and go back to all its products display or add a new product, check it out [(here)](/packageapp/static/images/screencaptures/products-none-browser.png).

The whole site has response from small devices to larger screens, moving sections from sideways to top/bottom when needed to achieve the best display. It is not responsive on 4k at the moment.

### Future Features Objectives
Ordering the possibilities in a list of viability, considering both complexity and relevance:

1. Creating password recovery system in case user forgets. (LOW complexity / MED relevance)

2. Adding a e-mail notification system when a product is about to reach de due date (MED complexity / MED relevance)

3. Adding promoted items for companies each time a search in the user's vanity outputs less than 5 items. (HIG complexity / MED relevance)

---

## Testing
During the development phase, using VS Code and running a local server in a virtual enviroment made it very easy to adjust response and test the majority as was coded, via Developer Tools and terminal outputs.

After finishing the coding, used "HTML validator", "CSS lint" and "PEP 8 validator" checking for possible warnings or errors.

>Note: as a template system is being used for this project we need to obviate some html validation "issues".

**Global Display:** tests were made on browsers (Chrome, Edge, Firefox), tablets and phones ensuring responsiveness of the WebApp on every screen size. Some examples of portable devices used by testers involved or myself were:

 * Huawei Mate 9 Lite, Huawei GR5 2017
 * Apple iPhone 11
 * Apple iPhone 8
 * Samsung Galaxy A50
 * BQ Aquaris M10 Ubuntu Edition
 * Microsoft Surface 2
 
**Template Routes:** I can't stress enough the important that has been filling console log at the start of every route during the developement process to be able to trace were the crash happened when it did. The second usefull thing has been using print() inside and after conditional statements. The combination of both of this features made the testing and indentifying issues as easy as it gets. This methodology has been a constant untill the product was finished.

**Database CRUD:** creation, deletion and edition of items (cosmetics) in the database was tested the help of some Beta-testers. Once more, this is very important to really be able to find problems with wrong inputs using a wide range of users. In this specific case, using MongoDB Clusters, made it very easy to check how was data being recorded and modify your code if needed.

**Links:** a single external link is present. It was tested after deployment at GitHub Pages.

---

## Deployment
This site is temporarily hosted on Heroku Apps, [(access here)](https://vanitymanager.herokuapp.com/). 

Deployment on Heroku was made before submitting the project for final testing. The project was kept on a virtual enviroment on my end for testing and modifications, even though it was committed to GitHub and updated via GitBash on a frequent basis.

#### Tech Used
1. HTML5
2. CSS3
3. [Materialize CSS](https://materializecss.com/about.html)
4. Python
5. [MongoDB Clusters](https://cloud.mongodb.com/)
6. Flask + Jinja2 framework + flask-extensions [(see requirements.txt)](requirements.txt)

#### Configuration on Heroku Apps
1. Subscribe to Heroku and create your new app.
2. In your GitBash/Terminal go to your master directory.
3. Type **"heroku login"** and follow the prompts.
4. Once logged in, type **"git push heroku master"** and wait untill process finishes.
5. Once your app is loaded on Heroku, type **"heroku ps:scale web=1"** to set Heroku on basic level.
6. After scarce time, your app should be ready. Either follow your terminal prompted link or go to your Heroku profile.
7. Mind that this App needs access to a database and the "Config Vars" on your Heroku App must be set to satisfy the Config.py file.

#### Cloning the GitHub Repository
To run it on your local computer with a virtual enviroment, see under, the repository must be cloned beforehand.

1. Once on the repository locate the *Clone or Download* dropdown menu.
2. Copy either the HTTPS or SSH route to your clipboard.
3. Open *GitBash* and move to the folder where you want to place the cloned repository files.
4. Type **"git clone"**, **tap spacebar once** and then paste the route copied in your clipboar at *step 2*.
5. Press Enter to exec the command and the local cloned files will be created.

#### Running it localy
To run it on your local computer with a virtual enviroment, the repository must be cloned beforehand, see above.

1. Install python3 on your computer.
2. Access to the master directory in your terminal and type **"python3 -m venv venv"** to create a virtual enviroment called "venv" in this case (second venv on command).
3. After venv files are created, if you are using Mac/Linux type **"source venv/bin/activate"**, on Windows type **"venv\Scripts\activate"** instead.
4. Your terminal should be placed on your master directory but one level further in your virtual enviroment "venv".
5. Now you must indicate were is the Flask app accesing from, for that we type **"export FLASK_APP=mainfile.py"**, being "mainfile" the one you need. Please use "set" instead of "export" if you are using Windows.
6. Once the entry point is set, we can type **"flask run"** and the terminal will give us our local port to access the app live.

---

## Credits

All the ideas, materials displayed, database entry and all the site designs belong to Ángel González.

### Images
[*Canva.com*](https://www.canva.com/)

**Disclaimer:** This site and its contents or any portion thereof may not be reproduced or used in any manner whatsoever without the express written permission of the publisher except for the use of brief quotations as credits and/or recommendation. Copyright © 2020.

### Acknowledgements
Great help once more from the documentation of these two sites, you can really learn as you go and adapt their examples to your own code:

* [w3schools](https://www.w3schools.com/)
* [MDN](https://developer.mozilla.org/en-US/)
* [MongoDB](https://docs.atlas.mongodb.com/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)

Also a shoutout to my mentor on this project [Maranatha A. Ilesanmi](https://github.com/mbilesanmi) for providing guidance when needed.

---

## Contact

**E-mail:** a.cruzana88@gmail.com :technologist:
