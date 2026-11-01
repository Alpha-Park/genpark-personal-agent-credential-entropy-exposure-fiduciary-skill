# -*- coding: utf-8 -*-
import json
from client import PersonalAgentCredentialEntropyExposureFiduciary

security = PersonalAgentCredentialEntropyExposureFiduciary()

print("=" * 64)
print("DEMO: Personal Credential Entropy & Exposure Fiduciary")
print("=" * 64)

# 1. Evaluate password entropy & cracking time
c1 = security.calculate_credential_bit_entropy_and_cracking_time("Summer2024!")
print(f"\n1. Weak Credential Evaluation ('Summer2024!'):")
print(f"   Entropy: {c1['shannon_entropy_bits']} bits | Pool Size: {c1['character_pool_size']}")
print(f"   Estimated GPU Cracking Time: {c1['estimated_cracking_time']} ({c1['cryptographic_strength']})")

c2 = security.calculate_credential_bit_entropy_and_cracking_time("xK9#mQ2$vL8!zW5@")
print(f"\n2. Strong Credential Evaluation ('xK9#mQ2$vL8!zW5@'):")
print(f"   Entropy: {c2['shannon_entropy_bits']} bits | Pool Size: {c2['character_pool_size']}")
print(f"   Estimated GPU Cracking Time: {c2['estimated_cracking_time']} ({c2['cryptographic_strength']})")

# 3. Credential reuse blast radius
accounts = [
    {"service": "Chase Bank", "category": "FINANCE", "credential_id": "pwd_hash_A"},
    {"service": "Coinbase", "category": "FINANCE", "credential_id": "pwd_hash_A"},
    {"service": "Netflix", "category": "MEDIA", "credential_id": "pwd_hash_A"},
    {"service": "GitHub", "category": "DEV", "credential_id": "pwd_hash_B"}
]
blast = security.audit_credential_reuse_and_blast_radius(accounts)
print(f"\n3. Credential Reuse Blast Radius:")
print(f"   Audited: {blast['total_accounts_audited']} accounts ({blast['total_vulnerable_accounts']} vulnerable)")
print(f"   Blast Radius Score: {blast['credential_blast_radius_score']}/100")
print(f"   Risk: {blast['risk_assessment']}")

# 4. K-Anonymity privacy prefix
k_anon = security.generate_k_anonymity_privacy_hash_prefix("MySecretPassphrase123!")
print(f"\n4. K-Anonymity Leak Check Prefix:")
print(f"   5-Char Query Prefix: {k_anon['hash_prefix_5char']} (Safe to send over public APIs)")
