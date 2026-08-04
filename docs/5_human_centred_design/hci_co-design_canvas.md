# Human-Computer Interaction (HCI) Design Space

---

# Canvas #01: PROBLEM SPACE

## What problem are you solving?

The system addresses uncertainty, delays, and communication barriers within Mercer General’s emergency department.

Patients currently have limited visibility into their care journey while waiting. Staff experience pressure from repeated status questions, manual processes, and limited digital infrastructure.

The HCI solution creates a connected digital pathway that allows patients and healthcare workers to access relevant information while maintaining human clinical decision-making.

---

# USER

## Primary Users

## Group(s)

**Patients attending Mercer General Emergency Department**

---

## Characteristics

Patients may:

* Arrive through walk-in or ambulance pathways.
* Experience stress, pain, anxiety, or uncertainty.
* Have different levels of digital literacy.
* Own or not own smartphones.
* Include vulnerable groups such as elderly patients, children, and pregnant patients.

---

## Needs

Patients need:

* Clear registration.
* Understanding of their waiting status.
* Simple health explanations.
* Confidence that they are being monitored.
* Access regardless of smartphone ownership.

---

## Goal(s)

### Short-Term

Patients want to:

* Register quickly.
* Receive a wristband.
* Understand what happens next.
* Access updates during waiting.

### Long-Term

Patients want to:

* Feel informed and reassured.
* Trust the ED process.
* Participate more actively in their care journey.

---

# Secondary Users

## Group(s)

**Healthcare staff**

* Nurses.
* Doctors.
* Registration staff.
* Hospital administrators.

---

## Characteristics

Healthcare staff:

* Work in high-pressure environments.
* Require fast access to accurate information.
* Need systems that reduce workload rather than increase it.

---

## Needs

Staff need:

* Reliable patient information.
* Clear alerts.
* Clinical oversight.
* Easy documentation.
* Ability to override automated recommendations.

---

## Goal(s)

### Short-Term

Staff want to:

* Reduce repeated patient enquiries.
* Improve patient information flow.
* Support triage decisions.

### Long-Term

Staff want to:

* Improve ED efficiency.
* Improve patient experience.
* Support safer continuous monitoring.

---

# COMPUTER SYSTEM

## Tasks

---

# Registration Kiosk

## Short-Term Tasks

* Capture patient information.
* Record presenting complaint.
* Create digital patient record.
* Assign wristband.

## Long-Term Tasks

* Replace paper intake processes.
* Create the foundation for digital triage.

---

# Patient Mobile Application

## Short-Term Tasks

* Connect with wristband.
* Display patient updates.
* Explain waiting processes.
* Provide educational content.

## Long-Term Tasks

* Support continuous patient engagement.
* Provide personalised accessibility features.

---

# Nurse Dashboard

## Short-Term Tasks

* Display patient information.
* Show vital trends.
* Provide ESI recommendations.
* Allow manual confirmation.

## Long-Term Tasks

* Support continuous re-triage.
* Improve workflow coordination.

---

# Advantages

## What advantages does using a computer interface bring compared with human-only interaction?

---

## Accessibility

* Patients can access information without repeatedly approaching staff.
* Supports patients who may not communicate easily.

---

## Consistency

* Provides standardised information.
* Reduces variation in explanations.

---

## Data Management

* Converts paper processes into structured digital information.
* Supports future electronic health record integration.

---

## Continuous Monitoring

* Receives wearable information over time.
* Identifies trends rather than single measurements.

---

## Personalisation

Allows future adaptation:

* Language.
* Accessibility settings.
* Communication preferences.

---

## Connection to Systems

Interfaces connect:

* Registration database.
* Wristband Bluetooth system.
* Patient app.
* Clinical dashboard.

---

# Canvas #02: ETHICAL CONSIDERATIONS

---

# Physical Safety

## Problem

Patients may misunderstand digital information or rely on it instead of seeking help.

## Solution

* Clear warnings that information does not replace medical advice.
* Easy access to staff assistance.
* Emergency escalation pathways.

---

# Transparency

## Problem

Patients may assume predictions are final decisions.

## Solution

* Label AI outputs as recommendations.
* Show confidence levels.
* Provide explanations.

---

# Emotional Consideration

## Problem

Waiting for emergency care creates anxiety.

## Solution

* Friendly language.
* Reassuring explanations.
* Avoid alarming notifications.

---

# Data Security

## Problem

The system handles sensitive health information.

## Solution

* Secure authentication.
* Limited data access.
* Patient privacy controls.
* Hospital-approved storage.

---

# Equality Across Users

## Problem

Technology may exclude people without smartphones or digital skills.

## Solution

* Registration kiosk access.
* GIGI physical access.
* Accessible design.
* Alternative staff-supported pathways.

---

# Behaviour Enforcement

## Problem

Patients may misuse systems or enter incorrect information.

## Solution

* Clear instructions.
* Validation checks.
* Staff review.

---

# Canvas #03: DESIGN GUIDELINES

---

