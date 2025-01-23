login = document.querySelector('#login-form')
register = document.querySelector('#registration-form')

login_link = register.querySelector('span')
register_link = login.querySelector('span')

buttons = Array.from(login.parentNode.querySelectorAll('button'))
login_btn = buttons.filter(btn => btn.innerText == 'Login')[0]
register_btn = buttons.filter(btn => btn.innerText == 'Register')[0]
button_container = login_btn.parentNode

login_cancel = login.querySelector('#login-cancel')
register_cancel = register.querySelector('#register-cancel')

swapShrink([login, register])

// register.classList.add('shrinkY')
login_btn.addEventListener('click', () => swapShrink([button_container, login]))
register_btn.addEventListener('click', () => swapShrink([button_container, register]))
login_link.addEventListener('click', () => swapShrink([register, login]))
register_link.addEventListener('click', () => swapShrink([login, register]))
login_cancel.addEventListener('click', () => swapShrink([login, button_container]))
register_cancel.addEventListener('click', () => swapShrink([register, button_container]))

function swapShrink(array) {
    array.forEach(cls => {
        cls.classList.toggle('shrinkY')
    })
}