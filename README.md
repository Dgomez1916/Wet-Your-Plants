# Module3 Project Gamma

## Getting started

You have a project repository, now what? The next section
lists all of the deliverables that are due at the end of the
week. Below is some guidance for getting started on the
tasks for this week.

## Install Extensions

- Prettier: <https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode>
- Black Formatter: <https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter>

## Deliverables

- [ ] Wire-frame diagrams
- [ ] API documentation
- [ ] Project is deployed to Caprover (BE, DB) & GitLab-pages (FE)
- [ ] GitLab issue board is setup and in use (or project management tool of choice)
- [ ] Journals

## Project layout

The layout of the project is just like all of the projects
you did with `docker-compose` in module #2. You will create
a directory in the root of the repository for each service
that you add to your project just like those previous
projects were setup.

### Directories

Several directories have been added to your project. The
directories `docs` and `journals` are places for you and
your team-mates to, respectively, put any documentation
about your project that you create and to put your
project-journal entries. See the _README.md_ file in each
directory for more info.

The other directories, `ghi` and `api`, are services, that
you can start building off of.

Inside of `ghi` is a minimal React app that has an "under
construction" page. It is setup similarly to all of the
other React projects that you have worked on.

Inside of `api` is a minimal FastAPI application.
"Where are all the files?" you might ask? Well, the
`main.py` file is the whole thing, and go take look inside
of it... There's not even much in there..., hmm? That is
FastAPI, we'll learn more about it in the coming days. Can
you figure out what this little web-application does even
though you haven't learned about FastAPI yet?

Also in `api` is a directory for your migrations.
If you choose to use PostgreSQL, then you'll want to use
migrations to control your database. Unlike Django, where
migrations were automatically created for you, you'll write
yours by hand using DDL. Don't worry about not knowing what
DDL means; we have you covered. There's a sample migration
in there that creates two tables so you can see what they
look like.

The Dockerfile and Dockerfile.dev run your migrations
for you automatically.

### Other files

The following project files have been created as a minimal
starting point. Please follow the guidance for each one for
a most successful project.

- `docker-compose.yaml`: there isn't much in here, just a
  **really** simple UI and FastAPI service. Add services
  (like a database) to this file as you did with previous
  projects in module #2.
- `.gitlab-ci.yml`: This is your "ci/cd" file where you will
  configure automated unit tests, code quality checks, and
  the building and deployment of your production system.
  Currently, all it does is deploy an "under construction"
  page to your production UI on GitLab and a sample backend
  to CapRover. We will learn much more about this file.
- `.gitignore`: This is a file that prevents unwanted files
  from getting added to your repository, files like
  `pyc` files, `__pycache__`, etc. We've set it up so that
  it has a good default configuration for Python projects.
- `.env.sample`: This file is a template to copy when
  creating environment variables for your team. Create a
  copy called `.env` and put your own passwords in here
  without fear of it being committed to git (see `.env`
  listed in `.gitignore`). You can also put team related
  environment variables in here, things like api and signing
  keys that shouldn't be committed; these should be
  duplicated in your deployed environments.

## How to complete the initial deploy

There will be further guidance on completing the initial
deployment, but it just consists of these steps:

### Setup GitLab repo/project

- make sure this project is in a group. If it isn't, stop
  now and move it to a GitLab group
- remove the fork relationship: In GitLab go to:

  Settings -> General -> Advanced -> Remove fork relationship

- add these GitLab CI/CD variables:
  - PUBLIC_URL : this is your gitlab pages URL
  - REACT_APP_API_HOST: enter "blank" for now

#### Your GitLab pages URL

You can't find this in GitLab until after you've done a deploy
but you can figure it out yourself from your GitLab project URL.

If this is your project URL

https://gitlab.com/GROUP_NAME/PROJECT_NAME

then your GitLab pages URL will be

https://GROUP_NAME.gitlab.io/PROJECT_NAME

### Initialize CapRover

1. Attain IP address and domain from an instructor
1. Follow the steps in the CD Cookbook in Learn.

### Update GitLab CI/CD variables

Copy the service URL for your CapRover service and then paste
that into the value for the REACT_APP_API_HOST CI/CD variable
in GitLab.

### Deploy it

Merge a change into main to kick off the initial deploy. Once the build pipeline
finishes you should be able to see an "under construction" page on your GitLab
pages site.
# Wet Your Plants
- Adrianna Fowler 
- Danny Gomez
- Jason Seet
- Deon Nguyen

Tech Stack
- Backend: FastAPI
- Frontend: Vite + JavaScript
- Database: PostgreSQL
- UI Framework: Material-UI

## Design

- [API design](docs/apis.md)
- [Data model](docs/data-model.md)
- [GHI](docs/ghi.md)
- [Integrations](docs/integrations.md)

## Intended market

Wet Your Plants - Plant Care Assistant
Welcome to Wet Your Plants, your dedicated application for stress-free and consistent house plant care. This application is tailored for the less experienced or busy house plant enthusiasts, providing a robust solution to cultivate healthy and thriving plants. Whether you're new to plant care or navigating a busy schedule, Wet Your Plants is your partner in cultivating a green and vibrant indoor oasis.

## Functionality

Features
1. Home Page
Explore the app's functionalities with a user-friendly interface that guides you through the features and benefits of Wet Your Plants.

2. Sign Up and Login
Securely authenticate users with our streamlined sign-up and login process, ensuring a personalized experience for every user.

3. Greenhouse Page
Utilize the Greenhouse page as your central hub for managing plant inventory. Track each plant's health, maintenance needs, and care history effortlessly.

4. Plant Detail Page
Harness the power of the PlantID API to access detailed care instructions and descriptions for each house plant. Empower yourself with the knowledge needed for optimal plant growth.

5. Plant Care Dashboard
Local Weather Integration: Real-time weather updates from the OpenWeatherMap API to tailor your plant care routine based on local conditions.
Weather Warning Bar: Receive alerts when weather conditions pose a potential threat to your outdoor plants.
Daily To-Do List: Generate a personalized to-do list based on watering needs and other care requirements, with the ability to add manual tasks.

6. Plant Care History
Review your plant care journey with the Plant Care History feature. Store completed tasks and monitor your progress in nurturing your plants.

## Project Initialization

To fully enjoy this application on your local machine, please make sure to follow these steps:

1. Clone the repository down to your local machine
2. CD into the new project directory
3. code . to open your IDE
4. Create a file in "api" named keys.py (insert the code below)
5.  PERENUAL_API_KEY = "Replace with key from plantID API"
    OPEN_WEATHER_API_KEY = "Replace with key from openweathermap API"
6. Run `docker compose build`
7. Run `docker compose up`
