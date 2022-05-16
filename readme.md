# Codoc Test

## Summary

This Django project contains three apps:

* `patients` - Contains the code about patients.
* `cohorts` - Contains the code about cohorts (group of patients).
* `commons` - Contains code used by multiple apps.

There are tests already written and all of them should currently pass. **You are allowed
to modify and create any test as needed.**

To help you in your tasks, I invite you to read the [Django](https://docs.djangoproject.com/en/4.0/)'s
and [DRF](https://www.django-rest-framework.org/)'s documentation.

## How to run the app

To run the app, you need to first install the dependencies (`python 3.6+` required). It is recommended
to install the dependencies within a virtual environment :

```shell
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirement
```

To create a database, you can run :

* `python3 manage.py migrate`

This will create a `db.sqlite3` file that will be used as a database.

To run the app :

* `python3 manage.py runserver`

And to run the tests :

* `python3 manage.py test`

If for some reason you need some data, you can find some patients in `JSON` format in
`resources/patients.json`.

Note that you should not need to create the DB or run the app : the tests should be enough.

## Your tasks

1. Currently, any authenticated user can delete a cohort. You have to modify the
    `cohorts` app so that only the owner and superusers (`user.is_superuser is True`) can delete a
    cohort.
2. Doctor would like to be able to add comment**s** for each patient of their cohorts. You have to
    add the django's `Model` and the viewset allowing to do that. The comment must depend on the cohort
    since a same patient can be in multiple cohort.
3. Modify the viewset you just created to only allow the cohort's owner and superuser to do any request on
    cohort's comments.

## Goals

The goal of this test is not to see if you can do everything, but to understand the way you code
and the way you proceed through problems.

Do not hesitate to modify any existing part of the code as you see fit.

You can send your work to `quentin@codoc.co` as a `zip` or a `git` link. Do not hesitate to describe
(in the mail or in a `.md` file) the problem you encountered and how you tried to solve them.

Even if the test is not satisfying enough for us to proceed to the next part of the recruitment
process, we will send an email describing the parts of the test we liked and the parts we would have
done differently.
