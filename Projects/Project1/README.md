# Project 1

##Ascending Clock Auction
An ascending clock auction is an auction where the seller starts bidding at a low price and gradually raises the price as the auction progresses. As the price increases, bidders can choose to stay in the auction (bid for the item at the clock price) or drop out and forgo their chance at winning the item. The clock price is usually raised by a fixed discrete increment. The auction ends when there is only one bidder remaining. The winning bidder gets the item and pays the posted price (clock price from the last round with multiple bidders).

- Example: A seller is auctioning off a baseball card. The starting auction price is \$10 and the clock increment is \$1. In the first round of bidding there are 5 people who place bids of \$10. The seller then raises the price to \$11 and bidding continues until there is only one bidder willing to pay the clock price. Say this continues until the clock price is \$15 and there are two bidders left. If one bidder drops out, the remaining bidder wins the baseball card and pays the posted price of $14.

You will need to write a Monte Carlo simulation to estimate the seller revenue from an ascending clock auction. For this assignment, assume the following parameters:

- There are 5 buyers
- Buyer values are drawn between 0 and 100 in increments of 5
- Seller reserve prices are allowed to be between 0 and 100 in increments of 5
- The item is considered sold when the clock price is greater than or equal to the reserve price
- The auction ends when there is one or less buyers bidding at the clock price.
-In the case of two buyers dropping out at the same price, you can go back to the previous price and randomly choose the winning buyer.
 

What is the expected revenue if there are 5 buyers and the clock increment is $1?

What is the expected revenue if there are 5 buyers and the clock increment is \$10?  How did the increment affect the expected revenue and why does it have that effect?

What is the expected revenue if there are 20 buyers with a clock increment of $1? Compare with item (a) and explain the difference.
 

Let's extend our Monte Carlo simulation of the ascending clock auction to allow the seller to choose a reserve price. A reserve price is the minimum price a seller is willing to accept to sell the item. If the final clock price is below the reserve price the seller receives zero revenue. This means the auction now ends when either there are zero buyers bidding at the current clock price, or there is one buyer bidding and the reserve price has been met.

 

   D. What reserve price should the seller choose (which price generates the most revenue)? Provide an illustration that supports your result.