"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [0],
            "answer": 1,
        },
        {
            "input": [10],
            "answer": 0,
        },
        {
            "input": [100],
            "answer": 5,
        },
    ],
    "Extra": [
        {
            "input": [10000],
            "answer": 7,
        },
        {
            "input": [33],
            "answer": 2,
        },
    ]
}
