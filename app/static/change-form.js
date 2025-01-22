login = document.querySelector('#login-form')
register = document.querySelector('#registration-form')

login_link = register.querySelector('span')
register_link = login.querySelector('span')

const swapShrink = () => {
    Array(register, login).forEach(cls => {
        cls.classList.toggle('shrinkY')
    })
}

register.classList.add('shrinkY')
login_link.addEventListener('click', swapShrink)
register_link.addEventListener('click', swapShrink)