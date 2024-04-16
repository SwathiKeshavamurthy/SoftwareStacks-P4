/* jshint esversion: 6 */
document.addEventListener('DOMContentLoaded', function() {
    const deletePostModalElement = document.getElementById('deletePostModal');
    const deletePostButton = deletePostModalElement.querySelector('#confirmDeletePost');

    deletePostModalElement.addEventListener('show.bs.modal', function(event) {
        const buttonClicked = event.relatedTarget;
        const postSlug = buttonClicked.getAttribute('data-post-slug');
        deletePostButton.onclick = function() {
            fetch(`/post/delete/${postSlug}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),  
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            }).then(response => {
                if (response.ok) {
                    window.location.href = '/';  // Redirect after delete
                } else {
                    alert('Failed to delete the post.');
                }
            }).catch(error => console.error('Error deleting post:', error));
        };
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
