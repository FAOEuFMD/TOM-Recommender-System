# README - TOM Recommender System 
## Purpose
The goal of this project is to create a course recommender system for country-level managers within The European Commission for the Control of Foot-and-Mouth Disease(EuFMD). The recommender system is designed to identify and minimise gaps in emergency preparedness for FMD And Similar Transboundary animal diseases. The recommender will recommend courses that will bridge gaps in knowledge that exist among veterinary staff at a country level.

In other words, this recommender should do two things:
1. Identify skills gaps in veterinary professionals of a given country
2. Recommend courses that will help the country bridge the skills gaps most effectively 

## Context 

### Project status
As of July 2024 initial EDA has been completed and progress in identifying skills gaps has been made. Data cleaning and defining project scope has been the main focus.

### The Get Prepared Wall
The European Commission for the Control of Foot-and-Mouth Disease(EuFMD) has defined several skills that are necessary to prevent, combat, and recover from FMD and similar transboundary animal diseases. These skills are "bricks" listed in the "Get prepared wall" on the EuFMD website and are organised into four main categories:
1. Foundation
2. Alert
3. Emergency
4. Reconstruction

   Click [HERE](https://trello.com/b/SrsgHKzM/get-prepared-the-wall) to see the "Get prepared wall" and the skill "bricks" that make up each of these four categories

## Data used
The following datasets were used for the initial pilot/ EDA:
- tom_enrolments database: This was used to identify how many people within a country posessed a particular skill/ "brick". This data needed to be joined with other information in order to generate the necessary calculations
- Excel sheet with the "get prepared" brick mappings. This listed each course main topic and defined the skills/ "bricks" covered in each main topic. This was provided by a EuFMD staff member
- master_courses table. This contains information about all the courses including shortname, longname, language, and main_topic.  This was necessary to incorporate into the tom_enrolments table to get the accurate main_topic for each course. The tom_enrolments and master_courses tables were merged on course_id and moodle_id respectively.

## Data cleaning: labeling, imputation, and merging
### Labeling: main actions
- Brick mapping: Insead of having an 'X' indicate whether a course covers a particular skill we use 1
- Add the brick category to the brick mapping column titles to make EDA easier

### Imputation: main actions
- Drop main_topics that are not listed in the brick mapping
- Fill NaN values in brick mapping with zeroes. This is to indicate a skill is NOT present in a topic

### Merging: main actions
- Use master_courses to get the accurate main_topic for each course. The tom_enrolments and master_courses tables were merged on course_id and moodle_id respectively.


## Identifying the skills gaps at a country level: approach
In order to identify a skills gap for a given country the final cleaned enrolments dataset (complete with brick mapping data) needs to be manipulated in the following ways (note: we only consider courses that are fully completed):
1. enrolments data is grouped by learner country
2. For each country and brick type we count the number of bricks that were acquired
3. The lowest brick counts indicate skills gaps

This is our initial approach and does not take into account all available data including but not limited to course level, country risk, geography, etc...

## Project overview as of July 2024

## Next Steps as of July 2024
1. Use more data. This initial project was a pilot and only used a subset of the user data. To explore the data trends in more detail moodle_courses, moodle_enrols, moodle_users
2. Create and experiment with different recommenders. Consider more carefully how to identify skills gaps within a country and explore different approaches to mitigating the risk (e.g. how to prioritise which courses are needed, how to factor in geography and disease risk levels, etc…)
3. Add more differentiators or factors on the recommender systems such as Country, progress of the course, the last time continued on the course (in this case for example if the last login was too past, re-recommend again the course), course level (Beginner, Intermediate and Advanced) etc.
4. Collaborate with full stack colleagues to create a first version of a course recommendation system


