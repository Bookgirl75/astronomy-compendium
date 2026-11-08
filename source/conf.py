# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'astronomy-compendium'
copyright = '2026, Rylan Hayes'
author = 'Rylan Hayes'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

## this NGC 5189 nebula image comes from
## https://en.wikipedia.org/wiki/Pillars_of_Creation#/media/File:Pillars_of_Creation_(NIRCam_Image).jpg
## It was big, so I resized it with:
## convert -resize 1500x NGC_5189.png NGC_5189_small.png
html_logo = 'NGC_5189_small.png'

## also of interest could be the Pillars of Creation, but its aspect ratio is
## too tall for this logo location.  The JWST picture is at:
## https://en.wikipedia.org/wiki/Pillars_of_Creation#/media/File:Pillars_of_Creation_(NIRCam_Image).jpg
#html_logo = 'Pillars_of_Creation.jpg'
