# Multi-User Blog

Hello, and welcome to my submission for the Multi-User Blog project in the Udacity Full Stack Nanodegree.

The blog is built upon the Google App Engine SDK for Python, with templating provided through `jinja2`. The live version is hosted [here](https://disposedtrolley-blog.appspot.com/blog).

## Running Locally

1. Download and install the [Google App Engine SDK](https://cloud.google.com/appengine/downloads) for Python.
2. Clone or download this repo onto your machine.
3. `cd` into the root directory of the app.
4. Run `dev_appserver.py app.yaml` to start a locally-hosted instance of the blog.
5. Navigate to http://localhost:8080/blog

## References

+   Some of the handler functionality was taken from the homework 4 solutions `hw4.tgz` and modified to suit the revised architecture of the app.
+   Code from http://bootsnipp.com/snippets/b4Npe was used in the design of the login and registration pages.