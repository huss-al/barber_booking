# Django Barber Shop Booking System

## Table of Contents
- [User Experience (UX)](#user-experience-ux)
  - [User Stories](#user-stories)
- [Features](#features)
  - [Existing Features](#existing-features)
    - [Nav Bar (Collapsable)](#nav-bar-collapsable)
    - [Landing/Home Page](#landinghome-page)
    - [Booking Page](#booking-page)
    - [Admin Page](#admin-page)
    - [Footer](#footer)
  - [Future Features](#future-features)
    - [Email Notification](#email-notification)
    - [Custom Booking Form](#custom-booking-form)
    - [Google Reviews Carousel](#google-reviews-carousel)
- [Design](#design)
  - [Images](#images)
  - [Colour Scheme](#colour-scheme)
  - [Wireframes](#wireframes)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries-programs-used)
- [Validator Testing](#validator-testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Testing](#testing)


## User Experience (UX)

### User Stories
1. As a user I want to View the home page with navigation bar and footer so I can easily navigate through the website.
2. As a user I want to view the "Services & Prices" page so I can see the services offered and their prices.
3. As a user I want to view the "Gallery" page with pictures so that I can see images of the barber shop and its work.
4. As a user I want to view the "About Us" page so that I can learn more about the barber shop.
5. As a user I want to access the "Contact Us" page with a contact form so that I can reach out to the barber shop for inquiries.
6. As a user I want to click the "BOOK NOW" button so that I can choose a barber and service and book on them on a date and time that suits me.
7. As a user I want to register for an account so that I can book appointments and manage my bookings.
8. As a user I want to log in to my account so that I can access my booking details and manage my profile.
9. As a user I want to see social media icons in the footer I can easily access the barber shop's social media pages.
10. As a user I want to view available time slots for my chosen barber and service I can choose a convenient time for my appointment. 
11. As a user I want to see relevant links in the footer I can quickly find important information and navigate the website more efficiently.
12. As an admin I want to log in to the admin panel so that I can manage the website's content.
13. As an admin I want to edit services and prices so that I can keep the services and prices up to date.
14. As an admin I want to add, and remove pictures in the gallery so that I can update the visual content of the website.
15. As an admin I want to add and remove barbers who work at the shop so that I can remove barbers who don't work there anymore and add new barbers.
16. As an admin I want to manage user accounts and bookings so that I can assist users with their bookings and account-related issues. 

<p align="center">
<img src="static/images/Screenshot 2024-07-14 at 12.41.41.png" width="600" height="100%">
</p>


## Features

### Existing Features

#### Nav Bar (Collapsable)
- Desktop Nav bar 

<p align="center">
<img src="static/images/Desktop navbar.png" width="600" height="100%">
</p>



- Mobile Nav bar 
<p align="center">
<img src="static/images/Mobile navbar.png" width="600" height="100%">
</p>


- Mobile Nav bar - Collapsed 
<p align="center">
<img src="static/images/Mobile navbar collapsed.png" width="600" height="100%">
</p>

#### Landing/Home Page


- Video at the top of the page.
<p align="center">
<img src="static/images/Video feature.png" width="600" height="100%">
</p>


- Buttons on the landing page: GALLERY, PRICES, CONTACT US, GOOGLE REVIEWS, BOOK NOW.
<p align="center">
<img src="static/images/homepage buttons.png" width="600" height="100%">
</p>


- Google reviews section.

<p align="center">
<img src="static/images/homepage buttons 2.png" width="600" height="100%">
</p>


#### Booking Page


- Dropdown to choose cut type.

<p align="center">
<img src="static/images/Booking from cut type drop.png" width="600" height="100%">
</p>


- Dropdown to select barber (client's choice).

<p align="center">
<img src="static/images/Booking form barber drop.png" width="600" height="100%">
</p>

- Dropdown time slots in 15-minute intervals with selection restricted to opening times (9-6).

<p align="center">
<img src="static/images/Booking form time drop.png" width="600" height="100%">
</p>


#### Admin Page

- Admin can add cut type name, price, and duration from the admin page using the home app, which will reflect on the main services & prices page.

<p align="center">
<img src="static/images/Home app cut type.png" width="600" height="100%">
</p>

<p align="center">
<img src="static/images/home app CUT TYPE edit .png" width="600" height="100%">
</p>


- Admin can upload images in the admin page, which will be displayed on the main gallery page.

<p align="center">
<img src="static/images/Home app gallery.png" width="600" height="100%">
</p>

<p align="center">
<img src="static/images/GALLERY edit.png" width="600" height="100%">
</p>

- Admin can add About Us image and text, which will be displayed on the main About Us page.

<p align="center">
<img src="static/images/home app about us.png" width="600" height="100%">
</p>

<p align="center">
<img src="static/images/ABOUT US edit.png" width="600" height="100%">
</p>


- Cut Type in the appointments app, differing from the home app, to offer separate services for walk-ins and booked appointments.

<p align="center">
<img src="static/images/Appointment app cut type.png" width="600" height="100%">
</p>

<p align="center">
<img src="static/images/appointment CUT TYPE  edit.png" width="600" height="100%">
</p>


- Admin can add barber details, which will display on the home page under 'Meet Our Barbers' and update the barber choices on the booking page.

<p align="center">
<img src="static/images/Barbers app Barbers.png" width="600" height="100%">
</p>

<p align="center">
<img src="static/images/BARBERS edit.png" width="600" height="100%">
</p>


- Contact messages show messages sent by users via the contact form.

<p align="center">
<img src="static/images/home app Contact us.png" width="600" height="100%">
</p>



#### Footer
- Featured on all pages and identical on each page for consistency.
- Contains three sections:
  - Logo and social media icons.
  - Useful links: Home, Services, Gallery, About Us.
  - Contact us with address and phone number.
  - Opening hours.

### Future Features

#### Email Notification
- Email notification for admin and user upon registration, contact form submission, booking, editing, and cancelling an appointment.

#### Custom Booking Form
- Custom booking form with dynamic availability based on selected service and barber.

#### Google Reviews Carousel
- Integration of live Google reviews carousel on the home page.

#### Admin control over home page
- Admin will be able to also upload/delete the video on the top of the home page as well as the welcome message.


## Design

### Images
- Images and video sourced from [Pexels](https://www.pexels.com/).
- Logo created using [Logo.com](https://www.logo.com/).
- Screenshot: ![Insert screenshots of various images used](path/to/screenshot)

### Wireframes

#### Home page
<p align="center">
<img src="static/images/Wireframe-home page.png" width="600" height="100%">
</p>

#### Services & Prices page
<p align="center">
<img src="static/images/Wireframes-services page.png" width="600" height="100%">
</p>

#### Gallery page
<p align="center">
<img src="static/images/Wireframes-gallery page.png" width="600" height="100%">
</p>

#### About Us page
<p align="center">
<img src="static/images/Wireframes-about us page.png" width="600" height="100%">
</p>

#### Contact Us page
<p align="center">
<img src="static/images/Wireframes-contact us page.png" width="600" height="100%">
</p>

#### Login page
<p align="center">
<img src="static/images/Wireframes-login page.png" width="600" height="100%">
</p>

#### Register page
<p align="center">
<img src="static/images/Wireframes-register page.png" width="600" height="100%">
</p>

#### Booking page
<p align="center">
<img src="static/images/Wireframes-booking page.png" width="600" height="100%">
</p>

#### Booking Confirmation page
<p align="center">
<img src="static/images/Wireframes-booking confirmation.png" width="600" height="100%">
</p>



## Technologies Used

### Languages Used
- HTML5
- CSS3
- Python

### Frameworks, Libraries & Programs Used
- Git
- GitHub
- Gitpod
- Django
- Cloudinary
- Bootstrap
- Google Fonts
- Font Awesome
- Balsamiq
- VS Code

## Testing

### Validator Testing
- HTML Validator

#### Home
<p align="center">
<img src="static/images/home.html validator.png" width="600" height="100%">
</p>

#### Services & Prices
<p align="center">
<img src="static/images/services.html .png" width="600" height="100%">
</p>

#### Gallery
<p align="center">
<img src="static/images/gallery.png" width="600" height="100%">
</p>

#### About Us
<p align="center">
<img src="static/images/About Us.png" width="600" height="100%">
</p>

#### Contact Us
<p align="center">
<img src="static/images/Contact Us.png" width="600" height="100%">
</p>

#### Register
<p align="center">
<img src="static/images/register.png" width="600" height="100%">
</p>

#### Login
<p align="center">
<img src="static/images/login.png" width="600" height="100%">
</p>

#### Log out question
<p align="center">
<img src="static/images/logout question.png" width="600" height="100%">
</p>

#### Manage Bookings
<p align="center">
<img src="static/images/manage bookings.png" width="600" height="100%">
</p>

#### Book Now 
<p align="center">
<img src="static/images/booking page.png" width="600" height="100%">
</p>

#### Booking Success 
<p align="center">
<img src="static/images/booking success page.png" width="600" height="100%">
</p>

#### Edit Booking
<p align="center">
<img src="static/images/edit booking.png" width="600" height="100%">
</p>

#### Cancel Booking
<p align="center">
<img src="static/images/cancel booking.png" width="600" height="100%">
</p>

- CSS Validator

<p align="center">
<img src="static/images/CSS validator.png" width="600" height="100%">
</p>


## Deployment
- Deployed through Heroku.


## Credits

- ChatGPT
- Stack Overflow
- Ludiflex (Login Form) - [Ludiflex YouTube Video](https://www.youtube.com/watch?v=KWIM5FuUJ8U&t=1s)


## Testing
