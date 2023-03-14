
# on peut tag meme le s feature
@fonctionnel2
Feature: tester la fonctionnalité login de l'application orange HRM
  en tant que admin user lorsque je me log sur l apllication oramge HRM
  le mode deashbord s'affiche sur la page d'accuille
  ecrir par krimou le 13/03/2023

  Background: étapes communes
    Given ouvrir  application orange sur chrome
  @regression
  Scenario: se connecter avec des identifiants validés

    When saisir le nom utlisateur "Admin" et mot de passe "admin123"
    And cliquer sur le botoun login
    Then valider que le mode deashbord s affiche sur l accuille

  @smoke
  Scenario Outline:se connecter avec des identifiants non valide

    When saisir le nom utlisateur "<user>" et mot de passe "<pass>"
    And cliquer sur le botoun login
    Then valider que le message d erreur s affiche
    Examples:
      | user      | pass      |
      | Admin10   | Admin123  |
      | Admin | admin123 |
      | Admin1001 | Admin1233 |
#behave features --tags=-smoke sauf ce cas de test
  #behave features --tags=smoke uniquement ce cas test