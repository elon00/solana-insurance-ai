# -*- coding: utf-8 -*-
import hashlib
import time
import json

class SolanaPoolInsuranceActuary:
    def __init__(self, cluster: str = "https://api.devnet.solana.com"):
        self.cluster = cluster

    def evaluate_svm_liquidity_health(self, pool_pubkey: str, oracle_price: float, pool_price: float) -> dict:
        divergence = abs(pool_price - oracle_price) / oracle_price * 100
        is_flash_crash = divergence > 4.5
        return {
            "pool_pubkey": pool_pubkey,
            "cluster": self.cluster,
            "oracle_price": oracle_price,
            "pool_price": pool_price,
            "divergence_pct": round(divergence, 3),
            "flash_crash_confirmed": is_flash_crash,
            "spl_indemnity_authorized": is_flash_crash,
            "timestamp": int(time.time())
        }

if __name__ == "__main__":
    actuary = SolanaPoolInsuranceActuary()
    res = actuary.evaluate_svm_liquidity_health("52xNiJZYwnmWMvRvfcBq7cANM1CvoUcHqiDUqubTLxL3", 150.0, 142.1)
    print("Solana SVM Pool Assessment:", json.dumps(res, indent=2))
