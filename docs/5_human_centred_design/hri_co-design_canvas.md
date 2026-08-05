# Human-Robot Interaction (HRI) Design Space

---
# Canvas #01: PROBLEM SPACE

## SOCIAL ROBOT CO-DESIGN CANVASES

### What problem are you solving?

## USER

### Primary Users

## Group(s)

**Patients waiting in Mercer General Emergency Department**

### Characteristics

* Patients experiencing uncertainty, anxiety, discomfort, or long waiting times.
* Different ages, health literacy levels, and technology abilities.
* Some patients may not own smartphones or may not be comfortable using digital technology.
* Patients may need reassurance while waiting for clinical review.

### Needs

* Access to their care status without relying on personal technology.
* Clear explanations of waiting processes and health information.
* Reassurance that their condition is being monitored.
* A simple and approachable way to interact with the healthcare system.

### Goal(s)

**Short-Term**

* Complete registration.
* Receive a wristband.
* Access information about their current ED journey.
* Understand what happens next while waiting.

**Long-Term**

* Improve confidence and trust in ED processes.
* Reduce anxiety caused by uncertainty.
* Improve patient engagement and understanding.

---

### Secondary Users

## Group(s)

**Nurses, doctors, and ED staff**

### Characteristics

* Healthcare professionals working under time pressure.
* Responsible for patient assessment and clinical decisions.
* Need efficient communication methods that do not increase workload.

### Needs

* Patients who understand the waiting process.
* Reduced repetitive questions.
* A reliable communication support tool.
* Ability to maintain human oversight.

### Goal(s)

**Short-Term**

* Reduce avoidable interruptions.
* Support patient communication.
* Improve waiting-room experience.

**Long-Term**

* Improve ED workflow.
* Support safer continuous re-triage.
* Improve patient satisfaction.

---

# ROBOT

## GIGI (Guided Information & Guidance Interface)

---

## Task(s)

### Short-Term

GIGI performs:

* Provides patient information access.
* Allows wristband identification through Bluetooth.
* Displays waiting status updates.
* Explains basic health information.
* Provides educational content.
* Answers non-clinical patient questions.

### Long-Term

GIGI supports:

* Digital inclusion for patients without smartphones.
* Improved patient communication.
* Reduced uncertainty during ED waiting.
* Consistent patient education across app and physical interaction.

---

# Advantages

## What advantages does using a robot bring compared with a computer or human?

### Social Presence

* Provides a physical interaction point in the waiting environment.
* Creates a sense that patients are acknowledged.
* Reduces the feeling of being forgotten during long waits.

### Accessibility

* Allows patients without smartphones to access the same information available through the mobile app.
* Supports patients with limited digital literacy.

### Patient Engagement

* Encourages patients to understand their care journey.
* Provides information without requiring constant staff involvement.

### Consistent Communication

* Delivers the same friendly information style as the patient application.

---

# Social Skills

## User’s Emotional Response

GIGI should create:

* Trust.
* Calmness.
* Reassurance.
* Comfort.

GIGI should avoid:

* Pretending to be a healthcare professional.
* Creating emotional dependency.
* Giving false reassurance.

---

## Personalisation

Possible future personalisation:

* Preferred language.
* Accessibility preferences.
* Communication style.
* Font size and display settings.

Personalisation should improve accessibility without collecting unnecessary personal data.

---

## Precise Tasks

GIGI performs:

* Patient identification through wristband interaction.
* Information retrieval.
* Patient education.
* Waiting process explanation.
* Navigation support.

GIGI does not:

* Diagnose patients.
* Assign ESI levels independently.
* Change patient priority.
* Replace healthcare professionals.

---

## Data Collection with Sensors

GIGI uses:

* Bluetooth connection to wristbands.
* Touch interaction.
* Screen interaction.
* Optional voice input.

Data received:

* Patient identifier.
* Approved status information.
* Educational content requirements.

GIGI does not independently collect unnecessary clinical data.

---

## Mobility

**Stationary robot**

GIGI remains in the ED waiting area.

Reasons:

* Safer deployment.
* Lower maintenance requirements.
* More suitable for Mercer’s resource environment.
* Reduces physical safety risks.

---

## Environment Manipulation

GIGI can:

* Display information.
* Provide audio communication.
* Present educational content.
* Provide visual feedback.

GIGI cannot:

* Move patients.
* Perform medical procedures.
* Physically intervene in care.

---

## Connection to Systems

GIGI connects with:

* Patient registration system.
* Bluetooth wristband system.
* Patient mobile application.
* Hospital information system after Phase 0 digitisation.

Information flow:

**Registration kiosk → Wristband → GIGI/App → Clinical system**

---

# Canvas #02: ETHICAL CONSIDERATIONS

## Physical Safety

### Problem

Patients may interact with the robot while stressed, confused, or physically unwell.

### Solution

* Stationary design.
* No physical movement around patients.
* Clear emergency contact instructions.
* Human staff remain responsible for care.

---

## Transparency

### Problem

Patients may misunderstand GIGI’s capabilities.

### Solution

GIGI clearly communicates:

* It provides information only.
* It does not diagnose.
* Healthcare staff make decisions.

---

## Emotional Consideration

### Problem

Patients may form strong emotional attachment to GIGI.

