This is a project demo showing how I would go about implementing the code for an SAT question generator feature which was part of a prompt engineering technical interview.

#### Feature requirements:

- We want the AI to create a set of sample questions and choices to be used as practice for the SAT.
- Assume the UI handles all interaction with the student. We only need to generate questions in a standardized format to pass to the UI.
- The UI will pass us a `theme_string` variable that we should use to generate questions with that theme.
- Generate exactly 5 questions for each category: math, reading, vocabulary.
- Assume the AI generates good questions by default.

#### Additional enhancements discussed
- Add the ability to pass a rubric to the AI to facilitate question creation.
- We don't want to keep the student waiting while all the questions are generated.
- Ensure the JSON we pass to the UI is valid

I have created two separate versions of this implementation, the first on the [main](https://github.com/duncantmiller/sat_bot_demo/blob/main/question_builder.py) branch implements all of the logic within the prompt to the AI.

The second on the [optimized](https://github.com/duncantmiller/sat_bot_demo/blob/optimized/question_builder.py) branch uses python code to:

- keep track of the questions asked and question numbers
- pick random categories and ensure they have 5 questions each
- only ask the AI to generate one question at a time
- validate the json and generate the question again if it is invalid
- send the json to the ui (I just built a dummy method for this)

The tests can be run with `python test.py` in either branch.

If you use [pipenv](https://pypi.org/project/pipenv/) you can install the dependencies with `pipenv install`, otherwise use `pip install -r requirements.txt`.

To run the tests you will need an environment variable named `OPENAI_API_KEY`. This should contain the value of an OpenAI API key. You can add the key to your environment variables, or to a .env file in the root directory.
