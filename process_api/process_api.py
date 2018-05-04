#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Set the proxy server.
os.environ['HTTP_PROXY']='<Your proxy server if neccessary>'
os.environ['HTTPS_PROXY']='<Your proxy server if neccessary>'


# API documentation on Github search repositories: https://developer.github.com/v3/search/#search-repositories

# Query repositories written in Python and the stars are over 30000
url = 'https://api.github.com/search/repositories?q=language:python+stars:>30000&sort=stars'  #  API call endpoint

# Define a response object called r. We can get all the information from this object.
r = requests.get(url)

# Status code: 200
# This means the request was successful
print("Status code:", r.status_code)

# There's also a built-in JSON decoder.
# The API returns the information in JSON format.
response_dict = r.json()

# {'total_count': 11, 'incomplete_results': False, 'items': [{'id': 21289110, 'name': 'awesome-python', 'full_name': 'vinta/awesome-python', ther_user}', ...}]}
print(response_dict)

# dict_keys(['total_count', 'incomplete_results', 'items'])
print(response_dict.keys())

# Total repositories: 11
print("Total repositories:", response_dict['total_count'])

repo_dicts = response_dict['items']

# Return the first repository information
# Keys: 72
# archive_url
# archived
# assignees_url
# blobs_url
# branches_url
# clone_url
# collaborators_url
# ....

repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

# Selected information about first repository:
# Name: awesome-python
# Owner: vinta
# Stars: 48828
# Repository: https://github.com/vinta/awesome-python
# Created: 2014-06-27T21:00:06Z
# Updated: 2018-04-23T04:57:54Z
# Description: A curated list of awesome Python frameworks, libraries, software and resources
print("\nSelected information about first repository:")
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])


names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')


my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie.'},
    {'value': 15028, 'label': 'Description of django.'},
    {'value': 14798, 'label': 'Description of flask.'},
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
