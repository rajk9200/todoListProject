# from django.test import TestCase

# Create your tests here.
import instaloader

loader = instaloader.Instaloader()

# Reel URL
url = "https://www.instagram.com/reel/DRUdEMKCMTn/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=="

# Extract shortcode
shortcode = url.split("/")[-2]

# Download
loader.download_post(instaloader.Post.from_shortcode(loader.context, shortcode), target="reels_download")
