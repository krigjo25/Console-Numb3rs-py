# Numb3rs
An application that validates IPV4 Addresses using regular expressions.

The application was implemented as a CS50P assignment.<br>
Please respect, and keep the [Academic Honesty Policy](https://cs50.harvard.edu/x/2023/honesty/) in mind.

A demo can be watched at [CS50P's Problemt set 7: NUM3RS](https://cs50.harvard.edu/python/2022/psets/7/numb3rs/)

## Installation
1. Clone the repository:
```sh
# Using SSh 
ssh git@github.com:krigjo25/Console-Numb3rs-py.git

# Using git bash
git clone https://github.com/krigjo25/Console-Numb3rs-py.git

# Using Github Cli
gh repo clone Console-Numb3rs-py
```

2. Navigate to the project directory
```sh
cd Console-Numb3rs-py
```

3. Install the requirements
```sh
pip install -r requirements.txt
```

4. Run the file
```sh
python app.py
```

##  Usage
To use the application, run the following command in your terminal

```sh
Usage : type in the terminal python app.py.
python app.py
```

## Example
```sh
python app.py

IPv4 Address: <127.0.0.1>
expected output: True

IPv4 Address: <265.265.265.265>
expected output: False
```
Replace `<127.0.0.1>` with the desired IPV4 address

##  Testing framework / Datasets
Pytest has been used to test the project

```sh
pytest -k test_app.py
pytest --html=index.html
```

## LICENCE
The application is under [The Unlicensed](./LICENCE).

## Notes from the developer
Created with love, for python programming,

Thanks for reading, and have a blessed day,<br>
@krigjo25
