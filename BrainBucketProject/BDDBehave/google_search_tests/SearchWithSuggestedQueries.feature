Feature: Google search with suggested queries
  Given I am on the Google homepage
  When I enter "best coffee shops" in the search bar
  And I click the "Google Search" button
  And I look at the suggested queries
  Then I should see suggestions for "best coffee shops near me", "best coffee shops in NYC", and "best coffee shops in San Francisco"
  And when I click on "best coffee shops in NYC"
  Then I should see search results for "best coffee shops in NYC"

  Examples:
  |queri|outcome|
  |best coffee shops|
  |best coffee shops near me|
  |est coffee shops in SF|
