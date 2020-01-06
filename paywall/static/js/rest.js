function setOutput(json) {
    document.getElementById('output').value = JSON.stringify(json)

}

function toJson(response) {
    return response.json()

}

function get() {
    fetch(`/secret?code=${document.getElementById('getCode').value}`)
        .then(toJson)
        .then(setOutput)

}

function post() {
    fetch('/secret', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'code': document.getElementById('postCode').value})
    })
        .then(toJson)
        .then(setOutput)

}

function put() {
    fetch(`/secret?from=${document.getElementById('fromCode').value}&to=${document.getElementById('toCode').value}`, {
        'method': 'PUT'
    })
        .then(toJson)
        .then(setOutput)
}

function restDelete() {
    fetch(`/secret?code=${document.getElementById('deleteCode').value}`, {method: 'DELETE'})
        .then(toJson)
        .then(setOutput)

}
