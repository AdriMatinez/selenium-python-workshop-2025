Feature: Buscar producto
Scenario: Esta buscando un producto
        Given el usuario se encuentra en la pagina mercado libre
        When el usuario escribe el nombre del producto
        Then visualiza las coincidencias del producto