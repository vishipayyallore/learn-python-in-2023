# TDD Python

I am learning the TDD with Python book. I am using the book to learn the TDD process and the Python language. The book is worderful and I am enjoying the process.

## Few Commands

> 1. We are using git bash for windows
> 1. Running the Django dev server
>    - python manage.py runserver
> 1. Running the functional tests
>    - python functional_tests.py
> 1. Running the unit tests
>    - python manage.py test

```bash
mkdir tddpygoatbook
cd tddpygoatbook

source .venv/Scripts/activate
which python
deactivate

pip install "django<4.3" "selenium"
python.exe -m pip install --upgrade pip

python -c "from selenium import webdriver; webdriver.Firefox()"

python ./functional_tests.py

django-admin startproject superlists .

git status
git diff
git diff -w

git add .
git commit -a # The -a means “automatically add any changes to tracked files
git commit -m "First commit"

python manage.py startapp lists

python manage.py test

python manage.py runserver

python manage.py makemigrations

python manage.py migrate

rm db.sqlite3
python manage.py migrate --noinput

python manage.py test # Executes both Unit and Functional Tests
python manage.py test .\functional_tests\
python manage.py test .\lists\
```
