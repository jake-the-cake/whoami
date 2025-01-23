login = document.querySelector('#login-form')
register = document.querySelector('#registration-form')

login_link = register.querySelector('span')
register_link = login.querySelector('span')

buttons = Array.from(login.parentNode.querySelectorAll('button'))
login_btn = buttons.filter(btn => btn.innerText == 'Login')[0]
register_btn = buttons.filter(btn => btn.innerText == 'Register')[0]
button_container = login_btn.parentNode
console.log(button_container)

swapShrink([login, register])

register.classList.add('shrinkY')
login_btn.addEventListener('click', () => swapShrink([login, button_container]))
register_btn.addEventListener('click', () => swapShrink([register, button_container]))
login_link.addEventListener('click', () => swapShrink([login, register]))
register_link.addEventListener('click', () => swapShrink([login, register]))

function swapShrink(array) {
    array.forEach(cls => {
        cls.classList.toggle('shrinkY')
    })
}