import requests
from InstagramAPI import InstagramAPI

# Function to get the image with the best resolution from the instagram hashtag search
def get_largest_image(candidates):
    candidate = {}
    pixels = 0
    for cand in candidates:
    # pick the highest resolution one
        res = cand['height']*cand['width']
        if res > pixels:
            pixels = res
            candidate = cand
    return candidate

# Save image to file
def save_image_from_candidate(url):
    filename = ''
    response = requests.get(url)
    # check the response status code, 200 means good
    if response.status_code == 200: 
        filename = url.split("/")[-1].split('?')[0]
    with open(filename, 'wb') as f:
        f.write(response.content)
    return filename

