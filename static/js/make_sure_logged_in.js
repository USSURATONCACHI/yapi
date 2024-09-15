const make_sure_logged_in = () => {
    fetch('/api/am_i_logged_in', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `${localStorage['current_access_token']}`
        }
    })
    .then(response => {
        if (response.status == 200) {
            console.log('Yeah, im logged in');
        } else {
            window.location.assign("/unauthorized");
        }
    })
};

make_sure_logged_in();