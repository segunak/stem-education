/*
	Hyperspace by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

(function($) {

	var	$window = $(window),
		$body = $('body'),
		$sidebar = $('#sidebar');

	// Breakpoints.
		breakpoints({
			xlarge:   [ '1281px',  '1680px' ],
			large:    [ '981px',   '1280px' ],
			medium:   [ '737px',   '980px'  ],
			small:    [ '481px',   '736px'  ],
			xsmall:   [ null,      '480px'  ]
		});

	// Hack: Enable IE flexbox workarounds.
		if (browser.name == 'ie')
			$body.addClass('is-ie');

	// Play initial animations on page load.
		$window.on('load', function() {
			window.setTimeout(function() {
				$body.removeClass('is-preload');
			}, 100);
		});

	// Forms.

		// Hack: Activate non-input submits.
			$('form').on('click', '.submit', function(event) {

				// Stop propagation, default.
					event.stopPropagation();
					event.preventDefault();

				// Submit form.
					$(this).parents('form').submit();

			});

	// Sidebar.
		if ($sidebar.length > 0) {

			var $sidebar_a = $sidebar.find('a');

			$sidebar_a
				.addClass('scrolly')
				.on('click', function() {

					var $this = $(this);

					// External link? Bail.
						if ($this.attr('href').charAt(0) != '#')
							return;

					// Deactivate all links.
						$sidebar_a.removeClass('active');

					// Activate link *and* lock it (so Scrollex doesn't try to activate other links as we're scrolling to this one's section).
						$this
							.addClass('active')
							.addClass('active-locked');

				})
				.each(function() {

					var	$this = $(this),
						id = $this.attr('href'),
						$section = $(id);

					// No section for this link? Bail.
						if ($section.length < 1)
							return;

					// Scrollex.
						$section.scrollex({
							mode: 'middle',
							top: '-20vh',
							bottom: '-20vh',
							initialize: function() {

								// Deactivate section.
									$section.addClass('inactive');

							},
							enter: function() {

								// Activate section.
									$section.removeClass('inactive');

								// No locked links? Deactivate all links and activate this section's one.
									if ($sidebar_a.filter('.active-locked').length == 0) {

										$sidebar_a.removeClass('active');
										$this.addClass('active');

									}

								// Otherwise, if this section's link is the one that's locked, unlock it.
									else if ($this.hasClass('active-locked'))
										$this.removeClass('active-locked');

									// Update progress tracker
									updateProgressTracker(id.substring(1));

							}
						});

				});

		}

	// Progress Tracker
	function updateProgressTracker(currentSection) {
		// Remove active class from all steps
		$('.progress-step').removeClass('active');

		// Add active class to the current step and all previous steps
		var sections = ["intro", "prompt1", "prompt2", "prompt3", "prompt4", "prompt5", "bonus-prompts", "wordbank"];
		var currentIndex = sections.indexOf(currentSection);

		if (currentIndex >= 0) {
			for (var i = 0; i <= currentIndex; i++) {
				$('.progress-step[data-step="' + sections[i] + '"]').addClass('active');
			}
		}
	}

	// Initialize progress tracker with first step active
	$(document).ready(function() {
		// Set first step active by default
		$('.progress-step[data-step="intro"]').addClass('active');

		// Add click handlers to progress steps
		$('.progress-step').on('click', function() {
			var section = $(this).data('step');
			$('html, body').animate({
				scrollTop: $('#' + section).offset().top
			}, 1000);
		});

		// Add floating helper for quick word bank access
		$('.floating-helper').on('click', function() {
			$('html, body').animate({
				scrollTop: $('#wordbank').offset().top
			}, 1000);
		});

		// Make word bank items clickable to copy text
		$('.word-list span').on('click', function() {
			var text = $(this).text();
			
			// Create temporary element for copying
			var $temp = $("<input>");
			$("body").append($temp);
			$temp.val(text).select();
			document.execCommand("copy");
			$temp.remove();
			
			// Visual feedback
			$(this).css('background', '#5e42a6');
			
			// Show tooltip
			$(this).append('<div class="copy-tooltip">Copied!</div>');
			
			setTimeout(function() {
				$(this).find('.copy-tooltip').fadeOut(function() {
					$(this).remove();
				});
				$(this).css('background', '');
			}.bind(this), 800);
		});

		 // Initialize bonus prompts section
		const bonusToggleBtn = document.getElementById('toggle-bonus-prompts');
		const bonusPromptContainer = document.querySelector('.bonus-prompts-container');
		
		if (bonusToggleBtn && bonusPromptContainer) {
			bonusToggleBtn.addEventListener('click', function() {
				this.classList.toggle('active');
				bonusPromptContainer.classList.toggle('show');
			});
		}

		// Enhance intro section on mobile - collapse lengthy text
		if ($(window).width() <= 736) {
			enhanceMobileIntro();
		}

		// Check which section is currently in view when page loads
		checkCurrentSection();
	});

	// Function to make intro more mobile-friendly
	function enhanceMobileIntro() {
		var $introList = $('#intro ol');
		if ($introList.length > 0 && !$introList.hasClass('enhanced')) {
			$introList.addClass('enhanced');
			
			// Create a toggle button
			var $toggle = $('<div class="mobile-toggle">Show detailed instructions</div>');
			$introList.after($toggle);
			
			// Initially hide all but first 2 items on small screens
			$introList.find('li:gt(1)').hide();
			
			// Toggle visibility on click
			$toggle.on('click', function() {
				$introList.find('li:gt(1)').slideToggle();
				$(this).text($(this).text() === 'Show detailed instructions' ? 'Hide detailed instructions' : 'Show detailed instructions');
			});
		}
	}

	// Check which section is currently in view
	function checkCurrentSection() {
		var scrollPosition = $(window).scrollTop() + ($(window).height() / 2);
		var sections = ["intro", "prompt1", "prompt2", "prompt3", "prompt4", "prompt5", "bonus-prompts", "wordbank"];
		
		// Find which section is currently in view
		for (var i = 0; i < sections.length; i++) {
			var $section = $('#' + sections[i]);
			if ($section.length > 0) {
				var sectionTop = $section.offset().top;
				var sectionBottom = sectionTop + $section.height();
				
				if (scrollPosition >= sectionTop && scrollPosition <= sectionBottom) {
					updateProgressTracker(sections[i]);
					break;
				}
			}
		}
	}

	// Update active section on scroll
	$(window).on('scroll', function() {
		checkCurrentSection();
	});

	// Scrolly.
		$('.scrolly').scrolly({
			speed: 1000,
			offset: function() {

				// If <=large, >small, and sidebar is present, use its height as the offset.
					if (breakpoints.active('<=large')
					&&	!breakpoints.active('<=small')
					&&	$sidebar.length > 0)
						return $sidebar.height();

				return 0;

			}
		});

	// Spotlights.
		$('.spotlights > section')
			.scrollex({
				mode: 'middle',
				top: '-10vh',
				bottom: '-10vh',
				initialize: function() {

					// Deactivate section.
						$(this).addClass('inactive');

				},
				enter: function() {

					// Activate section.
						$(this).removeClass('inactive');

				}
			})
			.each(function() {

				var	$this = $(this),
					$image = $this.find('.image'),
					$img = $image.find('img'),
					x;

				// Assign image.
					$image.css('background-image', 'url(' + $img.attr('src') + ')');

				// Set background position.
					if (x = $img.data('position'))
						$image.css('background-position', x);

				// Hide <img>.
					$img.hide();

			});

	// Features.
		$('.features')
			.scrollex({
				mode: 'middle',
				top: '-20vh',
				bottom: '-20vh',
				initialize: function() {

					// Deactivate section.
						$(this).addClass('inactive');

				},
				enter: function() {

					// Activate section.
						$(this).removeClass('inactive');

				}
			});

})(jQuery);