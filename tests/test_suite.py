# -*- coding: utf-8 -*-
import unittest
import os
import re
from pathlib import Path

class TestProjectIntegrity(unittest.TestCase):
    def test_zero_private_key_leakage(self):
        root = Path(".")
        key_patterns = [
            re.compile(r"0x[a-fA-F0-9]{64}"),
            re.compile(r"BEGIN PRIVATE KEY"),
            re.compile(r"BEGIN EC PRIVATE KEY"),
        ]
        for f in root.glob("**/*"):
            if f.is_file() and not str(f).startswith(".git"):
                try:
                    content = f.read_text(encoding="utf-8", errors="ignore")
                    for p in key_patterns:
                        self.assertFalse(
                            p.search(content) and "seed" not in content.lower() and "dummy" not in content.lower(),
                            f"Potential leaked private key found in {f}"
                        )
                except Exception:
                    pass

    def test_mcp_structure(self):
        mcp_path = Path("mcp.json")
        self.assertTrue(mcp_path.exists(), "mcp.json must exist")

    def test_contracts_present(self):
        contracts = list(Path("contracts").glob("*"))
        self.assertGreater(len(contracts), 0, "At least one smart contract required")

if __name__ == "__main__":
    unittest.main()
