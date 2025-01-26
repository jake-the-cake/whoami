window.addEventListener('load', () => {
  const scrollPosition = localStorage.getItem('scrollPosition')
  const previousPage = localStorage.getItem('previousPage')
  if (scrollPosition) {
    if (previousPage) {
      window.scrollTo(0, parseInt(scrollPosition, 10))
      localStorage.removeItem('previousPage')
    }
    localStorage.removeItem('scrollPosition')
  }
})