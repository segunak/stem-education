document.addEventListener('DOMContentLoaded', function () {
    // Function to determine if the device is likely a mobile
    const isMobileDevice = () => {
        // Set the breakpoint for mobile vs tablet/desktop
        const mobileBreakpoint = 768; // Typical tablet size in portrait mode

        // Access the user-agent string and convert it to lowercase for case-insensitive matching
        const userAgent = navigator.userAgent.toLowerCase();

        // Check if the window's inner width is less than or equal to the breakpoint or if the user agent contains 'mobile'
        // This helps determine if the device is mobile based on screen size or user-agent indications
        const isMobile = window.innerWidth <= mobileBreakpoint || /mobile/i.test(userAgent);

        // Return true if either condition is met (indicating a mobile device), otherwise false
        return isMobile;
    };

    const updateLinkTargets = () => {
        // Retrieve all 'a' elements (links) in the document
        const links = document.getElementsByTagName('a');

        // Iterate over each link to determine the correct target attribute
        [...links].forEach(link => {
            // Check if the link belongs to the masthead menu and skip updating it
            if (link.closest('.visible-links')) {
                return;
            }
            // Check if the link's target is explicitly set to '_blank' and skip updating it. Allow override if I really want a new tab opened.
            else if (link.target === '_blank') {
                return;
            }
            // Check if the link is internal by comparing the link's host with the current window's host
            else if (link.hostname === window.location.hostname) {
                // If the link is internal, open it in the same tab
                link.target = '_self';
            }
            else {
                // Determine the appropriate target attribute value based on whether the device is mobile
                // Use '_self' to open links in the same tab for mobile devices and '_blank' to open links in a new tab for non-mobile devices
                const targetAttribute = isMobileDevice() ? '_self' : '_blank';
                link.target = targetAttribute;
            }
        });
    };

    // Call the function to initially set the target attributes for all links
    updateLinkTargets();

    // Add an event listener to the window to handle resizing
    // This ensures that link targets are updated if the window size changes, which might change the device classification (e.g., from portrait to landscape)
    window.addEventListener('resize', updateLinkTargets);
});