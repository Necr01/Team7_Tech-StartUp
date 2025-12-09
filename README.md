### CodeNova Security System

Project Overview

CodeNova Security System is a console-based simulation for enterprise cybersecurity and incident response, designed for a tech startup environment. The system demonstrates the following:

- User authentication with strong passwords and hashed storage

- Cryptography & hashing demo (SHA-256, Base64)

- Incident handling & reporting

- Business Impact Analysis (BIA)

- Threat & Vulnerability Assessment

- Security Controls (Technical, Administrative, Physical)

- Legal & Ethical Compliance measures

- Audit logs and accountability

This system was built as a Final Project for a tech startup cybersecurity simulation.


⚙ **Features**

**User Management**

1. Register and login users/admins

2. Enforces strong password rules

3. Passwords stored securely using SHA-256 hashing

**Cryptography & Hashing Demo**

1. SHA-256 hash of passwords

2. Base64 encoding demonstration

3. Validates user login via hash comparison

**Incident Handling**

1. Report and track security incidents

2. View all incident logs with date, time, affected systems, and status

**Business Impact Analysis (BIA)**

1. Add/view BIA records

2. Includes asset, threat scenario, financial & operational impact, recovery strategy

**Threat & Vulnerability Assessment**

1. Manage threats and vulnerabilities

2. Assign likelihood, impact, and countermeasures

**Security Controls**

1. Technical, Administrative, and Physical controls

2. View or manage security policies

**Legal & Ethical Compliance**

1. Store company policies

2. Audit enforcement of compliance and actions

**Audit Logging**

1. All activities logged in system.log

2. Tracks user actions for accountability

### Cryptography & Hashing Demo

- Run the demo:

      python crypto_demo_full.py

- Register a user:

      Username: crypto_test

      Password: Crypto123!

- Login to see:

      SHA-256 hashed password

      Base64 encoded password

      Hash comparison validation

- View stored hashes:

      python view_users.py




### 📄 JSON & Database Files

| File | Purpose |
|------|---------|
| `users.db` | Stores user credentials with hashed passwords (SHA-256). |
| `incidents.json` | Contains all reported security incidents. |
| `bia.json` | Stores Business Impact Analysis (BIA) records. |
| `assets.json` | Maintains the company’s asset inventory. |
| `threats.json` | Contains the threat and vulnerability matrix. |
| `physical_controls.json` | Lists physical security controls. |
| `compliance.json` | Stores legal and ethical compliance policies. |
