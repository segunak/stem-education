// DOM Elements
const hamburger = document.querySelector('.hamburger');
const nav = document.querySelector('nav');
const charlotteProfilesGrid = document.querySelector('#charlotte-tab .profiles-grid');
const raleighProfilesGrid = document.querySelector('#raleigh-tab .profiles-grid');
const currentYearSpan = document.getElementById('current-year');
const tabButtons = document.querySelectorAll('.tab-button');
const tabContents = document.querySelectorAll('.tab-content');
const backToTopButton = document.getElementById('back-to-top');
const body = document.body;

// Professionals data
const professionalsData = {
  "charlotte": {
    "professionals": [
      // {
      //   "name": "James Bolling",
      //   "title": "Charlotte Campus Director",
      //   "linkedIn": "https://www.linkedin.com/in/jamesbolling/",
      //   "notes": ""
      // },
      {
        "name": "Chemere Davis",
        "title": "Charlotte Business Program Manager",
        "linkedIn": "https://www.linkedin.com/in/chemeredavis/",
        "isStarred": true,
        "notes": "Campus leader for community, culture, and employee experience, definitely connect!"
      },
      {
        "name": "Millie Kembe",
        "title": "Software Engineer Intern",
        "linkedIn": "https://www.linkedin.com/in/millie-kembe/",
        "notes": ""
      },
      {
        "name": "Thomas Chattman",
        "title": "Program Manager",
        "linkedIn": "https://www.linkedin.com/in/thomas-chattmaniv/",
        "notes": ""
      },
      {
        "name": "Enya Schumacher",
        "title": "Director of Customer Experience",
        "linkedIn": "https://www.linkedin.com/in/enyaschumacher/",
        "notes": ""
      },
      {
        "name": "Joe Baily",
        "title": "Security Specialist",
        "linkedIn": "https://www.linkedin.com/in/joe-baily-662057165/",
        "notes": ""
      },
      {
        "name": "Da'Les Hill",
        "title": "Marketing Consultant",
        "linkedIn": "https://www.linkedin.com/in/dales-hill/",
        "notes": ""
      },
      // {
      //   "name": "Liz Martin",
      //   "title": "Business Program Manager",
      //   "linkedIn": "https://www.linkedin.com/in/liz-martin-rhia-cdip-cpc-cpc-i-crc-52537813a/",
      //   "notes": ""
      // },
      {
        "name": "Samuel Blackmon",
        "title": "Customer Success Account Manager",
        "linkedIn": "https://www.linkedin.com/in/sblackmon/",
        "notes": ""
      },
      {
        "name": "Will Case",
        "title": "Product Manager",
        "linkedIn": "https://www.linkedin.com/in/willspacecase/",
        "notes": ""
      },      {
        "name": "Kristoff Little",
        "title": "Support Engineer",
        "linkedIn": "https://www.linkedin.com/in/kristoff-little-53382a199/",
        "notes": ""
      },
      {
        "name": "Jillian Dozier",
        "title": "Business Program Manager",
        "linkedIn": "https://www.linkedin.com/in/jill-do/",
        "notes": ""
      },
      // {
      //   "name": "Mohan Ravindran",
      //   "title": "Cloud Solution Architect",
      //   "linkedIn": "https://www.linkedin.com/in/mohan-ravindran-736a2516/",
      //   "notes": ""
      // },
      {
        "name": "Amy Vargo",
        "title": "Customer Success Account Manager",
        "linkedIn": "https://www.linkedin.com/in/amy-vargo-20022313a/",
        "notes": ""
      },
      {
        "name": "LeShawn Johnson Vega",
        "title": "Employee Relations Director",
        "linkedIn": "https://www.linkedin.com/in/leshawnjohnsonvega-mba-mshrm/",
        "notes": ""
      },
      // {
      //   "name": "Parth Desai",
      //   "title": "Support Engineer",
      //   "linkedIn": "https://www.linkedin.com/in/parth-82996a211/",
      //   "notes": ""
      // },
      // {
      //   "name": "Christopher Love",
      //   "title": "Customer Success Account Manager",
      //   "linkedIn": "https://www.linkedin.com/in/lovechristopher/",
      //   "notes": ""
      // },
      // {
      //   "name": "Holly Todd",
      //   "title": "Customer Success Account Manager",
      //   "linkedIn": "https://www.linkedin.com/in/hollyrtodd/",
      //   "notes": ""
      // },
      // {
      //   "name": "Kayla Brooks",
      //   "title": "UX Product Manager",
      //   "linkedIn": "https://www.linkedin.com/in/kayla-brooks-abc/",
      //   "notes": ""
      // },
      // {
      //   "name": "Sankar Muthu",
      //   "title": "Cloud Solution Architect",
      //   "linkedIn": "https://www.linkedin.com/in/sankarmuthu/",
      //   "notes": ""
      // },
      // {
      //   "name": "Juan Flowers",
      //   "title": "Customer Success Account Manager",
      //   "linkedIn": "https://www.linkedin.com/in/juanflowers/",
      //   "notes": ""
      // },
      // {
      //   "name": "Darlesia Weatherly",
      //   "title": "Support Engineer",
      //   "linkedIn": "https://www.linkedin.com/in/darlesia/",
      //   "notes": ""
      // },
      // {
      //   "name": "Evan Kirk",
      //   "title": "Customer Success Account Manager",
      //   "linkedIn": "https://www.linkedin.com/in/evan-kirk-5a5a2b211/",
      //   "notes": ""
      // },
      // {
      //   "name": "Anthony Morris",
      //   "title": "Support Engineer",
      //   "linkedIn": "https://www.linkedin.com/in/morjit/",
      //   "notes": ""
      // },
      // {
      //   "name": "Allison Geoghegan",
      //   "title": "Support Engineer Manager",
      //   "linkedIn": "https://www.linkedin.com/in/allison-geoghegan/",
      //   "notes": ""
      // },
      // {
      //   "name": "Parneet Kaur",
      //   "title": "Customer Success Account Manager",
      //   "linkedIn": "https://www.linkedin.com/in/boparaikparneet/",
      //   "notes": ""
      // },
      // {
      //   "name": "Carlos Oquendo Jr.",
      //   "title": "Director Business Application Specialist",
      //   "linkedIn": "https://www.linkedin.com/in/carlos-oquendo-jr/",
      //   "notes": ""
      // },
      // {
      //   "name": "Lue Hale",
      //   "title": "Business Strategy Analyst",
      //   "linkedIn": "https://www.linkedin.com/in/luetennerhaleiii",
      //   "notes": ""
      // },
      {
        "name": "Anusha Meka",
        "title": "Principal Group Engineering Manager",
        "linkedIn": "https://www.linkedin.com/in/anushameka/",
        "notes": "2025 Charlotte Business Journal Women in Business Honoree",
        "isStarred": true
      },
      // {
      //   "name": "Brandon Gary",
      //   "title": "Thermal Architect",
      //   "linkedIn": "https://www.linkedin.com/in/begary/",
      //   "notes": ""
      // },
      {
        "name": "Imani Ricks",
        "title": "UX Designer",
        "linkedIn": "https://www.linkedin.com/in/imani-ricks/",
        "notes": "Works on the Minecraft team"
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
      {
        "name": "Trevor Suarez",
        "title": "Cloud Solution Architect",
        "linkedIn": "https://www.linkedin.com/in/trevorsuarez/",
        "notes": ""
      },
      // {
      //   "name": "Mayha Shah",
      //   "title": "Cloud Solution Architect",
      //   "linkedIn": "https://www.linkedin.com/in/mayhashah/",
      //   "notes": ""
      // },
      {
        "name": "Andrew Dawkins",
        "title": "Senior Consultant", 
        "linkedIn": "https://www.linkedin.com/in/andrewdawkinsit/",
        "notes": ""
      },
      {
        "name": "Kyle Watson",
        "title": "Talent Acquisition Manager",
        "linkedIn": "https://www.linkedin.com/in/kyle-e-watson/",
        "notes": "Works in recruiting!",
        "isStarred": true
      },
      {
        "name": "Jimmy Avila",
        "title": "Cloud Solution Architect",
        "linkedIn": "https://www.linkedin.com/in/jimmyavila/",
        "notes": ""
      },
      // {
      //   "name": "Henrique Oliveira",
      //   "title": "Cloud Solution Architect",
      //   "linkedIn": "https://www.linkedin.com/in/henryoliveira5/",
      //   "notes": ""
      // },
      // {
      //   "name": "Chloe Duffield",
      //   "title": "Customer Success Account Manager",
      //   "linkedIn": "https://www.linkedin.com/in/chloeduffielducla/",
      //   "notes": ""
      // },
      // {
      //   "name": "Uchenna Nwosu",
      //   "title": "Customer Success Account Manager",
      //   "linkedIn": "https://www.linkedin.com/in/unwosu44/",
      //   "notes": ""
      // },
      // {
      //   "name": "Daniel Santana-Garcia",
      //   "title": "Customer Success Account Manager",
      //   "linkedIn": "https://www.linkedin.com/in/danielsntn/",
      //   "notes": ""
      // },
      {
        "name": "Pauline Robinson",
        "title": "Customer Success Account Manager",
        "linkedIn": "https://www.linkedin.com/in/pauline-robinson/",
        "notes": ""
      },
      // {
      //   "name": "Denisse Alvarado",
      //   "title": "Customer Success Account Manager",
      //   "linkedIn": "https://www.linkedin.com/in/denissealvarado/",
      //   "notes": ""
      // },
      {
        "name": "Moises Castro",
        "title": "Principal Director of Software Engineering",
        "linkedIn": "https://www.linkedin.com/in/moises-castro-52637117/",
        "notes": "2024 Charlotte Business Journal Power 100 Honoree",
        "isStarred": true
      },
      // {
      //   "name": "Tennill Mitchell",
      //   "title": "Relationship Manager",
      //   "linkedIn": "https://www.linkedin.com/in/tennill-mitchell-mfa-7a44565/",
      //   "notes": ""
      // },
      // {
      //   "name": "Dave Vespa",
      //   "title": "Software Engineer",
      //   "linkedIn": "https://www.linkedin.com/in/drvespa/",
      //   "notes": ""
      // },
      // {
      //   "name": "Peshal Nepal",
      //   "title": "Software Engineer",
      //   "linkedIn": "https://www.linkedin.com/in/peshalnepal/",
      //   "notes": ""
      // },
      // {
      //   "name": "Franz Maurrasse",
      //   "title": "Support Engineer",
      //   "linkedIn": "https://www.linkedin.com/in/franzlmaurrasse/",
      //   "notes": ""
      // },
      {
        "name": "Cynthia Rice",
        "title": "Technical Advisor",
        "linkedIn": "https://www.linkedin.com/in/cynthia-rice-20825a14/",
        "notes": ""
      },
      // {
      //   "name": "Avlokita Sharma",
      //   "title": "Technical Support Engineer",
      //   "linkedIn": "https://www.linkedin.com/in/avlokita-sharma220201/",
      //   "notes": ""
      // },
      // {
      //   "name": "Allan Matias",
      //   "title": "Technical Support Engineer",
      //   "linkedIn": "https://www.linkedin.com/in/allanmatias1986/",
      //   "notes": ""
      // },
      {
        "name": "John Daly",
        "title": "Technical Support Engineer",
        "linkedIn": "https://www.linkedin.com/in/therealjohndaly/",
        "notes": ""
      },
      // {
      //   "name": "Stacey Whitfield",
      //   "title": "Technical Support Engineer",
      //   "linkedIn": "https://www.linkedin.com/in/staceywhitfield/",
      //   "notes": ""
      // },
      {
        "name": "Segun Akinyemi",
        "title": "Software Engineer",
        "linkedIn": "https://www.linkedin.com/in/segunakinyemi/",
        "notes": "Site creator"
      }
    ]
  },
  "raleigh": {
    "professionals": [
      {
        "name": "Ken Key",
        "title": "Raleigh Campus Director",
        "linkedIn": "https://www.linkedin.com/in/ken-key-898803a/",
        "notes": "",
        "isStarred": true
      },
      {
        "name": "Angelyn Smith",
        "title": "Raleigh Business Program Manager",
        "linkedIn": "https://www.linkedin.com/in/angelynempowers/",
        "notes": "Campus leader for community, culture, and employee experience, definitely connect!",
        "isStarred": true
      },
      {
        "name": "Rashida Hodge",
        "title": "Corporate Vice President of Azure Data & AI",
        "linkedIn": "https://www.linkedin.com/in/rashidahodge/",
        "notes": "Distinguished NC State alumnus with extraordinary impact, powerhouse tech industry leader, yet an extremely down-to-earth and approchable person!",
        "isStarred": true
      },
      {
        "name": "Tenesha Robinson",
        "title": "Senior Consultant",
        "linkedIn": "https://www.linkedin.com/in/tenesha-robinson-62046337/",
        "notes": ""
      },
      {
        "name": "Chenae Erkerd",
        "title": "Technical Recruiter",
        "linkedIn": "https://www.linkedin.com/in/chenae-erkerd-j-d-racr-798b2389/",
        "notes": "Works in recruiting!",
        "isStarred": true
      },
      // {
      //   "name": "Nevonda Davis",
      //   "title": "Customer Success Account Manager",
      //   "linkedIn": "https://www.linkedin.com/in/nevondamba/",
      //   "notes": ""
      // },
      {
        "name": "Breanne Dixon",
        "title": "Recruiter",
        "linkedIn": "https://www.linkedin.com/in/breanne-dixon-1576968a/",
        "notes": "Works in recruiting!",
        "isStarred": true
      },
      // {
      //   "name": "Taylor Allen-Rider",
      //   "title": "UX Researcher",
      //   "linkedIn": "https://www.linkedin.com/in/tallen-rider/",
      //   "notes": ""
      // },
      // {
      //   "name": "Alfred Gamble",
      //   "title": "Human Resources Consultant",
      //   "linkedIn": "https://www.linkedin.com/in/alfred-gamble-mshrm-phr-shrm-cp-2446002b/",
      //   "notes": ""
      // },
      // {
      //   "name": "Brigitte Woods",
      //   "title": "Director of Business Planning & Management",
      //   "linkedIn": "https://www.linkedin.com/in/brigitte-woods/",
      //   "notes": ""
      // },
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
      },
      // {
      //   "name": "Ria Simpson",
      //   "title": "Business Administrator",
      //   "linkedIn": "https://www.linkedin.com/in/ria-simpson/",
      //   "notes": ""
      // },
      // {
      //   "name": "Kyle Reese",
      //   "title": "Account Executive",
      //   "linkedIn": "https://www.linkedin.com/in/kylemreese/",
      //   "notes": ""
      // },
      // {
      //   "name": "Trent Sandles",
      //   "title": "Specialist",
      //   "linkedIn": "https://www.linkedin.com/in/trentsandles/",
      //   "notes": ""
      // }
    ]
  }
};

