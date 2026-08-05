# Deployment System Requirements Document

---

# Part A. Deployment Vision

The CariSurg MedTech Pathways system provides continuous patient support, monitoring, and triage assistance across multiple patient entry pathways. All pathways connect into one continuous re-triage pipeline that remains active until the patient leaves the department.

Mercer General currently operates using paper-based processes and does not have an electronic health record system. Sister Alleyne identified digitisation of the existing triage form as a necessary first step before predictive systems can be introduced.

The deployment follows two phases:

## Phase 0: Digital Foundation

The existing paper triage front page is digitised to create a reliable digital patient record.

## Phase 1: Intelligent Patient Pathway

The system introduces:

* Predictive ESI recommendations.
* Continuous wearable monitoring.
* Patient communication through a mobile application.
* Physical accessibility support through Gigi.
* Continuous re-triage support for clinical staff.

The system supports healthcare professionals but does not replace nurses or doctors. All final clinical decisions remain human-controlled.

---

# System Architecture

The system consists of five connected components:

1. Registration kiosk.
2. Reusable Bluetooth wristband.
3. Patient smartphone application.
4. Gigi social robot.
5. Nurse dashboard.

The overall pathway is:

**Patient arrival → Registration → Wristband assignment → App/Gigi access → Continuous monitoring → Nurse review**

---

# Patient Entry and Data Streams

## Stream 1: Walk-In Self-Registration

Patients arriving independently enter through the walk-in pathway.

The registration kiosk provides:

* Patient registration.
* Demographic capture.
* Presenting complaint collection.
* Initial symptom information.
* Wristband assignment.
* Smartphone app connection.

Patients without smartphones can access their information through Gigi.

Mercer’s waiting room capacity and daily patient volume create practical constraints on kiosk numbers, queue speed, and physical placement.

---

## Stream 2: Ambulance Pre-Arrival

Patients arriving by ambulance enter through the emergency transport pathway.

Where available, ambulance information may include:

* Vital signs.
* Presenting complaint.
* Clinical observations.
* Pre-arrival notes.

The system generates an early ESI recommendation to support preparation before arrival.

Ambulance digital transmission is considered a target capability and requires confirmation from Mercer.

---

## Stream 3: Connected Wearable Integration

Wearable technology provides additional physiological information.

Supported devices include:

* Mercer-issued reusable Bluetooth wristbands.
* Compatible patient-owned smartwatches.
* Approved Bluetooth-enabled wearable devices.

The wearable layer supports:

* Heart rate monitoring.
* Oxygen saturation monitoring.
* Blood pressure monitoring where available.
* Vital trend tracking.

Wearable information supports clinical review but does not replace professional assessment.

---

# Component Requirements

# 1. Registration Kiosk Requirements

## Purpose

The registration kiosk provides the first digital interaction point for patients entering Mercer ED.

## Functions

The kiosk must:

* Capture patient demographics.
* Record presenting complaint.
* Capture arrival information.
* Create or link a patient record.
* Assign a wristband.
* Connect the patient to the mobile application when available.
* Provide instructions for accessing Gigi.

## Requirements

The kiosk must:

* Function without smartphone ownership.
* Support different levels of digital literacy.
* Provide accessibility options.
* Protect patient privacy.
* Support Mercer’s patient volume.

The kiosk provides information capture only and does not independently determine clinical priority.

---

# 2. Reusable Bluetooth Wristband Requirements

## Purpose

The wristband provides continuous patient monitoring using a simple reusable sensing device.

## Functions

The wristband:

* Collects supporting vital information.
* Connects through Bluetooth.
* Links the patient to the digital pathway.
* Sends information to approved systems.

## Requirements

The wristband must:

* Operate without requiring smartphone ownership.
* Connect with the patient app.
* Connect with Gigi where appropriate.
* Support approved smartwatch integration.
* Use wipeable, non-porous materials.
* Support repeat sterilisation.
* Have unique asset tracking.
* Display connection status.

The device must include appropriate accuracy limitations when consumer-grade wearable data is used.

---

# 3. Patient Application Requirements

## Purpose

The patient app provides a friendly digital companion that improves understanding and reduces uncertainty during ED care.

## Functions

The app provides:

* Patient status updates.
* Vital trend explanations.
* Educational information.
* Notifications.
* Conversational support through the Gigi personality.

The app should explain information without unnecessary medical terminology.

Example:

Instead of:

> Blood pressure: High

The app provides:

> Your blood pressure is above the usual range. Your care team will continue monitoring this information.

## Requirements

The application must:

* Be easy to navigate.
* Support accessibility features.
* Provide understandable explanations.
* Avoid self-diagnosis.
* Maintain patient privacy.
* Provide reassurance without replacing clinical communication.

Future personalisation features may include:

* Language selection.
* Communication preferences.
* Accessibility settings.

---

# 4. Gigi Social Robot Requirements

## Purpose

Gigi provides a physical interaction point for patients who do not have smartphones and improves engagement within the ED waiting environment.

