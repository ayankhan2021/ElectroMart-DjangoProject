document.addEventListener('DOMContentLoaded', function () {
  const navLinks = document.querySelectorAll('.nav__link');
  const currentPath = window.location.pathname;

  navLinks.forEach(link => {
    const href = link.getAttribute('href') || '';

    // Check if the link's href matches the current path
    if (currentPath === href) {
      link.classList.add('active');
    }
  });
});


const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('show')
    } else {
      entry.target.classList.remove('show')
    }
  })
})

const hiddenElements = document.querySelectorAll('.hidden-up')
hiddenElements.forEach((el) => observer.observe(el))



// Automatically hide alerts after 3-4 seconds

document.addEventListener("DOMContentLoaded", function () {
  const alerts = document.querySelectorAll(".alert");
  alerts.forEach(alert => {
    setTimeout(() => {
      alert.style.transition = "opacity 0.5s ease";
      alert.style.opacity = "0";
      setTimeout(() => alert.remove(), 500); 
    }, 3000);
  });
});