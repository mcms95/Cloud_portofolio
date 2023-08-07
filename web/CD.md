
Workflow yaml file that have
1- Events
2- Jobs
3-Runners
4-Steps
5-Actions

create a directory on repository with name .github/workflows

on: push -> when someone push it will run all the jobs in the workflow

jobs: -> container that can have multiple steps and actions 
    name of the job:
        runs-on: ubuntu-latest || microsoft || mac os -> Env Runner