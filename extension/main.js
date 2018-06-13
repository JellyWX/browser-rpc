function update(tabInfo) {
  console.log('updating')
  console.log(tabInfo[0])

  var xhr = new XMLHttpRequest()
  xhr.open('POST', 'https://rpc.jellywx.co.uk/')

  xhr.setRequestHeader('Content-Type', 'application/json')
  xhr.setRequestHeader('email', 'judewrs@gmail.com')

  xhr.send(JSON.stringify({"state": tabInfo[0].title}))
}

function err(error) {
  console.log(error)
}

function getTab() {
  var current = browser.tabs.query({currentWindow: true, active: true})
  current.then(update, err)
}


setInterval(getTab, 5000)
