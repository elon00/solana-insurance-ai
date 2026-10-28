// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title SolanaInsurancePolicy
 * @dev High-Velocity SVM Liquidity & Oracle Flash-Crash Insurance Model
 */
contract SolanaInsurancePolicy {
    struct SvmPoolCover {
        address poolAuthority;
        uint256 insuredTvlSol;
        uint256 depegThresholdBps;
        bool active;
    }

    mapping(address => SvmPoolCover) public poolCovers;
    event PoolCoverActivated(address indexed pool, uint256 tvl, uint256 threshold);
    event DepegPayoutTriggered(address indexed pool, uint256 payoutSol);

    function bindSvmPoolCover(uint256 tvlSol, uint256 depegThreshold) external payable {
        require(msg.value > 0, "Premium required");
        poolCovers[msg.sender] = SvmPoolCover({
            poolAuthority: msg.sender,
            insuredTvlSol: tvlSol,
            depegThresholdBps: depegThreshold,
            active: true
        });

        emit PoolCoverActivated(msg.sender, tvlSol, depegThreshold);
    }

    function triggerDepegIndemnity(address pool, uint256 currentDeviationBps) external {
        SvmPoolCover storage c = poolCovers[pool];
        require(c.active, "Cover inactive");
        require(currentDeviationBps > c.depegThresholdBps, "Deviation below threshold");

        c.active = false;
        uint256 payout = (c.insuredTvlSol * currentDeviationBps) / 10000;
        payable(c.poolAuthority).transfer(payout);

        emit DepegPayoutTriggered(pool, payout);
    }
}
