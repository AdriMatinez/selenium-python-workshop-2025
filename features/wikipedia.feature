Feature: Búsqueda de artículos en Wikipedia

  Scenario: Verificar el título del artículo de Python
    Given el usuario está en la página principal de Wikipedia
    When busca "Python (lenguaje de programación)"
    Then el título del artículo debe ser "Python (lenguaje de programación)"
