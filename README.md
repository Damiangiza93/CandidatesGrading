# Grading Tasks

A web API that will allow grading and listing Tasks given by a Recruiter to the Candidate

## Table of contents

1. [General info/Motivation](https://github.com/Damiangiza93/CandidatesGrading#general-infomotivation)
2. [Used technologies](https://github.com/Damiangiza93/CandidatesGrading#used-technologies)
3. [Features](https://github.com/Damiangiza93/CandidatesGrading#features)
4. [Quick Start Guide](https://github.com/Damiangiza93/CandidatesGrading#quick-start-guide)
5. [Configuration](https://github.com/Damiangiza93/CandidatesGrading#configuration)
6. [Screenshots](https://github.com/Damiangiza93/CandidatesGrading#screenshots)

## General info/Motivation

I made the application for the recruitment 

## Used technologies

1. Python 3.8
2. Django 3.1.1
3. Docker 2.4.0.0

## Features

1. Adding new candidates, recruiters and tasks
2. Adding Grades for the tasks (one task can have only one grade and be connected with one candidate)
3. Show the list of the Candidates with their grades and average grade

## Quick Start Guide

```bash
docker-compose up
```

Now you can open app in your web browser at [localhost](https://localhost:8080)

## Configuration

To configure your: 
- environment variables and ports- go to docker-compose.yml and change data in services:web

## Screenshots

![](https://github.com/Damiangiza93/CandidatesGrading/blob/main/Recruitment/photos/addmark.JPG)
![](https://github.com/Damiangiza93/CandidatesGrading/blob/main/Recruitment/photos/addcandidate.JPG)
![](https://github.com/Damiangiza93/CandidatesGrading/blob/main/Recruitment/photos/candidateslist.JPG)