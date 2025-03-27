// LinkedIn Profiles Data
const professionals = [
    {
        name: "Sarah Johnson",
        title: "Software Engineer",
        company: "Microsoft",
        linkedIn: "https://www.linkedin.com/in/example1/",
        expertise: "Cloud Computing, Azure"
    },
    {
        name: "Michael Chen",
        title: "Product Manager",
        company: "Microsoft",
        linkedIn: "https://www.linkedin.com/in/example2/",
        expertise: "Product Development, UI/UX"
    },
    {
        name: "Aisha Patel",
        title: "Data Scientist",
        company: "Microsoft",
        linkedIn: "https://www.linkedin.com/in/example3/",
        expertise: "Machine Learning, AI"
    },
    {
        name: "David Wilson",
        title: "UX Designer",
        company: "Microsoft",
        linkedIn: "https://www.linkedin.com/in/example4/",
        expertise: "User Experience, Accessibility"
    },
    {
        name: "Sophia Rodriguez",
        title: "Security Engineer",
        company: "Microsoft",
        linkedIn: "https://www.linkedin.com/in/example5/",
        expertise: "Cybersecurity, Ethical Hacking"
    },
    {
        name: "James Thompson",
        title: "Program Manager",
        company: "Microsoft",
        linkedIn: "https://www.linkedin.com/in/example6/",
        expertise: "Project Management, Agile"
    }
];

// DOM Elements
const hamburger = document.querySelector('.hamburger');
const nav = document.querySelector('nav');
const profilesGrid = document.querySelector('.profiles-grid');
const currentYearSpan = document.getElementById('current-year');

// Set current year in footer
currentYearSpan.textContent = new Date().getFullYear();

// Mobile Navigation Toggle
hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    nav.classList.toggle('active');
});

// Close mobile nav when clicking a nav link
document.querySelectorAll('nav ul li a').forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        nav.classList.remove('active');
    });
});

// Create and populate profile cards
function displayProfiles() {
    professionals.forEach(profile => {
        const profileCard = document.createElement('div');
        profileCard.className = 'profile-card';
        
        // Get initials for the avatar
        const initials = profile.name.split(' ').map(n => n[0]).join('');
        
        profileCard.innerHTML = `
            <div class="profile-avatar">
                <div class="initials">${initials}</div>
            </div>
            <div class="profile-info">
                <h3>${profile.name}</h3>
                <p>${profile.title}, ${profile.company}</p>
                <p><strong>Expertise:</strong> ${profile.expertise}</p>
                <a href="${profile.linkedIn}" target="_blank" class="profile-link">
                    <i class="fab fa-linkedin"></i> Connect on LinkedIn
                </a>
            </div>
        `;
        
        profilesGrid.appendChild(profileCard);
    });
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        if (targetElement) {
            const headerHeight = document.querySelector('header').offsetHeight;
            const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// Animate elements on scroll
function animateOnScroll() {
    const elements = document.querySelectorAll('.resource-card, .ms-resource, .step');
    
    elements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const elementVisible = 150;
        
        if (elementTop < window.innerHeight - elementVisible) {
            element.classList.add('animate');
        }
    });
}

// Initialize the page
function init() {
    displayProfiles();
    
    // Add scroll event listener
    window.addEventListener('scroll', animateOnScroll);
    
    // Initial check for elements in view
    animateOnScroll();
}

// Run initialization when DOM is fully loaded
document.addEventListener('DOMContentLoaded', init);