fetch('/paywall_ajax')
    .then(response => response.json())
    .then(json => document.getElementById('ajax_code').textContent = json.code)