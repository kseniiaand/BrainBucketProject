Feature: Google search with multiple tabs
  Given I am on the Google homepage
  When I enter "<search>" in the search bar
  And I click the "Google Search" button
  And I click on the "<tab>" tab
  Then I should see all the information related to "<search>"

  Examples:
      |tab| search |
      |News|machine learning|
      |Images|artificial intelligence|