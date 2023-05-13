console.log('Hello, World!');

const showPost = (event) => {
    const cell = event.target;
    const text = cell.textContent;
    console.log(text);
    alert(text);
};

document.querySelectorAll('.qwe').forEach(function(cell) {
    cell.addEventListener('click', showPost);
});
document.querySelectorAll('.asd').forEach(function(cell) {
    cell.addEventListener('click', showPost);
});