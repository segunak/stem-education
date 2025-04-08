// DOM Elements
const hamburger = document.querySelector('.hamburger');
const nav = document.querySelector('nav');
const charlotteProfilesGrid = document.querySelector('#charlotte-tab .profiles-grid');
const raleighProfilesGrid = document.querySelector('#raleigh-tab .profiles-grid');
const charlotteKeyProfiles = document.querySelector('#charlotte-tab .key-profiles');
const raleighKeyProfiles = document.querySelector('#raleigh-tab .key-profiles');
const currentYearSpan = document.getElementById('current-year');
const tabButtons = document.querySelectorAll('.tab-button');
const tabContents = document.querySelectorAll('.tab-content');

// Professionals data
const professionalsData = {
  "charlotte": {
    "keyContacts": [
      {
        "name": "James Bolling",
        "title": "Charlotte Campus Director",
        "linkedIn": "https://www.linkedin.com/in/jamesbolling/",
        "notes": ""
      },
      {
        "name": "Chemere Davis",
        "title": "Charlotte Business Program Manager",
        "linkedIn": "https://www.linkedin.com/in/chemeredavis/",
        "notes": ""
      }
    ],
    "professionals": [
      {
        "name": "Imani Ricks",
        "title": "UX Designer",
        "linkedIn": "https://www.linkedin.com/in/imani-ricks/",
        "notes": "Works on the Minecraft team",
        "isStarred": true
      },
      {
        "name": "Carrie White",
        "title": "Customer Success Account Manager", 
        "linkedIn": "https://www.linkedin.com/in/carriejwhite/",
        "notes": "",
      },
      {
        "name": "Lue Hale",
        "title": "Business Strategy Analyst",
        "linkedIn": "https://www.linkedin.com/in/luetennerhaleiii",
        "notes": ""
      },
      {
        "name": "Brandon Gary",
        "title": "Thermal Architect",
        "linkedIn": "https://www.linkedin.com/in/begary/",
        "notes": ""
      },
      {
        "name": "Jerome Collins",
        "title": "Commercial Executive",
        "linkedIn": "https://www.linkedin.com/in/jerome-collins-7789862b/",
        "notes": ""
      },
      {
        "name": "Rasuwl Walls",
        "title": "Director of Sales",
        "linkedIn": "https://www.linkedin.com/in/rasuwl/",
        "notes": ""
      },
      {
        "name": "Lex Barbosa",
        "title": "Design Operations Program Manager",
        "linkedIn": "https://www.linkedin.com/in/lexbarbosa/",
        "notes": "2025 Charlotte Business Journal 40 under 40 Honoree",
        "isStarred": true
      },
      // Cloud Solution Architects
      {
        "name": "Trevor Suarez",
        "title": "Cloud Solution Architect",
        "linkedIn": "https://www.linkedin.com/in/trevorsuarez/",
        "notes": ""
      },
      {
        "name": "Mayha Shah",
        "title": "Cloud Solution Architect",
        "linkedIn": "https://www.linkedin.com/in/mayhashah/",
        "notes": ""
      },
      {
        "name": "Jimmy Avila",
        "title": "Cloud Solution Architect",
        "linkedIn": "https://www.linkedin.com/in/jimmyavila/",
        "notes": ""
      },
      {
        "name": "Henrique Oliveira",
        "title": "Cloud Solution Architect",
        "linkedIn": "https://www.linkedin.com/in/henryoliveira5/",
        "notes": ""
      },
      // Customer Success Account Managers
      {
        "name": "Chloe Duffield",
        "title": "Customer Success Account Manager",
        "linkedIn": "https://www.linkedin.com/in/chloeduffielducla/",
        "notes": ""
      },
      {
        "name": "Carrie White",
        "title": "Customer Success Account Manager",
        "linkedIn": "https://www.linkedin.com/in/carriejwhite/",
        "notes": ""
      },
      {
        "name": "Uchenna Nwosu",
        "title": "Customer Success Account Manager",
        "linkedIn": "https://www.linkedin.com/in/unwosu44/",
        "notes": ""
      },
      {
        "name": "Samuel Blackmon",
        "title": "Customer Success Account Manager",
        "linkedIn": "https://www.linkedin.com/in/sblackmon/",
        "notes": ""
      },
      {
        "name": "Daniel Santana-Garcia",
        "title": "Customer Success Account Manager",
        "linkedIn": "https://www.linkedin.com/in/danielsntn/",
        "notes": ""
      },
      {
        "name": "Pauline Robinson",
        "title": "Customer Success Account Manager",
        "linkedIn": "https://www.linkedin.com/in/pauline-robinson/",
        "notes": ""
      },
      {
        "name": "Denisse Alvarado",
        "title": "Customer Success Account Manager",
        "linkedIn": "https://www.linkedin.com/in/denissealvarado/",
        "notes": ""
      },
      // Customer Success Account Manager Management
      {
        "name": "Jonathan Lindsay",
        "title": "Customer Success Account Manager Management",
        "linkedIn": "https://www.linkedin.com/in/jonathanllindsay/",
        "notes": ""
      },
      // Cybersecurity Managing Director
      {
        "name": "Rich Chambers",
        "title": "Cybersecurity Managing Director",
        "linkedIn": "https://www.linkedin.com/in/richkchambers/",
        "notes": ""
      },
      // Director Specialist
      {
        "name": "Jason Waybright",
        "title": "Director Specialist",
        "linkedIn": "https://www.linkedin.com/in/jason-waybright-6841987/",
        "notes": ""
      },
      // Integration Technical Infrastructure Manager
      {
        "name": "Victor Hart",
        "title": "Integration Technical Infrastructure Manager",
        "linkedIn": "https://www.linkedin.com/in/vhart/",
        "notes": ""
      },
      // Principal Director of Software Engineering
      {
        "name": "Moises Castro",
        "title": "Principal Director of Software Engineering",
        "linkedIn": "https://www.linkedin.com/in/moises-castro-52637117/",
        "notes": "2024 Charlotte Business Journal Power 100 Honoree",
        "isStarred": true
      },
      // Product Managers
      {
        "name": "Will Case",
        "title": "Product Manager",
        "linkedIn": "https://www.linkedin.com/in/willspacecase/",
        "notes": ""
      },
      {
        "name": "Meiko Lopez",
        "title": "Product Manager",
        "linkedIn": "https://www.linkedin.com/in/mldukes/",
        "notes": ""
      },
      // Principal Group Engineering Manager
      {
        "name": "Anusha Meka",
        "title": "Principal Group Engineering Manager",
        "linkedIn": "https://www.linkedin.com/in/anushameka/",
        "notes": "2025 Charlotte Business Journal Women in Business Honoree",
        "isStarred": true
      },
      // Software Engineers
      {
        "name": "Dave Vespa",
        "title": "Software Engineer",
        "linkedIn": "https://www.linkedin.com/in/drvespa/",
        "notes": ""
      },
      {
        "name": "Peshal Nepal",
        "title": "Software Engineer",
        "linkedIn": "https://www.linkedin.com/in/peshalnepal/",
        "notes": ""
      },
      // Support Engineers
      {
        "name": "Kristoff Little",
        "title": "Support Engineer",
        "linkedIn": "https://www.linkedin.com/in/kristoff-little-53382a199/",
        "notes": ""
      },
      {
        "name": "Franz Maurrasse",
        "title": "Support Engineer",
        "linkedIn": "https://www.linkedin.com/in/franzlmaurrasse/",
        "notes": ""
      },
      // Talent Acquisition Manager
      {
        "name": "Kyle Watson",
        "title": "Talent Acquisition Manager",
        "linkedIn": "https://www.linkedin.com/in/kyle-e-watson/",
        "notes": "Works in recruiting",
        "isStarred": true
      },
      // Technical Advisor
      {
        "name": "Cynthia Rice",
        "title": "Technical Advisor",
        "linkedIn": "https://www.linkedin.com/in/cynthia-rice-20825a14/",
        "notes": ""
      },
      // Technical Support Engineers
      {
        "name": "Avlokita Sharma",
        "title": "Technical Support Engineer",
        "linkedIn": "https://www.linkedin.com/in/avlokita-sharma220201/",
        "notes": ""
      },
      {
        "name": "Allan Matias",
        "title": "Technical Support Engineer",
        "linkedIn": "https://www.linkedin.com/in/allanmatias1986/",
        "notes": ""
      },
      {
        "name": "John Daly",
        "title": "Technical Support Engineer",
        "linkedIn": "https://www.linkedin.com/in/therealjohndaly/",
        "notes": ""
      },
      {
        "name": "Stacey Whitfield",
        "title": "Technical Support Engineer",
        "linkedIn": "https://www.linkedin.com/in/staceywhitfield/",
        "notes": ""
      },
      {
        "name": "Segun Akinyemi",
        "title": "Software Engineer",
        "linkedIn": "https://www.linkedin.com/in/segunakinyemi/",
        "notes": "Site creator",
        "isStarred": true
      }
    ]
  },
  "raleigh": {
    "keyContacts": [
      {
        "name": "Ken Key",
        "title": "Raleigh Campus Director",
        "linkedIn": "https://www.linkedin.com/in/ken-key-898803a/",
        "notes": ""
      },
      {
        "name": "Angelyn Smith",
        "title": "Raleigh Business Program Manager",
        "linkedIn": "https://www.linkedin.com/in/angelynempowers/",
        "notes": ""
      }
    ],
    "professionals": [
      {
        "name": "Chenae Erkerd",
        "title": "Technical Recruiter",
        "linkedIn": "https://www.linkedin.com/in/chenae-erkerd-j-d-racr-798b2389/",
        "notes": ""
      },
      {
        "name": "Rashida Hodge",
        "title": "Corporate Vice President of Azure Data & AI",
        "linkedIn": "https://www.linkedin.com/in/rashidahodge/",
        "notes": "Distinguished NC State alumnus with extraordinary impact, powerhouse tech industry leader, yet extremely down-to-earth",
        "isStarred": true
      },
      {
        "name": "Lakevious Battle",
        "title": "Cloud Solution Architect",
        "linkedIn": "https://www.linkedin.com/in/lakevious-battle/",
        "notes": ""
      },
      {
        "name": "Jasmine Young",
        "title": "Data Scientist",
        "linkedIn": "https://www.linkedin.com/in/jasmine-young-jgy2020/",
        "notes": ""
      },
      {
        "name": "Kevin Rewkowski",
        "title": "Customer Success Account Manager",
        "linkedIn": "https://www.linkedin.com/in/rewkowski/",
        "notes": ""
      }
    ]
  }
};

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
    // Display Charlotte key contacts
    if (professionalsData.charlotte && professionalsData.charlotte.keyContacts) {
        displayKeyContacts(professionalsData.charlotte.keyContacts, charlotteKeyProfiles);
    }
    
    // Display Raleigh key contacts
    if (professionalsData.raleigh && professionalsData.raleigh.keyContacts) {
        displayKeyContacts(professionalsData.raleigh.keyContacts, raleighKeyProfiles);
    }
    
    // Display Charlotte professionals
    if (professionalsData.charlotte && professionalsData.charlotte.professionals) {
        displayProfessionalCards(professionalsData.charlotte.professionals, charlotteProfilesGrid);
    }
    
    // Display Raleigh professionals
    if (professionalsData.raleigh && professionalsData.raleigh.professionals) {
        displayProfessionalCards(professionalsData.raleigh.professionals, raleighProfilesGrid);
    }
}

