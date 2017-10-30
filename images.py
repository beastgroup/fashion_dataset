import pandas as pd
import os


def file_garments_names():
    return_files = []
    root_dir, dirs, files = next(os.walk('./garments'))
    for name in files:
        return_files.append(os.path.join(root_dir, name))
    return return_files


def search_ids(name):
    list_ = []
    headers = ['id', 'name']
    for filename in file_garments_names():
        df = pd.read_csv(filename, sep="\t", header=None, names=headers)
        list_.append(df.loc[df['name'] == name])

    return pd.concat(list_)


def images(searchable):
    garments = search_ids(searchable)
    photo_files = []
    root_dir, dirs, files = next(os.walk('./photos'))
    for name in files:
        photo_files.append(os.path.join(root_dir, name))

    list_ = []
    headers = ['id', 'name']
    for filename in photo_files:
        df = pd.read_csv(filename, sep="\t", header=None, names=headers)
        list_.append(df.loc[df['id'].isin(garments['id'])])

    pd.concat(list_).to_csv('image_to_download.csv', index=False)


# change category
images('hoodie')
