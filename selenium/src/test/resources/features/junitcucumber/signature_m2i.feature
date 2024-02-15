Feature: M2i Sign

  Connexion, signature et vérification

  @m2i_connexion
  Scenario Outline: connexion à m2i sign
    Given J'ouvre le site <url>
    When Je clique sur Espace stagiaire
    Then Le formulaire de connexion s'ouvre
    When Je clique sur le champ Email ou n° de téléphone
    And J'indique mon numéro de télephonne comme identifiant <login>
    Then Mon numéro de téléphone apparait dans le champ et est aligné à gauche
    When Je clique sur le champ Code pin
    And J'indique mon code comme mot de passe <mdp>
    Then Mon code apparait dans le champ et est aligné à gauche
    When Je clique sur le bouton Se connecter
    Then Je suis connecté à mon espace personnel
    Examples:
      | url                             | login        | mdp     |
      | "https://sign.m2iformation.fr/" | "**********" | "*****" |

  @ouvrir_calendrier_1
  Scenario Outline: ouvrir feuille de présence méthode 1
    Given Je suis connecté à mon espace personnel <url> <login> <mdp>
    When Je clique sur le lien Feuille de présence dans le header-container
    Then J'ouvre le calendrier de signatures
    Examples:
      | url                            | login        | mdp     |
      | "https://sign.m2iformation.fr" | "**********" | "*****" |

  @ouvrir_calendrier_2
  Scenario Outline: ouvrir feuille de présence méthode 2
    Given Je suis connecté à mon espace personnel <url> <login> <mdp>
    When Je clique sur le lien Feuille de présence dans le body
    Then J'ouvre le calendrier de signatures
    Examples:
      | url                            | login        | mdp     |
      | "https://sign.m2iformation.fr" | "**********" | "*****" |

  @signer
  Scenario Outline: signer au bon endroit (date du jour, am ou pm)
    Given Je suis sur la page du calendrier de signatures <url> <login> <mdp>
    And Ma signature est déjà créée
    When Je clique sur l'image Emarger ici correspondant à la date du jour et à la plage horaire
    Then L'image Emarger ici est remplacée par ma signature
    Examples:
      | url                            | login        | mdp     |
      | "https://sign.m2iformation.fr" | "**********" | "*****" |

  @quitter
  Scenario Outline: valider et se déconecter de l'espace personnel
    Given Ma signature est bien présente dans la case (date du jour, plage horaire) <url> <login> <mdp>
    When Je remonte tout en haut de la page
    Then L'affichage de la top-bar réapparait
    When Je clique sur le lien en haut à droite Valider et se déconecter
    Then Le formulaire de connexion s'ouvre
    When Je clique sur le lien Retour à l'accueil en haut de page
    Then Je reviens sur la page d'accueil
    Examples:
      | url                            | login        | mdp     |
      | "https://sign.m2iformation.fr" | "**********" | "*****" |