[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/d_wmESyD)
# IST356 Assignment 04 (assignment_04)

## Meta

### Learning Objectives

This assignment you will use pandas and streamlit to create a universal dataset browser. Let's call it **unibrow** 😂

### Assignment Layout

The each assignment will have a common layout.

- `code` folder contains our code / application. This is where you will create files and write code.
- `code/solution` folder contains the solution to the assignment, for reference.
- `data` data files folder
- `tests` folder contains code to test our application
- `requirements.txt` contains the packages we need to `pip install` to execute the application code
- `readme.md` contains these instructions
- `.vscode` folder contains VS Code setup configurations for running / debugging the application and tests.
- `reflection.md` is where you submit your reflection, comments on what you learned, things that confuse you, etc.

### Prerequisites 

Before starting this assignment you must:

Install the assignemnt python requirements:

1. From VS Code, open a terminal: Menu => Terminal => New Terminal
2. In the terminal, type and enter: `pip install -r requirements.txt`


### Running Tests

There is some code and tests already working in this assignment. These are sanity checks to ensure VS Code is configured properly.

1. Open **Testing** in the activity bar: Menu => View => Testing
2. You'll need to install the testing tools. Choose **pytest**
3. Open the **>** by clicking on it next to **assignment_04**. Keep clicking on **>** until you see **test_should_pass** in the **test_assignment.py**
4. Click the Play button `|>` next to **test_should_pass** to execute the test. 
5. A green check means the test code ran and the test has passed.
6. A red X means the test code ran but the test has failed. When a test fails you will be given an error message and stack trace with line numbers.

## Assignment: UniBrow

The **UniBrow** application is a streamlit application which displays a data from a file. 

It consists of 3 inputs:

- upload a file in Excel (XLSX), Comma-Separared, with Header (CSV), or Row-Oriented Json (JSON) into a dataframe
- select which columns to display from the dataframe
- build a fiter on the dataframe based on a text column and one of the values in the column.

And 2 outputs:

- the dataframe with column / row filters applied.
- the describe of the dataframe (to see statistics for the numerical columns)

**NOTE** There are sample files to load in the `data` folder.

## Advice

`pandaslib.py`

start by writing the functions in this file. They are ordered from easiest to most difficult.

- Function definitions with type hints and doc strings have been written for you. just complete the function body.
- Use the pytest tests to ensure your functions are correct
- The tests will not debug, so write code under the `if __name__=='__main__'` section to debug it that way.

`unibrow.py`

- use streamlit widgets to accept file browser input
- for the column multi-select, start with all columns selected
- a toggle to ask to include a filter, if enabled...
- You need two drop down widgets for the filter: object column names and  unique values in that column
- display the dataframe filtered by rows / columns
- descrived the dataframe (again the one filtered by row/columns)

## Commit Requirements

This assignment requires a minimum of 2 git commits. One suggestion is to commit after you complete a coding session (whether your code works or not.) At minimum you should commit after you complete `pandaslib.py` then again after `unibrow.py` 

## Turning it in

- Make sure tests pass and code works as expected
- Write your reflection in `reflection.md`
- Commit your changes: VS Code -> menu -> View -> Source Control -> Enter Commit message -> Click "Commit"
- Push your changes: VS Code -> menu -> View -> Source Control -> Click "Sync Changes"

## Grading 

🤖 Beep, Boop. This assignment is bot-graded! When you push your code to GitHub, my graderbot is notified there is something to grade. The bot then takes the following actions:

1. Your assignment repository is cloned from Github
2. The bot checks your code and commits according to guidelines outlined in `assignment-criteria.json` (it runs tests, checking code correctness, etc.)
3. The bot reads your `reflection.md` and provides areas for improvement (based on the instructions in the file).
4. A grade is assigned by the bot. Feedback is generated including justification for the grade given.
5. The grade and feedback are posted to Blackboard.

You are welcome to review the bot's feedback and improve your submission as often as you like.

**NOTE: ** Consider this an experiment in the future of education. The graderbot is an AI teaching assistant. Like a human grader, it will make mistakes. Please feel free to question the bots' feedback! Do not feel as if you should gamify the bot. Talk to me! Like a person, we must teach it how to do its job effectively. 


