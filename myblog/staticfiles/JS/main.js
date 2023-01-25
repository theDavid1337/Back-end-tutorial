let header = document.querySelector('header')
let blog_detail_left = document.querySelector('.blog_detail_left')
let blog_detail_edit_remove = document.querySelector('.blog_detail_edit_remove')
window.addEventListener('scroll', () => {
    let scroll = window.scrollY
    if (window.scrollY > 0) {
        header.classList.add('active')
    } else {
        header.classList.remove('active')
    }
    console.log(scroll);
    // blog_detail_left.style.top = `${scroll / 20}px`
})

function edit_or_remove() {
    blog_detail_edit_remove.classList.toggle('active')
}