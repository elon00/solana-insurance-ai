# Solana Insurance AI ($SOLINS) — ARCHITECTURE SPECIFICATION
**System Architecture & State Machine Book**

---

## 1. System Topology
The system comprises four decoupled, interoperable tiers:
1. **Autonomous Intelligence Tier:** Python agent service (`src/solana_actuary_agent.py`) executing actuarial risk decision logic.
2. **Deterministic Invariant Tier:** Rust 64-bit Conway automaton engine (`src/main.rs`) running 10,000 validation cycles.
3. **On-Chain Settlement Tier:** Native smart contract (`contracts/SolanaInsurancePolicy.sol`) on Solana Sealevel (SVM Devnet).
4. **Interactive QUX Presentation Tier:** HTML5/Tailwind responsive launchpad (`index.html`).

---

## 2. Security Boundaries & Fail-Closed Guards
- **Zero Key Storage:** Browser forms and client scripts never capture, store, or transmit private keys.
- **Fail-Closed Spend Protection:** Mainnet spending strictly locked at $0.00 until explicit user authorization.
- **Post-Quantum Cryptography:** Aligned with NIST FIPS 203 (ML-KEM) and FIPS 204 (ML-DSA) standards.
