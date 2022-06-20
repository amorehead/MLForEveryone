<div align="center">

# MLForEveryone
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

A series of tutorials on learning Machine Learning using the Python programming language, for everyone!

<img src="images/python_icon.png" alt="Python Icon" width="150"/>

<img src="images/machine_learning_chart.png" alt="Python Icon" width="1398"/>

Image Credit: [Towards Data Science](https://towardsdatascience.com/machine-learning-algorithms-in-laymans-terms-part-1-d0368d769a7b)

</div>

## Course objectives

By the end of this course, one will:
1. Master the fundamentals of writing Python scripts
2. Gain an understanding of the fundamental concepts in machine learning
3. Employ Python to train machine learning models using either supervised learning, unsupervised learning, or reinforcement learning

## Technical Setup
### Creating and configuring a local Conda environment

First, install Anaconda for your operating system of choice (e.g., Windows, macOS, Linux) using the instructions found at https://www.anaconda.com/.

Then, create and configure your Conda environment:

```bash
# Clone this repository:
git clone https://github.com/amorehead/MLForEveryone

# Change to project directory:
cd MLForEveryone

# Set up Conda environment locally
conda env create --name MLForEveryone -f environment.yml

# Activate Conda environment located in the current directory:
conda activate MLForEveryone

# (Optional) Perform a full install of the pip dependencies described in 'requirements.txt':
pip3 install -e .

# (Optional) To remove the long Conda environment prefix in your shell prompt, modify the env_prompt setting in your .condarc file with:
conda config --set env_prompt '({name})'
```

Install the new Conda environment as a new Jupyter notebook kernel:

```bash
conda activate MLForEveryone
python3 -m ipykernel install --user
```

## Tutorials

To begin this course, as desired, open up the Jupyter notebooks in the `notebook_tutorials` directory. For example, currently you can choose from:

<a href="https://colab.research.google.com/github/amorehead/MLForEveryone/blob/main/notebook_tutorials/Introduction_to_Python.ipynb" target="_blank">Introduction to Python</a>

<a href="https://colab.research.google.com/github/amorehead/MLForEveryone/blob/main/notebook_tutorials/Introduction_to_Machine_Learning.ipynb" target="_blank">Introduction to Machine Learning</a>

<a href="https://colab.research.google.com/github/amorehead/MLForEveryone/blob/main/notebook_tutorials/Introduction_to_Deep_Reinforcement_Learning.ipynb" target="_blank">Introduction to Deep Reinforcement Learning</a>
