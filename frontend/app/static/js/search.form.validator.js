// Disable submit while invalid field found
(() => {
  "use strict";

  const searchField = document.querySelector("#search");

  searchField.form.addEventListener(
    "submit",
    (event) => {
      if (!searchField.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
        searchField.classList.add("is-invalid");
      }
    },
    false
  );

  searchField.form.addEventListener("input", (event) => {
    if (searchField.checkValidity()) {
      searchField.classList.remove("is-invalid");
    }
  });
})();
