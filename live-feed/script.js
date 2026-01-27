/**
 * Live Feed Page JavaScript
 * Handles tab switching, auto-refresh with visibility detection, and manual refresh
 */

// ======= DOM Elements =======
const tabButtons = document.querySelectorAll('.tab-btn');
const codePanels = document.querySelectorAll('.code-panel');
const liveToggle = document.getElementById('liveToggle');
const statusText = document.getElementById('statusText');
const refreshBtn = document.getElementById('refreshBtn');
const feedFrame = document.getElementById('feedFrame');
const currentYearSpan = document.getElementById('current-year');
const formToggle = document.getElementById('formToggle');
const formAccordion = document.getElementById('formAccordion');

// ======= State =======
let isLiveMode = false;
let refreshInterval = null;
const REFRESH_INTERVAL_MS = 10000; // 10 seconds

// ======= Initialize =======
function init() {
    // Set current year in footer
    if (currentYearSpan) {
        currentYearSpan.textContent = new Date().getFullYear();
    }
    
    // Set up tab switching
    setupTabs();
    
    // Set up form accordion
    setupFormAccordion();
    
    // Set up live mode toggle
    setupLiveToggle();
    
    // Set up manual refresh
    setupManualRefresh();
    
    // Set up visibility change detection
    setupVisibilityDetection();
}

// ======= Form Accordion =======
function setupFormAccordion() {
    formToggle.addEventListener('click', () => {
        const isOpen = formAccordion.classList.contains('open');
        
        formAccordion.classList.toggle('open', !isOpen);
        formToggle.classList.toggle('active', !isOpen);
        
        // Update button text
        const textSpan = formToggle.querySelector('span:last-child');
        textSpan.textContent = isOpen ? 'Show Submission Form' : 'Hide Submission Form';
    });
}

// ======= Tab Switching =======
function setupTabs() {
    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const targetTab = button.dataset.tab;
            
            // Update active tab button
            tabButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');
            
            // Show corresponding panel
            codePanels.forEach(panel => {
                panel.classList.remove('active');
                if (panel.id === targetTab) {
                    panel.classList.add('active');
                }
            });
        });
    });
}

// ======= Live Mode Toggle =======
function setupLiveToggle() {
    liveToggle.addEventListener('click', () => {
        isLiveMode = !isLiveMode;
        liveToggle.classList.toggle('active', isLiveMode);
        
        if (isLiveMode) {
            startAutoRefresh();
        } else {
            stopAutoRefresh();
        }
        
        updateStatusText();
    });
}

function startAutoRefresh() {
    // Only start if tab is visible
    if (document.visibilityState === 'visible') {
        stopAutoRefresh(); // Clear any existing interval
        refreshInterval = setInterval(refreshFeed, REFRESH_INTERVAL_MS);
    }
}

function stopAutoRefresh() {
    if (refreshInterval) {
        clearInterval(refreshInterval);
        refreshInterval = null;
    }
}

function updateStatusText() {
    if (!isLiveMode) {
        statusText.textContent = 'Auto-refresh off';
    } else if (document.visibilityState === 'hidden') {
        statusText.textContent = 'Paused (tab hidden)';
    } else {
        statusText.textContent = 'Refreshing every 10s';
    }
}

// ======= Manual Refresh =======
function setupManualRefresh() {
    refreshBtn.addEventListener('click', () => {
        refreshFeed();
        
        // Visual feedback
        const icon = refreshBtn.querySelector('i');
        icon.style.animation = 'none';
        // Trigger reflow
        icon.offsetHeight;
        icon.style.animation = 'spin 0.5s ease';
    });
}

function refreshFeed() {
    const baseSrc = feedFrame.src.split('?')[0];
    const cacheBust = 'cb=' + Date.now();
    feedFrame.src = baseSrc + '?viewControls=on&' + cacheBust;
}

// ======= Visibility Detection =======
function setupVisibilityDetection() {
    document.addEventListener('visibilitychange', () => {
        if (document.visibilityState === 'visible') {
            // Tab became visible
            if (isLiveMode) {
                // Refresh immediately when coming back
                refreshFeed();
                startAutoRefresh();
            }
        } else {
            // Tab became hidden - pause auto-refresh to save resources
            stopAutoRefresh();
        }
        
        updateStatusText();
    });
}

// ======= Start =======
document.addEventListener('DOMContentLoaded', init);
