let but = function (a, b) {
    let x = document.getElementById('x')
    let y = document.getElementById('y')
    let res = document.getElementById('res');
    console.log(x.innerText, y)
    res.textContent = Number(x.value) * Number(y.value);
}

let time = function(func) {

    setTimeout(func, 1000)
}
// console.log(22222222222222)
// window.alert(22222222222222)