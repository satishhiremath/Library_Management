# Library_Management
This Repo has implementation for Library management

## Command to run Test:
`python3 test_library_management.py`

## Command to run Library Management API
`python3 library_management.py`
and then follow the instructions on console

## Architecture
* The library management API has several files and classes. Explanation about each is as follows:
1. __custom_exceptions.py__:
    * This file has all the custom created exceptions to handle exceptions and errors
2. __library.py__:
    * It has class `Library` which has all the functions related to Library
3. __user.py__:
    * It has class `User` which has all the functions related to User
4. __library_management.py__:
    * It has class `LibraryManagement` which has all the functions related to Library management
5. __test_library_management.py__:
    * This file has all the unit test cases for testing functions in all above classes


## Installing pre-commit hooks
I use a tool called pre-commit for vaious static checks while creating a commit. Install it using below command:
`pip3 install pre-commit`

Enable precommit in a repository with
`pre-commit install`

## Install bazel
Follow the step provided from [installation_steps](https://docs.bazel.build/versions/main/install-ubuntu.html)

## Build via bazel
Use command below to build all the targets in current repo
`bazel build ...`

If you want to build specific targets
`bazel build <path to target>`

for Example:
`bazel build //:library_management_binary`
