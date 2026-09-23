# Smart Fitness Session Analyzer
by Jakob Oliver Evensen

Student number: s385406

## Description

This program looks at simulated data during a training session. It checks each measurement for bad or missing data, caluclates averages and compares the result to the participants normal values. Based on this it decides if the session was resting, moderate activity, high activity or recovering. Lastly it prints a short report explaning why

## Class design
Participant - Represents a session participant and their personal baseline values.

Observation - Represents a single window of measurement. 

Session - Groups a Paticipant with a list of Obseration objects

SessionAnalyzer - Takes a Session and makes the full analysis, summary, baseline comparison etc.

Standalone functions: compute_summary, compare_to_baseline, detect_recovery, format_report".

Separated to fulfill the assignment as well as handling calculations and presentation independently so they could be reused and tested on their own. 


## Composition, encapsulation and inheritance

Composition:

Session has a Participant and a list of Observation objects. SessionAnalyzer has a Session. Composition is used to model them because none has relationships that are "is-a". 

Encapsulation:

every class stores its data in private variables so you cant directly access these from outside the class. I made get-methods instead that return the value. By doing this i ensure that the class is in control of its own data rather than other code being able to just overwrite it.

Inheritance:

I saw no reason to use inheritance in this task other than forceing it to fulfill the requirements. By using only using composition i keep each class focused on a single responsibility while still having them collaborate. For exampl ewhen session calls for get_is_valid from observation. 

## Assumptions and classification rules

Based on the "DATA_DESCRIPTION.md" i used the following ranges for validation:

heart_rate: 35-205 bpm

skin_response: 0 or greater

temperature: 25-42 C

activity_level: 0-1

signal_quality: 0-1

Observations that fail the check will be treated as invalid and not be included in the analysis

Classification:

Insufficient data: fewer than 3 valid observations in the session

Recovering: average heart rate in the second half of the sessionis at least 10 bpm lower than in the first half AND the overall average is still 15 bpm above baseline. 

Resting: average heart rate is within 15 bpm of baseline

Moderate activity: average heart rate is 15-45 bpm above baseline

High activity: average heart rate is more than 45 bpm above baseline


## Installation and running instructions

No third-party packages are required

```bash
git clone https://github.com/JakobEve/fitness_session_analyzer.git
cd fitness_session_analyzer
python main.py
```

Running the rest requires only
```bash
python tests.py
```

## Example output
```
Resting session
---- Session Report ----
Participant: P001
Usable observations: 12 of 12
Classification: resting
Explanation: Heart rate is close to the participant's baseline

Moderate activity
---- Session Report ----
Participant: P001
Usable observations: 12 of 12
Classification: moderate activity
Explanation: Heart rate is moderately elevated above baseline

High activity
---- Session Report ----
Participant: P001
Usable observations: 12 of 12
Classification: high activity
Explanation: Heart rate is very elevated above baseline

Activity followed by recovery
---- Session Report ----
Participant: P001
Usable observations: 12 of 12
Classification: recovering
Explanation: Heart rate is falling toward baseline after elevated activity

Poor-quality sensor data
---- Session Report ----
Participant: P001
Usable observations: 0 of 12
Classification: insufficient data
Explanation: too few valid observations to analyze the session
```


## Known limitations

Recovery detection compares the average of the first half to the second half so it doent analyze the metric in detail

Program has only been tested against false scenarios made by the generator, not against real data. 