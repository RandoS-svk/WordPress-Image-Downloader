
# Wordpress Image Downloader

This Python script allows you to download all images from a Wordpress site by utilizing the Wordpress REST API. Simply provide your Wordpress API key and the script will download all images found on the site.

## Installation

To use this script, you'll need to have Python installed on your machine. You'll also need to install the requests library. You can install it via pip by running:





```bash
  pip install requests

```

## Usage

To use this script, you'll need to provide your Wordpress API key. You can obtain this key by following the instructions on the Wordpress REST API documentation.

Once you have your API key, open the app.py file and replace the **YOUR_API_KEY_HERE** placeholder with your actual API key.

Then simply run the script using:

```bash
  python app.py

```

Note that this script is only capable of downloading images from publicly accessible Wordpress sites. If the site requires authentication to access its API, you'll need to modify the script to include authentication headers.

