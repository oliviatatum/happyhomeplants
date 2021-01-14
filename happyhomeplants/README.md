<h1>Happy Home Plants</h1>

<a href="https://happyhomeplants.herokuapp.com/">View Demo</a>

Happy Home Plants is an online shop selling indoor plants and pots.

<h2>UX</h2>
Happy Home Plants is aimed for people who want to buy plants and pots for their home. 

<h3>User Stories</h3>

<table>
<thead>
  <tr>
    <th>User Story </th>
    <th>User Type</th>
    <th>Wants to have the ability to..</th>
    <th>In order to...</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="4"><b>Viewing and Navigation</b></td>
  </tr>
  <tr>
    <td>1</td>
    <td>Customer</td>
    <td>Browse a list of products</td>
    <td>Choose some to purchase</td>
  </tr>
  <tr>
    <td>2</td>
    <td>Customer</td>
    <td>View individual product details</td>
    <td>Find the price, description and larger image of the item</td>
  </tr>
  <tr>
    <td>3</td>
    <td>Customer</td>
    <td>Easily identify special offers</td>
    <td>Find the best savings on items I may like to buy</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Customer</td>
    <td>Easily view my grand total</td>
    <td>Avoid spending too much/stick to a budget</td>
  </tr>
  <tr>
    <td colspan="4"><b>Registration and User Accounts</b></td>
  </tr>
  <tr>
    <td>5</td>
    <td>Site User</td>
    <td>Easily register for an account</td>
    <td>Be able to view profile including past orders</td>
  </tr>
  <tr>
    <td>6</td>
    <td>Site User</td>
    <td>Login/out quickly and simply</td>
    <td>Access my account</td>
  </tr>
  <tr>
    <td>7</td>
    <td>Site User</td>
    <td>Recover my password easily if I forget it</td>
    <td>Regain access if neccessary</td>
  </tr>
  <tr>
    <td>8</td>
    <td>Site User</td>
    <td>Receive an email confirmation after registering</td>
    <td>Ensure details are correct and registration was successful</td>
  </tr>
  <tr>
    <td>9</td>
    <td>Site User</td>
    <td>Have a personalised user profile</td>
    <td>Save payment information and order history</td>
  </tr>
  <tr>
    <td colspan="4"><b>Sorting and Searching</b></td>
  </tr>
  <tr>
    <td>10</td>
    <td>Shopper</td>
    <td>Sort and Filter the available products</td>
    <td>Sort products by category&nbsp;&nbsp;or price etc</td>
  </tr>
  <tr>
    <td>11</td>
    <td>Shopper</td>
    <td>Sort individual categories of products</td>
    <td>Find the best rated product of a category or sort by name or price</td>
  </tr>
</tbody>
</table>

<h3>Wireframes</h3>
<a href="happyhomeplants/pdfs/happyhomeplants.pdf">Wireframe 1 - Home page</a>
<a href="happyhomeplants/pdfs/happyhomeplants.pdf">Wireframe 2 - Products page</a>


<h2>Features</h2>

<h3>Homepage and Navigation </h3>
The home page (and every other page) features a navigation bar with drop downs for the different categories: All 
Products, Plants, Pots, and Sale. Inside the plants category are further sub categories of Pet Friendly, Easy Care, 
Hanging Plants, Large Plants, Sale Items, and All Plants. Each link opens the products window with the products that 
belong in those categories. This is the same in the pots section, where we have Small, Medium and Large Pots. All 
products allows the user to open the products page with the products sorted by Name, Price, or Category. 
<h3>Products Page</h3>
On the products page, users can see the photo of each product, the name and the price. 
<h3>Products Details </h3>
When clicking on an individual product, the user is taken to a products details page, which renders the details of 
that product, including the product image, the product name, and an alternative name if applicable, to allow for 
plants that have two names, the price of the product and a product description. From here the user is able to select 
the quantity of the product if they wish to purchase it and add it to their basket. When the user adds an item to 
their basket, a toast appears from the top right corner where the user's basket link is located. 
<h3>Success Toast</h3>
Within this toast, the user gets a success message as well as a summary of what is in their basket, including an image of each item, 
its name, and its price. If they are below the spend threshold for free shipping, the toast will also contain a message 
telling them how much more they need to spend to get free shipping. Finally, the toast contains a link to the secure check out.

