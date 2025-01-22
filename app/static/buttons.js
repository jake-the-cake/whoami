document.addEventListener('DOMContentLoaded', () => {
    removeCurrentPageLink()
})

function removeCurrentPageLink(href = window.location.href) {
    navbuttons = Array.from(document.querySelector('nav').children)
    navbuttons.forEach(button => {
        if (button.href === href) button.style.display = 'none'
    });
}