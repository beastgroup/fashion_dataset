import os
import itertools
import urllib.request
from joblib import Parallel, delayed
import pandas as pd
import sys


def download(img):
    # filename is (post_id)_(image_name)
    try:
        filename = str(img[0]) + '_' + img[1].split('/')[-1]
        image_filename = os.path.join(image_dir, filename)
       # print("Fetching '%s' to '%s'..." % (img, image_filename))
        urllib.request.urlretrieve(img[1], image_filename)
    except urllib.error.HTTPError:
        print("HTTPError error:", sys.exc_info()[0])


###
#  uncommenct the following if you would like to download all the images
# and comment the line follow
###


# photo_dir = os.path.join(os.getcwd(), 'photos')
# images = [[(line.rstrip().split("\t")[0], line.rstrip().split("\t")[1]) for line in open(
#     os.path.join(photo_dir, f))] for f in os.listdir(photo_dir) if f.endswith('.txt')]
# images = list(itertools.chain.from_iterable(images))
images = pd.read_csv('image_to_download.csv').values
# images = [str(images['id'].values.tolist()), images['name'].values.tolist()]

print('Downloading %s images to "./images" directory...' % len(images))

image_dir = os.path.join(os.getcwd(), 'images')
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# Download in parallel
Parallel(n_jobs=8)(delayed(download)(img) for img in images)
