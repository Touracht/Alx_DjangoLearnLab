document.addEventListener('DOMContentLoaded', function() {
    console.log('Blog page loaded');

    // Get all toggle buttons
    const buttons = document.querySelectorAll('.toggle-comments-btn');
    
    // Attach click event listener to each button
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const postId = button.getAttribute('data-post-id');
            const commentsSection = document.getElementById('comments-' + postId);
            const arrow = button.querySelector('.arrow');

            // Toggle the comments section visibility
            if (commentsSection.style.display === 'none' || commentsSection.style.display === '') {
                commentsSection.style.display = 'block';
                arrow.textContent = '▲'; // Up arrow
                button.textContent = 'Hide Comments ';
                button.appendChild(arrow); // Re-append the arrow to ensure it's displayed correctly
            } else {
                commentsSection.style.display = 'none';
                arrow.textContent = '▼'; // Down arrow
                button.textContent = 'Show Comments ';
                button.appendChild(arrow); // Re-append the arrow to ensure it's displayed correctly
            }
        });
    });
});
