# Lab 5 — Reflection

**Student SRN:** PES1UG25CS856

## 1. What is static code analysis?
Static code analysis examines source code without executing the program. It can detect potential bugs, unsafe patterns, maintainability problems, and style violations early. It complements testing and code review rather than replacing them.

## 2. How do Pylint, Bandit, and Flake8 differ?
Pylint checks code quality, naming, and common programming mistakes. Bandit searches Python source for common security-sensitive patterns. Flake8 checks Python style and formatting, including many PEP 8 violations. Using all three provides broader coverage.

## 3. What issues were found and fixed?
The review covered XML parsing, assertion-based validation, remote shell command construction, checksum choice, mutable default arguments, daily fare capping, distance boundaries, card validation, and style. The revised code uses `defusedxml`, explicit checks, SHA-256, optional categories defaulting to `None`, a capped total, input validation, and consistent naming. Bandit may still flag B601 because Paramiko executes a remote command; the actual after-report should be checked rather than claiming that warning disappeared without evidence.

## 4. What did you learn?
I learned that code can work for normal inputs while still having security, correctness, and maintainability problems. Static analysis tools provide useful warnings, but some functional bugs require code review and tests. Changes should be verified by rerunning the tools and testing important behavior.