# Environment Guidelines

The interface must work in:

* Busy emergency departments.
* Noisy environments.
* High patient volume conditions.

The design must prioritise:

* Speed.
* Accessibility.
* Reliability.

---

# Interaction Guidelines

The interface should:

* Minimise unnecessary steps.
* Use simple language.
* Support multiple input methods.
* Allow patients to control interaction.

---

# Behaviour Guidelines

The system should:

* Provide predictable responses.
* Avoid unnecessary alerts.
* Adapt to user needs.

---

# Form Guidelines

The interface should be:

* Simple.
* Calm.
* Easy to understand.
* Accessible.

---

# Canvas #04: HCI DESIGN MVP

---

# Where and When

## Registration Kiosk

Location:

* ED entrance.

Time:

* Patient arrival.

---

## Patient App

Location:

* Patient smartphone.

Time:

* During ED waiting.

---

## Nurse Dashboard

Location:

* Clinical workspace.

Time:

* Throughout patient care.

---

# Interface Role

The system acts as:

* Guide.
* Information provider.
* Monitoring support tool.

---

# Personality

Patient-facing interface:

* Friendly.
* Reassuring.
* Clear.

Clinical interface:

* Professional.
* Efficient.
* Precise.

---

# Interaction Modalities

## Input

✓ Touchscreen
✓ Keyboard/text entry
✓ Bluetooth wristband
✓ Smartwatch data
✓ Nurse input

---

## Output

✓ Text
✓ Icons
✓ Visual alerts
✓ Notifications
✓ Vital summaries

---

# Connection to Systems

Interfaces connect with:

* Wristband.
* Smartwatch.
* Hospital database.
* Nurse dashboard.

---

# Canvas #05: ENVIRONMENT

---

# Users

Primary:

* Patients.

Secondary:

* Nurses.
* Doctors.
* Registration staff.

---

# Where

* ED entrance.
* Waiting area.
* Clinical workspace.

---

# When

* Registration.
* Waiting period.
* Continuous monitoring.

---

# External Sensors

* Bluetooth wearable sensors.
* Smartwatch sensors.

---

# Data Collection

Collected:

* Registration details.
* Vital trends.
* User interactions.

Stored:

* According to healthcare privacy requirements.

---

# Simultaneous Users

The system supports:

* Multiple patients.
* Multiple staff users.

---

# Canvas #06: FORM

---

# Interface Appearance

The system should appear:

* Friendly.
* Clean.
* Healthcare appropriate.

---

# Visual Design

Includes:

* Clear icons.
* Large readable text.
* Simple navigation.

---

# Notifications

Alerts should include:

* Text.
* Symbols.
* Colour indicators.

Colour should never be the only cue.

---

# Accessibility

Supports:

* Large text.
* Multiple languages.
* Simple explanations.

---

# Canvas #07: INTERACTION

---

# Interaction Modalities

## Input

* Touch.
* Text.
* Voice (future).
* Wearable connection.

## Output

* Screen information.
* Notifications.
* Educational content.

---

# Leadership

**User-led**

Patients and staff control when interaction occurs.

---

# Situation Flow

**Flexible**

Different users enter and exit at different points.

---

# Goal

Task completion + information sharing.

---

# Canvas #08: BEHAVIOUR

---

# System Behaviour

The interface should:

* Respond quickly.
* Provide useful information.
* Avoid overwhelming users.

---

# Context-Based Behaviour

Changes based on:

* Patient status.
* Waiting stage.
* Alert level.

---

# Personalisation

Possible:

* Language.
* Accessibility settings.
* Communication preferences.

---

# Mode of Operation

Semi-autonomous:

* Automated information delivery.
* Human clinical control.

---

# Canvas #09: SERVICE ECOSYSTEM

---

# Primary Users

Patients.

---

# Secondary Users

* Nurses.
* Doctors.
* Administrators.

---

# External Systems

* Wristband.
* Smartwatch.
* Registration kiosk.
* Patient app.
* Hospital database.

---

# Data Flow

Patient → Interface → Wearable → Clinical system → Staff

---

# Canvas #10: EXPERIENCE FLOW

---

# BEFORE

## Patient

* Arrives at ED.
* Uses registration kiosk.
* Receives wristband.

## System

* Creates patient record.
* Connects digital pathway.

---

# DURING

## Patient

* Checks updates.
* Receives explanations.
* Views monitoring information.

## System

* Collects wearable data.
* Provides notifications.

## Staff

* Reviews information.
* Confirms clinical decisions.

---

# AFTER

## Patient

* Receives discharge or next-step information.

## System

* Ends monitoring.
* Stores appropriate records.

---

## Final HCI Design Summary

The HCI system creates a connected digital pathway between patients, wearable technology, and healthcare staff. It improves transparency and reassurance while ensuring that clinical decisions remain with healthcare professionals.

**HCI Components:**

* Registration kiosk.
* Patient mobile application.
* Nurse dashboard.
* Wearable interface.

**HRI Component:**

* GIGI social robot.
