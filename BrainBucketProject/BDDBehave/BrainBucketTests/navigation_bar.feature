Feature: Show available products
  Scenario Outline: Show all available products
    Given a web browser is at the BrainBucket home page
    When the user selects <product>  from product menu
    Then all <product> available are shown

   Examples:
    |Product    |
    |Cameras    |
    |MP3 Players|
    |Tablets    |