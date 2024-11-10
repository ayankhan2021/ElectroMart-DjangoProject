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
