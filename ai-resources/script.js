// DOM elements
const hamburger = document.querySelector('.hamburger');
const nav = document.querySelector('nav');
const backToTopButton = document.getElementById('back-to-top');
const header = document.querySelector('header');

// Mobile menu toggle
if (hamburger) {
    hamburger.addEventListener('click', () => {
        nav.classList.toggle('active');
    });
}

// Close mobile menu on link click
document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', () => {
        nav.classList.remove('active');
    });
});

// Hero rant accordion
const rantTrigger = document.getElementById('rant-trigger');
const rantBody = document.getElementById('rant-body');
if (rantTrigger && rantBody) {
    rantTrigger.addEventListener('click', () => {
        const wrapper = rantTrigger.parentElement;
        const isActive = wrapper.classList.contains('active');
        if (isActive) {
            wrapper.classList.remove('active');
            rantBody.style.maxHeight = null;
        } else {
            wrapper.classList.add('active');
            rantBody.style.maxHeight = rantBody.scrollHeight + 'px';
        }
    });
}

// FAQ accordion
document.querySelectorAll('.faq-question').forEach(button => {
    button.addEventListener('click', () => {
        const item = button.parentElement;
        const answer = item.querySelector('.faq-answer');
        const isActive = item.classList.contains('active');

        // Close all
        document.querySelectorAll('.faq-item').forEach(i => {
            i.classList.remove('active');
            i.querySelector('.faq-answer').style.maxHeight = null;
        });

        // Open clicked if it wasn't already open
        if (!isActive) {
            item.classList.add('active');
            answer.style.maxHeight = answer.scrollHeight + 'px';
        }
    });
});

// General accordion (What to Learn, Who to Follow)
document.querySelectorAll('.accordion-trigger').forEach(button => {
    button.addEventListener('click', () => {
        const item = button.parentElement;
        const body = item.querySelector('.accordion-body');
        const isActive = item.classList.contains('active');

        // Close siblings only within same accordion-list
        const parent = item.parentElement;
        parent.querySelectorAll('.accordion-item').forEach(i => {
            i.classList.remove('active');
            i.querySelector('.accordion-body').style.maxHeight = null;
        });

        if (!isActive) {
            item.classList.add('active');
            body.style.maxHeight = body.scrollHeight + 'px';
        }
    });
});

// Scroll: back to top + header shadow
window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;

    // Back to top visibility
    if (backToTopButton) {
        backToTopButton.style.display = scrollY > 400 ? 'flex' : 'none';
    }

    // Header shadow on scroll
    if (header) {
        header.classList.toggle('scrolled', scrollY > 10);
    }
});

if (backToTopButton) {
    backToTopButton.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

// Footer year
const yearSpan = document.getElementById('current-year');
if (yearSpan) {
    yearSpan.textContent = new Date().getFullYear();
}
