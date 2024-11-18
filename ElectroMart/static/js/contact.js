// Define the array of testimonials with their details
const testimonials = [              
    {
      name: "Eva Sawyer",
      job: "CEO, Fashworks",
      image: "../static/images/Veronica.png",
      testimonial:
        "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Obcaecati, tempore!",
    },
    {
      name: "Katey Topaz",
      job: "Developer, TechCrew",
      image: "../static/images/person2.png",
      testimonial:
        "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Obcaecati, tempore!",
    },
    {
      name: "Jae Robin",
      job: "UI Designer, Affinity Agency",
      image: "../static/images/selena.png",
      testimonial:
        "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Obcaecati, tempore!",
    },
    {
      name: "Nicola Blakely",
      job: "CEO,Zeal Wheels",
      image: "../static/images/person1.png",
      testimonial:
        "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Obcaecati, tempore!",
    },
  ];
  
  // Initialize the current index to 0 and set up the event listeners for the next and previous buttons
  let currentIndex = 0;
  const testimonialContainer = document.getElementById("testimonial-container");
  const nextBtn = document.getElementById("next");
  const prevBtn = document.getElementById("prev");
  
  // Function to create the HTML structure for a testimonial
  const createTestimonialHTML = (testimonial) => {
    return `
        <div class="testimonial">
          <p>${testimonial.testimonial}</p>
          <img src=${testimonial.image} alt="${testimonial.name}">
          <h3>${testimonial.name}</h3>
          <h6>${testimonial.job}</h6>
        </div>
      `;
  };
  
  // Function to update the testimonials displayed
  const updateTestimonials = () => {
    const nextIndex = (currentIndex + 1) % testimonials.length;
    const prevIndex = (currentIndex - 1 + testimonials.length) % testimonials.length;
  
    testimonialContainer.innerHTML = `
        ${createTestimonialHTML(testimonials[prevIndex])}
        ${createTestimonialHTML(testimonials[currentIndex])}
        ${createTestimonialHTML(testimonials[nextIndex])}
      `;
  
    testimonialContainer.style.transform = "translateX(-100%)";
  };
  
  // Function to slide to the next testimonial
  const slideNext = () => {
    testimonialContainer.style.transition = "transform 0.5s ease-in-out";
    testimonialContainer.style.transform = "translateX(-200%)";
  
    testimonialContainer.addEventListener(
      "transitionend",
      () => {
        currentIndex = (currentIndex + 1) % testimonials.length;
        updateTestimonials();
        testimonialContainer.style.transition = "none";
        testimonialContainer.style.transform = "translateX(-100%)";
      },
      { once: true }
    );
  };
  
  // Function to slide to the previous testimonial
  const slidePrev = () => {
    testimonialContainer.style.transition = "transform 0.5s ease-in-out";
    testimonialContainer.style.transform = "translateX(0)";
  
    testimonialContainer.addEventListener(
      "transitionend",
      () => {
        currentIndex = (currentIndex - 1 + testimonials.length) % testimonials.length;
        updateTestimonials();
        testimonialContainer.style.transition = "none";
        testimonialContainer.style.transform = "translateX(-100%)";
      },
      { once: true }
    );
  };
  
  // Add event listeners for next and previous buttons
  nextBtn.addEventListener("click", slideNext);
  prevBtn.addEventListener("click", slidePrev);
  
  // Initial call to update testimonials
  updateTestimonials();
  testimonialContainer.style.transform = "translateX(-100%)";
  testimonialContainer.style.transition = "none";
  
  // Intersection Observer to handle element visibility
  const observer_contact = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("show");
      } else {
        entry.target.classList.remove("show");
      }
    });
  });
  
  // Observe elements with the class "hidden"
  const hiddenElements_contact = document.querySelectorAll(".hidden");
  hiddenElements_contact.forEach((el) => observer_contact.observe(el));
  
  // <------------------------------ Thoast Notification ------------------------------>
  
  // showToast Function ( Display Different Thoast according to the input field )
  
  
  const showToast = (message, type) => {
    let border = document.querySelector("#toast-border");
    border.classList.remove("toastBoderAnimation");
  
    toast_notification.classList.remove("toastanimate", "toastanimateout");
    void toast_notification.offsetWidth;
  
    border.classList.add("toastBoderAnimation");
  
    toast_notification.classList.add("toastanimate");
  
    // Update the toast message and icon
    toast_notification.querySelector('.toast__message h4').innerText = type;
    toast_notification.querySelector('.toast__message p').innerText = message;
  
    if (type === 'Success') {
      toast_notification.querySelector('.toast__link i').classList.remove('fa-xmark');
      toast_notification.querySelector('.toast__link i').classList.add('fa-check');
    } else {
      toast_notification.querySelector('.toast__link i').classList.remove('fa-check');
      toast_notification.querySelector('.toast__link i').classList.add('fa-xmark');
    }
    toast_notification.classList.add('show');
  
    setTimeout(() => {
      toast_notification.classList.remove("toastanimate");
      toast_notification.classList.add("toastanimateout");
      setTimeout(() => {
        toast_notification.classList.remove("toastanimateout");
        toast_notification.classList.remove('show');
      }, 300);
    }, 2300);
  };
  
  // Email Validate the inputs
  const isValidEmail = (email) => {
    const emailRegex = /^[^\s@]+@gmail\.com$/;
    return emailRegex.test(email);
  };
  
  const toast_notification = document.querySelector("#toast_notification");   //   thoastNotification Container
  const checkButton = document.querySelector("#btn");
  
  checkButton.addEventListener("click", (e) => {                              // Apply the click event to the button and the toast container 
    e.preventDefault();
  
    let name = document.querySelector("#name").value;
    let email = document.querySelector("#email").value;
    let number = document.querySelector("#phonenumber").value;
    let message = document.querySelector(".message").value;
    
    const params = {
      user_name: name,
      ph_no: number,
      user_email: email,
      message: message,
    };
    
    if (name === "" || email === "" || number === "" || message === "") {    // Check empty string 
      showToast("Fill out all the input fields", "Error");
    } else if (!isValidEmail(email)) {
      showToast("Please enter a valid Gmail address.", "Error");
    } else if (number.length !== 11) {
      showToast("Phone number must be 11 digits.", "Error");
    } else {
      showToast("Your message was successfully sent.", "Success");
      
      // Clear the input fields
      document.querySelector("#name").value = "";
      document.querySelector("#email").value = "";
      document.querySelector("#phonenumber").value = "";
      document.querySelector(".message").value = "";
      
      // Send Email Function (Using EmailJS)
      emailjs.send("service_a4wsrkd", "template_4f02w0v", params)
      .then(function (res) {});
    }
  });
  