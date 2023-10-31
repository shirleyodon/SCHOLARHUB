// Disable submit while invalid field found
(() => {
  "use strict";

  const matriculeField = document.querySelector("#matricule");
  const nameField = document.querySelector("#name");
  const emailField = document.querySelector("#email");
  const passwordField = document.querySelector("#password");
  const confirmField = document.querySelector("#confirm-password");

  matriculeField.form.addEventListener(
    "submit",
    (event) => {
      if (!matriculeField.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
        matriculeField.classList.add("is-invalid");
      }
    },
    false
  );

  matriculeField.form.addEventListener("input", (event) => {
    if (matriculeField.checkValidity()) {
      matriculeField.classList.remove("is-invalid");
    }
  });

  nameField.form.addEventListener(
    "submit",
    (event) => {
      if (!nameField.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
        nameField.classList.add("is-invalid");
      }
    },
    false
  );

  nameField.form.addEventListener("input", (event) => {
    if (nameField.checkValidity()) {
      nameField.classList.remove("is-invalid");
    }
  });

  emailField.form.addEventListener(
    "submit",
    (event) => {
      if (!emailField.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
        emailField.classList.add("is-invalid");
      }
    },
    false
  );

  emailField.form.addEventListener("input", (event) => {
    if (emailField.checkValidity()) {
      emailField.classList.remove("is-invalid");
    }
  });

  passwordField.form.addEventListener(
    "submit",
    (event) => {
      if (!passwordField.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
        passwordField.classList.add("is-invalid");
      }
    },
    false
  );

  passwordField.form.addEventListener("input", (event) => {
    if (passwordField.checkValidity()) {
      passwordField.classList.remove("is-invalid");
    }
  });

  confirmField.form.addEventListener(
    "submit",
    (event) => {
      if (!confirmField.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
        confirmField.classList.add("is-invalid");
      }
    },
    false
  );

  confirmField.form.addEventListener("input", (event) => {
    if (
      confirmField.checkValidity() &&
      confirmField.value === passwordField.value
    ) {
      confirmField.classList.remove("is-invalid");
    }
  });
})();
