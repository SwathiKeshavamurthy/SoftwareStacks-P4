document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('.like-icon').forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            const postId = this.getAttribute('data-post-id');
            fetch('{% url 'toggle_like' %}', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'), 
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ post_id: postId })
            })
            .then(response => response.json())
            .then(data => {
                if(data.liked) {
                    this.classList.add('liked'); 
                } else {
                    this.classList.remove('liked');
                }
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        });
    });
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