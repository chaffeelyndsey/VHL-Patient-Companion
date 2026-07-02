# Database Schema

## Tables

### tumors
| Field | Type | Description|
|---|---|---|
| tumor_id| INTEGER PRIMARY KEY | Unique tumor record |
| organ_system | TEXT | Brain, spine, kidney, pancreas, adrenal, eye, inner ear |
| location | TEXT | Specific anatomical location | 
| size_mm | REAL | Tumor size in millimeters | 
| date_found | DATE | Date tumor was first identified | 
| last_imaging_date | DATE | Most recent imaging date |
| physician | TEXT | Additional notes | 

### appointments
| Field | Type | Description | 
|---|---|---|
| appointment_id | INTEGER PRIMARY KEY | 
| appointment_type | TEXT | 
| date | DATE |
| provider | TEXT |
| location | TEXT | 
| notes | TEXT |
| follow_up_needed | BOOLEAN | 

### symptoms 
| Field | Type | Description | 
|---|---|---| 
| symptom_id | INTEGER PRIMARY KEY | 
| date | DATE | 
| symptom | TEXT | 
| severity | INTEGER | 
| duration | TEXT | 
| notes | TEXT | 

### medications
| Field | Type | Description |
|---|---|---| 
| medication_id| INTEGER PRIMARY KEY | 
| medication_name | TEXT | 
| dose | TEXT | 
| frequency | TEXT | 
| start_date | DATE | 
| notes | TEXT | 

