CodeNova Security System

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

📂 Folder Structure
CodeNova_Security_System/
│ app.py                   ← main console system
│ crypto_demo_full.py      ← cryptography & hashing demo
│ view_users.py            ← view users & hashed passwords
│ database.py              ← database setup
│ incident_response.py     ← incident handling module
│ bia.py                   ← business impact analysis module
│ utils.py                 ← helper functions
│ system.log               ← audit/log file
│ README.md
└── data/
    ├ users.db             ← SQLite database for users
    ├ incidents.json       ← incident reports
    ├ bia.json             ← BIA records
    ├ assets.json          ← company assets
    ├ threats.json         ← threat & vulnerability matrix
    ├ physical_controls.json ← physical security controls
    └ compliance.json      ← legal & ethical compliance policies

⚙ Features

User Management

Register and login users/admins

Enforces strong password rules

Passwords stored securely using SHA-256 hashing

Cryptography & Hashing Demo

SHA-256 hash of passwords

Base64 encoding demonstration

Validates user login via hash comparison

Incident Handling

Report and track security incidents

View all incident logs with date, time, affected systems, and status

Business Impact Analysis (BIA)

Add/view BIA records

Includes asset, threat scenario, financial & operational impact, recovery strategy

Threat & Vulnerability Assessment

Manage threats and vulnerabilities

Assign likelihood, impact, and countermeasures

Security Controls

Technical, Administrative, and Physical controls

View or manage security policies

Legal & Ethical Compliance

Store company policies

Audit enforcement of compliance and actions

Audit Logging

All activities logged in system.log

Tracks user actions for accountability

💻 Installation

Clone the repository:

git clone https://github.com/yourusername/CodeNova_Security_System.git
cd CodeNova_Security_System


Ensure Python 3.8+ is installed:

python --version


Install any dependencies (if needed):

pip install -r requirements.txt


Note: This system uses only the Python standard library, so no additional packages are required.

🚀 How to Run

Initialize the database (first run only):

python database.py


Start the main console system:

python app.py


Navigate the menu:

Login/Register Users

Manage Incidents

Manage BIA Records

View Threats & Security Controls

Compliance & Audit Logs

🔐 Cryptography & Hashing Demo

Run the demo:

python crypto_demo_full.py


Register a user:

Username: crypto_test

Password: Crypto123!

Login to see:

SHA-256 hashed password

Base64 encoded password

Hash comparison validation

View stored hashes:

python view_users.py


Explain: Demonstrates secure password storage and authentication process.

📄 JSON & Database Files

All persistent data stored in data/:

File	Purpose
users.db	User credentials (hashed passwords)
incidents.json	Incident reports
bia.json	BIA records
assets.json	Asset inventory
threats.json	Threat & vulnerability matrix
physical_controls.json	Physical security controls
compliance.json	Legal & ethical compliance policies
