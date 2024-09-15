(() => {
    // Step 1: Get the hash fragment
    const hash = window.location.hash;

    // Step 2: Remove the `#` symbol
    const queryString = hash.substring(1);

    // Step 3: Parse the query string into an object
    const params = new URLSearchParams(queryString);
    
    if (params.get('error')) {
        alert('Возникла ошибка авторизации')
    } else {
        // Step 4: Access individual parameters
        const accessToken = params.get('access_token');
        const tokenType = params.get('token_type');
        const expiresIn = params.get('expires_in');
        const cid = params.get('cid');
    
        // Log the extracted values
        console.log('Access Token:', accessToken);
        console.log('Token Type:', tokenType);
        console.log('Expires In:', expiresIn);
        console.log('CID:', cid);
    
        const postData = {
            access_token: accessToken,
            expires_in: expiresIn,
        };
    
        // Send a POST request to the Flask endpoint
        fetch('/api/yandex_authorize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(postData)
        })
        .then(response => response.json()) // Parse the JSON response
        .then(data => {
            // Handle the JSON data from the response
            console.log('Success:', data);
            localStorage['current_access_token'] = data.current_access_token;
            window.location.replace(data.redirect_to);
        })
        .catch(error => {
            // Handle any errors
            console.error('Error:', error);
            alert(`Возникла ошибка авторизации: ${error}`);
            window.location.replace("/");
        });
    }

})();