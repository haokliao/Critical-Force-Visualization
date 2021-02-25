**Work in Progress**

## Table of Contents 
- [Table of Contents](#table-of-contents)
- [General Info](#general-info)
- [Set Up](#set-up)
- [To-do](#to-do)
- [Credits](#credits)


## General Info 
Data Visualizations done based on data from Lattice Training's paper [An all-out test to determine finger flexor critical force in rock climbers.](https://www.researchgate.net/publication/343601001_An_all-out_test_to_determine_finger_flexor_critical_force_in_rock_climbers) 
The experiments done by Dr. David Giles et al. collected data from 121 subjects whom provided consent, health history, bouldering (high impact climbing from shorter distances) and sport climbing (lengthier climbing involving ropes) grades and subjected them to a series of "max hangs", maximum voluntary contractions on a 20mm rung, with their dominant hand to measure ff-CF (finger flexor Critical Force). 

**EDA_001_notebook** contains introductory data analysis, visualizing basic demographics for the research group through different charts and graphs.

(To do)
**EDA_002_notebook will go** further in depth with the data, trying to answer some questions which I (and many others probably) are very curious about regarding the group, such as critical force in relationship to grade, how much work capacity (W') affects peak force and etc. 


## Set Up
This project was created with Conda as a package manager, so that the package and dependencies process could be as painless as possible for the audience(you!)
The documentation for this process is located [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-from-file), but it's as simple as going into your terminal and recreating the environment from the **CFVenv.yml** file. 


Create your environment from the `CFVenv.yml` file, then activate the environment created
```
    conda env create -f CFVenv.yml
    conda activate CFVenv
```

## To-do
- [ ] Everything
- [x] Package manager (Conda)
- [x] Read through study, take good notes, get a better grasp on material

- [x] Introduction Section : (Sex, Age, Years Climbing, Discipline, General vis)
  - [x] Clean all files
  - [x] Create piechart for Gender
  - [x] Create barchart for Age
  - [x] Set inline
  - [x] Create chart for years climbing
  - [x] Create chart for disciplines

- [ ] EDA Notebook 2
  - [ ] Intermediate DA section : (Peak force vs grade, grade vs training time)
  
- [ ] Visualization
  - [ ] Make things pretty! 
  - [ ] Colorways
  - [ ] Interesting charts to use
  - [ ] Figure out areas where there could be more data vis to convey information
- [ ] Find out tools I want to use to achieve visualization

- [ ] Work on spaghetti code




## Credits 
Special thanks to Dr. David Giles who allowed us to work with his data from his paper, [An all-out test to determine finger flexor critical force in rock climbers](https://www.researchgate.net/publication/343601001_An_all-out_test_to_determine_finger_flexor_critical_force_in_rock_climbers) 
