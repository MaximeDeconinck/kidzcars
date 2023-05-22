# kidzcars

This site allow users to see a list of cars, sorted by brands. If the car you want to see isn't here, you can add it, or add a new brand. Most cars are from a childhood game, Gran Turismo 4 on PlayStation 2.
The framework used is Django, with 2 additional libraries : wikipedia, to get articles, and joblib, to add multiple cars at once.

This site is part of my training for the Web Programming class at Paris-Dauphine University, in first year of Master MIAGE.

Feel free to reuse the project for non-commercial use.

## Installation

To install librairies : 
```bash
  pip3 install wikipedia && pip3 install joblib && pip3 install django
```

## Deployment

To deploy the project : 
```bash
  python3 manage.py runserver
```

## Admin user
```
  username : admin & password : admin
```

## Car list page
![Capture d’écran 2023-05-22 à 10 43 33](https://github.com/MaximeDeconinck/kidzcars/assets/83770758/764c6711-db4a-4310-96fb-aa9201493a21)

## Car detail page
![Capture d’écran 2023-05-22 à 10 50 33](https://github.com/MaximeDeconinck/kidzcars/assets/83770758/7bc1a907-659f-49c2-99b9-d5e5fbbcbe27)
