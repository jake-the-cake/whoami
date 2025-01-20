document.addEventListener('DOMContentLoaded', () => {
    navbuttons = Array.from(document.querySelector('nav').children)
    navbuttons.forEach(button => {
        if (button.href === window.location.href) button.style.display = 'none'
    });
})