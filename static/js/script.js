async function fetchYandexLoginUrl() {
    try {
        const response = await fetch('/api/get_yandex_login_url', {
            method: 'GET', // or 'POST' if the endpoint requires it
            headers: {
                'Content-Type': 'application/json',
            }
        });
  
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
  
        const data = await response.json(); // Assuming the server responds with JSON
        console.log(data); // Print the JSON object to the console or use it in your app
        return data;
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}

function handleYandexOauthClick(redirect_url) {
    window.location.assign(redirect_url);
}
  


document.addEventListener('DOMContentLoaded', () => {
    fetchYandexLoginUrl().then(data => {
        console.log(data);
        // Do something with the data
        const button = document.getElementById('yandex-oauth-btn');
        if (button) {
            button.onclick = () => handleYandexOauthClick(data.url);
        }
    
    });
      

});
  