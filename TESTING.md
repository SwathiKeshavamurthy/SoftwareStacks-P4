# Testing

This is the TESTING file for the [SoftwareStacks](https://software-stacks-442e4344b2ad.herokuapp.com/) website.

Return back to the [README.md](README.md) file.

## Testing  Table of Contents  
- [Testing](#testing)
  - [Testing  Table of Contents](#testing--table-of-contents)
  - [Validation](#validation)
      - [HTML Validation](#html-validation)
      - [CSS Validation](#css-validation)
      - [JavaScript Validation](#javascript-validation)
      - [Python Validation](#python-validation)
      - [CSS Validation](#css-validation-1)
      - [JavaScript Validation](#javascript-validation-1)
      - [Lighthouse Scores](#lighthouse-scores)
      - [Wave Accessibility Evaluation](#wave-accessibility-evaluation)
  - [Manual Testing](#manual-testing)
    - [User Input/Form Validation](#user-inputform-validation)
    - [Browser Compatibility](#browser-compatibility)
    - [Django Messages Implementation Testing](#django-messages-implementation-testing)
    - [User Story Testing](#user-story-testing)
    - [Responsiveness - Dev Tools/Real World Device Testing](#responsiveness---dev-toolsreal-world-device-testing)


## Validation 

To ensure the reliability, usability, and accessibility of Software Stacks, various validation methodologies were implemented. These tvalidations ensure that the application not only meets development standards but also provides a seamless user experience across different platforms and browsers. Below is an overview of the validation processes:

#### HTML Validation
- **Tool Used:** [HTML W3C Markup Validator](https://validator.w3.org/)
- **Purpose:** Validates the HTML code of the application to ensure it is free from syntax errors and adheres to the standards set by the World Wide Web Consortium (W3C).
- **Process:** All HTML pages of the Software Stacks are checked through the W3C validator to identify and fix any markup errors or warnings.

![HTML Screenshot](documentation/screenshots/html.JPG)

**HTML Validation Results**

Below is a table summarizing the HTML validation results for various pages of the Software Stacks website. This validation ensures that the HTML is up to standards, improving cross-browser compatibility, and enhancing SEO performance.

| HTML Source Code/Page        | Validation Results PDF                | Errors | Warnings |
|------------------------------|---------------------------------------|--------|----------|
| **Base Page**            | [View PDF](https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4/blob/main/documentation/validation/html/base.pdf) | 0      | 0        |
| **Home Page**     | [View PDF](https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4/blob/main/documentation/validation/html/index.pdf) | 0      | 0        |
| **About & Contact Page**     | [View PDF](https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4/blob/main/documentation/validation/html/aboutandcontact.pdf)| 0      | 0        |
| **Categories Page**          | [View PDF](https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4/blob/main/documentation/validation/html/category.pdf) | 0      | 0        |
| **Search Results Page**      | [View PDF](https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4/blob/main/documentation/validation/html/search.pdf)| 0      | 0        |
| **Register Page**            | [View PDF](https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4/blob/main/documentation/validation/html/signup.pdf) | 4    | 0        |
| **Login Page**               | [View PDF](https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4/blob/main/documentation/validation/html/signin.pdf) | 0      | 0        |
| **Logout Page**              | [View PDF](https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4/blob/main/documentation/validation/html/signout.pdf)| 0     | 0        |
| **Post Detail**              | [View PDF](https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4/blob/main/documentation/validation/html/postdetail.pdf)| 28      | 0        |
| **Add Stack Page**           | [View PDF](https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4/blob/main/documentation/validation/html/addpost.pdf)  | 0      | 0        |
| **My Bookmarks Page**        | [View PDF](https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4/blob/main/documentation/validation/html/mybookmarks.pdf)| 0   | 0        |
| **My Likes Page**            | [View PDF](https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4/blob/main/documentation/validation/html/mylikes.pdf) | 0      | 0        |
| **My Comments Page**         | [View PDF](https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4/blob/main/documentation/validation/html/mycomments.pdf)| 0   | 0        |
| **My Posts Page**            | [View PDF](https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4/blob/main/documentation/validation/html/myposts.pdf) | 0      | 0        |
| **404 Page**                 | [View PDF](https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4/blob/main/documentation/validation/html/404.pdf)   | 0      | 0        |

**Signup Page Errors** 

![Signup Page Error](documentation/validation/html/siguperror.JPG)

**Post Detail Page Errors**

![Post Detail Page Error](documentation/validation/html/collage.jpg)

**I tried to resolve the above errors of SignUp Page and Post Detail Page but there were from SUMMERNOTE. I asked a Tutor about this.** 

![tutor](documentation/validation/html/tutor.JPG)

- **Errors** are the actual HTML issues that need to be fixed as they may affect the functionality or appearance of the website.
- **Warnings** are generally suggestions for best practices, which are not critical but could improve the code efficiency or accessibility.

#### CSS Validation
- **Tool Used:** [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- **Purpose:** Ensures that the CSS code used across the platform adheres to the standards set by the W3C and is free of errors.
- **Process:** The CSS files are submitted to the W3C CSS Validator. Corrections are made based on feedback to improve performance and cross-browser compatibility.

![CSS Screenshot](documentation/screenshots/css.JPG)

**[CSS Validation Results PDF](https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4/blob/main/documentation/validation/html/css.pdf)**


#### JavaScript Validation
- **Tool Used:** [JSLint/JSHint](https://jshint.com/)
- **Purpose:** To detect errors and potential problems in the JavaScript code, making sure that all scripts run efficiently and are error-free.
- **Process:** JavaScript code is run through JSLint/JSHint to identify issues related to syntax, deprecated methods, and other inefficiencies.

Below is a table summarizing the JavaScript validation results for specific files within the Software Stacks website. 

| JavaScript File              | Results Screenshots               | Errors | Warnings |
|------------------------------|--------------------------------------|--------|----------|
| **comments.js**                  | ![screenshot](documentation/validation/commentjs.JPG)  | 0      | 0        |
| **like_bookmark.js**            | ![screenshot](documentation/validation/likejs.JPG) | 0  | 0        |
| **post.js**         | ![screenshot](documentation/validation/postjs.JPG) | 0 | 0        |


#### Python Validation
- **Tool Used:** [CI Python Linter](https://pep8ci.herokuapp.com/#)
- **Purpose:** Analyzes Python source code to identify coding errors, enforce a coding standard, and look for code smells.
- **Process:** Python code within Software Stacks is analyzed with Pylint to ensure adherence to coding standards and to improve code quality.

**SoftwareStacks - Project Module Python Validation Results**
| Python File   | Results Screenshots                        | Errors | Warnings |
|----------------------------|--------------------------------------------|--------|----------|
| **settings.py**            | ![screenshot](documentation/validation/settings.JPG) | 0      | 0        |
| **manage.py**            | ![screenshot](documentation/validation/manage.JPG) | 0      | 0        |
| **urls.py**                | ![screenshot](documentation/validation/ss-urls.JPG)     | 0      | 0        |
| **views.py**                | ![screenshot](documentation/validation/ss-views.JPG)     | 0      | 0        |
| **wsgi.py**                | ![screenshot](documentation/validation/ss-wsgi.JPG)     | 0      | 0        |
| **asgi.py**                | ![screenshot](documentation/validation/ss-asgi.JPG)     | 0      | 0        |

**Blog Module Python Validation Results**

| Python File                | Results Screenshots                        | Errors | Warnings |
|----------------------------|--------------------------------------------|--------|----------|
| **views.py**               | ![screenshot](documentation/validation/blog-views.JPG)   | 0      | 0        |
| **models.py**              | ![screenshot](documentation/validation/blog-models.JPG)  | 0      | 0        |
| **forms.py**               | ![screenshot](documentation/validation/blog-forms.JPG)   | 0      | 0        |
| **urls.py**                | ![screenshot](documentation/validation/blog-urls.JPG)| 0      | 0        |
| **admin.py**               | ![screenshot](documentation/validation/blog-admin.JPG)   | 0      | 0       |
| **apps.py**              | ![screenshot](documentation/validation/blog-apps.JPG)  | 0      | 0        |

**About Module Python Validation Results**

| Python File                | Results Screenshots                        | Errors | Warnings |
|----------------------------|--------------------------------------------|--------|----------|
| **views.py**               | ![screenshot](documentation/validation/about-views.JPG)   | 0      | 0        |
| **models.py**              | ![screenshot](documentation/validation/about-models.JPG)  | 0      | 0        |
| **forms.py**               | ![screenshot](documentation/validation/about-forms.JPG)   | 0      | 0        |
| **urls.py**                | ![screenshot](documentation/validation/about-urls.JPG)     | 0      | 0        |
| **admin.py**               | ![screenshot](documentation/validation/about-admin.JPG)   | 0      | 0        |
| **apps.py**              | ![screenshot](documentation/validation/about-apps.JPG)  | 0      | 0        |

#### CSS Validation
- **Tool Used:** [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- **Purpose:** Ensures that the CSS code used across the platform adheres to the standards set by the W3C and is free of errors.
- **Process:** The CSS files are submitted to the W3C CSS Validator. Corrections are made based on feedback to improve performance and cross-browser compatibility.

![CSS Screenshot](documentation/screenshots/css.JPG)

**[CSS Validation Results PDF](https://github.com/SwathiKeshavamurthy/SoftwareStacks-P4/blob/main/documentation/validation/css.pdf)**


#### JavaScript Validation
- **Tool Used:** [JSLint/JSHint](https://jshint.com/)
- **Purpose:** To detect errors and potential problems in the JavaScript code, making sure that all scripts run efficiently and are error-free.
- **Process:** JavaScript code is run through JSLint/JSHint to identify issues related to syntax, deprecated methods, and other inefficiencies.

Below is a table summarizing the JavaScript validation results for specific files within the Software Stacks website. 

| JavaScript File              | Results Screenshots               | Errors | Warnings |
|------------------------------|--------------------------------------|--------|----------|
| **comments.js**                  | ![screenshot](documentation/validation/commentjs.JPG)  | 0      | 0        |
| **like_bookmark.js**            | ![screenshot](documentation/validation/likejs.JPG) | 0  | 0        |
| **post.js**         | ![screenshot](documentation/validation/postjs.JPG) | 0 | 0        |

#### Lighthouse Scores
- **Tool Used:** [Google Lighthouse](https://en.wikipedia.org/wiki/Google_Lighthouse)
- **Purpose:** To assess the quality of web pages in terms of performance, accessibility, progressive web apps, SEO, and best practices.
- **Process:** Software Stacks is tested with Google Lighthouse, which provides a detailed report on various aspects of the site’s performance and offers recommendations for improvement.

| HTML Page / Source           |     Lighthouse Report Screenshot     | 
|------------------------------|--------------------------------------|
| **Home Page**                | ![screenshot](documentation/validation/lighthouse/home1.JPG) |  
| **About & Contact Page**     | ![screenshot](documentation/validation/lighthouse/aboutcontact.JPG) | 
| **Categories Page**          | ![screenshot](documentation/validation/lighthouse/catpa.JPG) |
| **Search Results Page**      | ![screenshot](documentation/validation/lighthouse/search.JPG) | 
| **Register Page**            | ![screenshot](documentation/validation/lighthouse/signup.JPG) | 
| **Login Page**               | ![screenshot](documentation/validation/lighthouse/signin.JPG) | 
| **Logout Page**              | ![screenshot](documentation/validation/lighthouse/signout.JPG) | 
| **Post Detail**              | ![screenshot](documentation/validation/lighthouse/examplepostdetail.JPG) | 
| **Add Stack Page**           | ![screenshot](documentation/validation/lighthouse/addpost.JPG) | 
| **My Bookmarks Page**        | ![screenshot](documentation/validation/lighthouse/bookmarks.JPG) | 
| **My Likes Page**            | ![screenshot](documentation/validation/lighthouse/liked.JPG) | 
| **My Comments Page**         | ![screenshot](documentation/validation/lighthouse/comments.JPG) | 
| **My Posts Page**            | ![screenshot](documentation/validation/lighthouse/posts.JPG) | 


#### Wave Accessibility Evaluation
- **Tool Used:** [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org/)
- **Purpose:** To ensure that the website is accessible to individuals with disabilities by identifying and suggesting fixes for web accessibility issues.
- **Process:** The Wave tool evaluates each page of Software Stacks to ensure it complies with accessibility standards like WCAG and Section 508.

![Wave Web Accessibility Evaluation Tool](documentation/validation/wave.JPG)

## Manual Testing

### User Input/Form Validation

Rigorous testing was conducted on all forms throughout Software Stacks to ensure all user inputs were validated correctly and feedback was provided where necessary.

**Form Validation**

| Feature            | Tested? | Action        | Expected Outcome | Pass/Fail | Screenshots |
|--------------------|---------|---------------|------------------|-----------|-------|
| Registration Form  | Yes     | Submit form   | User receives confirmation message and is redirected to the profile page | Pass      | ![screenshot](documentation/validation/testing/siginup.JPG)     |
| Login Form         | Yes     | Submit credentials | User is logged in and redirected to the homepage | Pass      | ![screenshot](documentation/validation/testing/signin.JPG)     |
| Add Stack Form          | Yes     | Create post   | Post is created and submitted for review | Pass      | ![screenshot](documentation/validation/testing/addpostfieldmissing.JPG)     |
| Contact Form  | Yes     | Submit form   | User receives confirmation message  | Pass      | ![screenshot](documentation/validation/testing/contactus.JPG)     |
| Comment Form       | Yes     | Submit comment | Comment is added to the post awaiting moderation | Pass      | ![screenshot](documentation/validation/testing/postingcommentas.JPG)     |

**User Input**

| Feature                               | Tested? | User Input Required           | User Feedback Provided                                                          | Pass/Fail | Notes on Fix (If Any) |
|---------------------------------------|---------|------------------------------|--------------------------------------------------------------------------------|-----------|----------------------|
| Navigation Links                      | Yes     | Click                        | Links redirect to corresponding pages. Hover effects indicate interactivity.    | Pass      | -                    |
| Home Page Posts                     | Yes     | Click                        | Clicked on posts take users to detailed views of posts. | Pass      | -                    |
| Sign Up Page                          | Yes     | Username/Password/Again Password/Email(optional)    | Validation prompts for incorrect input. Success message on account creation.    | Pass      | Tried to remove or move bullets for password rules, could not do it                   |
| Login Page                            | Yes     | Username and Password  | Correct credentials required for login. Error message for failed login attempt. | Pass      | -                    |
| Add Post and Submission                    | Yes     | Text/Image Upload(optional)            | Mandatory fields checked. Confirmation message upon successful submission.       | Pass      | Changed the add post FORM width, but did not work as expected                    |
| Comment Submission                    | Yes     | Text Input                   | Users can submit comments. Awaiting moderation message displayed.               | Pass      | -                    |
| Like/Bookmark Interaction             | Yes     | Click                        | Visual feedback on like/bookmark. Counts update accordingly.                    | Pass      | -                    |
| Search Functionality                  | Yes     | Text Input                   | Relevant search results displayed. Message for no results found.                 | Pass      | -                    |
| Contact Us Form Submission            | Yes     | Text Input                   | Contact details of the user is submitted.       | Pass      | -                    |
| Pagination Controls                   | Yes     | Click                        | Users can navigate through pages of posts.                                       | Pass      | -                    |
| Post Detail Interaction               | Yes     | Click on various elements    | Detailed view of post with comments and like/bookmark options.                  | Pass      | -                    |
| Mobile Navigation (Hamburger Menu)    | Yes     | Touch/Click                  | Responsive menu works on touch devices. Toggles correctly.                       | Pass      | -                    |
| Form Error Handling                   | Yes     | Invalid Inputs               | Forms handle errors with descriptive messages guiding the user.                  | Pass      | -                    |
| Logout Functionality                  | Yes     | Click                        | Users can log out successfully with a confirmation message.                      | Pass      | -                    |
| Footer Social Media Icons             | Yes     | Click                        | Social media icons link to external pages in a new tab.                          | Pass      | -                    |
| Responsive Design Elements            | Yes     | Resize/Change Orientation    | All elements resize and stack appropriately for different screen sizes.          | Pass      | -                    |
| Accessibility Features (e.g., ARIA)   | Yes     | Use of assistive technology  | ARIA labels and roles are present, ensuring accessibility compliance.            | Pass      | -                    |


### Browser Compatibility

The application was tested on the latest versions of major browsers to ensure cross-browser compatibility.

| Browser    | Tested? | Issues Found | Pass/Fail |
|------------|---------|--------------|-----------|
| Chrome     | Yes     | None         | Pass      |
| Firefox    | Yes     | None         | Pass      |
| Edge       | Yes     | None         | Pass      |

Certainly! Below is a sample table detailing how Django messages can be implemented and documented in the Software Stacks application, assuming we have different types of messages that inform the user of various actions or system states:

### Django Messages Implementation Testing

This table documents the Django messages used throughout the Software Stacks website to provide feedback to users after certain actions have been performed.

| Action Performed                      | Message Type | Message Text                                          | Implementation Location         |  Screenshots           |
|---------------------------------------|--------------|------------------------------------------------------|---------------------------------|---------|
| User Registration Success | Success   | "Welcome to Software Stacks! Your account is created." | After user form submission      | ![screenshot](documentation/validation/testing/signed-in-msg.JPG)   |
| Login Success  | Success      | "Logged in successfully. Welcome back!"  | After user authentication       | ![screenshot](documentation/validation/testing/signed-in-msg.JPG)   |
| Logout Action  | Success      | "You have been logged out successfully."   | After user clicks logout        |  ![screenshot](documentation/validation/testing/signed-out-msg.JPG)   |
| Post/Stack Submission Success            | Success      | "Your Post has been submitted for review."         | After submitting an article form|  ![screenshot](documentation/validation/testing/post-added-and-awaiting-msg.JPG)   |
| Post/Stack Review Status            | Success      | "Your Post has been submitted for review."         | After submitting an article form|  ![screenshot](documentation/validation/testing/post-pending-msg.JPG)   ![screenshot](documentation/validation/testing/post-rejected-msg.JPG)  ![screenshot](documentation/validation/testing/post-accepted-msg.JPG) |
| Comment Added                         | Success      | "Your comment has been added and is awaiting approval."| After submitting a comment     | ![screenshot](documentation/validation/testing/leavecomment.JPG) ![screenshot](documentation/validation/testing/postingas.JPG) ![screenshot](documentation/validation/testing/comment-awaiting-approval.JPG)   |
| Comment Updated                         | Success      | "Your comment has been Updated."| After updating a comment     |  ![screenshot](documentation/validation/testing/comment-updated-msg.JPG)   |
| Comment Deleted                         | Success      | "Your comment has been Deleted."| After deleting a comment     |  ![screenshot](documentation/validation/testing/post-deleted-succesfully-msg.JPG)   |
| Bookmark Added                        | Info         | "Post bookmarked. Find it in your bookmarks page."         | When a post is bookmarked       |  ![screenshot](documentation/validation/testing/bookmark-icon.JPG) ![screenshot](documentation/validation/testing/bookmarked-msg.JPG)   |
| Like Added                            | Info         | "You liked a post.Find it in your likes page."      | When a post is liked            |  ![screenshot](documentation/validation/testing/liked-icon.JPG) ![screenshot](documentation/validation/testing/liked-msg.JPG)   |
| Bookmark Removed                        | Info         | "Post bookmark removed. Removed from your bookmarks page."         | When a post is unbookmarked       |  ![screenshot](documentation/validation/testing/unbookmark-icon.JPG) ![screenshot](documentation/validation/testing/unbookmarked-msg.JPG)   |
| Like Removed                            | Info         | "You uniked a post.Removed from your likes page."      | When a post is unliked            |  ![screenshot](documentation/validation/testing/unliked-icon.JPG) ![screenshot](documentation/validation/testing/unliked-msg.JPG)   |
| Contact Us        | Info     | "Contact Submitted Successfully! I endeavour to respond within 2 working days."       | When Contact details is submitted.       | ![screenshot](documentation/validation/testing/conatct-submitted-msg.JPG) |
| Form Submission Missing Fields        | Warning      | "Please fill in all required fields."                 | Form validation fail            |  ![screenshot](documentation/validation/testing/missing.JPG)   |
| Search No Results                     | Info         | "No posts found matching your query."    | Search functionality            |  ![screenshot](documentation/validation/testing/search.JPG) ![screenshot](documentation/validation/testing/searched.JPG) ![screenshot](documentation/validation/testing/searchedposts.JPG) ![screenshot](documentation/validation/testing/sun.JPG) ![screenshot](documentation/validation/testing/nosun.JPG) |
| Post Edit Confirmation                 | Success      | "The content has been successfully edited."          | After editing post            |  ![screenshot](documentation/validation/testing/postupdated.JPG)   |
| Post Deletion Confirmation                 | Success      | "The content has been successfully deleted."          | After deleting post            |  ![screenshot](documentation/validation/testing/post-deleted-succesfully-msg.JPG)   |

### User Story Testing

Here's a detailed table showcasing the testing of various user stories associated with the Software Stacks project to reflect the progression of functionality implementation and testing:

| User Story ID | Title | Milestone | Tested? | Acceptance Criteria Met? | Pass/Fail |
|---------------|-------|-----------|---------|--------------------------|-----------|
| #1 | Browse without Logging in | Core Functionality | Yes | Visitors can browse the site without needing to log in | Pass |
| #2 | Open a Post | Core Functionality | Yes | Users can open and read individual posts | Pass |
| #3 | View comments | Core Functionality | Yes | Users can view comments on posts | Pass |
| #4 | Browse Categories | Enhanced User Experience | Yes | Users can browse posts categorized by topics | Pass |
| #5 | Account Registration | Core Functionality | Yes | New users can register for an account | Pass |
| #6 | Search Blog Posts | Enhanced User Experience | Yes | Users can search blog posts using keywords | Pass |
| #7 | View paginated list of posts | Enhanced User Experience | Yes | Users can view posts in a paginated format for easier navigation | Pass |
| #8 | Like Blog Posts | Core Functionality | Yes | Users can like blog posts to show appreciation | Pass |
| #9 | Bookmark Blog Posts | Core Functionality | Yes | Users can bookmark blog posts for later viewing | Pass |
| #10 | Comment on a post | Core Functionality | Yes | Users can add comments to posts | Pass |
| #11 | Modify or delete comment on a post | Community Interaction | Yes | Users can edit or delete their comments on posts | Pass |
| #12 | Manage posts | Core Functionality | Yes | Users can manage their posts through editing or deleting | Pass |
| #13 | Create drafts | Core Functionality | Yes | Users can create and save drafts | Pass |
| #14 | Approve comments | Content Management | Yes | Admins can approve user comments | Pass |
| #15 | Edit Existing Blog Post | Content Management | Yes | Authors can edit their posts to update or correct information | Pass |
| #16 | Inquiry via Contact Section | Could Have | Yes | Contact form is functional and sends inquiries correctly | Pass |
| #17 | Navigate to an about page | Could Have | Yes | Users can navigate to the About page from any section of the website | Pass |
| #18 | Delete Existing Blog Post | Could Have | Yes | Authors can delete their posts | Pass |
| #19 | Navigate easily | Core Functionality | Yes | Navigation is intuitive and straightforward | Pass |
| #20 | 'Register' and 'Login' buttons disappear after 'Login' | Core Functionality | Yes | Login and Register buttons manage correctly based on user authentication state | Pass |
| #21 | Create Project App | N/A | No | N/A | N/A |
| #22 | Software Stacks Blog | N/A | No | N/A | N/A |
| #23 | Deploying the Django Project on Heroku | N/A | No | N/A | N/A |
| #24 | Creating the Database in ElephantSQL | N/A | No | N/A | N/A |
| #25 | Read about the site | Future Considerations | No | N/A | N/A |
| #26 | Add and update the about text | Future Considerations | No | N/A | N/A |
| #27 | Contact Form Submission Feature (Registered User) | Community Interaction | Yes | Users can submit contact forms | Pass |
| #28 | Contact Form Submission Feature (Site Owner) | Community Interaction | Yes | Site owner can receive and manage contact submissions | Pass |
| #29 | Marking Contact Requests as "Read" | Future Considerations | No | N/A | N/A |
| #30 | Allow Registered user to Create New Posts | Content Management | Yes | Users can create new posts | Pass |
| #31 | Enable Post Modifications by Author/Post Owner | Content Management | Yes | Users can edit their own posts | Pass |
| #32 | Facilitate Removal of Outdated or Incorrect Posts | Content Management | Yes | Users can delete their own posts | Pass |
| #33 | Implement Comprehensive Testing | Content Management | Yes | All functionalities tested and documented | Pass |
| #34 | Enhance Data Validation | Enhanced User Experience | Yes | Data inputs are validated correctly across forms | Pass |
| #35 | Create Comprehensive Documentation | Core Functionality | Yes | Documentation covers all aspects of the project | Pass |

This table ensures all user stories have been tested against their respective milestones and functionalities, ensuring a comprehensive validation of the Software Stacks project before deployment.

### Responsiveness - Dev Tools/Real World Device Testing

Responsiveness and interactive elements were tested on various devices and through browser developer tools.

| Device/Method           | Features Tested | Pass/Fail |
|-------------------------|-----------------|-----------|
| Chrome DevTools         | All            | Pass      |
| Firefox Responsive Mode | All            | Pass      |
| Real iPhone XR          | Navigation, forms, posts | Pass |
| iPad               | Navigation, forms, posts | Pass |
| Real Android Device     | Navigation, forms, posts | Pass |

**Here are some images**

![screenshot](documentation/validation/testing/phone.JPG)
![screenshot](documentation/validation/testing/phoneL.JPG)
![screenshot](documentation/validation/testing/tab.JPG)
![screenshot](documentation/validation/testing/laptop.JPG)
![screenshot](documentation/validation/testing/laptopL.JPG)
