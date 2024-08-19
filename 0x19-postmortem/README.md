# 0x19. Postmortem
- DevOps, SysAdmin

# Postmortem Report: Apache2 Server Downtime on WebServer-01

## Overview

This repository contains the postmortem report for the Apache2 server downtime incident that occurred on WebServer-01 on 08/18/2024. The incident affected premium service users, leading to login errors and system outages. The report includes a detailed timeline, root cause analysis, resolution steps, and corrective measures to prevent future occurrences.

## Report Structure

- **Issue Summary**: Provides an overview of the incident, including its duration, impact, and root cause.
- **Timeline**: A chronological breakdown of the events during the incident, highlighting key actions and decisions.
- **Root Cause and Resolution**: Detailed explanation of the underlying issue and the steps taken to resolve it.
- **Corrective and Preventative Measures**: Actionable tasks and improvements aimed at preventing similar incidents in the future.
- **Lessons Learned**: Insights gained from the incident response, highlighting areas for improvement.

## Visual Representations

The following images visually represent the web server monitoring and incident response system used during the incident:

### Image 1: Software engineer responding to a system error call
![postmortem1](https://github.com/user-attachments/assets/02ae995b-8a8a-4b2d-9b50-3b5473f22095)


### Image 2: Web Server Monitoring and Incident Response 
![postmortem-wide](https://github.com/user-attachments/assets/0aa35a4b-0bed-4978-b192-36cebc97e31b)


These images illustrate the relationship between the monitored service (Apache2), the monitoring tool (Datadog), the on-call management system (PagerDuty), and the software engineer's response process.

## Usage

This report is intended to serve as a reference for understanding the incident, analyzing the root cause, and implementing preventative measures. It is also a valuable resource for teams handling similar infrastructure and monitoring setups.

## License

This report and associated files are licensed under the [MIT License](LICENSE).
