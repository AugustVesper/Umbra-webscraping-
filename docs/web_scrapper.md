# Menu Scraper

## Introducción
Este módulo proporciona una interfaz de menú para scraping sitios web.

## Funciones

### `menu_scraper()`
Muestra la interfaz de menú del scraper.

**Parámetros**

- Ninguno

**Retorna**

- `str`: La URL ingresada por el usuario, o `None` si la URL es inválida.

### `show_options()`
Muestra las opciones de scraping.

**Parámetros**

- Ninguno

**Retorna**

- `None`

### `get_option()`
Obtiene la opción del usuario.

**Parámetros**

- Ninguno

**Retorna**

- `str`: La opción del usuario.

---

# Web Scraper

## Introducción
Este módulo proporciona funcionalidades de scraping web.

## Funciones

### `get_url()`
Obtiene la URL del usuario.

**Parámetros**

- Ninguno

**Retorna**

- `str`: La URL ingresada por el usuario, o `None` si la URL es inválida.

### `parse_page(url)`
Analiza la página HTML.

**Parámetros**

- `url` (`str`): La URL a analizar.

**Retorna**

- `BeautifulSoup`: La página HTML analizada, o `None` si ocurre un error.

### `scrape_titles(soup)`
Scrapea todos los títulos (`h3`) de la página HTML.

**Parámetros**

- `soup` (`BeautifulSoup`): La página HTML analizada.

**Retorna**

- `None`

### `scrape_links(soup)`
Scrapea todos los enlaces de la página HTML.

**Parámetros**

- `soup` (`BeautifulSoup`): La página HTML analizada.

**Retorna**

- `None`

### `display_results(soup, option)`
Muestra los resultados del scraping.

**Parámetros**

- `soup` (`BeautifulSoup`): La página HTML analizada.
- `option` (`str`): La opción del usuario.

**Retorna**

- `bool`: `True` si la opción es válida, `False` en caso contrario.

### `main()`
Punto de entrada principal.

**Parámetros**

- Ninguno

**Retorna**

- `None`

---

# Constants

## Introducción
Este módulo proporciona constantes para el scraper web.

## Constantes

### `TITLE_PATTERN`
Patrón de título (`h3`).

### `LINK_PATTERN`
Patrón de enlace (`a`).

