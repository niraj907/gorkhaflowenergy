const menuBtn = document.getElementById('menuToggle')
const mobileMenu = document.getElementById('mobileMenu')

menuBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden')
})

const menuButtons = document.querySelectorAll('.menu-btn')
const mobileMenus = document.querySelectorAll('.mobile-menu')

menuButtons.forEach((btn, index) => {
    btn.addEventListener('click', () => {
        mobileMenus[index].classList.toggle('hidden')
    })
})