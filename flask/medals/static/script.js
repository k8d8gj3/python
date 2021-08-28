elements = {
    button_getData: document.querySelector('.button_get-data'),
    medals: document.querySelector('.medals')
}

build_table = (data) => {
    console.log(data)
    html = '<table>' + data[0].map((el) => `<th>${el}</th>`).join('')
    data.shift()
    data.forEach(el => {
        html += '<tr>' + el.map((el) => `<td>${el}</td>`).join('')
    })
    html += '</table>'
    div = document.createElement('div')
    div.innerHTML = html
    elements.medals.append(div)
}

elements.button_getData.addEventListener('click', (event) => {
    elements.button_getData.remove()
    fetch('/getData').then((res) => {
        return res.json()
    }).then((data) => {
        build_table(data.medals)
    })
})