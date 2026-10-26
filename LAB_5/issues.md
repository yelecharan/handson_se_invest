# Lab 5 — Static Code Analysis Issues and Fixes

**Student SRN:** PES1UG25CS856

Line numbers may change after formatting. Confirm findings against the reports generated locally.

| Issue | Category | Location | Description | Fix / verification |
|---|---|---|---|---|
| Unsafe XML parsing | Bandit/security | `load_stops` | Untrusted XML should be parsed using a hardened parser. | Use `defusedxml.ElementTree.fromstring`; rerun Bandit to verify. |
| Assertion-based validation | Bandit/correctness | `tap_out` | Assertions can be removed under optimized Python execution. | Use explicit type validation and raise `TypeError`. |
| Paramiko shell command warning | Bandit/security | `push_fares_to_gate` | Paramiko `exec_command` runs a remote shell command; Bandit may still flag it. | Validate the file path, quote the argument, verify host keys, check command status, and review any remaining B601 warning. |
| Weak checksum | Security review | `ticket_checksum` | MD5 is unsuitable where collision resistance is required. | Use SHA-256. A checksum is not authentication. |
| Mutable default argument | Pylint/correctness | `journey_fare`, `tap_out` | A shared default list can leak state between calls. | Use `None` and an empty iterable when omitted. |
| Daily cap logic | Functional correctness | `daily_total` | The final total must be capped after summing fares. | Return `min(sum(fares), DAILY_CAP)`. |
| Distance validation | Functional correctness | `fare_for_distance` | Negative distances should be rejected and boundaries treated consistently. | Reject negative distance and use inclusive slab limits. |
| Card and top-up validation | Reliability | `issue_card`, `tap_out`, `top_up` | Invalid cards, top-ups, and insufficient balance need clear handling. | Add explicit validation. |
| Style/readability | Pylint/Flake8 | Multiple functions | Consistent naming and formatting improve maintainability. | Use snake_case and conventional formatting. |

## Verification checklist
- Preserve reports generated from the original source.
- Generate Pylint, Bandit, and Flake8 reports after changes.
- Target a Pylint score above 9.5/10 and resolve Flake8 findings.
- Review any remaining Bandit warning, especially B601.
- Test fare boundaries, daily cap, card balance, top-up, checksum, and XML parsing.
- Test SSH only with a safe test host and known host key.
