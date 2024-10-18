// Get the theme switcher checkbox
const themeSwitcher = document.getElementById('themeSwitcher');

// Check if the user already has a preferred theme in localStorage
const currentTheme = localStorage.getItem('theme');
if (currentTheme) {
    document.body.className = currentTheme;
    themeSwitcher.checked = currentTheme === 'dark-theme';
}

// Toggle between dark and light themes when the checkbox is clicked
themeSwitcher.addEventListener('change', function () {
    if (this.checked) {
        document.body.className = 'dark-theme';
        localStorage.setItem('theme', 'dark-theme');
    } else {
        document.body.className = 'light-theme';
        localStorage.setItem('theme', 'light-theme');
    }
});
