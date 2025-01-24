document.addEventListener('DOMContentLoaded', () => {
    const pageAddress = window.location.origin + window.location.pathname
    removeCurrentPageLink(pageAddress)
})

function removeCurrentPageLink(href) {
    navbuttons = Array.from(document.querySelector('nav').children)
    navbuttons.forEach(button => {
        if (button.href === href) button.style.display = 'none'
    });
}