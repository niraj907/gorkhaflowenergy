  const togglePassword = document.getElementById("togglePassword");
  const password = document.getElementById("password");
  const eyeIcon = document.getElementById("eyeIcon");

  togglePassword.addEventListener("click", function () {
    const type = password.getAttribute("type") === "password" ? "text" : "password";
    password.setAttribute("type", type);

    // Toggle icon class
    eyeIcon.classList.toggle("fa-eye");
    eyeIcon.classList.toggle("fa-eye-slash");
  });