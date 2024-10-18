// Get the theme switcher checkbox
const themeSwitcher = document.getElementById('themeSwitcher');

// Check if the user already has a preferred theme in localStorage
const currentTheme = localStorage.getItem('theme');

if (currentTheme) {
    document.body.classList.add(currentTheme);
    themeSwitcher.checked = currentTheme === 'dark-theme';
}

// Add an event listener to the checkbox to toggle themes
themeSwitcher.addEventListener('change', function () {
    if (this.checked) {
        document.body.classList.add('dark-theme');
        document.body.classList.remove('light-theme');
        localStorage.setItem('theme', 'dark-theme');
    } else {
        document.body.classList.add('light-theme');
        document.body.classList.remove('dark-theme');
        localStorage.setItem('theme', 'light-theme');
    }
});
