import os
import django
from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
import json
from django.core.files import File
from blog.models import Post, Category
from django.contrib.auth.models import User
from django.conf import settings
import random
import re

#from django_project.secret_key import API_KEY

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
django.setup()


class Command(BaseCommand):
    help = "Fetch and process articles"

    def handle(self, *args, **kwargs):
        """
        Fetch and process articles from the News API.
        """
        api_key = 'd4bb8a6625c74351a151e70b549d2abb'
        base_url = "https://newsapi.org/v2/"
        endpoint = "top-headlines"
        categories = ["technology", "entertainment", "science", "sports", "health"]

        for category_name in categories:
            category, created = Category.objects.get_or_create(name=category_name)
            self.fetch_and_process_articles(api_key, base_url, endpoint, category,)

    def fetch_and_process_articles(self, api_key, base_url, endpoint, category):
        """
        Fetch and process articles for a specific category.

        Args:
            api_key (str): The News API key.
            base_url (str): The base URL of the API.
            endpoint (str): The API endpoint for top headlines.
            category (Category): The category to fetch articles for.
        """
        params = {
            "apiKey": api_key,
            "category": category.name,
            "pageSize": 10,
            "page": 3,
            "language": "en",
        }

        response = requests.get(base_url + endpoint, params=params)
        if response.status_code == 200:
            data = response.json()
            articles = data.get("articles", [])

            for article in articles:
                title = article.get("title")
                content = article.get("content")
                image_url = article.get("urlToImage")
                source_url = article.get("url")

                random_user = random.choice(User.objects.all())

                if image_url is None:
                    print(
                        f"Warning: Skipping article '{title}' due to missing image URL."
                    )
                    continue

                image_path = self.download_image(image_url, title)
                if image_path:
                    soup = self.fetch_and_parse_source(source_url)
                    if soup:
                        content = self.extract_content(soup)

                    self.create_and_save_post(
                        title, content, random_user, category, image_path
                    )

                else:
                    print(f"Error: Unable to download image for article '{title}'.")
                    image_url = "media/post_pics/default_header_image.png"
        else:
            print(f"Error: Unable to fetch data for category '{category}'.")
            

    def download_image(self, image_url, title):
        """
        Download an image from a given URL and save it.

        Args:
            image_url (str): The URL of the image.
            title (str): The title of the article (used for the image file name).

        Returns:
            str: The local path to the downloaded image or None if unsuccessful.
        """
        response = requests.get(image_url)
        if response.status_code == 200:
            image_path = os.path.join(settings.MEDIA_ROOT, "post_pics", f"{title}.jpg")
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            with open(image_path, "wb") as image_file:
                image_file.write(response.content)
            return image_path
        return None

    def fetch_and_parse_source(self, source_url):
        """
        Fetch and parse the source of an article.

        Args:
            source_url (str): The URL of the source article.

        Returns:
            BeautifulSoup: The parsed source content or None if unsuccessful.
        """
        source_page = requests.get(source_url)
        if source_page.status_code == 200:
            return BeautifulSoup(source_page.content, "html.parser")
        return None

    def extract_content(self, soup):
        """
        Extract content from the parsed source.

        Args:
            soup (BeautifulSoup): The parsed source content.

        Returns:
            str: The extracted content.
        """
        content_elements = soup.find_all(
            ["p", "h1", "h2", "h3", "h4", "h5", "h6", "b", "i", "table", "iframe"]
        )
        content = ""
        for element in content_elements:
            content += str(element)
        return content
    
    
    def create_and_save_post(self, title, content, author, category, image_path):
        """
        Create and save a Post object.

        Args:
            title (str): The article title.
            content (str): The article content.
            author (User): The author of the article.
            category (Category): The category of the article.
            image_path (str): The local path to the article's image.
        """
        existing_post = Post.objects.filter(title=title).first()

        if existing_post:
            # If a post with the same title exists, do not create a new one
            self.stdout.write(self.style.WARNING(f"Post '{title}' already exists. Skipping."))
        else:
            # If no post with the same title exists, create and save the post
            post = Post(
                title=title,
                content=content,
                author=author,
                category=category,
            )
            post.header_image.save(
                os.path.join("post_pics", f"{title}.jpg"), File(open(image_path, "rb"))
            )

            post.save() 

            self.stdout.write(self.style.SUCCESS(f"Created post: {post.title}"))

    