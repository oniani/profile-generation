"""
@author: David Oniani
@date: 2019
"""

from collections import namedtuple
from datetime import datetime
from random import randint, randrange, sample
from typing import Any, Dict, List, Union

from flask import Flask, jsonify, render_template
from flask_cors import cross_origin

from util.bio.get_bio import generate_bio
from util.hobby.get_hobby import generate_hobbies
from util.name.get_name import generate_full_name
from util.textgen.get_text import read_text
from util.thispersondoesnotexist.get_image import save_image

APP = Flask(__name__)

COUNTRIES = "static/data/text/country.txt"
HOBBIES = "static/data/text/hobby.txt"
PROFILE_PICTURE = "static/data/image/profile.jpg"
UNISEX_FIRST_NAMES = "static/data/text/unisex.txt"

Post = namedtuple("Post", ["text", "updated"])


def generate_posts(num: int) -> List[Post]:
    """Return a list of posts stuff."""
    texts = sample(read_text("./static/data/text/posts.txt"), num)
    date = datetime.now().strftime("%B %d, %Y, %H:%M:%S")
    return [Post(text=texts[i], updated=date) for i in range(num)]


def generate_user() -> Dict[str, Union[str, Any]]:
    """Generate user information."""
    user_id = randrange(10 ** 11, 10 ** 12)
    first_name, last_name = generate_full_name(UNISEX_FIRST_NAMES)
    generated_hobbies = generate_hobbies(HOBBIES)
    generated_bio = generate_bio(first_name, generated_hobbies, COUNTRIES)
    generated_posts = generate_posts(randint(1, 25))

    username = f"{first_name.lower()}{last_name.lower()}"
    fake_blog = f"{username}.fakeblog.com"
    fake_tweet = f"@fakeig_{username}"
    fake_ig = f"@faketweet_{username}"

    save_image(PROFILE_PICTURE)
    profile_picture = f"http://localhost:5000/{PROFILE_PICTURE}"

    return {
        "user_id": user_id,
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
        "bio": generated_bio,
        "posts": generated_posts,
        "profile_picture": profile_picture,
        "fake_blog": fake_blog,
        "fake_tweet": fake_tweet,
        "fake_ig": fake_ig,
    }


@APP.route("/", methods=["GET", "POST"])
def index():
    """Index page."""
    user = generate_user()

    return render_template(
        "index.html",
        user_id=user["user_id"],
        username=user["username"],
        first_name=user["first_name"],
        last_name=user["last_name"],
        bio=user["bio"],
        posts=user["posts"],
        fake_blog=user["fake_blog"],
        fake_tweet=user["fake_tweet"],
        fake_ig=user["fake_ig"],
    )


@APP.route("/api", methods=["GET"])
@cross_origin()
def api():
    """API page."""
    user = generate_user()

    return jsonify(
        {
            "user_id": user["user_id"],
            "username": user["username"],
            "first_name": user["first_name"],
            "last_name": user["last_name"],
            "bio": user["bio"],
            "posts": [
                {"text": post.text, "updated": post.updated}
                for post in user["posts"]
            ],
            "profile_picture": user["profile_picture"],
            "fake_blog": user["fake_blog"],
            "fake_ig": user["fake_ig"],
            "fake_tweet": user["fake_tweet"],
        }
    )
