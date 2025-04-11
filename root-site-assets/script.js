/**
 * STEM Education Landing Page JavaScript
 * Adds interactivity and animations to the landing page
 */

// DOM Elements
const header = document.querySelector('.header');
const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
const mainNav = document.querySelector('.main-nav');
const backToTopButton = document.getElementById('back-to-top');
const currentYearSpan = document.getElementById('current-year');
const codeLines = document.querySelectorAll('.code-line');

// Set current year in footer
currentYearSpan.textContent = new Date().getFullYear();

// Mobile Navigation Toggle
if (mobileNavToggle) {
    mobileNavToggle.addEventListener('click', () => {
        const expanded = mobileNavToggle.getAttribute('aria-expanded') === 'true';
        mobileNavToggle.setAttribute('aria-expanded', !expanded);
        mobileNavToggle.classList.toggle('active');
        mainNav.classList.toggle('active');
    });
}

// Close mobile menu when clicking a link
document.querySelectorAll('.main-nav a').forEach(link => {
    link.addEventListener('click', () => {
        mobileNavToggle.classList.remove('active');
        mobileNavToggle.setAttribute('aria-expanded', 'false');
        mainNav.classList.remove('active');
    });
});

// Header scroll effect
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }

    // Show/hide back to top button
    if (window.scrollY > 500) {
        backToTopButton.classList.add('visible');
    } else {
        backToTopButton.classList.remove('visible');
    }
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        // Skip if it's not actually an anchor link
        if (this.getAttribute('href') === '#') return;
        
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            const headerHeight = document.querySelector('.header').offsetHeight;
            const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// Back to top button functionality
backToTopButton.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// Typewriter effect for code in hero section
function animateCode() {
    codeLines.forEach((line, index) => {
        setTimeout(() => {
            line.classList.add('animate');
        }, 300 * index);
    });
}

// Animate elements when they come into view
const animateOnScroll = () => {
    const elements = document.querySelectorAll('.workshop-card, .resource-card, .about-image');
    const triggerBottom = window.innerHeight * 0.8;
    
    elements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        if (elementTop < triggerBottom) {
            element.classList.add('in-view');
        }
    });
};

// Run animations on page load
window.addEventListener('load', () => {
    // Add CSS class for animated code
    codeLines.forEach(line => {
        line.style.opacity = '0';
        line.style.transform = 'translateY(10px)';
        line.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
    });
    
    // Allow time for page to settle before animations
    setTimeout(() => {
        animateCode();
        animateOnScroll();
    }, 500);
    
    // Add CSS for animations
    const style = document.createElement('style');
    style.textContent = `
        .code-line.animate {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
        
        .workshop-card, .resource-card, .about-image {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.6s ease, transform 0.6s ease;
        }
        
        .workshop-card.in-view, .resource-card.in-view, .about-image.in-view {
            opacity: 1;
            transform: translateY(0);
        }
    `;
    document.head.appendChild(style);
});

// Run animations when scrolling
window.addEventListener('scroll', animateOnScroll);

// Handle form submission if contact form exists
const contactForm = document.getElementById('contact-form');
if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
        e.preventDefault();
        // Here you would typically send the form data to a server
        // For this demo, we'll just show a success message
        contactForm.innerHTML = '<div class="success-message"><i class="fas fa-check-circle"></i><p>Thank you for your message! I\'ll get back to you soon.</p></div>';
    });
}