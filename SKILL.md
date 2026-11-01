---
name: genpark-personal-agent-credential-entropy-exposure-fiduciary-skill
description: Personal Agent Credential Entropy Exposure Fiduciary. Calculates NIST bit entropy and GPU brute-force cracking resistance, audits credential reuse blast radius, and generates privacy-preserving k-anonymity hash prefixes.
license: MIT
version: 1.0.0
tools:
  - calculate_credential_bit_entropy_and_cracking_time
  - audit_credential_reuse_and_blast_radius
  - generate_k_anonymity_privacy_hash_prefix
---

# Personal Agent Credential Entropy Exposure Fiduciary

## Overview & Agent Behavioral Directives
You are a sovereign Personal Agent cybersecurity and identity fiduciary. Your objective is to quantify password cryptographic entropy, prevent catastrophic credential reuse blast radiuses, and enable breach auditing without ever exposing raw secrets.

## When to Activate This Skill
- When an agent or user reviews account security posture, password strength, or login credentials.
- When auditing account networks for password reuse risks across sensitive financial vs leisure platforms.
- When generating k-anonymity SHA-256 prefixes for zero-knowledge breach database queries.

## How to Execute

### Option 1: Zero-Dependency Python Execution
```python
from client import PersonalAgentCredentialEntropyExposureFiduciary

sec = PersonalAgentCredentialEntropyExposureFiduciary()
res = sec.calculate_credential_bit_entropy_and_cracking_time("mypassword")
print("Entropy Bits:", res["shannon_entropy_bits"])
```

### Option 2: FastMCP Tool Calling
- `calculate_credential_bit_entropy_and_cracking_time(credential_candidate)`
- `audit_credential_reuse_and_blast_radius(accounts_json)`
- `generate_k_anonymity_privacy_hash_prefix(credential)`

## Core Mathematical Principles
1. **NIST Bit Entropy**: $H = L \log_2(N)$ measures keyspace size. $H \ge 64$ bits resists online attacks; $H \ge 80$ bits resists high-speed GPU clusters ($10^{11}\ 	ext{hashes/sec}$).
2. **K-Anonymity Privacy Model**: Querying breach APIs using only `SHA256(pwd)[:5]` guarantees mathematical zero-knowledge privacy.
