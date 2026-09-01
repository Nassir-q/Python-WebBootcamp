# 🏆 Lab Challenge: Django Pages & Dynamic Navigation

This folder documents the solution for the applied challenge of building multiple interfaces and linking them together using the Django framework. The focus is on transitioning to the template system and enhancing the user experience through dynamic navigation.

## 🚀 Implementation Details

* **App Creation:** Established a dedicated app named `pages` responsible for managing and rendering the website's pages.
* **Templates & Render:** Upgraded the view methodology by replacing `HttpResponse` with the `render` function to load and display complete HTML files instead of returning plain text strings.
* **Page Development:** Built three primary, independent pages:
  * `index.html` (Home Page).
  * `faq.html` (Frequently Asked Questions).
  * `team.html` (Team Page).
* **Dynamic Navbar:** Programmed a connected top `<nav>` bar that links all three pages seamlessly. The dedicated Django `{% url 'name' %}` template tag was utilized to generate the links, ensuring flexibility and preventing broken links if URL routing paths change in the future.