# Tech Assignment - Network Speed

## Project Structure
solution.py contains the solution, test_solution.py contains the unit tests. 
backend.py contains a simple Flask backend for deployment to the cloud, in this case Heroku. 
requirements.txt, Procfile and runtime.txt are necessary files for deploying to Heroku

## Usage
The program solves for the highest non-zero speed for a given Device and an assortment of NetworkStation's.

Run the project with
```
python solution.py
```
Run unit tests with 
```
python -m unittest test_solution
```

## Scalability
The solution is broken down into classes and functions to be as modular as possible. Objects are loaded in from dictionaries to allow for future expansion such as creating an API and adding Devices and NetworkStation's with JSON. 

Once run, the solution will return a list of lists containing each device and their respective network station with highest speed, if any.
The console also outputs the speed and distance for each attempt and also keeps the user informed if a certain station is excluded due to having a distance too large.

The user may create a new NetworkStation() object and Device() object with different coordinates and reach in a Python shell to evaluate further network speeds.

## Deploying to the cloud
Creating an account on Heroku is easy and free, once done, install the CLI for your system and login using heroku login. 

To push the code to the cloud run:
```
heroku create your_app_name_here
git add .
git commit -am 'Initial commit'
git push heroku main
```

