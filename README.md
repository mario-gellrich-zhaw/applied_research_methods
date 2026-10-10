# Applied Research Methods: Quantitative Data Analysis

Repository of the Data Analytics module at ZHAW

## Getting Started

### Creating a Fork of the Course Repository

To fork the GitHub repository into your GitHub account, navigate with your web browser to:

```bash
https://github.com/mario-gellrich-zhaw/applied_research_methods.git

# --> Click on the "Fork" button at the top right of the page.
# --> This will generate a fork (copy) of the repository in your GitHub account.
```

### Creating a GitHub Codespaces environment

Based on your fork, create a new Codespace: GitHub -> Upper menu -> Create new -> New Codespace.  

All installations will be made automatically.  

Wait until the postcreate command has completed the installation of the Python libraries.  

## Folder Structure

The folder structure of the course is:

```
Applied Research Methods/
│
├── .devcontainer/
│   └── devcontainer.json
|
├── Week_07/
├── Week_08/
├── Week_09/
├── Week_10/
├── Week_11/
├── Week_12/
├── Week_13/
|
├── .gitignore
├── README.md
└── requirements.txt
```

Each week folder contains the exercise sheet (PDF), the Jupyter notebooks and a folder `Data` with the input data. The notebooks read and write files relative to their own week folder (e.g. `./Data/apartments_data_zuerich.csv`). Files created by the notebooks (e.g. prepared data, html exports) are not part of the repository.

## Working with the Jupyter notebooks

- Open a notebook in VS Code and select the Python kernel of the Codespace (upper right corner -> Select Kernel).
- Run the notebooks of a week in the order given in the exercise sheet, as some notebooks use the output of other notebooks.
- To export a notebook as html-file (submission on Moodle), use the menu of the notebook in VS Code (`...` -> Export -> HTML) or the terminal:

```bash
jupyter nbconvert --to html Week_08/apartments_data_preparation_zuerich.ipynb
```

## Sync your fork (origin) with the upstream repository

Before the first sync, add the course repository as `upstream` (only needed once):

```bash
git remote add upstream https://github.com/mario-gellrich-zhaw/applied_research_methods.git

# Check the remotes (origin = your fork, upstream = course repository)
git remote -v
```

To sync your fork (origin) with the upstream repository you can use the following Git commands (VS Code Terminal):

```bash
# Option (1): Sync your fork/clone with the upstream (your local changes are preserved but merge conflicts may have to be resolved)
git fetch upstream
git checkout master
git merge upstream/master
git push origin master

# Option (2): Sync your fork/clone to exactly match the upstream
# WARNING: all your local changes will be overwritten - use this only if you want to reset your fork!
git fetch upstream
git checkout master
git reset --hard upstream/master
git push origin master --force
```

## Solve merge conflicts

In the course you will modify the Python code provided on GitHub. When you modify Python code, merge conflicts may occur which is when two or more changes conflict with each other. This usually happens when multiple people are working on the same project and they try to merge their changes into a common codebase.

In VS Code, you can use the Merge Editor to solve merge conflicts.

The following video explains how this works: https://www.youtube.com/watch?v=KuB6hYoLozw