// Set current year in footer
currentYearSpan.textContent = new Date().getFullYear();

// Mobile Navigation Toggle
hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    nav.classList.toggle('active');
    body.classList.toggle('menu-open'); // Lock scrolling when menu is open
});

// Close mobile nav when clicking a nav link
document.querySelectorAll('nav ul li a').forEach(link => {
    link.addEventListener('click', () => {
        hamburger.classList.remove('active');
        nav.classList.remove('active');
        body.classList.remove('menu-open'); // Unlock scrolling
    });
});

// Back to Top functionality
window.addEventListener('scroll', () => {
    if (window.scrollY > 500) { // Show after scrolling down 500px
        backToTopButton.classList.add('visible');
    } else {
        backToTopButton.classList.remove('visible');
    }
});

backToTopButton.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// Create and populate profile cards
function displayProfiles() {
    // Display Charlotte professionals
    if (professionalsData.charlotte && professionalsData.charlotte.professionals) {
        displayProfessionalCards(professionalsData.charlotte.professionals, charlotteProfilesGrid);
    }
    
    // Display Raleigh professionals
    if (professionalsData.raleigh && professionalsData.raleigh.professionals) {
        displayProfessionalCards(professionalsData.raleigh.professionals, raleighProfilesGrid);
    }
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
tabButtons.forEach((button) => {
    button.addEventListener('click', () => {
        const targetTab = button.getAttribute('data-tab');
        
        // Update active states
        tabButtons.forEach(btn => btn.classList.remove('active'));
        tabContents.forEach(content => content.classList.remove('active'));
        
        button.classList.add('active');
        document.getElementById(`${targetTab}-tab`).classList.add('active');
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
            // Add a small additional offset for better spacing
            const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - headerHeight - 20;
            
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
    
    // Initial check for back-to-top button visibility
    if (window.scrollY > 500) {
        backToTopButton.classList.add('visible');
    }
}

// Run initialization when DOM is fully loaded
document.addEventListener('DOMContentLoaded', init);