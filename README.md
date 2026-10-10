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
├── Week_07/   # SW07 / KW44
├── Week_08/   # SW08 / KW45
├── Week_09/   # SW09 / KW46
├── Week_10/   # SW10 / KW47
├── Week_11/   # SW11 / KW48
├── Week_12/   # SW12 / KW49
├── Week_13/   # SW13 / KW50
|
├── .gitignore
├── README.md
└── requirements.txt
```

## Sync your fork (origin) with the upstream repository

To sync your fork (origin) with the upstream repository you can use the following Git commands (VS Code Terminal):

```bash
# Option (1): Sync your fork/clone to exactly match the upstream (your local changes will be overwritten)
git fetch upstream
git checkout master
git reset --hard upstream/master
git push origin master --force

# Option (2): Sync your fork/clone with the upstream (your local changes are preserved but merge conflicts may have to be resolved)
git fetch upstream
git checkout master
git merge upstream/master
git push origin master
```

## Solve merge conflicts

In the course you will modify the Python code provided on GitHub. When you modify Python code, merge conflicts may occur which is when two or more changes conflict with each other. This usually happens when multiple people are working on the same project and they try to merge their changes into a common codebase.

In VS Code, you can use the Merge Editor to solve merge conflics.

The following video explains how this works: https://www.youtube.com/watch?v=KuB6hYoLozw
