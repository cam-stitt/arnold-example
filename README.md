arnold-example
==============

An example setup for using [arnold](https://github.com/cam-stitt/arnold).

Installation
============

First, you have to install arnold:

`pip install arnold`

Then, clone the repository:

```
$ git clone https://github.com/cam-stitt/arnold-example.git
$ cd arnold-example
```

Now, run the migration script to show an example of how migrations work:

```
$ python migrator.py "up"
```
Or
```
$ python migrator.py "down"
```

Roadmap
=======

* Add an example of actual peewee migrations
