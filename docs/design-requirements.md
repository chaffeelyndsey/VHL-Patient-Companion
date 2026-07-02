# Design Requirements

## User Needs

The application should help a VHL patient to keep track of lifelong surveillance needs, symptoms, appointments, and tumor history. 


## Functional Requirements

1. The system shall allow the user to enter tumor information.
2. The system shall allow the user to track tumor size over time.
3. The system shall allow the user to enter appointments.
4. The system shall allow the user to log symptoms.
5. The system shall allow the user to record medications.
6. The system shall display upcoming surveillance tasks.
7. The system shall provide an emergency information summary.

## Nonfunctional Requirements

1. The interface should be simple and readible.
2. The system should protect sensitive health information in future versions.
3. The application should be easy to update.
4. The system should be documented clearly enough fo ranother developer to understand.

##Initial Data Fields

### Tumor Tracker

- Tumor ID
- Organ system
- Location
- Size
- Date found
- Last imaging date
- Notes
- Physician

### Appointment Tracker

- Appointment type
- Date
- Provider
- Location
- Notes
- Follow-up needed

### Symptom Tracker

- Date
- Symptom
- Severity
- Duration
- Notes

### Medication Tracker

- Medication name
- Dose
- Frequency
- Start date
- Notes
- Prescribing physician
