# fix 500 internal server error

exec { 'fix-php-typo':
    command => 'sudo sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
    provider => shell,
}
