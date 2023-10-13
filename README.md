<h1 align="center" id="title">WriteSphere</h1>

<p align="center"><img src="https://socialify.git.ci/Karoll-e/writesphere_blog_website/image?font=Jost&amp;name=1&amp;owner=1&amp;pattern=Formal%20Invitation&amp;theme=Auto" alt="project-image"></p>

<p id="description">WriteSphere is a fully functional blog website developed using the Django framework. It offers a platform for users to create manage and share their thoughts ideas and stories through blog posts. This README provides an overview of the project its key features and how to get started.</p>

<br>
<h2>Project Screenshots:</h2>


<img src="https://gifs.com/gif/nyan-cat-at-4k-resolution-Kr128X" alt="project-screenshot" width="1080" height="1080/"> 

  
<h2>🧐 Features</h2>


Here are some of the project's best features:

*   <strong>User Authentication:</strong> The website includes secure user authentication with features like user registration login and password reset. Users can create accounts and log in to start blogging.
*   <strong>Profile Management:</strong> Registered users have their own profiles where they can add a profile picture update personal information and view their published posts.
  ![Captura de pantalla 2023-10-13 151422](https://github.com/Karoll-e/writesphere_blog_website/assets/141882497/81c97ed4-9e89-4424-bfcb-876f4b43f42d)

*   <strong>Post Creation and Categorization:</strong> Users can create new blog posts categorize them for easy navigation and format their content using a rich text editor.
  ![Captura de pantalla 2023-10-13 151304](https://github.com/Karoll-e/writesphere_blog_website/assets/141882497/6c5c346f-9635-4340-8f22-546d637a1270)
  ![Captura de pantalla 2023-10-13 151442](https://github.com/Karoll-e/writesphere_blog_website/assets/141882497/13b17d79-37b5-46ce-9612-ce10a59566da)


*   <strong>Post and Profile Editing:</strong> Users can edit and delete their own posts as well as update their profile information including the profile picture.
  ![Captura de pantalla 2023-10-13 151900](https://github.com/Karoll-e/writesphere_blog_website/assets/141882497/93bdbd78-a986-4e3b-b687-7bc930ce20e3)

*   <strong>Pagination:</strong> The website implements pagination to handle many blog posts efficiently ensuring a smooth user experience.
*   <strong>Database Schema:</strong> The project incorporates a well-structured database schema to efficiently manage user profiles blog posts and categories.
*   <strong>Bootstrap Integration:</strong> Bootstrap framework is integrated into the project to enhance styling and maintain layout consistency throughout the website.
*   <strong>Class-Based Views:</strong> Django's Class-Based Views handle different aspects of the application promoting code modularity and maintainability. 

<h2>🛠️ Installation Steps:</h2>


<p>1. Clone the Repository:</p>

```
git clone https://github.com/Karoll-e/writesphere_blog_website.git
```

<p>2. Move to the coned folder:</p>

```
cd writesphere_blog_website
```

<p>3. Create a Virtual Environment:</p>

```
python -m venv venv
```

<p>4. Activate the Virtual Environment:</p>

*   On Windows:
```
venv\Scripts\activate
```
*   On macOS and Linux:
```
source venv/bin/activate
```
<p>5. Install Dependencies:</p>

```
pip install -r requirements.txt
```

<p>6. Set Up the Database:</p>

```
python manage.py makemigrations
```

<p>7. Create a Superuser (Admin Account):</p>

```
python manage.py createsuperuser
```

<p>8. Run the Development Server:</p>

```
python manage.py runserver
```
<h2>💻 Built with</h2>


Technologies used in the project:

*   FrontEnd: HMTL | CSS | Bootstrap |
*   BackEnd: Python | Django | SQLite |
*   Testing:  Pytest
