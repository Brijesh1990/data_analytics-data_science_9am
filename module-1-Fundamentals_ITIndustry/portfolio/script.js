document.addEventListener("DOMContentLoaded", () => {
    // 1. Preloader
    const preloader = document.getElementById("preloader");
    window.addEventListener("load", () => {
        preloader.style.opacity = "0";
        setTimeout(() => {
            preloader.style.display = "none";
        }, 500);
    });

    // 2. Dark Mode Toggle
    const darkModeToggle = document.getElementById("darkModeToggle");
    const icon = darkModeToggle.querySelector("i");
    const currentTheme = localStorage.getItem("theme");

    if (currentTheme) {
        document.documentElement.setAttribute("data-theme", currentTheme);
        if (currentTheme === "dark") {
            icon.classList.remove("fa-moon");
            icon.classList.add("fa-sun");
        }
    }

    darkModeToggle.addEventListener("click", () => {
        let theme = document.documentElement.getAttribute("data-theme");
        if (theme === "dark") {
            document.documentElement.setAttribute("data-theme", "light");
            localStorage.setItem("theme", "light");
            icon.classList.remove("fa-sun");
            icon.classList.add("fa-moon");
        } else {
            document.documentElement.setAttribute("data-theme", "dark");
            localStorage.setItem("theme", "dark");
            icon.classList.remove("fa-moon");
            icon.classList.add("fa-sun");
        }
    });

    // 3. Mobile Menu Toggle
    const hamburger = document.querySelector(".hamburger");
    const navLinks = document.querySelector(".nav-links");
    const navItems = document.querySelectorAll(".nav-link");

    hamburger.addEventListener("click", () => {
        hamburger.classList.toggle("active");
        navLinks.classList.toggle("active");
    });

    navItems.forEach(item => {
        item.addEventListener("click", () => {
            hamburger.classList.remove("active");
            navLinks.classList.remove("active");
        });
    });

    // 4. Sticky Navbar & Active Link Highlight
    const navbar = document.getElementById("navbar");
    const sections = document.querySelectorAll(".section-scroll");
    
    window.addEventListener("scroll", () => {
        let current = "";
        
        if (window.scrollY > 50) {
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (scrollY >= sectionTop - 150) {
                current = section.getAttribute("id");
            }
        });

        navItems.forEach(item => {
            item.classList.remove("active");
            if (current && item.getAttribute("href").includes(current)) {
                item.classList.add("active");
            }
        });
        
        // Scroll to Top Button Visibility
        const scrollTopBtn = document.getElementById('scrollToTopBtn');
        if (window.scrollY > 300) {
            scrollTopBtn.classList.add('show');
        } else {
            scrollTopBtn.classList.remove('show');
        }
    });

    // 5. Scroll to Top Behavior
    const scrollTopBtn = document.getElementById('scrollToTopBtn');
    scrollTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // 6. Typing Animation
    const typingText = document.querySelector(".typing-text");
    const roles = ["Data Analyst", "Data Scientist", "ML Enthusiast"];
    let roleIndex = 0;
    let charIndex = 0;
    let isDeleting = false;

    function typeEffect() {
        const currentRole = roles[roleIndex];
        
        if (isDeleting) {
            typingText.textContent = currentRole.substring(0, charIndex - 1);
            charIndex--;
        } else {
            typingText.textContent = currentRole.substring(0, charIndex + 1);
            charIndex++;
        }

        let typeSpeed = isDeleting ? 50 : 100;

        if (!isDeleting && charIndex === currentRole.length) {
            typeSpeed = 1500; // Pause at end
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            roleIndex = (roleIndex + 1) % roles.length;
            typeSpeed = 500; // Pause before new word
        }

        setTimeout(typeEffect, typeSpeed);
    }
    // Start typing effect
    if(typingText) setTimeout(typeEffect, 1000);

    // 7. Scroll Reveal setup using IntersectionObserver
    const revealElements = document.querySelectorAll(".reveal");
    
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("active");
                // Trigger counters and progress bars if contained
                if (entry.target.querySelector('.counter')) {
                    startCounters(entry.target);
                }
                if (entry.target.querySelector('.progress-bar')) {
                    startProgressBars(entry.target);
                }
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.15
    });

    revealElements.forEach(el => revealObserver.observe(el));

    // 8. Animated Counters
    function startCounters(element) {
        const counters = element.querySelectorAll(".counter");
        counters.forEach(counter => {
            const target = +counter.getAttribute("data-target");
            const duration = 2000;
            const increment = target / (duration / 16);
            
            let current = 0;
            const updateCounter = () => {
                current += increment;
                if (current < target) {
                    counter.innerText = Math.ceil(current) + (target > 5 ? "+" : "");
                    requestAnimationFrame(updateCounter);
                } else {
                    counter.innerText = target + (target > 5 ? "+" : "");
                }
            };
            updateCounter();
        });
    }

    // 9. Animated Progress Bars
    function startProgressBars(element) {
        const progressBars = element.querySelectorAll(".progress-bar");
        progressBars.forEach(bar => {
            const progress = bar.getAttribute("data-progress");
            bar.style.width = progress;
        });
    }

    // 10. Form Submission
    const contactForm = document.getElementById("contactForm");
    const formStatus = document.getElementById("formStatus");

    if (contactForm) {
        contactForm.addEventListener("submit", (e) => {
            e.preventDefault();
            
            const btn = contactForm.querySelector('button[type="submit"]');
            btn.innerHTML = 'Sending...';
            btn.disabled = true;

            // Simulate form submission
            setTimeout(() => {
                btn.innerHTML = 'Send Message';
                btn.disabled = false;
                formStatus.textContent = "Message sent successfully!";
                formStatus.className = "form-status success";
                contactForm.reset();
                
                setTimeout(() => {
                    formStatus.textContent = "";
                }, 4000);
            }, 1000);
        });
    }

    // 11. Set current year in footer
    const yearEl = document.getElementById("currentYear");
    if(yearEl) {
        yearEl.textContent = new Date().getFullYear();
    }
});