### Solution

* Friendly but professional personality.
* Avoid language suggesting human feelings.
* Encourage connection with healthcare staff.

---

## Data Security

### Problem

GIGI accesses patient-related information.

### Solution

* Bluetooth authentication through wristband.
* Limited data access.
* Secure storage.
* Privacy controls.

---

## Equality Across Users

### Problem

Technology may exclude patients with limited digital access.

### Solution

* Physical GIGI access.
* App alternative.
* Accessible interface design.
* Multiple communication methods.

---

## Behaviour Enforcement

### Problem

Users may misuse or abuse the robot.

### Solution

* Clear interaction rules.
* Limited capabilities.
* Staff escalation option.

---

# Canvas #03: DESIGN GUIDELINES

## Environment Guidelines

* Designed for ED waiting rooms.
* Must operate in a busy, noisy environment.
* Must support multiple users.
* Must not obstruct patient movement.

---

## Interaction Guidelines

* Patient-led interaction.
* Simple touch and voice options.
* Short, clear conversations.
* Focus on information and reassurance.

---

## Behaviour Guidelines

* Calm and predictable behaviour.
* Friendly but professional.
* Context-aware responses.
* No independent clinical decisions.

---

## Form Guidelines

* Approachable appearance.
* Not overly human-like.
* Easy-to-clean materials.
* Visible screen and communication indicators.

---

# Canvas #04: ROBOT DESIGN MVP

## Where and When

**Location:**

* Mercer ED waiting room.

**Time:**

* Continuous operation during ED hours.

---

## Robot’s Role

GIGI is:

* A guide.
* A helper.
* A patient communication assistant.

---

## Personality

GIGI is:

* Friendly.
* Calm.
* Supportive.
* Informative.

---

## Interaction Modalities

### Input

✓ Touch
✓ Voice (optional)
✓ Wristband Bluetooth connection
✓ Screen interaction

### Output

✓ Screen
✓ Voice
✓ Visual indicators
✓ Educational content

---

## Connection to Systems

GIGI connects to:

* Patient application.
* Wristband system.
* Registration system.
* Hospital digital records.

---

# Canvas #05: ENVIRONMENT

## User(s)

Primary:

* ED patients.

Secondary:

* Nurses.
* Doctors.
* Visitors/caregivers.

---

## Where

* Emergency department waiting room.

---

## When

* During patient waiting periods.
* Before clinical assessment or while awaiting updates.

---

## External Sensors and Actuators

Sensors:

* Bluetooth receiver.
* Touchscreen.
* Optional microphone.

Outputs:

* Screen.
* Speaker.
* Visual indicators.

---

## Data Collection

Collected data:

* Wristband identification.
* User interaction information.

Stored:

* According to hospital privacy requirements.

---

## Simultaneous Users

Recommended:

* One patient interaction at a time.
* Multiple patients can access through separate sessions.

---

# Canvas #06: FORM

## Appearance

Hybrid:

* Friendly technology.
* Healthcare appropriate.
* Not human-like.

---

## Size

* Compact.
* Suitable for waiting-room placement.

---

## Movement

* Stationary.

---

## Voice

* Calm.
* Neutral.
* Accessible.

---

## Visual Cues

Includes:

* Screen.
* Status indicators.
* Friendly interface graphics.

---

# Canvas #07: INTERACTION

## Interaction Modalities

### Input

* Touch.
* Voice.
* Wristband identification.

### Output

* Screen.
* Voice.
* Visual information.

---

## Leadership

**User-led**

The patient chooses when to interact.

---

## Situation Flow

**Predefined but flexible**

Common interaction:

Patient taps wristband → GIGI identifies patient → Displays updates → Answers questions.

---

## Goal

**Informative + task completion**

---

## Robot Name

**GIGI**

Meaning:

**Guided Information & Guidance Interface**

---

# Canvas #08: BEHAVIOUR

## Social Behaviours

* Greets users.
* Uses polite language.
* Provides reassurance.
* Explains processes.

---

## Personality

* Friendly.
* Patient.
* Reliable.

---

## Personalisation

Possible:

* Language.
* Accessibility.
* Communication preferences.

---

## Robot Role

Helper and guide.

---

## Mode of Operation

Semi-autonomous:

* Automated information delivery.
* Human-controlled clinical decisions.

---

## Social Skills

Moderate:

* Greeting.
* Conversation.
* Basic assistance.

---

# Canvas #09: SERVICE ECOSYSTEM

## Primary Users

Patients.

## Secondary Users

* Nurses.
* Doctors.
* Hospital administrators.

## Robot

GIGI.

## External Systems

* Registration kiosk.
* Patient app.
* Wristband system.
* Hospital database.

## Data Flow

Patient → Wristband → GIGI/App → Hospital system → Staff

---

# Canvas #10: EXPERIENCE FLOW

## Before

### Patient

* Arrives at ED.
* Registers.
* Receives wristband.

### GIGI

* Available in waiting area.

---

## During

### Patient

* Checks status.
* Receives explanations.
* Learns about care process.

### GIGI

* Identifies patient.
* Displays information.
* Provides reassurance.

---

## After

### Patient

* Receives next-step instructions.

### GIGI

* Ends interaction.
* Maintains system readiness for next patient.