Gigi extends the same friendly communication style used in the patient application.

## Location

Gigi is positioned within the ED waiting room.

## Functions

Gigi provides:

* Wristband identification.
* Patient status access.
* Waiting process updates.
* Educational explanations.
* Conversational guidance.
* Assistance navigating the ED experience.

## Requirements

Gigi must:

* Provide a calm and friendly interaction.
* Support patients without smartphones.
* Connect through Bluetooth.
* Provide offline educational content.
* Display clear connection states.
* Maintain patient privacy.
* Use accessible communication methods.

Gigi must not:

* Diagnose patients.
* Change ESI priority.
* Replace nurses or doctors.
* Provide independent medical decisions.

---

# 5. Nurse Dashboard Requirements

## Purpose

The nurse dashboard supports clinical decision-making and continuous re-triage.

## Functions

The dashboard displays:

* Patient information.
* ESI recommendation.
* Confidence level.
* Vital trends.
* Alerts.
* Manual assessments.

## Requirements

The dashboard must:

* Clearly identify automated recommendations.
* Allow nurse confirmation or override.
* Display deterioration alerts.
* Support continuous patient reassessment.

---

# Continuous Re-Triage Requirements

The system continuously evaluates patient information using:

* Wristband measurements.
* Smartwatch data where available.
* Patient-reported information.
* Nurse observations.
* Manual clinical assessments.

The system follows Mercer’s existing ESI framework:

* **ESI 1:** Immediate.
* **ESI 2:** Within 10 minutes.
* **ESI 3:** Within 30 minutes.
* **ESI 4:** Within 60 minutes.
* **ESI 5:** Can wait.

Priority rules:

* Deterioration increases urgency.
* Stabilisation does not reduce queue position.
* Patients are not penalised for improvement.

---

# Part B. Human-Machine Interface Requirements

## Patient Interfaces

The app, kiosk, and Gigi interface must:

* Present information clearly.
* Avoid relying on colour alone.
* Include text and icons with alerts.
* Support different literacy levels.
* Provide accessibility options.

---

## Clinical Interfaces

The nurse dashboard must:

* Display confidence levels.
* Clearly separate recommendations from decisions.
* Allow manual overrides.
* Maintain human control.

---

# Part C. Inputs and Outputs

## Inputs

The system receives:

* Registration information.
* Ambulance information.
* Wristband data.
* Smartwatch data.
* Patient app interactions.
* Gigi interactions.
* Nurse assessments.
* Manual overrides.

---

## Outputs

The system produces:

* Predicted ESI recommendations.
* Vital trend summaries.
* Patient updates.
* Educational explanations.
* Clinical alerts.
* Queue information.

---

# Part D. Build Path Choice

A hybrid development approach is proposed.

## Web Interface

Used for:

* Registration kiosks.
* Nurse dashboards.
* Digital triage records.

## Mobile Interface

Used for:

* Patient application.
* Wearable connection.
* Patient communication.

## Physical Prototype

Used for:

* Bluetooth wristband.
* Gigi social robot.

Physical hardware is reserved for areas where it provides clear value.

---

# Part E. Sustainable Development Goal Alignment

## SDG 3: Good Health and Well-Being

Supports safer monitoring, communication, and early recognition of deterioration.

## SDG 9: Industry, Innovation and Infrastructure

Creates a technology system appropriate for Mercer’s environment.

## SDG 12: Responsible Consumption and Production

Reusable wristbands reduce waste compared with single-use alternatives.

## SDG 10: Reduced Inequalities

Gigi ensures patients without smartphones still have access to information.

---

# Sustainability Trade-Off

Reusable wristbands reduce waste and cost but introduce infection-control requirements.

Mitigations:

* Enforced sterilisation procedures.
* Clean/dirty tracking.
* Adequate spare wristband inventory.
* Infection-control approval.

---

# Part F. Flagged Assumptions

The following require confirmation before development:

* Ambulance digital transmission capability.
* Smartwatch accuracy requirements.
* Wristband sterilisation method and turnaround time.
* Gigi Bluetooth operating requirements.
* Offline functionality requirements.
* Data privacy and retention rules.
* Number of kiosks required for patient volume.
* Integration requirements after Phase 0 digitisation.

---

# Final System Coverage

| Scenario                   | Solution                             |
| -------------------------- | ------------------------------------ |
| Walk-in patient            | Registration kiosk + wristband       |
| Ambulance arrival          | Pre-arrival pathway                  |
| Smartphone user            | Patient app                          |
| Patient without smartphone | Gigi access                          |
| Smartwatch user            | Wearable integration                 |
| Unidentified patient       | Emergency registration pathway       |
| Assisted patient           | Staff/caregiver support              |
| Repeat visitor             | Digital record support after Phase 0 |

The final CariSurg MedTech Pathways system creates a connected ED experience that combines digital intake, wearable monitoring, patient communication, and social interaction while maintaining accessibility, sustainability, and human clinical oversight.
