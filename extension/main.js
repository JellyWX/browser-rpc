document.body.style.border = "5px solid red";

function update() {
  console.log('updating')
  console.log(window.location.href)

  var xhr = new XMLHttpRequest()
  xhr.open('POST', 'https://rpc.jellywx.co.uk/')

  xhr.setRequestHeader('Content-Type', 'application/json')
  xhr.setRequestHeader('email', 'judewrs@gmail.com')

  xhr.send(JSON.stringify({"state": window.location.href}))
}

setInterval(update, 5000)