<h3>Basket</h3>
Upon Clicking secure check out in the toast, the user is taken to their basket. This can also be accessed via the 
basket link in the top right hand corner. On the basket page, each item in the basket is rendered with its image,
name, price and quantity, as well as quantity plus and minus buttons under each, and a button to update the amended
quantities. There is also the option to remove the item from the basket. Once the user is happy with their order, they
can click the secure checkout button, which takes them to the checkout page.
<h3>Checkout and Checkout Success</h3>
On the checkout page the user is given a brief summary of their order, and then a form for them to fill out their contact, 
shipping and payment details. If the user is an account holder, and is logged in, and has saved their details previously, 
some of these fields will be auto filled for their convenience. If any required field is either left blank or not filled out 
correctly, the user will get a message notifying them of the error and prompting them to fill in the correct information. Once 
the user's form is filled in correctly they can press the submit button. A loading overlay appears then the order details screen, 
where the user is shown a brief summery of their order, a toast success pops up, from the top right corner, and the user will receive
an email confirming their order. 

<h2>Technologies Used</h2>
<ul>
<li><a href="https://getbootstrap.com/">Bootstrap</a> - I used bootstrap for their grid functionality, responsiveness, toasts, as well as some of their pre built classes. </li>
<li><a href="ttps://fontawesome.com/">Fontawesome</a> - I used fontawesome to add icons to some of my buttons to improve UX </li>
<li><a href="https://fonts.google.com/">Googlefonts</a> - I used Googlefonts to find a web safe font </li>
<li><a href="https://html.com/html5/">HTML5</a> - the main content and templates for my site were writen in HTML5</li>
<li><a href="http://www.css3.info/">CSS3</a> - I used CSS3 to style the majority of the elements of my site</li>
<li><a href="https://www.javascript.com/">JavaScript</a> - I used JavaScript for some of the logic of my site</li>
<li><a href="https://jquery.com/">JQuery</a> - I used JQuery to make JavaScript functions less verbose and to simplify DOM manipulation.</li>
<li><a href="https://www.python.org/">Python</a> - Almost all of the logic of my site was written in Python</li>
<li><a href="https://heroku.com/">Heroku</a> - I used Heroku to deploy my website</li>
<li><a href="https://git-scm.com/">Git</a> - I used Git to run commands in the trminal and for version control</li>
<li><a href="https://github.com/">Github</a> - I used Github to deploy mite and for version control</li> 
<li><a href="https://www.djangoproject.com/">Django</a> - I used Django for my model template views</li>
<li><a href="https://django-allauth.readthedocs.io/en/latest/">allauth</a> - I used allauth to power my user authentication functionality</li>
<li><a href="https://django-crispy-forms.readthedocs.io/en/latest/">crispy forms</a> - I used crispy forms to improve the look and function of my forms</li>
<li><a href="https://stripe.com/gb">stripe</a> - I used stripe to power my checkout and payment functionality</li>
</ul>


<h2>Deployment</h2>

Throughout my project I used git for version control, using git add ., to add saved changes, git commit-m "*message*" to commit them to the repository
and git push to push them to github. Once my website was ready to be deployed, I created a Heroku app and used an AWS S3 bucket to store my static files
and media files. I linked these in settings.py and custom_storages.py, and created a superuser in the terminal. In the deploy tab on heroku I linked
the heroku to my github repository so I could push my changes to both simultaneously.
To run my code locally from the terminal I type python3 manage.py runserver and open the server that pops up.
To run the app on heroku I click open app.

<h2>Credits</h2>
I used the <a href="https://github.com/ckz8780">Boutique Ado</a> project series as a guide while I worked on my project, and some of my code is adapted from code shown in the videos.
The descriptions of my products were taken from <a href="https://www.beardsanddaisies.co.uk/">Beards and Daisies</a>
The images were all found on google images.

<h2>Acknowledgements</h2>
Thank you to the tutors for all their help and support while I was working on this project.
