document.addEventListener('DOMContentLoaded', function() {
    // Initialize Fancybox
    Fancybox.bind("[data-fancybox='gallery']", {
        hideScrollbar: false,
        Carousel: {
            infinite: true,
        },
        on: {
            close: (fancybox, slide) => {
                // Remove Fancybox elements because of HTMX
                const fancyboxContainers = document.querySelectorAll('[id^="fancybox-"]');
                fancyboxContainers.forEach(container => {
                    container.remove();
                });
            }
        }
    });
});