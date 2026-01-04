document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;

    // Track mouse movement
    document.addEventListener('mousemove', (e) => {
        const x = e.clientX;
        const y = e.clientY;

        // Update CSS variables
        body.style.setProperty('--mouse-x', `${x}px`);
        body.style.setProperty('--mouse-y', `${y}px`);
    });
});

window.toggleExp = function(btn) {
    const details = btn.parentElement.querySelector('.exp-details');
    if (!details) return;
    
    const isHidden = details.style.display === 'none' || getComputedStyle(details).display === 'none';
    details.style.display = isHidden ? 'block' : 'none';
    btn.textContent = isHidden ? 'Show Less' : 'Read More';
};
