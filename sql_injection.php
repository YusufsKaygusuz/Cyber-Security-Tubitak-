<?php
$username = $_POST['username']; // Dictinory Attack --> Admin, admin, user, User

$password = $_POST['password']; // Brute Force 


$sql = "Select * from users where username = '$username' AND password = '$password' ";

Select * from users where username = '$username' AND password = '$password'
Select * from users where username = '$username' AND password = '' OR 1=1 --'


$result = mysqli_query($conn, $sql)
?>


// ------------------- Brute Force ------------------------------
<?php
// Hedef kullanıcı adı ve şifresi
$target_username = "hedef_kullanici";
$target_password = "hedef_sifre";

// Brute force saldırısı için parola listesi
$passwords = array("password1", "password2", "password3", "123456", "qwerty", "password123");

// Brute force saldırısı
foreach ($passwords as $password) {
    // Kullanıcı adı ve şifreyi kontrol et
    if ($target_username === "hedef_kullanici" && $target_password === $password) {
        echo "Hesaba başarıyla erişildi! Kullanıcı adı: $target_username, Şifre: $password";
        break;
    } else {
        echo "Kullanıcı adı: $target_username, Şifre: $password denendi. Başarısız!<br>";
    }
}
?>

// ------------------- Dictionary Attack ------------------------------
<?php

// Hedef kullanıcı adı
$target_username = "hedef_kullanici";

// Dictionary dosyasının yolu
$dictionary_file = "passwords.txt";

// Dictionary dosyasını oku
$passwords = file($dictionary_file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

// Dictionary attack
foreach ($passwords as $password) {
    // Kullanıcı adı ve şifreyi kontrol et
    if ($target_username === "hedef_kullanici" && $password === "hedef_sifre") {
        echo "Hesaba başarıyla erişildi! Kullanıcı adı: $target_username, Şifre: $password";
        break;
    } else {
        echo "Kullanıcı adı: $target_username, Şifre: $password denendi. Başarısız!<br>";
    }
}
?>
