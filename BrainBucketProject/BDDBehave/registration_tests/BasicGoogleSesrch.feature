Feature:Google search
  Scenario: Basic google search
    Given Iam on the Google homepage
    When I enter "<search>" in the search bar
    And I click the "Google Search" button
    Then I should see search results for "<outcome>"
    Example:
      |search|outcome|
      |openAI|openAI|
      |machine learning|Machine Learning|

  Scenario: Google search by voice
    Given I am on the Google homepage
    When I click on microphone sign on the right side of Google search bar
    And say "<request>"
    Then I should see list of <outcome>

    Example:
      |request|outcome|
      |coffee shops near me|nearest coffee shops|
      |most rich people in the world|richest people in the world|

  Scenario: Google search by Image
    Given I am on the Google homepage
    When I click on Camera sign on the right side of Google search bar
    And drag or upload image of pink summer dress
    Then I should see all the results for that dress and shopping options for it



