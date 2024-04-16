/*globals $:false */
/* jshint esversion: 6 */
$(document).ready(function() {
    $(".like-icon, .bookmark-icon").click(function() {
        var post_id = $(this).attr('data-post-id');
        var action = $(this).hasClass('like-icon') ? 'like' : 'bookmark';
        var authenticated = $(this).attr('data-authenticated'); // Check if user is authenticated

        if (authenticated === 'false') { // If user is not authenticated, show message and return
            alert("Please log in to " + action + " this post.");
            return;
        }

        var csrftoken = getCookie('csrftoken'); // Fetch CSRF token from cookie

        $.ajax({
            type: 'POST',
            url: action === 'like' ? '/like-post/' : '/bookmark-post/',
            data: {
                'post_id': post_id,
                'csrfmiddlewaretoken': csrftoken,
            },
            success: function(response) {
                // Update counts
                if (action === 'like') {
                    $(".like-icon[data-post-id='" + post_id + "']").html('<i class="far fa-heart"></i> ' + response.likes_count);
                } else {
                    $(".bookmark-icon[data-post-id='" + post_id + "']").html('<i class="far fa-bookmark"></i> ' + response.bookmarks_count);
                }
                // Change icon color
                if (response.liked || response.bookmarked) {
                    $(`.${action}-icon[data-post-id='${post_id}'] i`).removeClass('far').addClass('fas'); // Change to solid icon
                    $(`.${action}-icon[data-post-id='${post_id}']`).addClass(`${action}ed`); // Add 'liked' or 'bookmarked' class
                } else {
                    $(`.${action}-icon[data-post-id='${post_id}'] i`).removeClass('fas').addClass('far'); // Change to regular icon
                    $(`.${action}-icon[data-post-id='${post_id}']`).removeClass(`${action}ed`); // Remove 'liked' or 'bookmarked' class
                }
                // Display message
                alert(response.message);
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    });

    // Function to fetch CSRF token from cookie
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
