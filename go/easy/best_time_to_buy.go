package main

// import "fmt"

func maxProfit(prices []int) int {
  /*
  loop over prices
  each iteration check for
    - lowest price and max profit
  */
  maxProfit := 0
  lowInd := 0
  for i := 0; i < len(prices); i++ {
    profit := prices[i] - prices[lowInd]
    if profit > maxProfit {
      maxProfit = profit
    }
    if prices[i] < prices[lowInd] {
      lowInd = i
    }
  }
  return maxProfit
}
