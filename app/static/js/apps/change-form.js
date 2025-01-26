login = document.querySelector('#login-form')
register = document.querySelector('#registration-form')
login.addEventListener('submit', returnToPosition)
register.addEventListener('submit', returnToPosition)

login_link = register.querySelector('span')
register_link = login.querySelector('span')
login_link.addEventListener('click', () => toggleHeight([register, login]))
register_link.addEventListener('click', () => toggleHeight([login, register]))

buttons = Array.from(login.parentNode.querySelectorAll('button'))
login_btn = buttons.filter(btn => btn.innerText == 'Login')[0]
register_btn = buttons.filter(btn => btn.innerText == 'Register')[0]
button_container = login_btn.parentNode
login_btn.addEventListener('click', () => toggleHeight([button_container, login]))
register_btn.addEventListener('click', () => toggleHeight([button_container, register]))

login_cancel = login.querySelector('#login-cancel')
register_cancel = register.querySelector('#register-cancel')
login_cancel.addEventListener('click', () => toggleHeight([login, button_container]))
register_cancel.addEventListener('click', () => toggleHeight([register, button_container]))

function returnToPosition() {
    localStorage.setItem('scrollPosition', window.scrollY)
    localStorage.setItem('previousPage', window.location.pathname)
}

function toggleHeight(array) {
    array.forEach(cls => {
        cls.classList.toggle('shrinkY')
    })
}