import requests
import json
import os
from datetime import datetime


def download_images(website, token):
    """
    Downloads all images from a WordPress website using the REST API.

    Args:
        website (str): The URL of the WordPress website.
        token (str): The API token for the WordPress website.

    Returns:
        None
    """

    # Define the URL of the REST API endpoint and the API token
    url = f"{website}/wp-json/wp/v2/media"

    # Define the parameters for the API request
    params = {
        "per_page": 100,  # The number of results to return per page
        "page": 1,  # The page number of results to return
    }

    # Define the headers for the API request, including the API token
    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Loop through the results until there are no more pages to retrieve
    while True:
        # Make the API request and parse the JSON response
        response = requests.get(url, params=params, headers=headers)
        data = json.loads(response.text)

        # Loop through the data and download each image
        for item in data:
            # Extract the image URL and upload date from the API response
            image_url = item["source_url"]
            upload_date = datetime.strptime(item["date_gmt"], "%Y-%m-%dT%H:%M:%S")

            # Create a directory path based on the upload date
            year = upload_date.strftime("%Y")
            month = upload_date.strftime("%m")
            filename = image_url.split("/")[-1]
            directory = os.path.join(year, month)

            # Ensure the directory exists and download the image to a file
            os.makedirs(directory, exist_ok=True)
            filepath = os.path.join(directory, filename)
            print(image_url)
            with open(filepath, 'wb') as f:
                f.write(requests.get(image_url).content)

        # Check if there are more pages of results to retrieve
        total_pages = int(response.headers.get("X-WP-TotalPages"))
        if params["page"] < total_pages:
            params["page"] += 1
        else:
            break


if __name__ == '__main__':
    # Replace the website and token with your own values
    website = "http://example.com"
    token = "your-api-token"
    download_images(website, token)
