# TDD Python

## Few Commands

> 1. We are using git bash for windows

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

git add .
git commit -m "First commit"

python manage.py startapp lists
```