// Display key contacts
function displayKeyContacts(keyContacts, container) {
    container.innerHTML = '';
    
    keyContacts.forEach(contact => {
        const keyProfileCard = document.createElement('div');
        keyProfileCard.className = 'key-profile-card';
        
        // Get initials for the avatar
        const initials = contact.name.split(' ').map(n => n[0]).join('');
        
        keyProfileCard.innerHTML = `
            <div class="profile-avatar">
                <div class="initials">${initials}</div>
            </div>
            <div class="profile-info">
                <h4>${contact.name}</h4>
                <p>${contact.title}</p>
                <a href="${contact.linkedIn}" target="_blank" class="profile-link">
                    <i class="fab fa-linkedin"></i> Connect on LinkedIn
                </a>
            </div>
        `;
        
        container.appendChild(keyProfileCard);
    });
}

// Display professional cards
function displayProfessionalCards(professionals, container) {
    container.innerHTML = '';
    
    professionals.forEach(profile => {
        const profileCard = document.createElement('div');
        profileCard.className = profile.isStarred ? 'profile-card creator-card' : 'profile-card';
        
        // Get initials for the avatar
        const initials = profile.name.split(' ').map(n => n[0]).join('');
        
        let profileContent = `
            <div class="profile-avatar">
                <div class="initials">${initials}</div>
            </div>
            <div class="profile-info">
                <h4>${profile.name}</h4>
        `;
        
        if (profile.title) {
            profileContent += `<p><em>${profile.title}</em></p>`;
        }
        
        if (profile.notes) {
            profileContent += `<p><strong>Notes:</strong> ${profile.notes}</p>`;
        }
        
        profileContent += `
                <a href="${profile.linkedIn}" target="_blank" class="profile-link">
                    <i class="fab fa-linkedin"></i> Connect
                </a>
            </div>
        `;
        
        profileCard.innerHTML = profileContent;
        container.appendChild(profileCard);
    });
}

// Tab functionality for Charlotte and Raleigh profiles
tabButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Update active tab button
        tabButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
        
        // Show corresponding tab content
        const tabId = button.getAttribute('data-tab');
        tabContents.forEach(content => {
            content.classList.remove('active');
            if (content.id === `${tabId}-tab`) {
                content.classList.add('active');
            }
        });
    });
});

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
    const elements = document.querySelectorAll('.resource-card, .ms-resource, .step, .profile-card, .key-profile-card');
    
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