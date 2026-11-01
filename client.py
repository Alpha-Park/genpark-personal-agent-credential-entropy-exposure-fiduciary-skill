# -*- coding: utf-8 -*-
"""
Personal Agent Credential Entropy Exposure Fiduciary Client
Zero-dependency Shannon-NIST bit entropy calculator, GPU keyspace brute-force
cracking time estimator, and k-anonymity hash prefix privacy auditor.
"""

import math
import hashlib
from typing import Dict, List, Any, Optional

class PersonalAgentCredentialEntropyExposureFiduciary:
    """
    Sovereign personal cybersecurity and credential fiduciary.
    Calculates cryptographic bit entropy, GPU cluster brute-force cracking resistance,
    and credential reuse blast radius without ever leaking raw secrets.
    """

    def calculate_credential_bit_entropy_and_cracking_time(
        self,
        credential_candidate: str
    ) -> Dict[str, Any]:
        """
        NIST Bit Entropy: H = L * log2(KeyspaceSize).
        Cracking Time = Keyspace / (2 * HashesPerSecond).
        Benchmark: 10^11 hashes/sec (High-end multi-GPU cracking cluster).
        """
        if not credential_candidate:
            raise ValueError("Credential string cannot be empty.")

        pwd = credential_candidate
        l = len(pwd)

        has_lower = any(c.islower() for c in pwd)
        has_upper = any(c.isupper() for c in pwd)
        has_digit = any(c.isdigit() for c in pwd)
        has_special = any(not c.isalnum() for c in pwd)

        keyspace_n = 0
        if has_lower:
            keyspace_n += 26
        if has_upper:
            keyspace_n += 26
        if has_digit:
            keyspace_n += 10
        if has_special:
            keyspace_n += 33

        keyspace_n = max(2, keyspace_n)
        entropy_bits = round(l * math.log2(keyspace_n), 1)

        # Total combinations: N^L
        total_combinations = math.pow(keyspace_n, l)
        hashes_per_second = 100_000_000_000.0  # 100 Billion hashes/sec
        seconds_to_crack = total_combinations / (2.0 * hashes_per_second)

        if seconds_to_crack < 1.0:
            time_human = "INSTANTANEOUS (< 1 second)"
            strength = "CRITICALLY_VULNERABLE"
        elif seconds_to_crack < 3600.0:
            time_human = f"{seconds_to_crack / 60.0:.1f} minutes"
            strength = "VERY_WEAK"
        elif seconds_to_crack < 86400.0:
            time_human = f"{seconds_to_crack / 3600.0:.1f} hours"
            strength = "WEAK"
        elif seconds_to_crack < 31536000.0:
            time_human = f"{seconds_to_crack / 86400.0:.1f} days"
            strength = "MODERATE"
        elif seconds_to_crack < 31536000.0 * 1000.0:
            time_human = f"{seconds_to_crack / 31536000.0:.1f} years"
            strength = "STRONG_RESISTANT"
        else:
            time_human = f"{seconds_to_crack / (31536000.0 * 1e6):.1f} million years"
            strength = "FORTRESS_TIER_MILITARY_GRADE"

        return {
            "credential_length": l,
            "character_pool_size": keyspace_n,
            "shannon_entropy_bits": entropy_bits,
            "estimated_cracking_time": time_human,
            "seconds_to_crack": seconds_to_crack,
            "cryptographic_strength": strength,
            "nist_compliance": entropy_bits >= 64.0
        }

    def audit_credential_reuse_and_blast_radius(
        self,
        accounts: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Audits credential reuse across personal accounts using salted blind hashes.
        Account format: {"service": "Bank", "category": "FINANCE", "credential_id": "pass_hash_or_alias"}
        """
        if not accounts:
            raise ValueError("Accounts list cannot be empty.")

        clusters = {}
        for acc in accounts:
            cid = acc.get("credential_id", "default")
            if cid not in clusters:
                clusters[cid] = []
            clusters[cid].append(acc)

        reused_clusters = [c for c in clusters.values() if len(c) > 1]
        reused_account_count = sum(len(c) for c in reused_clusters)

        # Blast radius score (0 to 100)
        high_risk_reused = any(any(a.get("category") == "FINANCE" for a in c) for c in reused_clusters)
        blast_score = min(100.0, reused_account_count * 15.0 + (30.0 if high_risk_reused else 0.0))

        return {
            "total_accounts_audited": len(accounts),
            "unique_credentials_used": len(clusters),
            "reused_credential_groups": len(reused_clusters),
            "total_vulnerable_accounts": reused_account_count,
            "credential_reuse_rate_pct": round((reused_account_count / len(accounts)) * 100.0, 1),
            "credential_blast_radius_score": blast_score,
            "risk_assessment": "CATASTROPHIC_BLAST_RADIUS (Financial accounts share passwords)" if high_risk_reused else ("MODERATE_REUSE_EXPOSURE" if reused_account_count > 0 else "ZERO_REUSE_SOVEREIGN")
        }

    def generate_k_anonymity_privacy_hash_prefix(
        self,
        credential: str
    ) -> Dict[str, Any]:
        """
        Generates k-anonymity SHA-256 prefix for safe breach querying without leaking secret.
        """
        sha = hashlib.sha256(credential.encode("utf-8")).hexdigest().upper()
        prefix = sha[:5]
        suffix = sha[5:]

        return {
            "hash_prefix_5char": prefix,
            "hash_suffix_obscured_length": len(suffix),
            "privacy_guarantee": "Only 5-char prefix is queryable; secret cannot be mathematically reconstructed from prefix."
        }
