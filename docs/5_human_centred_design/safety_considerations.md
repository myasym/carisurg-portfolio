# Safety Considerations

## Purpose

This document outlines the key safety considerations for the Human Computer Interaction (HCI) and Human Robot Interaction (HRI) components of the proposed emergency department system. The aim is to ensure that technology supports clinical care without compromising patient safety, staff workflow or accessibility.

---

# Human Computer Interaction (HCI) Safety Considerations

## 1. Alarm Fatigue

**Risk**

Frequent or unnecessary alerts can desensitise healthcare staff, increasing the likelihood that important warnings are overlooked.

**Safety Mechanism**

The system prioritises alerts using the existing Emergency Severity Index (ESI) escalation model. Notifications are grouped by urgency, with audible alerts reserved only for significant deterioration such as amber and red alerts. Routine updates appear as visual notifications on the nurse dashboard to reduce unnecessary interruptions.

---

## 2. Display Legibility Under Stress

**Risk**

Emergency department staff make rapid decisions in high pressure environments. Poor interface design may delay recognition of critical patient information.

**Safety Mechanism**

The nurse dashboard uses large, high contrast text, consistent layouts, and colour coding supported by icons and text labels. Automated ESI recommendations include a visible confidence indicator and can be reviewed within approximately two seconds. Colour is never used as the only method of communicating urgency.

---

## 3. Accessibility for Different Users

**Risk**

Patients and clinicians have different levels of digital literacy, visual ability and physical capability. Interfaces designed for a single type of user may exclude vulnerable groups.

**Safety Mechanism**

The registration kiosk and patient application support large text, plain language, touchscreen navigation and accessible colour contrast. Patients without smartphones can access the same information through Gigi, ensuring that digital services remain available regardless of personal device ownership.

---

# Human Robot Interaction (HRI) Safety Considerations

## 1. Proximity Safety

**Risk**

A physical robot operating in a busy emergency department could obstruct movement or create hazards for patients and staff.

**Safety Mechanism**

Gigi is designed as a stationary robot located in the waiting area rather than a mobile platform. It remains outside primary clinical pathways, reducing collision risks while remaining accessible to patients.

---

## 2. Voice Input in Noisy Environments

**Risk**

Background conversations, medical equipment and emergency activity may reduce the accuracy of voice recognition.

**Safety Mechanism**

Voice interaction is optional rather than essential. All functions are available through a touchscreen interface with large buttons and simple navigation. If voice input is not recognised, Gigi automatically prompts the user to continue using the touchscreen.

---

## 3. Graceful Degradation During Connectivity Failure

**Risk**

Bluetooth disconnections or system failures could prevent Gigi from retrieving patient information, leading to confusion or incorrect expectations.

**Safety Mechanism**

If connectivity to the wristband or hospital system is lost, Gigi enters a clearly labelled offline mode. Instead of displaying incomplete or outdated patient information, it provides general educational content and advises the patient to speak with a member of staff. Clinical care continues through normal hospital procedures and does not depend on the robot.

---

# Summary

The proposed system is designed to support rather than replace healthcare professionals. Safety is achieved through clear interfaces, accessible interaction methods, prioritised alerts and fail safe behaviour that allows patient care to continue even if individual technologies become unavailable.
