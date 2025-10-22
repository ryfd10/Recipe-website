# 🍽️ Recipe Website

A simple Django-based recipe website for browsing and viewing recipes with images, search, and filtering.

---

## ✨ Overview

This project provides a visual, browsable collection of recipes. Each recipe includes details, images, and metadata such as difficulty level. The app includes forms for creating recipes and authors.

## 🔑 Key Features

- 📚 Recipe listing (homepage)
- 📄 Recipe detail page
- 🔍 Search recipes by name
- 🧭 Filter recipes by difficulty level (level)
- ➕ Forms to create recipes and authors (class-based views)
- 🖼️ Image gallery stored under `gallery/uploads/`

## 🛠️ Technologies

- Python 3.x
- Django (project's installed version)
- SQLite (default database)
- HTML / CSS (Django templates)

## 🗂️ Relevant Files & Structure

- `manage.py` — Django management script
- `db.sqlite3` — Project database (default)
- `Recipe/` — Project settings (Django project)
- `level1/` — Main application (views, urls, templates)
  - `level1/templates/` — Django templates
- `gallery/uploads/` — Stored images and media

## 🔗 Conceptual Routes

- `/` — Recipes list
- `/recipeDetails/<slug:slug>` — Recipe detail
- `/byName` — Search by name
- `/byLevel/<int:level>` — Filter by difficulty
- `/recipe_form` — Create recipe form
- `/author` — Author form/page

## 🗃️ Data & Media

- Images are kept in `gallery/uploads/`.
- The project's primary database is `db.sqlite3`.

