@fonctionnel1
Feature: valider l'affichage de logo HRMorange
  “As a [persona], I [want to], [so that].”
  en tant que utilisateur lors que j'ouvre prangeHRM sur chrome
  le logo doit etre vivible
  Scenario: validation de la presence de logo orange HRM
    Given l'utlisateur ouvre le navigateur chrome
    When lors que l utlisateur ouvre l'application orange
    Then le logo s'affiché sur la page d accuille