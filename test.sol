pragma solidity ^0.4.21;
pragma solidity 0.4.21;

library lb1 {}
library lb2 {}
library lb3 {}
library lb4 {}

contract test {

    event Deposit(
	address indexed bidder,
	uint amount,
	bytes32 abc
    );

    event HighestBidIncreased(address indexed bidder, uint amount);

    modifier onlySeller() {
        require(msg.sender == seller);
        _;
    }

    function fn0(uint z);

    function fn1(uint x) {
        storedData = x;
    }

    function fn2(uint y) {
        storedData = y;
    }

    enum State { Created, Locked, Inactive }
}

contract test2 {
    struct Voter {
        uint weight;
        bool voted;
        address delegate;
        uint vote;
    }

    function fn3(uint x) {
        storedData = x;
    }

    function fn4(uint y) {
        storedData = y;
    }

}
