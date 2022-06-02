<div align="center">

# MLForEveryone
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

A series of tutorials on learning Machine Learning using the Python programming language, for everyone!

<img src="images/python_icon.png" alt="Python Icon" width="150"/>

<img src="images/machine_learning_chart.png" alt="Python Icon" width="1398"/>

Image Credit: [Towards Data Science](https://towardsdatascience.com/machine-learning-algorithms-in-laymans-terms-part-1-d0368d769a7b)

</div>

## Creating and configuring a local Conda environment

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