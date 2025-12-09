**CodeNova Security System**

Project Overview

CodeNova Security System is a console-based simulation for enterprise cybersecurity and incident response, designed for a tech startup environment. The system demonstrates the following:

User authentication with strong passwords and hashed storage

Cryptography & hashing demo (SHA-256, Base64)

Incident handling & reporting

Business Impact Analysis (BIA)

Threat & Vulnerability Assessment

Security Controls (Technical, Administrative, Physical)

Legal & Ethical Compliance measures

Audit logs and accountability

This system was built as a Final Project for a tech startup cybersecurity simulation.


⚙ **Features**

**User Management**

        Register and login users/admins

        Enforces strong password rules

        Passwords stored securely using SHA-256 hashing

**Cryptography & Hashing Demo**

        SHA-256 hash of passwords

        Base64 encoding demonstration

        Validates user login via hash comparison

**Incident Handling**

        Report and track security incidents

        View all incident logs with date, time, affected systems, and status

**Business Impact Analysis (BIA)**

        Add/view BIA records

        Includes asset, threat scenario, financial & operational impact, recovery strategy

**Threat & Vulnerability Assessment**

        Manage threats and vulnerabilities

        Assign likelihood, impact, and countermeasures

**Security Controls**

        Technical, Administrative, and Physical controls

        View or manage security policies

**Legal & Ethical Compliance**

        Store company policies

        Audit enforcement of compliance and actions

**Audit Logging**

        All activities logged in system.log

        Tracks user actions for accountability


**🔐 Cryptography & Hashing Demo**

**Run the demo:**

python crypto_demo_full.py


**Register a user:**

Username: crypto_test

Password: Crypto123!

**Login to see:**

SHA-256 hashed password

Base64 encoded password

Hash comparison validation

**View stored hashes:
**

python view_users.py



📄 JSON & Database Files

All persistent data stored in data/:

**File	                        Purpose**
users.db	                User credentials (hashed passwords)
incidents.json	                Incident reports
bia.json	                BIA records
assets.json	                Asset inventory
threats.json	                Threat & vulnerability matrix
physical_controls.json	        Physical security controls
compliance.json	                Legal & ethical compliance policies
