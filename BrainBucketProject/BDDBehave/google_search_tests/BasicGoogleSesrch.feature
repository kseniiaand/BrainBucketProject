Feature:Google search
  Scenario: Basic google search
    Given a web browser is at the Google homepage
    When the user enters "<search>" in the search bar
    And clicks the "Google Search" button
    Then search results for "<outcome>" are displayed
    Example:
      |search          |outcome         |
      |openAI          |openAI          |
      |machine learning|Machine Learning|

  Scenario: Google search by voice
    Given a web browser is at the Google homepage
    When the user clicks on microphone sign on the right side of Google search bar
    And says "<request>"
    Then list of <outcome> is displayed

    Example:
      |request                      |outcome                    |
      |coffee shops near me         |nearest coffee shops       |
      |most rich people in the world|richest people in the world|

  Scenario: Google search by Image
    Given a web browser is at the Google homepage
    When the user clicks on Camera sign on the right side of Google search bar
    And drags or uploads image of pink summer dress
    Then pink summer dress results are displayed 



