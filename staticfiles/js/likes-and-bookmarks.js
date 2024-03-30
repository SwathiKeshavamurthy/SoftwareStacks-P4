document.addEventListener('DOMContentLoaded', function() {
    const likeIcon = document.querySelector('.like-icon');
    const bookmarkIcon = document.querySelector('.bookmark-icon');

    likeIcon.addEventListener('click', function() {
        const postId = this.dataset.postId;
        // AJAX call to toggle like
        console.log('Toggling like for post', postId);
        // Implement the fetch API to interact with your Django backend
    });

    bookmarkIcon.addEventListener('click', function() {
        const postId = this.dataset.postId;
        // AJAX call to toggle bookmark
        console.log('Toggling bookmark for post', postId);
        // Implement the fetch API to interact with your Django backend
    });
});
