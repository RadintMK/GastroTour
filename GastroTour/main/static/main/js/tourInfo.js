function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie!== '') {
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

const csrftoken = getCookie('csrftoken');

document.addEventListener('DOMContentLoaded', function() {
    var addToCartButtons = document.querySelectorAll('.add-to-cart-btn');

    addToCartButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault(); // Предотвратить стандартное поведение кнопки
            var restaurantId = this.getAttribute('data-restaurant-id');
            addToCart(restaurantId);
        });
    });

    function addToCart(restaurantName) {
        fetch(`/add-to-cart/${encodeURIComponent(restaurantName)}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({restaurant_name: restaurantName})
        })
      .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json(); 
        })
      .then(data => {

            console.log(data); 
        })
      .catch(error => {
            console.error('Произошла проблема с операцией fetch:', error);
        });
    }
});


function redirectToPayPage(element) {
    var restaurantName = element.getAttribute('data-restaurant-id');
    var encodedRestaurantName = encodeURIComponent(restaurantName);
    var payUrl = `/pay/${encodedRestaurantName}/`;
    window.location.href = payUrl;
}

