# Development Notes

- This project requires Python 3.7. 

- To ensure compatibility in development between machines, we will use a Python virtual environment (`virtualenv`) with 
a standard set of dependencies. These dependencies are listed in `requirements.txt` and will occasionally be updated as 
development progresses. Your virtual environment should be called `venv` and reside in the subdirectory of this project. 
This will ensure that it is ignored by `git` (as specified in the `.gitignore` file) when performing check-ins.

## Choosing your IDE

Jetbrains PyCharm is one of the best IDEs for Python development, and it is available for 
[free](https://www.jetbrains.com/student/) for students. Enter your CGU e-mail address for a 1-year subscription.

#### Creating your virtual environment

```bash
$ python -m venv venv
```

#### Activate virtual environment on Linux
```bash
$ source venv/bin/activate
```

#### Activate virtual environment on Windows
```bash
D:\ist303-team3-educational-game>venv\Scripts\activate.bat
```

#### Installing requirements
```bash
pip install -r requirements.txt
```

Use the `deactivate` terminal command to exit the virtual environment.

# Game Development

[Python Arcade PDF Book](https://media.readthedocs.org/pdf/arcade-book/latest/arcade-book.pdf) - Comprehensive Arcade development book, for developing the individual games and main menu.

[SQLAlchemy](https://docs.sqlalchemy.org/en/latest/orm/tutorial.html) - For relating the objects in each game with 
database tables, for recording game history.
