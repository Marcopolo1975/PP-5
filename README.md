# E Shop

E Shop is an e-commerce store . The site is targeted towards users who want to shop conveniently from home and get the products delivered to home.
The site provides a seamless online shopping experience, offering a wide range of high-quality products at competitive prices.

Users can browse and purchase a wide range of products or check out the different types of Products and make an enquiry. They can also look at images and testimonials of other Customers or leave a testimonial if they wish.

The payment system uses Stripe. Please note that this website is for educational purposes do not enter any personal credit/debit card details when using the site.

To test this system, test card details can be used. A list of these can be found in Stripe's documentation [here](https://stripe.com/docs/testing#cards).

The live link can be found here - [E Shop](https://e-shop-app-0892571914c8.herokuapp.com/)

![Site Mockup](docs/readme_images/site_mockup.png)

- [User Experience (UX)](#user-experience--ux-)
  * [User Stories](#user-stories)
  * [Design](#design)
    + [Colour Scheme](#colour-scheme)
    + [Imagery](#imagery)
    + [Fonts](#fonts)
    + [Wireframes](#wireframes)
- [Agile Methodology](#agile-methodology)
- [Database Schema](#database-schema)
- [Security Features and Defensive Design](#security-features-and-defensive-design)
  * [User Authentication](#user-authentication)
  * [Form Validation](#form-validation)
  * [Database Security](#database-security)
  * [Custom error pages:](#custom-error-pages-)
- [Features](#features)
  * [Header](#header)
  * [Footer](#footer)
  * [Home Page](#home-page)
  * [User Account Pages](#user-account-pages)
  * [Profile](#profile)
  * [Products](#home-decor--products-)
  * [Product Detail](#product-detail)
  * [Bag](#bag)
  * [Checkout](#checkout)
  * [Testimonials](#testimonials)
  * [Customer Reviews ](#testimonials)
  * [Contact Form](#contact-form)
  * [Enquiries Dashboard](#enquiries-dashboard)
  * [Error Pages](#error-pages)
- [Business Model](#business-model)
- [Marketing Strategy](#marketing-strategy)
  * [SEO](#seo)
  * [Content marketing](#content-marketing)
  * [Social Media Marketing](#social-media-marketing)
  * [Email Marketing](#email-marketing)
- [Testing](#testing)
- [Deployment - Heroku](#deployment---heroku)
- [AWS Set Up](#aws-set-up)
- [Forking this repository](#forking-this-repository)
- [Cloning this repository](#cloning-this-repository)
- [Languages](#languages)
- [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>





## User Experience (UX)

A visitor to E Shop would be someone who is most likely an adult who is interested in buying Quality products at reasonable prices conviniantly.

### User Stories

#### EPIC | Viewing and Navigation
- As a Site User, I can intuitively navigate around the site so that I can find content.
- As a Site User, I can view a list of products so that I can select a product to view.
- As a shopper, I can click on a product so that I can read the full product details.
- As a shopper, I can view a specific category of products so I can browse the type of products I'm looking for.
- As a shopper, I can search all products so that I can find what I am looking for.
- As a shopper, I can sort all products so that I can view products based on price or title.
- As a site user, I can view a list of Products so I can understand the quality and discription of the Product and make an enquiry if desired.
- As a site user, I can read testimonials left by other customers so I see what feedback they gave to their shopping experience with the store.
- As a site user, I can view pictures and the read the Views of other customers about the products and overall shopping experience with the Store so that I can      see quality of the products and credibility of the store and build trust on the Store.

#### EPIC | User Account and Profile
- As a site user, I can register an account so that I can have a personal account.
- As a site user, I can log in or log out of my account so that I can keep my account secure.
- As a site user, I can see my login status so that I know if I'm logged in or out.
- As a site user, I can save my personal details in my user profile so that I do not have to fill them out for future orders.
- As a site user, I can view my order history so that I can remember what purchases I've made.
- As a site user, I can recover my password in case I forget it so that I can recover access to my account.

#### EPIC | Purchasing
- As a shopper, I can add a number of products in different quantities to my shopping bag so that I can purchase them all together when I am ready.
- As a shopper, I can view a running total of my shopping bag as I am shopping so that I can see how much it costs in total.
- As a shopper, I can view the contents of my shopping bag at any time so I can see what is included and the total cost.
- As a shopper, I can adjust the quantity of individual products in my bag so that I can easily make changes before I purchase.
- As a shopper, I can see a summary of my shopping cart when I checkout so that I know what products are included and the total cost before I commit to purchasing.
- As a shopper, I can easily enter my payment information securely so that I can purchase my chosen products quickly with no issues.
- As a shopper checkout as a guest so I don't have to sign up for an account.
- As a shopper, I can view an order confirmation after checkout so that I know my purchase was successful.
- As a shopper, I can receive an email confirmation of my order so that I have a record of my purchase.


#### EPIC | Admin & Store Management
- As a store owner, I can add/edit/delete products through an easy-to-use interface so that I can manage the store's contents.
- As a site owner, I can view/read/ customer reviews through an easy-to-use interface so that I can manage the site's contents.
- As a site owner, I can add/delete images and description of products so that I can manage the site's contents.
- As a site owner, I can view, read, Reply and delete customer enquiries on The webpage without going to Admin page.

#### EPIC | User Interaction
- As a site user, I can submit an enquiry form so that I can enquire about a Product.
- As a site user, I can add / edit / delete a testimonial in relation to my perchase experience so that I can give my feedback.
- As a site user, I can add / edit / delete a review and give Rating to Products so that I can express my satisfaction about a product and the Store.

#### User stories not yet implemented

The following user stories were scoped out of the project due to time constraints and labelled as "Won't Have" on the project board on Github. It is intended that these user stories will be implemented at a later date.

- As a shopper, I can add products to my saved items so that I can go back and view them at a later date.
- As a shopper, I can view my saved products so I can find them easily in the one location.


### Design

The site has a vibrant and clean design with the use of Orange and white color combination to give the idea of luxury and opulence. 
#### Colour Scheme
Colour palette from Coolors

![Colour Scheme](docs/readme_images/colour_scheme.png)

The colour scheme of the site is mainly Orange and White. The colours chosen are quite neutral in order to showcase the Products with minimal distraction. 

Great care was taken to establish a good contrast between background colours and text at all times to ensure maximum user accessibility.

#### Imagery
There is only one main static image on the site which is of a laptop and a shopping Cart on the home page. The color scheme of the site makes a good contrast with the main homepage image which largely consists of orange and White. The rest of the imagery will be uploaded by the site owner for individual products. 

#### Fonts
The Lato font is the main font used for the body of the website. This font was imported via Google Fonts. Sans Serif is the backup font, in case for any reason the main font isn't being imported into the site correctly.

#### Wireframes

<details>

 <summary>Home Page</summary>

![Home Page](docs/wireframes/landing-page.png)
</details>

<details>

 <summary>Product Details Page</summary>

![Product Details](docs/wireframes/Product-details.png)
</details>

<details>

 <summary>Customers Reviews</summary>

![Customers Reviews](docs/wireframes/reviews-page.png)
![Customers Reviews](docs/wireframes/add-review-page.png)
</details>

<details>

 <summary>Testimonials</summary>

![Testimonials](docs/wireframes/testimonials-Page.png)
</details>

<details>

 <summary>Contact</summary>

![Contact](docs/wireframes/Contact-page.png)
</details>

<details>

 <summary>Bag</summary>

![Shopping Bag](docs/wireframes/shopping-bag.png)
</details>

<details>

 <summary>Checkout</summary>

![Checkout](docs/wireframes/checkout.png)
</details>

<details>

 <summary>Order Confirmation</summary>

![Order Confirmation](docs/wireframes/order-confirmation.png)
</details>

<details>

 <summary>Enquiries</summary>

![Enquiries](docs/wireframes/Enquiries-page.png)
![Enquiries](docs/wireframes/enqury-page.png)
</details>

<details>

 <summary>Profile</summary>

![Profile](docs/wireframes/profile-page.png)
</details>

<details>

 <summary>Product Management</summary>

![Product Management](docs/wireframes/Products-manage-page.png)
</details>

<details>

 <summary>Sign Up </summary>

![Sign Up](docs/wireframes/signup.png)
</details>

<details>

 <summary>Log In</summary>

![Log In](docs/wireframes/Login-Page.png)
</details>

<details>

 <summary>Sign Out</summary>

![Sign Out](docs/wireframes/signout-page.png)
</details>

## Agile Methodology
Github projects was used to manage the development process using an agile approach. Please see link to project board [here](https://github.com/users/)


The 5 Epics listed above were documented within the Github project as Milestones. A Github Issue was created for each User Story which was then allocated to a milestone(Epic). Each User Story has defined acceptance criteria to make it clear when the User Story has been completed. The acceptance criteria are further broken down into tasks to facilitate the User Story's execution.

## Database Schema 

Two relational databases were used to create this site - during production SQLite was used and then Postgres was used for the deployed Heroku version. Below is an image of how the database models relate to each other:

![Database Schema](docs/readme_images/database_schema.png)

## Security Features and Defensive Design
### User Authentication

Where I have used Django's Class-based-views; Django's LoginRequired is used to make sure that any requests to access secure pages by non-authenticated users are redirected to the login page. Django's UserPassesTest is used to limit access based on certain permissions i.e. to ensure users can only edit/delete Testimonials for which they are the author or if the user is the superuser. If the user doesn't pass the test they are shown an HTTP 403 Forbidden error.

Where I have used function based views I have used Django's login_required and user_passes_test decorators to restrict access as required. 

### Form Validation
If incorrect or empty data is added to a form, the form won't submit and a warning will appear to the user informing them what field raised the error.

### Database Security
The database url and secret key are stored in the env.py file to prevent unwanted connections to the database. Stripe keys and wh secret are also stored in the env.py file. 

Cross-Site Request Forgery (CSRF) tokens were used on all forms throughout this site.

### Custom error pages:
Custom Error Pages were created to give the user more information on the error and to provide them with buttons to guide them back to the site.

400 Bad Request - E Shop is unable to handle this request.
403 Page Forbidden - Looks like you're trying to access forbidden content. Please log out and sign in to the correct account.
404 Page Not Found - The page you're looking for doesn't exist.
500 Server Error - Due to an internal error we are unable to process this request.
