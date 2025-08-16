// DOM Elements
const stepCards = document.querySelectorAll('.step-card');
const resourceCards = document.querySelectorAll('.resource-card');
const internshipCards = document.querySelectorAll('.internship-card');
const adviceLinks = document.querySelectorAll('.advice-link');

// Simple tracking for internship clicks
function trackInternshipClicks() {
    const internshipLinks = document.querySelectorAll('.internship-list a');
    
    internshipLinks.forEach((link, index) => {
        link.addEventListener('click', (e) => {
            console.log(`Internship link ${index + 1} clicked: ${link.href}`);
        });
    });
}

// Enhanced smooth scroll with offset for fixed header
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const headerOffset = 80; // Account for sticky header
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Simple button interactions - just basic hover effects
function initButtonEffects() {
    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('mouseenter', () => {
            btn.style.transform = 'translateY(-1px)';
        });
        
        btn.addEventListener('mouseleave', () => {
            btn.style.transform = '';
        });
    });
}

// Remove step progress tracking and parallax - too distracting

// Enhanced accessibility features
function initAccessibilityFeatures() {
    // Add skip link
    const skipLink = document.createElement('a');
    skipLink.href = '#steps';
    skipLink.textContent = 'Skip to main content';
    skipLink.style.cssText = `
        position: absolute;
        left: -9999px;
        z-index: 999;
        padding: 1rem;
        background: var(--primary-color);
        color: white;
        text-decoration: none;
        border-radius: 0 0 4px 0;
    `;
    
    skipLink.addEventListener('focus', () => {
        skipLink.style.left = '0';
    });
    
    skipLink.addEventListener('blur', () => {
        skipLink.style.left = '-9999px';
    });
    
    document.body.insertBefore(skipLink, document.body.firstChild);
    
    // Enhance focus management
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Tab') {
            document.body.classList.add('user-is-tabbing');
        }
    });
    
    document.addEventListener('mousedown', () => {
        document.body.classList.remove('user-is-tabbing');
    });
}

// Initialize all functionality - much simpler now
document.addEventListener('DOMContentLoaded', () => {
    trackInternshipClicks();
    initSmoothScroll();
    initButtonEffects();
    initAccessibilityFeatures();
    
    // Add minimal CSS for basic interactions
    const style = document.createElement('style');
    style.textContent = `
        .user-is-tabbing *:focus {
            outline: 3px solid rgba(79, 70, 229, 0.6) !important;
            outline-offset: 2px !important;
        }
    `;
    document.head.appendChild(style);
    
    // Simple welcome message
    console.log('🚀 Microsoft Internship Portal loaded!');
});

// Enhanced Easter egg with better UX
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
    
    // Create enhanced modal
    const modal = document.createElement('div');
    modal.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%) scale(0);
        background: linear-gradient(135deg, #4f46e5, #06b6d4);
        color: white;
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        z-index: 1000;
        text-align: center;
        font-size: 1.25rem;
        font-weight: 600;
        max-width: 450px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(10px);
    `;
    
    modal.innerHTML = `
        ${randomMessage}
        <br><br>
        <small style="opacity: 0.9; font-size: 0.9rem;">Keep pushing forward! You're amazing! 💙</small>
    `;
    
    document.body.appendChild(modal);
    
    // Animate in
    setTimeout(() => {
        modal.style.transform = 'translate(-50%, -50%) scale(1)';
    }, 10);
    
    // Auto remove after 4 seconds
    setTimeout(() => {
        modal.style.transform = 'translate(-50%, -50%) scale(0)';
        setTimeout(() => modal.remove(), 300);
    }, 4000);
    
    // Click to dismiss
    modal.addEventListener('click', () => {
        modal.style.transform = 'translate(-50%, -50%) scale(0)';
        setTimeout(() => modal.remove(), 300);
    });
}
