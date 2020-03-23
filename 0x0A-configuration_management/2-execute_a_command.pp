# This file terminates the kilmmenow process

exec { "killmenow":
command  => "pkill killmenow",
provider => "shell",
}
