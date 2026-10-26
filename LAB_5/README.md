# Lab 5 — Static Code Analysis Submission

**Student SRN:** PES1UG25CS856

## Contents
- `fare_calculator.py`: revised program.
- `issues.md`: issue log and fixes.
- `reflection.md`: reflection answers.
- `run_analysis.ps1`: generates before/after reports.
- `reports/`: report output folder.

## Windows PowerShell setup
Run these commands from this folder:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pylint bandit flake8 paramiko cryptography defusedxml
```

Before running the script, save the original repository version as `fare_calculator_original.py` in this folder. Then run:

```powershell
.\run_analysis.ps1
```

The script creates three before-reports and three after-reports in `reports/`. They are genuine outputs from your local installed tool versions; inspect them before submitting. Review any remaining Bandit B601 warning for Paramiko `exec_command`.

Run the revised program with:

```powershell
python .\fare_calculator.py
```

## Git requirement
The lab handout asks for three meaningful commits and before/after reports. Commit the actual changes in stages; do not claim commits unless they were created in Git.
