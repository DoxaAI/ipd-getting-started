# Getting started with the IPD on DOXA

This repository contains a collection of materials for getting started with the iterated prisoner's dilemma (IPD) tournament on [DOXA](https://doxaai.com/). More information is available on the [DOXA competition page](https://doxaai.com/competition/ipd).

Feel free to fork this repository and use it as the base for implementing your own agents!

## Repository structure

- `examples/`: this directory contains implementations of a few rule-based agents (in `examples/simple.py`), as well as a basic tabular Q-learning agent (in `examples/qlearning.py`)
- `images/`: this directory contains images used in the accompanying Jupyter notebooks
- `submission/`: this is an example submission directory, which you could upload straight to DOXA without modification if you so wanted!
    - `submission/doxa.yaml`: this is a configuration file that tells DOXA how to treat your submission
    - `submission/ipd.py`: this is a Python module used to abstract away the logic of communicating with DOXA over `stdio` -- you can safely ignore this file for the most part
    - `submission/run.py`: this is where you should implement your own agent!
- `1_introduction.ipynb`: this is an introductory Jupyter notebook
- `2_tabular_q_learning.ipynb`: this is a Jupyter notebook that provides an introduction to tabular Q-learning
- `3_evaluation.ipynb`: this is a Jupyter notebook that allows you to test the agent `Agent` you implement in `submission/run.py`
- `engine.py`: this is a local implementation of the iterated prisoner's dilemma game (similar to what is used on DOXA for running the tournament), which you can use for testing your agent locally or even for training based on reinforcement learning.

## Submitting to DOXA

In order to submit your work to DOXA, you must prepare a folder containing all the files necessary to run your agent, including potentially any trained model and the code required to use it, as well as a `doxa.yaml` file.

If you do not have the DOXA CLI installed, you may install it from [PyPI](https://pypi.org/project/doxa-cli/) using `pip` as follows:

```bash
pip install doxa-cli
```

If you have not done so already, you must first log into the DOXA CLI using the following command:

```bash
doxa login
```

You can then upload your submission to the DOXA using the following command:

```bash
doxa upload [SUBMISSION DIRECTORY]
```

If you are working in the `submission` folder, this command becomes the following:

```bash
doxa upload submission
```
