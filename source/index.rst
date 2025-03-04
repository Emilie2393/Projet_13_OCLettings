.. oc_lettings documentation master file, created by
   sphinx-quickstart on Mon Mar  3 14:44:12 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

oc_lettings documentation
=========================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   **Introduction**

   Oc_lettings is a real estate website for holiday lettings.

   The website has undergone a complete overhaul to isolate the two parts: lettings and profiles, and make the script more scalable. 
   The database used is an sqlite database. The old models have been split between lettings and profiles. Now, the project contain the main app:
   oc_lettings_site, and then profiles and lettings. The data in the sqlite database was transferred from the old tables to the new ones:
   * lettings_address
   * lettings_letting
   * profiles_profile

   A sentry monitoring has been added. The admin section has been corrected and the project has been linted. 

   A 404 and 500 page have been added and test coverage is 84%. 

   **Installation**

   * First, you need a :
      * Sentry account;
      * Docker desktop application;
      * Docker Hub account;
      * Python 3.x;

   * Then, create a virtual environment at the root of this project :  
   ``python -m venv venv``  

   * Activate it :  
   ``venv/bin/activate`` 
   
   * Copy the dependancies available into the requirements.txt file:  
   ``pip install -r requirements.txt``  

   * Complete the .env file with your personnal information you just created before.  

   **Using cases**

   You can create a superuser to create data with:
   * ``python manage.py shell``
   * ``from django.contrib.auth.models import User``
   * ``User.objects.create_superuser(username='admin', email='admin@example.com', password='motdepasse123')``
      choose the username, email and password of your choice.

   In order to create more lettings or profiles, you can start to launch the Django app:
   * ``python manage.py runserver``

   Now you can check the app on http://localhost:8000/admin and login with your previous superuser credentials. You will be able 
   to create new data then. 

   **How to use it with Docker and Render**

   To deploy the Docker image locally you can:
   * Open Docker desktop.
   * Open a powershell command and enter the following:
   ``$DOCKER_TAG = (Invoke-RestMethod -Uri "https://hub.docker.com/v2/repositories/emilie2393/oc_lettings/tags?page_size=1").results[0].name; 
   docker pull emilie2393/oc_lettings:$DOCKER_TAG; if (docker ps -aq -f name=oc_lettings_site) { echo "Arrêt et suppression du conteneur existant..."; 
   docker stop oc_lettings_site; docker rm oc_lettings_site }; docker run --name oc_lettings_site -d -p 8000:8000 emilie2393/oc_lettings:$DOCKER_TAG``
   * You can now see the container running into your Docker desktop and access the app on http://localhost:8000/

   To deploy the website on Render, you need:
   * Be sure to clone the correct repository: https://gitlab.com/learning2431952/oc_lettings.git









