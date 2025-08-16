// DOM Elements
const stepCards = document.querySelectorAll('.step-card');
const resourceCards = document.querySelectorAll('.resource-card');
const internshipCards = document.querySelectorAll('.internship-card');

// Add entrance animations when cards come into view
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Initialize animations
function initAnimations() {
    // Set initial state for animated elements
    [...stepCards, ...resourceCards].forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });
}

// Track internship clicks
function trackInternshipClicks() {
    internshipCards.forEach((card, index) => {
        card.addEventListener('click', () => {
            // Add a visual feedback
            card.style.transform = 'scale(0.95)';
            setTimeout(() => {
                card.style.transform = '';
            }, 150);
            
            console.log(`Internship ${index + 1} clicked`);
        });
    });
}

// Smooth scroll for internal links
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Add hover effects to buttons
function initButtonEffects() {
    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('mouseenter', () => {
            btn.style.transform = 'translateY(-2px) scale(1.02)';
        });
        
        btn.addEventListener('mouseleave', () => {
            btn.style.transform = '';
        });
    });
}

// Progress indicator for steps
function initProgressIndicator() {
    const steps = document.querySelectorAll('.step-card');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const stepNumber = entry.target.querySelector('.step-number');
                stepNumber.style.background = 'rgba(242, 19, 104, 0.8)';
                stepNumber.style.transform = 'scale(1.1)';
                
                setTimeout(() => {
                    stepNumber.style.transform = 'scale(1)';
                }, 300);
            }
        });
    }, { threshold: 0.5 });
    
    steps.forEach(step => observer.observe(step));
}

// Initialize all functionality
document.addEventListener('DOMContentLoaded', () => {
    initAnimations();
    trackInternshipClicks();
    initSmoothScroll();
    initButtonEffects();
    initProgressIndicator();
    
    // Add a welcome message
    console.log('🚀 Microsoft Internship Portal loaded! Ready to launch your career?');
});

// Easter egg - Konami code for motivation
let konamiCode = [];
const konamiSequence = [
    'ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown',
    'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight',
    'KeyB', 'KeyA'
];

document.addEventListener('keydown', (e) => {
    konamiCode.push(e.code);
    konamiCode = konamiCode.slice(-konamiSequence.length);
    
    if (konamiCode.join('') === konamiSequence.join('')) {
        showMotivationalMessage();
        konamiCode = [];
    }
});

function showMotivationalMessage() {
    const messages = [
        "🎉 You've got this! Microsoft believes in you!",
        "💪 Every rejection is just redirection to something better!",
        "🚀 Your future starts with the first application!",
        "⭐ Dream big, code bigger, achieve the biggest!",
        "🔥 You're one click away from changing your life!"
    ];
    
    const randomMessage = messages[Math.floor(Math.random() * messages.length)];
    
    // Create a temporary modal
    const modal = document.createElement('div');
    modal.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: linear-gradient(135deg, #0092ca, #f21368);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        z-index: 1000;
        text-align: center;
        font-size: 1.2rem;
        font-weight: 600;
        max-width: 400px;
        animation: bounceIn 0.6s ease;
    `;
    
    modal.innerHTML = `
        ${randomMessage}
        <br><br>
        <small style="opacity: 0.8;">Keep pushing forward! 💙</small>
    `;
    
    document.body.appendChild(modal);
    
    setTimeout(() => {
        modal.style.animation = 'fadeOut 0.5s ease';
        setTimeout(() => document.body.removeChild(modal), 500);
    }, 3000);
}

// Add CSS for animations
const style = document.createElement('style');
style.textContent = `
    @keyframes bounceIn {
        0% { transform: translate(-50%, -50%) scale(0.3); opacity: 0; }
        50% { transform: translate(-50%, -50%) scale(1.05); }
        70% { transform: translate(-50%, -50%) scale(0.9); }
        100% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
    }
    
    @keyframes fadeOut {
        from { opacity: 1; }
        to { opacity: 0; }
    }
`;
document.head.appendChild(style);
