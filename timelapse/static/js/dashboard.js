

function handleButtons(buttonId) {
    let action;
    switch (buttonId) {
        case 'capture':
            action = 'capture';
            break;
     }
     fetch('/instructions/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({'instruction': action})
        }).then(response => {
            if (!response.ok) {
                throw new Error('Failed to send' + action + 'instruction');
            }
            return response.json();
        })
}


// stolen from ZenSpelling, thank you Makenna!
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