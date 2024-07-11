let button = document.getElementById('but');
let x = document.getElementById('x');
let y = document.getElementById('y');
let res = document.getElementById('res');



button.onclick = function() {
    res.textContent = Number(x.value) + Number(y.value);
}