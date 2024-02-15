Feature: testPersonalities

  Background:
  Given le client se connecte sur le site "https://www.16personalities.com/fr"

  @test
  Scenario: passer le test de personnalité en mode aléatoire
    When il clique sur le bouton Passer le test
    Then il est dirige sur la page du test
    When il repond aux questions de facon aleatoire en commencant par la question 1
    Then le bouton suivant s'affiche
    When il clique sur le bouton suivant
    Then la page resultat s'affiche

  @type
  Scenario Outline: afficher le type de personnalité <type>
    When il clique sur l'onglet types de personnalite qui se situe au milieu de la topbar
    Then la page types de personnalite s'affiche
    When scroller pour afficher le <type> de personalite
    And cliquer sur le <type> de personalite
    Then la page du type s'affiche
    Examples:
      | type       |
      | "Virtuose" |
      | "Avocate"  |

  @support
  Scenario: aller sur la page X
    When il clique sur l'onglet contact qui se situe sur la topbar
    Then la page contactez-nous s'affiche
    When il clique sur le logo twitter en bas a gauche
    Then la page 16 personalities de X s'affiche


