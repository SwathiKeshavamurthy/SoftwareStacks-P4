document.addEventListener("DOMContentLoaded", function() {
    const likeButtons = document.querySelectorAll('.like-post');
    const bookmarkButtons = document.querySelectorAll('.bookmark-post');

    const csrftoken = getCookie('csrftoken'); // Function to get CSRF token from cookies

    likeButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            toggleAction('toggle-like', this.dataset.postId, csrftoken);
        });
    });

    bookmarkButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            toggleAction('toggle-bookmark', this.dataset.postId, csrftoken);
        });
    });

    function toggleAction(action, postId, csrftoken) {
        fetch(`/${action}/${postId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({'post_id': postId})
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message); // Display message from server
            // Optionally, update UI based on action (e.g., change icon color)
        });
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
